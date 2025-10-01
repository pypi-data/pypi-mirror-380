from django.contrib import admin, messages
from django.urls import NoReverseMatch, path, reverse
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse
from django.utils.html import format_html, format_html_join
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from core.widgets import CopyColorWidget
from django.db.models import Count
from django.conf import settings
from pathlib import Path
from django.http import HttpResponse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlsplit, urlunsplit
from django.core.exceptions import PermissionDenied
from django.utils.dateparse import parse_datetime
import base64
import json
import pyperclip
from pyperclip import PyperclipException
import uuid
import subprocess

import requests
from requests import RequestException
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from .utils import capture_rpi_snapshot, capture_screenshot, save_screenshot
from .actions import NodeAction
from .reports import (
    collect_celery_log_entries,
    collect_scheduled_tasks,
    iter_report_periods,
    resolve_period,
)

from core.admin import EmailOutboxAdminForm
from .models import (
    Node,
    EmailOutbox,
    NodeRole,
    NodeFeature,
    NodeFeatureAssignment,
    ContentSample,
    NetMessage,
    NodeManager,
    DNSRecord,
)
from . import dns as dns_utils
from core.models import RFID
from core.user_data import EntityModelAdmin


class NodeAdminForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = "__all__"
        widgets = {"badge_color": CopyColorWidget()}


class NodeFeatureAssignmentInline(admin.TabularInline):
    model = NodeFeatureAssignment
    extra = 0
    autocomplete_fields = ("feature",)


class DeployDNSRecordsForm(forms.Form):
    manager = forms.ModelChoiceField(
        label="Node Manager",
        queryset=NodeManager.objects.none(),
        help_text="Credentials used to authenticate with the DNS provider.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["manager"].queryset = NodeManager.objects.filter(
            provider=NodeManager.Provider.GODADDY, is_enabled=True
        )


@admin.register(NodeManager)
class NodeManagerAdmin(EntityModelAdmin):
    list_display = ("__str__", "provider", "is_enabled", "default_domain")
    list_filter = ("provider", "is_enabled")
    search_fields = (
        "default_domain",
        "user__username",
        "group__name",
    )
    fieldsets = (
        (_("Owner"), {"fields": ("user", "group")}),
        (
            _("Credentials"),
            {"fields": ("api_key", "api_secret", "customer_id")},
        ),
        (
            _("Configuration"),
            {
                "fields": (
                    "provider",
                    "default_domain",
                    "use_sandbox",
                    "is_enabled",
                )
            },
        ),
    )


@admin.register(DNSRecord)
class DNSRecordAdmin(EntityModelAdmin):
    list_display = (
        "record_type",
        "fqdn",
        "data",
        "ttl",
        "node_manager",
        "last_synced_at",
        "last_verified_at",
    )
    list_filter = ("record_type", "provider", "node_manager")
    search_fields = ("domain", "name", "data")
    autocomplete_fields = ("node_manager",)
    actions = ["deploy_selected_records", "validate_selected_records"]

    def _default_manager_for_queryset(self, queryset):
        manager_ids = list(
            queryset.exclude(node_manager__isnull=True)
            .values_list("node_manager_id", flat=True)
            .distinct()
        )
        if len(manager_ids) == 1:
            return manager_ids[0]
        available = list(
            NodeManager.objects.filter(
                provider=NodeManager.Provider.GODADDY, is_enabled=True
            ).values_list("pk", flat=True)
        )
        if len(available) == 1:
            return available[0]
        return None

    @admin.action(description="Deploy Selected records")
    def deploy_selected_records(self, request, queryset):
        unsupported = queryset.exclude(provider=DNSRecord.Provider.GODADDY)
        for record in unsupported:
            self.message_user(
                request,
                f"{record} uses unsupported provider {record.get_provider_display()}",
                messages.WARNING,
            )
        queryset = queryset.filter(provider=DNSRecord.Provider.GODADDY)
        if not queryset:
            self.message_user(request, "No GoDaddy records selected.", messages.WARNING)
            return None

        if "apply" in request.POST:
            form = DeployDNSRecordsForm(request.POST)
            if form.is_valid():
                manager = form.cleaned_data["manager"]
                result = manager.publish_dns_records(list(queryset))
                for record, reason in result.skipped.items():
                    self.message_user(request, f"{record}: {reason}", messages.WARNING)
                for record, reason in result.failures.items():
                    self.message_user(request, f"{record}: {reason}", messages.ERROR)
                if result.deployed:
                    self.message_user(
                        request,
                        f"Deployed {len(result.deployed)} DNS record(s) via {manager}.",
                        messages.SUCCESS,
                    )
                return None
        else:
            initial_manager = self._default_manager_for_queryset(queryset)
            form = DeployDNSRecordsForm(initial={"manager": initial_manager})

        context = {
            **self.admin_site.each_context(request),
            "opts": self.model._meta,
            "form": form,
            "queryset": queryset,
            "title": "Deploy DNS records",
        }
        return render(
            request,
            "admin/nodes/dnsrecord/deploy_records.html",
            context,
        )

    @admin.action(description="Validate Selected records")
    def validate_selected_records(self, request, queryset):
        resolver = dns_utils.create_resolver()
        successes = 0
        for record in queryset:
            ok, message = dns_utils.validate_record(record, resolver=resolver)
            if ok:
                successes += 1
            else:
                self.message_user(request, f"{record}: {message}", messages.WARNING)
        if successes:
            self.message_user(
                request,
                f"Validated {successes} DNS record(s).",
                messages.SUCCESS,
            )


