from django import forms
from django.forms.widgets import ClearableFileInput
import json


class CopyColorWidget(forms.TextInput):
    input_type = "color"
    template_name = "widgets/copy_color.html"

    class Media:
        js = ["core/copy_color.js"]


class CodeEditorWidget(forms.Textarea):
    """Simple code editor widget for editing recipes."""

    def __init__(self, attrs=None):
        default_attrs = {"class": "code-editor"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    class Media:
        css = {"all": ["core/code_editor.css"]}
        js = ["core/code_editor.js"]


class OdooProductWidget(forms.Select):
    """Widget for selecting an Odoo product."""

    template_name = "widgets/odoo_product.html"

    class Media:
        js = ["core/odoo_product.js"]

    def get_context(self, name, value, attrs):
        attrs = attrs or {}
        if isinstance(value, dict):
            attrs["data-current-id"] = str(value.get("id", ""))
            value = json.dumps(value)
        elif not value:
            value = ""
        return super().get_context(name, value, attrs)

    def value_from_datadict(self, data, files, name):
        raw = data.get(name)
        if not raw:
            return {}
        try:
            return json.loads(raw)
        except Exception:
            return {}


class AdminBase64FileWidget(ClearableFileInput):
    """Clearable file input that exposes base64 data for downloads."""

    template_name = "widgets/admin_base64_file.html"

    def __init__(
        self,
        *,
        download_name: str | None = None,
        content_type: str = "application/octet-stream",
        **kwargs,
    ) -> None:
        self.download_name = download_name
        self.content_type = content_type
        super().__init__(**kwargs)

    def is_initial(self, value):
        if isinstance(value, str):
            return bool(value)
        return super().is_initial(value)

    def format_value(self, value):
        if isinstance(value, str):
            return value
        return super().format_value(value)

    def get_context(self, name, value, attrs):
        if isinstance(value, str):
            base64_value = value.strip()
            rendered_value = None
        else:
            base64_value = None
            rendered_value = value
        context = super().get_context(name, rendered_value, attrs)
        widget_context = context["widget"]
        widget_context["is_initial"] = bool(base64_value)
        widget_context["base64_value"] = base64_value
        widget_context["download_name"] = self.download_name or f"{name}.bin"
        widget_context["content_type"] = self.content_type
        return context