@admin.register(Node)
class NodeAdmin(EntityModelAdmin):
    list_display = (
        "hostname",
        "mac_address",
        "address",
        "port",
        "role",
        "last_seen",
    )
    search_fields = ("hostname", "address", "mac_address")
    change_list_template = "admin/nodes/node/change_list.html"
    change_form_template = "admin/nodes/node/change_form.html"
    form = NodeAdminForm
    actions = [
        "register_visitor",
        "run_task",
        "take_screenshots",
        "fetch_rfids",
    ]
    inlines = [NodeFeatureAssignmentInline]

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "register-current/",
                self.admin_site.admin_view(self.register_current),
                name="nodes_node_register_current",
            ),
            path(
                "register-visitor/",
                self.admin_site.admin_view(self.register_visitor_view),
                name="nodes_node_register_visitor",
            ),
            path(
                "<int:node_id>/action/<str:action>/",
                self.admin_site.admin_view(self.action_view),
                name="nodes_node_action",
            ),
            path(
                "<int:node_id>/public-key/",
                self.admin_site.admin_view(self.public_key),
                name="nodes_node_public_key",
            ),
        ]
        return custom + urls

    def register_current(self, request):
        """Create or update this host and offer browser node registration."""
        if not request.user.is_superuser:
            raise PermissionDenied
        node, created = Node.register_current()
        if created:
            self.message_user(
                request, f"Current host registered as {node}", messages.SUCCESS
            )
        token = uuid.uuid4().hex
        context = {
            "token": token,
            "register_url": reverse("register-node"),
        }
        return render(request, "admin/nodes/node/register_remote.html", context)

    @admin.action(description="Register Visitor Node")
    def register_visitor(self, request, queryset=None):
        return self.register_visitor_view(request)

    def register_visitor_view(self, request):
        """Exchange registration data with the visiting node."""

        node, created = Node.register_current()
        if created:
            self.message_user(
                request, f"Current host registered as {node}", messages.SUCCESS
            )

        token = uuid.uuid4().hex
        context = {
            **self.admin_site.each_context(request),
            "opts": self.model._meta,
            "title": _("Register Visitor Node"),
            "token": token,
            "info_url": reverse("node-info"),
            "register_url": reverse("register-node"),
            "visitor_info_url": "http://localhost:8000/nodes/info/",
            "visitor_register_url": "http://localhost:8000/nodes/register/",
        }
        return render(request, "admin/nodes/node/register_visitor.html", context)

    def public_key(self, request, node_id):
        node = self.get_object(request, node_id)
        if not node:
            self.message_user(request, "Unknown node", messages.ERROR)
            return redirect("..")
        security_dir = Path(settings.BASE_DIR) / "security"
        pub_path = security_dir / f"{node.public_endpoint}.pub"
        if pub_path.exists():
            response = HttpResponse(pub_path.read_bytes(), content_type="text/plain")
            response["Content-Disposition"] = f'attachment; filename="{pub_path.name}"'
            return response
        self.message_user(request, "Public key not found", messages.ERROR)
        return redirect("..")

    def run_task(self, request, queryset):
        if "apply" in request.POST:
            recipe_text = request.POST.get("recipe", "")
            results = []
            for node in queryset:
                try:
                    if not node.is_local:
                        raise NotImplementedError(
                            "Remote node execution is not implemented"
                        )
                    command = ["/bin/sh", "-c", recipe_text]
                    result = subprocess.run(
                        command,
                        check=False,
                        capture_output=True,
                        text=True,
                    )
                    output = result.stdout + result.stderr
                except Exception as exc:
                    output = str(exc)
                results.append((node, output))
            context = {"recipe": recipe_text, "results": results}
            return render(request, "admin/nodes/task_result.html", context)
        context = {"nodes": queryset}
        return render(request, "admin/nodes/node/run_task.html", context)

    run_task.short_description = "Run task"

    @admin.action(description="Take Screenshots")
    def take_screenshots(self, request, queryset):
        tx = uuid.uuid4()
        sources = getattr(settings, "SCREENSHOT_SOURCES", ["/"])
        count = 0
        for node in queryset:
            for source in sources:
                try:
                    url = source.format(node=node, address=node.address, port=node.port)
                except Exception:
                    url = source
                if not url.startswith("http"):
                    url = f"http://{node.address}:{node.port}{url}"
                try:
                    path = capture_screenshot(url)
                except Exception as exc:  # pragma: no cover - selenium issues
                    self.message_user(request, f"{node}: {exc}", messages.ERROR)
                    continue
                sample = save_screenshot(
                    path, node=node, method="ADMIN", transaction_uuid=tx
                )
                if sample:
                    count += 1
        self.message_user(request, f"{count} screenshots captured", messages.SUCCESS)

    @admin.action(description="Fetch RFIDs from selected")
    def fetch_rfids(self, request, queryset):
        local_node = Node.get_local()
        if not local_node:
            self.message_user(
                request,
                "Local node is not registered.",
                messages.ERROR,
            )
            return None

        security_dir = Path(local_node.base_path or settings.BASE_DIR) / "security"
        priv_path = security_dir / f"{local_node.public_endpoint}"
        if not priv_path.exists():
            self.message_user(
                request,
                "Local node private key not found.",
                messages.ERROR,
            )
            return None

        try:
            private_key = serialization.load_pem_private_key(
                priv_path.read_bytes(), password=None
            )
        except Exception as exc:  # pragma: no cover - unexpected key errors
            self.message_user(
                request,
                f"Failed to load private key: {exc}",
                messages.ERROR,
            )
            return None

        payload = json.dumps(
            {"requester": str(local_node.uuid)},
            separators=(",", ":"),
            sort_keys=True,
        )
        signature = base64.b64encode(
            private_key.sign(
                payload.encode(),
                padding.PKCS1v15(),
                hashes.SHA256(),
            )
        ).decode()
        headers = {
            "Content-Type": "application/json",
            "X-Signature": signature,
        }

        processed = 0
        total_created = 0
        total_updated = 0
        errors = 0

        for node in queryset:
            if local_node.pk and node.pk == local_node.pk:
                continue
            url = f"http://{node.address}:{node.port}/nodes/rfid/export/"
            try:
                response = requests.post(
                    url,
                    data=payload,
                    headers=headers,
                    timeout=5,
                )
            except RequestException as exc:
                self.message_user(request, f"{node}: {exc}", messages.ERROR)
                errors += 1
                continue

            if response.status_code != 200:
                self.message_user(
                    request,
                    f"{node}: {response.status_code} {response.text}",
                    messages.ERROR,
                )
                errors += 1
                continue

            try:
                data = response.json()
            except ValueError:
                self.message_user(
                    request,
                    f"{node}: invalid JSON response",
                    messages.ERROR,
                )
                errors += 1
                continue

            created = 0
            updated = 0
            rfids = data.get("rfids", []) or []
            for entry in rfids:
                rfid_value = entry.get("rfid")
                if not rfid_value:
                    continue
                defaults = {
                    "custom_label": entry.get("custom_label", ""),
                    "key_a": entry.get(
                        "key_a", RFID._meta.get_field("key_a").default
                    ),
                    "key_b": entry.get(
                        "key_b", RFID._meta.get_field("key_b").default
                    ),
                    "data": entry.get("data", []),
                    "key_a_verified": bool(entry.get("key_a_verified", False)),
                    "key_b_verified": bool(entry.get("key_b_verified", False)),
                    "allowed": bool(entry.get("allowed", True)),
                    "color": entry.get("color", RFID.BLACK),
                    "kind": entry.get("kind", RFID.CLASSIC),
                    "released": bool(entry.get("released", False)),
                    "origin_node": node,
                }
                if "last_seen_on" in entry:
                    last_seen_raw = entry.get("last_seen_on")
                    if last_seen_raw:
                        defaults["last_seen_on"] = parse_datetime(last_seen_raw)
                    else:
                        defaults["last_seen_on"] = None

                obj, created_flag = RFID.objects.update_or_create(
                    rfid=rfid_value,
                    defaults=defaults,
                )
                if created_flag:
                    created += 1
                else:
                    updated += 1

            processed += 1
            total_created += created
            total_updated += updated

        if processed:
            message = (
                f"Fetched RFIDs from {processed} node(s); "
                f"{total_created} created, {total_updated} updated."
            )
            level = messages.SUCCESS if not errors else messages.WARNING
            self.message_user(request, message, level)
        elif not errors:
            self.message_user(request, "No remote nodes selected.", messages.INFO)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context["node_actions"] = NodeAction.get_actions()
        if object_id:
            extra_context["public_key_url"] = reverse(
                "admin:nodes_node_public_key", args=[object_id]
            )
        return super().changeform_view(
            request, object_id, form_url, extra_context=extra_context
        )

    def action_view(self, request, node_id, action):
        node = self.get_object(request, node_id)
        action_cls = NodeAction.registry.get(action)
        if not node or not action_cls:
            self.message_user(request, "Unknown node action", messages.ERROR)
            return redirect("..")
        try:
            result = action_cls.run(node)
            if hasattr(result, "status_code"):
                return result
            self.message_user(
                request,
                f"{action_cls.display_name} executed successfully",
                messages.SUCCESS,
            )
        except NotImplementedError:
            self.message_user(
                request,
                "Remote node actions are not yet implemented",
                messages.WARNING,
            )
        except Exception as exc:  # pragma: no cover - unexpected errors
            self.message_user(request, str(exc), messages.ERROR)
        return redirect(reverse("admin:nodes_node_change", args=[node_id]))


@admin.register(EmailOutbox)
class EmailOutboxAdmin(EntityModelAdmin):
    form = EmailOutboxAdminForm
    list_display = (
        "owner_label",
        "host",
        "port",
        "username",
        "use_tls",
        "use_ssl",
        "is_enabled",
    )
    change_form_template = "admin/nodes/emailoutbox/change_form.html"
    fieldsets = (
        ("Owner", {"fields": ("user", "group")}),
        ("Credentials", {"fields": ("username", "password")}),
        (
            "Configuration",
            {
                "fields": (
                    "node",
                    "host",
                    "port",
                    "use_tls",
                    "use_ssl",
                    "from_email",
                    "is_enabled",
                )
            },
        ),
    )

    @admin.display(description="Owner")
    def owner_label(self, obj):
        return obj.owner_display()

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "<path:object_id>/test/",
                self.admin_site.admin_view(self.test_outbox),
                name="nodes_emailoutbox_test",
            )
        ]
        return custom + urls

    def test_outbox(self, request, object_id):
        outbox = self.get_object(request, object_id)
        if not outbox:
            self.message_user(request, "Unknown outbox", messages.ERROR)
            return redirect("..")
        recipient = request.user.email or outbox.username
        try:
            outbox.send_mail(
                "Test email",
                "This is a test email.",
                [recipient],
            )
            self.message_user(request, "Test email sent", messages.SUCCESS)
        except Exception as exc:  # pragma: no cover - admin feedback
            self.message_user(request, str(exc), messages.ERROR)
        return redirect("..")

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        extra_context = extra_context or {}
        if object_id:
            extra_context["test_url"] = reverse(
                "admin:nodes_emailoutbox_test", args=[object_id]
            )
        return super().changeform_view(request, object_id, form_url, extra_context)


class NodeRoleAdminForm(forms.ModelForm):
    nodes = forms.ModelMultipleChoiceField(
        queryset=Node.objects.all(),
        required=False,
        widget=FilteredSelectMultiple("Nodes", False),
    )

    class Meta:
        model = NodeRole
        fields = ("name", "description", "nodes")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["nodes"].initial = self.instance.node_set.all()


@admin.register(NodeRole)
class NodeRoleAdmin(EntityModelAdmin):
    form = NodeRoleAdminForm
    list_display = ("name", "description", "registered", "default_features")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_registered=Count("node", distinct=True)).prefetch_related(
            "features"
        )

    @admin.display(description="Registered", ordering="_registered")
    def registered(self, obj):
        return getattr(obj, "_registered", obj.node_set.count())

    @admin.display(description="Default Features")
    def default_features(self, obj):
        features = [feature.display for feature in obj.features.all()]
        return ", ".join(features) if features else "—"

    def save_model(self, request, obj, form, change):
        obj.node_set.set(form.cleaned_data.get("nodes", []))


@admin.register(NodeFeature)
class NodeFeatureAdmin(EntityModelAdmin):
    filter_horizontal = ("roles",)
    list_display = (
        "display",
        "slug",
        "default_roles",
        "is_enabled_display",
        "available_actions",
    )
    actions = ["check_features_for_eligibility", "enable_selected_features"]
    readonly_fields = ("is_enabled",)
    search_fields = ("display", "slug")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("roles")

    @admin.display(description="Default Roles")
    def default_roles(self, obj):
        roles = [role.name for role in obj.roles.all()]
        return ", ".join(roles) if roles else "—"

    @admin.display(description="Is Enabled", boolean=True, ordering="is_enabled")
    def is_enabled_display(self, obj):
        return obj.is_enabled

    @admin.display(description="Actions")
    def available_actions(self, obj):
        if not obj.is_enabled:
            return "—"
        actions = obj.get_default_actions()
        if not actions:
            return "—"

        links = []
        for action in actions:
            try:
                url = reverse(action.url_name)
            except NoReverseMatch:
                links.append(action.label)
            else:
                links.append(format_html('<a href="{}">{}</a>', url, action.label))

        if not links:
            return "—"
        return format_html_join(" | ", "{}", ((link,) for link in links))

    def _manual_enablement_message(self, feature, node):
        if node is None:
            return (
                "Manual enablement is unavailable without a registered local node."
            )
        if feature.slug in Node.MANUAL_FEATURE_SLUGS:
            return "This feature can be enabled manually."
        return "This feature cannot be enabled manually."

    @admin.action(description="Check features for eligibility")
    def check_features_for_eligibility(self, request, queryset):
        from .feature_checks import feature_checks

        features = list(queryset)
        total = len(features)
        successes = 0
        node = Node.get_local()
        for feature in features:
            enablement_message = self._manual_enablement_message(feature, node)
            try:
                result = feature_checks.run(feature, node=node)
            except Exception as exc:  # pragma: no cover - defensive
                self.message_user(
                    request,
                    f"{feature.display}: {exc} {enablement_message}",
                    level=messages.ERROR,
                )
                continue
            if result is None:
                self.message_user(
                    request,
                    f"No check is configured for {feature.display}. {enablement_message}",
                    level=messages.WARNING,
                )
                continue
            message = result.message or (
                f"{feature.display} check {'passed' if result.success else 'failed'}."
            )
            self.message_user(
                request, f"{message} {enablement_message}", level=result.level
            )
            if result.success:
                successes += 1
        if total:
            self.message_user(
                request,
                f"Completed {successes} of {total} feature check(s) successfully.",
                level=messages.INFO,
            )

    @admin.action(description="Enable selected action")
    def enable_selected_features(self, request, queryset):
        node = Node.get_local()
        if node is None:
            self.message_user(
                request,
                "No local node is registered; unable to enable features manually.",
                level=messages.ERROR,
            )
            return

        manual_features = [
            feature
            for feature in queryset
            if feature.slug in Node.MANUAL_FEATURE_SLUGS
        ]
        non_manual_features = [
            feature
            for feature in queryset
            if feature.slug not in Node.MANUAL_FEATURE_SLUGS
        ]
        for feature in non_manual_features:
            self.message_user(
                request,
                f"{feature.display} cannot be enabled manually.",
                level=messages.WARNING,
            )

        if not manual_features:
            self.message_user(
                request,
                "None of the selected features can be enabled manually.",
                level=messages.WARNING,
            )
            return

        current_manual = set(
            node.features.filter(slug__in=Node.MANUAL_FEATURE_SLUGS).values_list(
                "slug", flat=True
            )
        )
        desired_manual = current_manual | {feature.slug for feature in manual_features}
        newly_enabled = desired_manual - current_manual
        if not newly_enabled:
            self.message_user(
                request,
                "Selected manual features are already enabled.",
                level=messages.INFO,
            )
            return

        node.update_manual_features(desired_manual)
        display_map = {feature.slug: feature.display for feature in manual_features}
        newly_enabled_names = [display_map[slug] for slug in sorted(newly_enabled)]
        self.message_user(
            request,
            "Enabled {} feature(s): {}".format(
                len(newly_enabled), ", ".join(newly_enabled_names)
            ),
            level=messages.SUCCESS,
        )

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "celery-report/",
                self.admin_site.admin_view(self.celery_report),
                name="nodes_nodefeature_celery_report",
            ),
            path(
                "take-screenshot/",
                self.admin_site.admin_view(self.take_screenshot),
                name="nodes_nodefeature_take_screenshot",
            ),
            path(
                "take-snapshot/",
                self.admin_site.admin_view(self.take_snapshot),
                name="nodes_nodefeature_take_snapshot",
            ),
            path(
                "view-stream/",
                self.admin_site.admin_view(self.view_stream),
                name="nodes_nodefeature_view_stream",
            ),
        ]
        return custom + urls

    def celery_report(self, request):
        period = resolve_period(request.GET.get("period"))
        now = timezone.now()
        window_end = now + period.delta
        log_window_start = now - period.delta

        scheduled_tasks = collect_scheduled_tasks(now, window_end)
        log_collection = collect_celery_log_entries(log_window_start, now)

        period_options = [
            {
                "key": candidate.key,
                "label": candidate.label,
                "selected": candidate.key == period.key,
                "url": f"?period={candidate.key}",
            }
            for candidate in iter_report_periods()
        ]

        context = {
            **self.admin_site.each_context(request),
            "title": _("Celery Report"),
            "period": period,
            "period_options": period_options,
            "current_time": now,
            "window_end": window_end,
            "log_window_start": log_window_start,
            "scheduled_tasks": scheduled_tasks,
            "log_entries": log_collection.entries,
            "log_sources": log_collection.checked_sources,
        }
        return TemplateResponse(
            request,
            "admin/nodes/nodefeature/celery_report.html",
            context,
        )

    def _ensure_feature_enabled(self, request, slug: str, action_label: str):
        try:
            feature = NodeFeature.objects.get(slug=slug)
        except NodeFeature.DoesNotExist:
            self.message_user(
                request,
                f"{action_label} is unavailable because the feature is not configured.",
                level=messages.ERROR,
            )
            return None
        if not feature.is_enabled:
            self.message_user(
                request,
                f"{feature.display} feature is not enabled on this node.",
                level=messages.WARNING,
            )
            return None
        return feature

    def take_screenshot(self, request):
        feature = self._ensure_feature_enabled(
            request, "screenshot-poll", "Take Screenshot"
        )
        if not feature:
            return redirect("..")
        url = request.build_absolute_uri("/")
        try:
            path = capture_screenshot(url)
        except Exception as exc:  # pragma: no cover - depends on selenium setup
            self.message_user(request, str(exc), level=messages.ERROR)
            return redirect("..")
        node = Node.get_local()
        sample = save_screenshot(path, node=node, method="DEFAULT_ACTION")
        if not sample:
            self.message_user(
                request, "Duplicate screenshot; not saved", level=messages.INFO
            )
            return redirect("..")
        self.message_user(
            request, f"Screenshot saved to {sample.path}", level=messages.SUCCESS
        )
        try:
            change_url = reverse(
                "admin:nodes_contentsample_change", args=[sample.pk]
            )
        except NoReverseMatch:  # pragma: no cover - admin URL always registered
            self.message_user(
                request,
                "Screenshot saved but the admin page could not be resolved.",
                level=messages.WARNING,
            )
            return redirect("..")
        return redirect(change_url)

    def take_snapshot(self, request):
        feature = self._ensure_feature_enabled(
            request, "rpi-camera", "Take a Snapshot"
        )
        if not feature:
            return redirect("..")
        try:
            path = capture_rpi_snapshot()
        except Exception as exc:  # pragma: no cover - depends on camera stack
            self.message_user(request, str(exc), level=messages.ERROR)
            return redirect("..")
        node = Node.get_local()
        sample = save_screenshot(path, node=node, method="RPI_CAMERA")
        if not sample:
            self.message_user(
                request, "Duplicate snapshot; not saved", level=messages.INFO
            )
            return redirect("..")
        self.message_user(
            request, f"Snapshot saved to {sample.path}", level=messages.SUCCESS
        )
        try:
            change_url = reverse(
                "admin:nodes_contentsample_change", args=[sample.pk]
            )
        except NoReverseMatch:  # pragma: no cover - admin URL always registered
            self.message_user(
                request,
                "Snapshot saved but the admin page could not be resolved.",
                level=messages.WARNING,
            )
            return redirect("..")
        return redirect(change_url)

    def view_stream(self, request):
        feature = self._ensure_feature_enabled(request, "rpi-camera", "View stream")
        if not feature:
            return redirect("..")

        configured_stream = getattr(settings, "RPI_CAMERA_STREAM_URL", "").strip()
        if configured_stream:
            stream_url = configured_stream
        else:
            base_uri = request.build_absolute_uri("/")
            parsed = urlsplit(base_uri)
            hostname = parsed.hostname or "127.0.0.1"
            port = getattr(settings, "RPI_CAMERA_STREAM_PORT", 8554)
            scheme = getattr(settings, "RPI_CAMERA_STREAM_SCHEME", "http")
            netloc = f"{hostname}:{port}" if port else hostname
            stream_url = urlunsplit((scheme, netloc, "/", "", ""))
        context = {
            **self.admin_site.each_context(request),
            "title": _("Raspberry Pi Camera Stream"),
            "stream_url": stream_url,
        }
        return TemplateResponse(
            request,
            "admin/nodes/nodefeature/view_stream.html",
            context,
        )


@admin.register(ContentSample)
class ContentSampleAdmin(EntityModelAdmin):
    list_display = ("name", "kind", "node", "user", "created_at")
    readonly_fields = ("created_at", "name", "user", "image_preview")

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                "from-clipboard/",
                self.admin_site.admin_view(self.add_from_clipboard),
                name="nodes_contentsample_from_clipboard",
            ),
            path(
                "capture/",
                self.admin_site.admin_view(self.capture_now),
                name="nodes_contentsample_capture",
            ),
        ]
        return custom + urls

    def add_from_clipboard(self, request):
        try:
            content = pyperclip.paste()
        except PyperclipException as exc:  # pragma: no cover - depends on OS clipboard
            self.message_user(request, f"Clipboard error: {exc}", level=messages.ERROR)
            return redirect("..")
        if not content:
            self.message_user(request, "Clipboard is empty.", level=messages.INFO)
            return redirect("..")
        if ContentSample.objects.filter(
            content=content, kind=ContentSample.TEXT
        ).exists():
            self.message_user(
                request, "Duplicate sample not created.", level=messages.INFO
            )
            return redirect("..")
        user = request.user if request.user.is_authenticated else None
        ContentSample.objects.create(
            content=content, user=user, kind=ContentSample.TEXT
        )
        self.message_user(
            request, "Text sample added from clipboard.", level=messages.SUCCESS
        )
        return redirect("..")

    def capture_now(self, request):
        node = Node.get_local()
        url = request.build_absolute_uri("/")
        try:
            path = capture_screenshot(url)
        except Exception as exc:  # pragma: no cover - depends on selenium setup
            self.message_user(request, str(exc), level=messages.ERROR)
            return redirect("..")
        sample = save_screenshot(path, node=node, method="ADMIN")
        if sample:
            self.message_user(request, f"Screenshot saved to {path}", messages.SUCCESS)
        else:
            self.message_user(request, "Duplicate screenshot; not saved", messages.INFO)
        return redirect("..")

    @admin.display(description="Screenshot")
    def image_preview(self, obj):
        if not obj or obj.kind != ContentSample.IMAGE or not obj.path:
            return ""
        file_path = Path(obj.path)
        if not file_path.is_absolute():
            file_path = settings.LOG_DIR / file_path
        if not file_path.exists():
            return "File not found"
        with file_path.open("rb") as f:
            encoded = base64.b64encode(f.read()).decode("ascii")
        return format_html(
            '<img src="data:image/png;base64,{}" style="max-width:100%;" />',
            encoded,
        )


@admin.register(NetMessage)
class NetMessageAdmin(EntityModelAdmin):
    class NetMessageAdminForm(forms.ModelForm):
        class Meta:
            model = NetMessage
            fields = "__all__"
            widgets = {"body": forms.Textarea(attrs={"rows": 4})}

    form = NetMessageAdminForm
    change_form_template = "admin/nodes/netmessage/change_form.html"
    list_display = (
        "subject",
        "body",
        "filter_node",
        "filter_node_role",
        "node_origin",
        "created",
        "target_limit",
        "complete",
    )
    search_fields = ("subject", "body")
    list_filter = ("complete", "filter_node_role", "filter_current_relation")
    ordering = ("-created",)
    readonly_fields = ("complete",)
    actions = ["send_messages"]
    fieldsets = (
        (None, {"fields": ("subject", "body")}),
        (
            "Filters",
            {
                "fields": (
                    "filter_node",
                    "filter_node_feature",
                    "filter_node_role",
                    "filter_current_relation",
                    "filter_installed_version",
                    "filter_installed_revision",
                )
            },
        ),
        (
            "Propagation",
            {
                "fields": (
                    "node_origin",
                    "target_limit",
                    "propagated_to",
                    "complete",
                )
            },
        ),
    )

    def get_changeform_initial_data(self, request):
        initial = super().get_changeform_initial_data(request)
        initial = dict(initial) if initial else {}
        reply_to = request.GET.get("reply_to")
        if reply_to:
            try:
                message = (
                    NetMessage.objects.select_related("node_origin__role")
                    .get(pk=reply_to)
                )
            except (NetMessage.DoesNotExist, ValueError, TypeError):
                message = None
            if message:
                subject = (message.subject or "").strip()
                if subject:
                    if not subject.lower().startswith("re:"):
                        subject = f"Re: {subject}"
                else:
                    subject = "Re:"
                initial.setdefault("subject", subject[:64])
                if message.node_origin and "filter_node" not in initial:
                    initial["filter_node"] = message.node_origin.pk
        return initial

    def send_messages(self, request, queryset):
        for msg in queryset:
            msg.propagate()
        self.message_user(request, f"{queryset.count()} messages sent")

    send_messages.short_description = "Send selected messages"
