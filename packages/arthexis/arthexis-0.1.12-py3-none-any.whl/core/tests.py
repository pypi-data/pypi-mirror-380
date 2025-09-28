import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

from django.test import Client, TestCase, RequestFactory, override_settings
from django.urls import reverse
from django.http import HttpRequest
import json
from decimal import Decimal
from unittest import mock
from unittest.mock import patch
from pathlib import Path
import subprocess
from glob import glob
from datetime import datetime, timedelta, timezone as datetime_timezone
import tempfile
from urllib.parse import quote

from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.messages import get_messages
from .models import (
    User,
    UserPhoneNumber,
    EnergyAccount,
    ElectricVehicle,
    EnergyCredit,
    Product,
    Brand,
    EVModel,
    RFID,
    SecurityGroup,
    Package,
    PackageRelease,
    ReleaseManager,
    Todo,
    PublicWifiAccess,
)
from django.contrib.admin.sites import AdminSite
from core.admin import (
    PackageReleaseAdmin,
    PackageAdmin,
    UserAdmin,
    USER_PROFILE_INLINES,
)
from ocpp.models import Transaction, Charger

from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.db import IntegrityError
from .backends import LocalhostAdminBackend
from core.views import _step_check_version, _step_promote_build, _step_publish
from core import views as core_views
from core import public_wifi


class DefaultAdminTests(TestCase):
    def test_arthexis_is_default_user(self):
        self.assertTrue(User.objects.filter(username="arthexis").exists())
        self.assertFalse(User.all_objects.filter(username="admin").exists())

    def test_admin_created_and_local_only(self):
        backend = LocalhostAdminBackend()
        req = HttpRequest()
        req.META["REMOTE_ADDR"] = "127.0.0.1"
        user = backend.authenticate(req, username="admin", password="admin")
        self.assertIsNotNone(user)
        self.assertEqual(user.pk, 2)

        remote = HttpRequest()
        remote.META["REMOTE_ADDR"] = "10.0.0.1"
        self.assertIsNone(
            backend.authenticate(remote, username="admin", password="admin")
        )

    def test_admin_respects_forwarded_for(self):
        backend = LocalhostAdminBackend()

        req = HttpRequest()
        req.META["REMOTE_ADDR"] = "10.0.0.1"
        req.META["HTTP_X_FORWARDED_FOR"] = "127.0.0.1"
        self.assertIsNotNone(
            backend.authenticate(req, username="admin", password="admin"),
            "X-Forwarded-For should permit allowed IP",
        )

        blocked = HttpRequest()
        blocked.META["REMOTE_ADDR"] = "10.0.0.1"
        blocked.META["HTTP_X_FORWARDED_FOR"] = "8.8.8.8"
        self.assertIsNone(
            backend.authenticate(blocked, username="admin", password="admin")
        )


class UserOperateAsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.permission = Permission.objects.get(codename="view_todo")

    def test_staff_user_delegates_permissions(self):
        delegate = User.objects.create_user(username="delegate", password="secret")
        delegate.user_permissions.add(self.permission)
        operator = User.objects.create_user(
            username="operator", password="secret", is_staff=True
        )
        self.assertFalse(operator.has_perm("core.view_todo"))
        operator.operate_as = delegate
        operator.full_clean()
        operator.save()
        operator.refresh_from_db()
        self.assertTrue(operator.has_perm("core.view_todo"))

    def test_only_staff_may_operate_as(self):
        delegate = User.objects.create_user(username="delegate", password="secret")
        operator = User.objects.create_user(username="operator", password="secret")
        operator.operate_as = delegate
        with self.assertRaises(ValidationError):
            operator.full_clean()

    def test_non_superuser_cannot_operate_as_staff(self):
        staff_delegate = User.objects.create_user(
            username="delegate", password="secret", is_staff=True
        )
        operator = User.objects.create_user(
            username="operator", password="secret", is_staff=True
        )
        operator.operate_as = staff_delegate
        with self.assertRaises(ValidationError):
            operator.full_clean()

    def test_recursive_chain_and_cycle_detection(self):
        base = User.objects.create_user(username="base", password="secret")
        base.user_permissions.add(self.permission)
        middle = User.objects.create_user(
            username="middle", password="secret", is_staff=True
        )
        middle.operate_as = base
        middle.full_clean()
        middle.save()
        top = User.objects.create_superuser(
            username="top", email="top@example.com", password="secret"
        )
        top.operate_as = middle
        top.full_clean()
        top.save()
        top.refresh_from_db()
        self.assertTrue(top.has_perm("core.view_todo"))

        first = User.objects.create_superuser(
            username="first", email="first@example.com", password="secret"
        )
        second = User.objects.create_superuser(
            username="second", email="second@example.com", password="secret"
        )
        first.operate_as = second
        first.full_clean()
        first.save()
        second.operate_as = first
        second.full_clean()
        second.save()
        self.assertFalse(first._check_operate_as_chain(lambda user: False))

    def test_module_permissions_fall_back(self):
        delegate = User.objects.create_user(username="helper", password="secret")
        delegate.user_permissions.add(self.permission)
        operator = User.objects.create_user(
            username="mod", password="secret", is_staff=True
        )
        operator.operate_as = delegate
        operator.full_clean()
        operator.save()
        self.assertTrue(operator.has_module_perms("core"))

    def test_has_profile_via_delegate(self):
        delegate = User.objects.create_user(
            username="delegate", password="secret", is_staff=True
        )
        ReleaseManager.objects.create(user=delegate)
        operator = User.objects.create_superuser(
            username="operator",
            email="operator@example.com",
            password="secret",
        )
        operator.operate_as = delegate
        operator.full_clean()
        operator.save()
        profile = operator.get_profile(ReleaseManager)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user, delegate)
        self.assertTrue(operator.has_profile(ReleaseManager))

    def test_has_profile_via_group_membership(self):
        member = User.objects.create_user(username="member", password="secret")
        group = SecurityGroup.objects.create(name="Managers")
        group.user_set.add(member)
        profile = ReleaseManager.objects.create(group=group)
        self.assertEqual(member.get_profile(ReleaseManager), profile)
        self.assertTrue(member.has_profile(ReleaseManager))

    def test_release_manager_property_uses_delegate_profile(self):
        delegate = User.objects.create_user(
            username="delegate-property", password="secret", is_staff=True
        )
        profile = ReleaseManager.objects.create(user=delegate)
        operator = User.objects.create_superuser(
            username="operator-property",
            email="operator-property@example.com",
            password="secret",
        )
        operator.operate_as = delegate
        operator.full_clean()
        operator.save()
        self.assertEqual(operator.release_manager, profile)


class UserPhoneNumberTests(TestCase):
    def test_get_phone_numbers_by_priority(self):
        user = User.objects.create_user(username="phone-user", password="secret")
        later = UserPhoneNumber.objects.create(
            user=user, number="+15555550101", priority=10
        )
        earlier = UserPhoneNumber.objects.create(
            user=user, number="+15555550100", priority=1
        )
        immediate = UserPhoneNumber.objects.create(
            user=user, number="+15555550099", priority=0
        )

        phones = user.get_phones_by_priority()
        self.assertEqual(phones, [immediate, earlier, later])

    def test_get_phone_numbers_by_priority_orders_by_id_when_equal(self):
        user = User.objects.create_user(username="phone-order", password="secret")
        first = UserPhoneNumber.objects.create(
            user=user, number="+19995550000", priority=0
        )
        second = UserPhoneNumber.objects.create(
            user=user, number="+19995550001", priority=0
        )

        phones = user.get_phones_by_priority()
        self.assertEqual(phones, [first, second])

    def test_get_phone_numbers_by_priority_alias(self):
        user = User.objects.create_user(username="phone-alias", password="secret")
        phone = UserPhoneNumber.objects.create(
            user=user, number="+14445550000", priority=3
        )

        self.assertEqual(user.get_phone_numbers_by_priority(), [phone])


class ProfileValidationTests(TestCase):
    def test_system_user_cannot_receive_profiles(self):
        system_user = User.objects.get(username=User.SYSTEM_USERNAME)
        profile = ReleaseManager(user=system_user)
        with self.assertRaises(ValidationError) as exc:
            profile.full_clean()
        self.assertIn("user", exc.exception.error_dict)


class UserAdminInlineTests(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.factory = RequestFactory()
        self.admin = UserAdmin(User, self.site)
        self.system_user = User.objects.get(username=User.SYSTEM_USERNAME)
        self.superuser = User.objects.create_superuser(
            username="inline-super",
            email="inline-super@example.com",
            password="secret",
        )

    def test_profile_inlines_hidden_for_system_user(self):
        request = self.factory.get("/")
        request.user = self.superuser
        system_inlines = self.admin.get_inline_instances(request, self.system_user)
        system_profiles = [
            inline
            for inline in system_inlines
            if inline.__class__ in USER_PROFILE_INLINES
        ]
        self.assertFalse(system_profiles)

        other_inlines = self.admin.get_inline_instances(request, self.superuser)
        other_profiles = [
            inline
            for inline in other_inlines
            if inline.__class__ in USER_PROFILE_INLINES
        ]
        self.assertEqual(len(other_profiles), len(USER_PROFILE_INLINES))


class RFIDLoginTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="alice", password="secret")
        self.account = EnergyAccount.objects.create(user=self.user, name="ALICE")
        tag = RFID.objects.create(rfid="CARD123")
        self.account.rfids.add(tag)

    def test_rfid_login_success(self):
        response = self.client.post(
            reverse("rfid-login"),
            data={"rfid": "CARD123"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["username"], "alice")

    def test_rfid_login_invalid(self):
        response = self.client.post(
            reverse("rfid-login"),
            data={"rfid": "UNKNOWN"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)


class RFIDBatchApiTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="bob", password="secret")
        self.account = EnergyAccount.objects.create(user=self.user, name="BOB")
        self.client.force_login(self.user)

    def test_export_rfids(self):
        tag_black = RFID.objects.create(rfid="CARD999", custom_label="Main Tag")
        tag_white = RFID.objects.create(rfid="CARD998", color=RFID.WHITE)
        self.account.rfids.add(tag_black, tag_white)
        response = self.client.get(reverse("rfid-batch"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "rfids": [
                    {
                        "rfid": "CARD999",
                        "custom_label": "Main Tag",
                        "energy_accounts": [self.account.id],
                        "allowed": True,
                        "color": "B",
                        "released": False,
                    }
                ]
            },
        )

    def test_export_rfids_color_filter(self):
        RFID.objects.create(rfid="CARD111", color=RFID.WHITE)
        response = self.client.get(reverse("rfid-batch"), {"color": "W"})
        self.assertEqual(
            response.json(),
            {
                "rfids": [
                    {
                        "rfid": "CARD111",
                        "custom_label": "",
                        "energy_accounts": [],
                        "allowed": True,
                        "color": "W",
                        "released": False,
                    }
                ]
            },
        )

    def test_export_rfids_released_filter(self):
        RFID.objects.create(rfid="CARD112", released=True)
        RFID.objects.create(rfid="CARD113", released=False)
        response = self.client.get(reverse("rfid-batch"), {"released": "true"})
        self.assertEqual(
            response.json(),
            {
                "rfids": [
                    {
                        "rfid": "CARD112",
                        "custom_label": "",
                        "energy_accounts": [],
                        "allowed": True,
                        "color": "B",
                        "released": True,
                    }
                ]
            },
        )

    def test_import_rfids(self):
        data = {
            "rfids": [
                {
                    "rfid": "A1B2C3D4",
                    "custom_label": "Imported Tag",
                    "energy_accounts": [self.account.id],
                    "allowed": True,
                    "color": "W",
                    "released": True,
                }
            ]
        }
        response = self.client.post(
            reverse("rfid-batch"),
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["imported"], 1)
        self.assertTrue(
            RFID.objects.filter(
                rfid="A1B2C3D4",
                custom_label="Imported Tag",
                energy_accounts=self.account,
                color=RFID.WHITE,
                released=True,
            ).exists()
        )


class AllowedRFIDTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="eve", password="secret")
        self.account = EnergyAccount.objects.create(user=self.user, name="EVE")
        self.rfid = RFID.objects.create(rfid="BAD123")
        self.account.rfids.add(self.rfid)

    def test_disallow_removes_and_blocks(self):
        self.rfid.allowed = False
        self.rfid.save()
        self.account.refresh_from_db()
        self.assertFalse(self.account.rfids.exists())

        with self.assertRaises(IntegrityError):
            RFID.objects.create(rfid="BAD123")


class RFIDValidationTests(TestCase):
    def test_invalid_format_raises(self):
        tag = RFID(rfid="xyz")
        with self.assertRaises(ValidationError):
            tag.full_clean()

    def test_lowercase_saved_uppercase(self):
        tag = RFID.objects.create(rfid="deadbeef")
        self.assertEqual(tag.rfid, "DEADBEEF")

    def test_long_rfid_allowed(self):
        tag = RFID.objects.create(rfid="DEADBEEF10")
        self.assertEqual(tag.rfid, "DEADBEEF10")

    def test_find_user_by_rfid(self):
        user = User.objects.create_user(username="finder", password="pwd")
        acc = EnergyAccount.objects.create(user=user, name="FINDER")
        tag = RFID.objects.create(rfid="ABCD1234")
        acc.rfids.add(tag)
        found = RFID.get_account_by_rfid("abcd1234")
        self.assertEqual(found, acc)

    def test_custom_label_length(self):
        tag = RFID(rfid="FACE1234", custom_label="x" * 33)
        with self.assertRaises(ValidationError):
            tag.full_clean()


class RFIDAssignmentTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="x")
        self.user2 = User.objects.create_user(username="user2", password="x")
        self.acc1 = EnergyAccount.objects.create(user=self.user1, name="USER1")
        self.acc2 = EnergyAccount.objects.create(user=self.user2, name="USER2")
        self.tag = RFID.objects.create(rfid="ABCDEF12")

    def test_rfid_can_only_attach_to_one_account(self):
        self.acc1.rfids.add(self.tag)
        with self.assertRaises(ValidationError):
            self.acc2.rfids.add(self.tag)


class EnergyAccountTests(TestCase):
    def test_balance_calculation(self):
        user = User.objects.create_user(username="balance", password="x")
        acc = EnergyAccount.objects.create(user=user, name="BALANCE")
        EnergyCredit.objects.create(account=acc, amount_kw=50)
        charger = Charger.objects.create(charger_id="T1")
        Transaction.objects.create(
            charger=charger,
            account=acc,
            meter_start=0,
            meter_stop=20,
            start_time=timezone.now(),
            stop_time=timezone.now(),
        )
        self.assertEqual(acc.total_kw_spent, 20)
        self.assertEqual(acc.balance_kw, 30)

    def test_authorization_requires_positive_balance(self):
        user = User.objects.create_user(username="auth", password="x")
        acc = EnergyAccount.objects.create(user=user, name="AUTH")
        self.assertFalse(acc.can_authorize())

        EnergyCredit.objects.create(account=acc, amount_kw=5)
        self.assertTrue(acc.can_authorize())

    def test_service_account_ignores_balance(self):
        user = User.objects.create_user(username="service", password="x")
        acc = EnergyAccount.objects.create(
            user=user, service_account=True, name="SERVICE"
        )
        self.assertTrue(acc.can_authorize())

    def test_account_without_user(self):
        acc = EnergyAccount.objects.create(name="NOUSER")
        tag = RFID.objects.create(rfid="NOUSER1")
        acc.rfids.add(tag)
        self.assertIsNone(acc.user)
        self.assertTrue(acc.rfids.filter(rfid="NOUSER1").exists())


class ElectricVehicleTests(TestCase):
    def test_account_can_have_multiple_vehicles(self):
        user = User.objects.create_user(username="cars", password="x")
        acc = EnergyAccount.objects.create(user=user, name="CARS")
        tesla = Brand.objects.create(name="Tesla")
        nissan = Brand.objects.create(name="Nissan")
        model_s = EVModel.objects.create(brand=tesla, name="Model S")
        leaf = EVModel.objects.create(brand=nissan, name="Leaf")
        ElectricVehicle.objects.create(
            account=acc, brand=tesla, model=model_s, vin="VIN12345678901234"
        )
        ElectricVehicle.objects.create(
            account=acc, brand=nissan, model=leaf, vin="VIN23456789012345"
        )
        self.assertEqual(acc.vehicles.count(), 2)


class AddressTests(TestCase):
    def test_invalid_municipality_state(self):
        addr = Address(
            street="Main",
            number="1",
            municipality="Monterrey",
            state=Address.State.COAHUILA,
            postal_code="00000",
        )
        with self.assertRaises(ValidationError):
            addr.full_clean()

    def test_user_link(self):
        addr = Address.objects.create(
            street="Main",
            number="2",
            municipality="Monterrey",
            state=Address.State.NUEVO_LEON,
            postal_code="64000",
        )
        user = User.objects.create_user(username="addr", password="pwd", address=addr)
        self.assertEqual(user.address, addr)


class PublicWifiUtilitiesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="wifi", password="pwd")

    def test_grant_public_access_records_allowlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            allow_file = base / "locks" / "public_wifi_allow.list"
            with override_settings(BASE_DIR=base):
                with patch("core.public_wifi._iptables_available", return_value=False):
                    public_wifi.grant_public_access(self.user, "AA:BB:CC:DD:EE:FF")
            self.assertTrue(allow_file.exists())
            content = allow_file.read_text()
            self.assertIn("aa:bb:cc:dd:ee:ff", content)
            self.assertTrue(
                PublicWifiAccess.objects.filter(
                    user=self.user, mac_address="aa:bb:cc:dd:ee:ff"
                ).exists()
            )

    def test_revoke_public_access_for_user_updates_allowlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            allow_file = base / "locks" / "public_wifi_allow.list"
            with override_settings(BASE_DIR=base):
                with patch("core.public_wifi._iptables_available", return_value=False):
                    access = public_wifi.grant_public_access(
                        self.user, "AA:BB:CC:DD:EE:FF"
                    )
                    public_wifi.revoke_public_access_for_user(self.user)
            access.refresh_from_db()
            self.assertIsNotNone(access.revoked_on)
            if allow_file.exists():
                self.assertNotIn("aa:bb:cc:dd:ee:ff", allow_file.read_text())


class LiveSubscriptionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="bob", password="pwd")
        self.account = EnergyAccount.objects.create(user=self.user, name="SUBSCRIBER")
        self.product = Product.objects.create(name="Gold", renewal_period=30)
        self.client.force_login(self.user)

    def test_create_and_list_live_subscription(self):
        response = self.client.post(
            reverse("add-live-subscription"),
            data={"account_id": self.account.id, "product_id": self.product.id},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.account.refresh_from_db()
        self.assertEqual(
            self.account.live_subscription_product,
            self.product,
        )
        self.assertIsNotNone(self.account.live_subscription_start_date)
        self.assertEqual(
            self.account.live_subscription_start_date,
            timezone.localdate(),
        )
        self.assertEqual(
            self.account.live_subscription_next_renewal,
            self.account.live_subscription_start_date
            + timedelta(days=self.product.renewal_period),
        )

        list_resp = self.client.get(
            reverse("live-subscription-list"), {"account_id": self.account.id}
        )
        self.assertEqual(list_resp.status_code, 200)
        data = list_resp.json()
        self.assertEqual(len(data["live_subscriptions"]), 1)
        self.assertEqual(data["live_subscriptions"][0]["product__name"], "Gold")
        self.assertEqual(data["live_subscriptions"][0]["id"], self.account.id)
        self.assertEqual(
            data["live_subscriptions"][0]["next_renewal"],
            str(self.account.live_subscription_next_renewal),
        )

    def test_product_list(self):
        response = self.client.get(reverse("product-list"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data["products"]), 1)
        self.assertEqual(data["products"][0]["name"], "Gold")


class OnboardingWizardTests(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_superuser("super", "super@example.com", "pwd")
        self.client.force_login(User.objects.get(username="super"))

    def test_onboarding_flow_creates_account(self):
        details_url = reverse("admin:core_energyaccount_onboard_details")
        response = self.client.get(details_url)
        self.assertEqual(response.status_code, 200)
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "rfid": "ABCD1234",
            "vehicle_id": "VIN12345678901234",
        }
        resp = self.client.post(details_url, data)
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.url, reverse("admin:core_energyaccount_changelist"))
        user = User.objects.get(first_name="John", last_name="Doe")
        self.assertFalse(user.is_active)
        account = EnergyAccount.objects.get(user=user)
        self.assertTrue(account.rfids.filter(rfid="ABCD1234").exists())
        self.assertTrue(account.vehicles.filter(vin="VIN12345678901234").exists())


class EVBrandFixtureTests(TestCase):
    def test_ev_brand_fixture_loads(self):
        call_command(
            "loaddata",
            *sorted(glob("core/fixtures/ev_brands__*.json")),
            *sorted(glob("core/fixtures/ev_models__*.json")),
            verbosity=0,
        )
        porsche = Brand.objects.get(name="Porsche")
        audi = Brand.objects.get(name="Audi")
        self.assertTrue(
            {"WP0", "WP1"} <= set(porsche.wmi_codes.values_list("code", flat=True))
        )
        self.assertTrue(
            set(audi.wmi_codes.values_list("code", flat=True)) >= {"WAU", "TRU"}
        )
        self.assertTrue(EVModel.objects.filter(brand=porsche, name="Taycan").exists())
        self.assertTrue(EVModel.objects.filter(brand=audi, name="e-tron GT").exists())
        self.assertTrue(EVModel.objects.filter(brand=porsche, name="Macan").exists())
        model3 = EVModel.objects.get(brand__name="Tesla", name="Model 3 RWD")
        self.assertEqual(model3.est_battery_kwh, Decimal("57.50"))

    def test_brand_from_vin(self):
        call_command(
            "loaddata",
            *sorted(glob("core/fixtures/ev_brands__*.json")),
            verbosity=0,
        )
        self.assertEqual(Brand.from_vin("WP0ZZZ12345678901").name, "Porsche")
        self.assertEqual(Brand.from_vin("WAUZZZ12345678901").name, "Audi")
        self.assertIsNone(Brand.from_vin("XYZ12345678901234"))


class RFIDFixtureTests(TestCase):
    def test_fixture_assigns_gelectriic_rfid(self):
        call_command(
            "loaddata",
            "core/fixtures/users__arthexis.json",
            "core/fixtures/energy_accounts__gelectriic.json",
            "core/fixtures/rfids__ffffffff.json",
            verbosity=0,
        )
        account = EnergyAccount.objects.get(name="GELECTRIIC")
        tag = RFID.objects.get(rfid="FFFFFFFF")
        self.assertIn(account, tag.energy_accounts.all())
        self.assertEqual(tag.energy_accounts.count(), 1)


class RFIDKeyVerificationFlagTests(TestCase):
    def test_flags_reset_on_key_change(self):
        tag = RFID.objects.create(
            rfid="ABC12345", key_a_verified=True, key_b_verified=True
        )
        tag.key_a = "A1A1A1A1A1A1"
        tag.save()
        self.assertFalse(tag.key_a_verified)
        tag.key_b = "B1B1B1B1B1B1"
        tag.save()
        self.assertFalse(tag.key_b_verified)


class SecurityGroupTests(TestCase):
    def test_parent_and_user_assignment(self):
        parent = SecurityGroup.objects.create(name="Parents")
        child = SecurityGroup.objects.create(name="Children", parent=parent)
        user = User.objects.create_user(username="sg_user", password="secret")
        child.user_set.add(user)
        self.assertEqual(child.parent, parent)
        self.assertIn(user, child.user_set.all())


class ReleaseProcessTests(TestCase):
    def setUp(self):
        self.package = Package.objects.create(name="pkg")
        self.release = PackageRelease.objects.create(
            package=self.package, version="1.0.0"
        )

    @mock.patch("core.views.release_utils._git_clean", return_value=False)
    def test_step_check_requires_clean_repo(self, git_clean):
        with self.assertRaises(Exception):
            _step_check_version(self.release, {}, Path("rel.log"))

    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    @mock.patch("core.views.release_utils.network_available", return_value=False)
    def test_step_check_keeps_repo_clean(self, network_available, git_clean):
        version_path = Path("VERSION")
        original = version_path.read_text(encoding="utf-8")
        _step_check_version(self.release, {}, Path("rel.log"))
        proc = subprocess.run(
            ["git", "status", "--porcelain", str(version_path)],
            capture_output=True,
            text=True,
        )
        self.assertFalse(proc.stdout.strip())
        self.assertEqual(version_path.read_text(encoding="utf-8"), original)

    @mock.patch("core.views.requests.get")
    @mock.patch("core.views.release_utils.network_available", return_value=True)
    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    def test_step_check_ignores_yanked_release(
        self, git_clean, network_available, requests_get
    ):
        response = mock.Mock()
        response.ok = True
        response.json.return_value = {
            "releases": {
                "0.1.12": [
                    {"filename": "pkg.whl", "yanked": True},
                    {"filename": "pkg.tar.gz", "yanked": True},
                ]
            }
        }
        requests_get.return_value = response
        self.release.version = "0.1.12"
        _step_check_version(self.release, {}, Path("rel.log"))
        requests_get.assert_called_once()

    @mock.patch("core.views.requests.get")
    @mock.patch("core.views.release_utils.network_available", return_value=True)
    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    def test_step_check_blocks_available_release(
        self, git_clean, network_available, requests_get
    ):
        response = mock.Mock()
        response.ok = True
        response.json.return_value = {
            "releases": {
                "0.1.12": [
                    {"filename": "pkg.whl", "yanked": False},
                    {"filename": "pkg.tar.gz"},
                ]
            }
        }
        requests_get.return_value = response
        self.release.version = "0.1.12"
        with self.assertRaises(Exception) as exc:
            _step_check_version(self.release, {}, Path("rel.log"))
        self.assertIn("already on PyPI", str(exc.exception))
        requests_get.assert_called_once()

    @mock.patch("core.models.PackageRelease.dump_fixture")
    def test_save_does_not_dump_fixture(self, dump):
        self.release.pypi_url = "https://example.com"
        self.release.save()
        dump.assert_not_called()

    @mock.patch("core.views.subprocess.run")
    @mock.patch("core.views.PackageRelease.dump_fixture")
    @mock.patch("core.views.release_utils.promote", side_effect=Exception("boom"))
    def test_promote_cleans_repo_on_failure(self, promote, dump_fixture, run):
        with self.assertRaises(Exception):
            _step_promote_build(self.release, {}, Path("rel.log"))
        dump_fixture.assert_not_called()
        run.assert_any_call(["git", "reset", "--hard"], check=False)
        run.assert_any_call(["git", "clean", "-fd"], check=False)

    @mock.patch("core.views.subprocess.run")
    @mock.patch("core.views.PackageRelease.dump_fixture")
    @mock.patch("core.views.release_utils.promote")
    def test_promote_rebases_and_pushes_main(self, promote, dump_fixture, run):
        import subprocess as sp

        def fake_run(cmd, check=True, capture_output=False, text=False):
            if capture_output:
                return sp.CompletedProcess(cmd, 0, stdout="", stderr="")
            return sp.CompletedProcess(cmd, 0)

        run.side_effect = fake_run
        _step_promote_build(self.release, {}, Path("rel.log"))
        run.assert_any_call(["git", "fetch", "origin", "main"], check=True)
        run.assert_any_call(["git", "rebase", "origin/main"], check=True)
        run.assert_any_call(["git", "push"], check=True)

    @mock.patch("core.views.subprocess.run")
    @mock.patch("core.views.PackageRelease.dump_fixture")
    def test_promote_advances_version(self, dump_fixture, run):
        import subprocess as sp

        def fake_run(cmd, check=True, capture_output=False, text=False):
            if capture_output:
                return sp.CompletedProcess(cmd, 0, stdout="", stderr="")
            return sp.CompletedProcess(cmd, 0)

        run.side_effect = fake_run

        version_path = Path("VERSION")
        original = version_path.read_text(encoding="utf-8")
        version_path.write_text("0.0.1\n", encoding="utf-8")

        def fake_promote(*args, **kwargs):
            version_path.write_text(self.release.version + "\n", encoding="utf-8")

        with mock.patch("core.views.release_utils.promote", side_effect=fake_promote):
            _step_promote_build(self.release, {}, Path("rel.log"))

        self.assertEqual(
            version_path.read_text(encoding="utf-8"),
            self.release.version + "\n",
        )
        version_path.write_text(original, encoding="utf-8")

    @mock.patch("core.views.timezone.now")
    @mock.patch("core.views.PackageRelease.dump_fixture")
    @mock.patch("core.views.release_utils.publish")
    def test_publish_sets_pypi_url(self, publish, dump_fixture, now):
        now.return_value = datetime(2025, 3, 4, 5, 6, tzinfo=datetime_timezone.utc)
        _step_publish(self.release, {}, Path("rel.log"))
        self.release.refresh_from_db()
        self.assertEqual(
            self.release.pypi_url,
            f"https://pypi.org/project/{self.package.name}/{self.release.version}/",
        )
        self.assertEqual(
            self.release.release_on,
            datetime(2025, 3, 4, 5, 6, tzinfo=datetime_timezone.utc),
        )
        dump_fixture.assert_called_once()

    @mock.patch("core.views.PackageRelease.dump_fixture")
    @mock.patch("core.views.release_utils.publish", side_effect=Exception("boom"))
    def test_publish_failure_keeps_url_blank(self, publish, dump_fixture):
        with self.assertRaises(Exception):
            _step_publish(self.release, {}, Path("rel.log"))
        self.release.refresh_from_db()
        self.assertEqual(self.release.pypi_url, "")
        self.assertIsNone(self.release.release_on)
        dump_fixture.assert_not_called()

    def test_new_todo_does_not_reset_pending_flow(self):
        user = User.objects.create_superuser("admin", "admin@example.com", "pw")
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        Todo.objects.create(request="Initial checklist item")
        steps = [("Confirm release TODO completion", core_views._step_check_todos)]
        with mock.patch("core.views.PUBLISH_STEPS", steps):
            self.client.force_login(user)
            response = self.client.get(url)
            self.assertTrue(response.context["has_pending_todos"])
            self.client.get(f"{url}?ack_todos=1")
            self.client.get(f"{url}?start=1")
            self.client.get(f"{url}?step=0")
            Todo.objects.create(request="Follow-up checklist item")
            response = self.client.get(url)
            self.assertEqual(
                Todo.objects.filter(is_deleted=False, done_on__isnull=True).count(),
                1,
            )
            self.assertIsNone(response.context["todos"])
            self.assertFalse(response.context["has_pending_todos"])
            session = self.client.session
            ctx = session.get(f"release_publish_{self.release.pk}")
            self.assertTrue(ctx.get("todos_ack"))

    def test_release_progress_uses_lockfile(self):
        run = []

        def step1(release, ctx, log_path):
            run.append("step1")

        def step2(release, ctx, log_path):
            run.append("step2")

        steps = [("One", step1), ("Two", step2)]
        user = User.objects.create_superuser("admin", "admin@example.com", "pw")
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        with mock.patch("core.views.PUBLISH_STEPS", steps):
            self.client.force_login(user)
            self.client.get(f"{url}?step=0")
            self.assertEqual(run, ["step1"])
            client2 = Client()
            client2.force_login(user)
            client2.get(f"{url}?step=1")
            self.assertEqual(run, ["step1", "step2"])
            lock_file = Path("locks") / f"release_publish_{self.release.pk}.json"
            self.assertFalse(lock_file.exists())

    def test_release_progress_restart(self):
        run = []

        def step_fail(release, ctx, log_path):
            run.append("step")
            raise Exception("boom")

        steps = [("Fail", step_fail)]
        user = User.objects.create_superuser("admin", "admin@example.com", "pw")
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        count_file = Path("locks") / f"release_publish_{self.release.pk}.restarts"
        if count_file.exists():
            count_file.unlink()
        with mock.patch("core.views.PUBLISH_STEPS", steps):
            self.client.force_login(user)
            self.assertFalse(count_file.exists())
            self.client.get(f"{url}?step=0")
            self.client.get(f"{url}?step=0")
            self.assertEqual(run, ["step"])
            self.assertFalse(count_file.exists())
            self.client.get(f"{url}?restart=1")
            self.assertTrue(count_file.exists())
            self.assertEqual(count_file.read_text(), "1")
            self.client.get(f"{url}?step=0")
            self.assertEqual(run, ["step", "step"])
            self.client.get(f"{url}?restart=1")
            # Restart counter resets after running a step
            self.assertEqual(count_file.read_text(), "1")


class ReleaseProgressSyncTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser("admin", "admin@example.com", "pw")
        self.client.force_login(self.user)
        self.package = Package.objects.get(name="arthexis")
        self.version_path = Path("VERSION")
        self.original_version = self.version_path.read_text(encoding="utf-8")
        self.version_path.write_text("1.2.3", encoding="utf-8")

    def tearDown(self):
        self.version_path.write_text(self.original_version, encoding="utf-8")

    @mock.patch("core.views.PackageRelease.dump_fixture")
    @mock.patch("core.views.revision.get_revision", return_value="abc123")
    def test_unpublished_release_syncs_version_and_revision(
        self, get_revision, dump_fixture
    ):
        release = PackageRelease.objects.create(
            package=self.package,
            version="1.0.0",
        )
        release.revision = "oldrev"
        release.save(update_fields=["revision"])

        url = reverse("release-progress", args=[release.pk, "publish"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        release.refresh_from_db()
        self.assertEqual(release.version, "1.2.4")
        self.assertEqual(release.revision, "abc123")
        dump_fixture.assert_called_once()

    def test_published_release_not_current_returns_404(self):
        release = PackageRelease.objects.create(
            package=self.package,
            version="1.2.4",
            pypi_url="https://example.com",
        )

        url = reverse("release-progress", args=[release.pk, "publish"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)


class ReleaseProgressFixtureVisibilityTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            "fixture-check", "fixture@example.com", "pw"
        )
        self.client.force_login(self.user)
        current_version = Path("VERSION").read_text(encoding="utf-8").strip()
        package = Package.objects.filter(is_active=True).first()
        if package is None:
            package = Package.objects.create(name="fixturepkg", is_active=True)
        try:
            self.release = PackageRelease.objects.get(
                package=package, version=current_version
            )
        except PackageRelease.DoesNotExist:
            self.release = PackageRelease.objects.create(
                package=package, version=current_version
            )
        self.session_key = f"release_publish_{self.release.pk}"
        self.log_name = f"{self.release.package.name}-{self.release.version}.log"
        self.lock_path = Path("locks") / f"{self.session_key}.json"
        self.restart_path = Path("locks") / f"{self.session_key}.restarts"
        self.log_path = Path("logs") / self.log_name
        for path in (self.lock_path, self.restart_path, self.log_path):
            if path.exists():
                path.unlink()
        try:
            self.fixture_step_index = next(
                idx
                for idx, (name, _) in enumerate(core_views.PUBLISH_STEPS)
                if name == core_views.FIXTURE_REVIEW_STEP_NAME
            )
        except StopIteration:  # pragma: no cover - defensive guard
            self.fail("Fixture review step not configured in publish steps")
        self.url = reverse("release-progress", args=[self.release.pk, "publish"])

    def tearDown(self):
        session = self.client.session
        if self.session_key in session:
            session.pop(self.session_key)
            session.save()
        for path in (self.lock_path, self.restart_path, self.log_path):
            if path.exists():
                path.unlink()
        super().tearDown()

    def _set_session(self, step: int, fixtures: list[dict]):
        session = self.client.session
        session[self.session_key] = {
            "step": step,
            "fixtures": fixtures,
            "log": self.log_name,
            "started": True,
        }
        session.save()

    def test_fixture_summary_visible_until_migration_step(self):
        fixtures = [
            {
                "path": "core/fixtures/example.json",
                "count": 2,
                "models": ["core.Model"],
            }
        ]
        self._set_session(self.fixture_step_index, fixtures)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["fixtures"], fixtures)
        self.assertContains(response, "Fixture changes")

    def test_fixture_summary_hidden_after_migration_step(self):
        fixtures = [
            {
                "path": "core/fixtures/example.json",
                "count": 2,
                "models": ["core.Model"],
            }
        ]
        self._set_session(self.fixture_step_index + 1, fixtures)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["fixtures"])
        self.assertNotContains(response, "Fixture changes")


class PackageReleaseAdminActionTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = PackageReleaseAdmin(PackageRelease, self.site)
        self.admin.message_user = lambda *args, **kwargs: None
        self.package = Package.objects.create(name="pkg")
        self.package.is_active = True
        self.package.save(update_fields=["is_active"])
        self.release = PackageRelease.objects.create(
            package=self.package,
            version="1.0.0",
            pypi_url="https://pypi.org/project/pkg/1.0.0/",
        )
        self.request = self.factory.get("/")

    @mock.patch("core.admin.PackageRelease.dump_fixture")
    @mock.patch("core.admin.requests.get")
    def test_validate_deletes_missing_release(self, mock_get, dump):
        mock_get.return_value.status_code = 404
        self.admin.validate_releases(self.request, PackageRelease.objects.all())
        self.assertEqual(PackageRelease.objects.count(), 0)
        dump.assert_called_once()

    @mock.patch("core.admin.PackageRelease.dump_fixture")
    @mock.patch("core.admin.requests.get")
    def test_validate_keeps_existing_release(self, mock_get, dump):
        mock_get.return_value.status_code = 200
        self.admin.validate_releases(self.request, PackageRelease.objects.all())
        self.assertEqual(PackageRelease.objects.count(), 1)
        dump.assert_not_called()

    @mock.patch("core.admin.PackageRelease.dump_fixture")
    @mock.patch("core.admin.requests.get")
    def test_refresh_from_pypi_creates_releases(self, mock_get, dump):
        mock_get.return_value.raise_for_status.return_value = None
        mock_get.return_value.json.return_value = {
            "releases": {
                "1.0.0": [
                    {"upload_time_iso_8601": "2024-01-01T12:30:00.000000Z"}
                ],
                "1.1.0": [
                    {"upload_time_iso_8601": "2024-02-02T15:45:00.000000Z"}
                ],
            }
        }
        self.admin.refresh_from_pypi(self.request, PackageRelease.objects.none())
        new_release = PackageRelease.objects.get(version="1.1.0")
        self.assertEqual(new_release.revision, "")
        self.assertEqual(
            new_release.release_on,
            datetime(2024, 2, 2, 15, 45, tzinfo=datetime_timezone.utc),
        )
        dump.assert_called_once()

    @mock.patch("core.admin.PackageRelease.dump_fixture")
    @mock.patch("core.admin.requests.get")
    def test_refresh_from_pypi_updates_release_date(self, mock_get, dump):
        self.release.release_on = None
        self.release.save(update_fields=["release_on"])
        mock_get.return_value.raise_for_status.return_value = None
        mock_get.return_value.json.return_value = {
            "releases": {
                "1.0.0": [
                    {"upload_time_iso_8601": "2024-01-01T12:30:00.000000Z"}
                ]
            }
        }
        self.admin.refresh_from_pypi(self.request, PackageRelease.objects.none())
        self.release.refresh_from_db()
        self.assertEqual(
            self.release.release_on,
            datetime(2024, 1, 1, 12, 30, tzinfo=datetime_timezone.utc),
        )
        dump.assert_called_once()

    @mock.patch("core.admin.PackageRelease.dump_fixture")
    @mock.patch("core.admin.requests.get")
    def test_refresh_from_pypi_restores_deleted_release(self, mock_get, dump):
        self.release.is_deleted = True
        self.release.save(update_fields=["is_deleted"])
        mock_get.return_value.raise_for_status.return_value = None
        mock_get.return_value.json.return_value = {
            "releases": {
                "1.0.0": [
                    {"upload_time_iso_8601": "2024-01-01T12:30:00.000000Z"}
                ]
            }
        }

        self.admin.refresh_from_pypi(self.request, PackageRelease.objects.none())

        self.assertTrue(
            PackageRelease.objects.filter(version="1.0.0").exists()
        )
        dump.assert_called_once()


class PackageActiveTests(TestCase):
    def test_only_one_active_package(self):
        default = Package.objects.get(name="arthexis")
        self.assertTrue(default.is_active)
        other = Package.objects.create(name="pkg", is_active=True)
        default.refresh_from_db()
        other.refresh_from_db()
        self.assertFalse(default.is_active)
        self.assertTrue(other.is_active)


class PackageReleaseCurrentTests(TestCase):
    def setUp(self):
        self.package = Package.objects.get(name="arthexis")
        self.version_path = Path("VERSION")
        self.original = self.version_path.read_text()
        self.version_path.write_text("1.0.0")
        self.release = PackageRelease.objects.create(
            package=self.package, version="1.0.0"
        )

    def tearDown(self):
        self.version_path.write_text(self.original)

    def test_is_current_true_when_version_matches_and_package_active(self):
        self.assertTrue(self.release.is_current)

    def test_is_current_false_when_package_inactive(self):
        self.package.is_active = False
        self.package.save()
        self.assertFalse(self.release.is_current)

    def test_is_current_false_when_version_differs(self):
        self.release.version = "2.0.0"
        self.release.save()
        self.assertFalse(self.release.is_current)


class PackageReleaseChangelistTests(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_superuser("admin", "admin@example.com", "pw")
        self.client.force_login(User.objects.get(username="admin"))

    def test_prepare_next_release_button_present(self):
        response = self.client.get(reverse("admin:core_packagerelease_changelist"))
        prepare_url = reverse(
            "admin:core_packagerelease_actions", args=["prepare_next_release"]
        )
        self.assertContains(response, prepare_url, html=False)

    def test_refresh_from_pypi_button_present(self):
        response = self.client.get(reverse("admin:core_packagerelease_changelist"))
        refresh_url = reverse(
            "admin:core_packagerelease_actions", args=["refresh_from_pypi"]
        )
        self.assertContains(response, refresh_url, html=False)

    def test_prepare_next_release_action_creates_release(self):
        package = Package.objects.get(name="arthexis")
        PackageRelease.all_objects.filter(package=package).delete()
        response = self.client.post(
            reverse(
                "admin:core_packagerelease_actions", args=["prepare_next_release"]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            PackageRelease.all_objects.filter(package=package).exists()
        )


class PackageAdminPrepareNextReleaseTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.site = AdminSite()
        self.admin = PackageAdmin(Package, self.site)
        self.admin.message_user = lambda *args, **kwargs: None
        self.package = Package.objects.get(name="arthexis")

    def test_prepare_next_release_active_creates_release(self):
        PackageRelease.all_objects.filter(package=self.package).delete()
        request = self.factory.get("/admin/core/package/prepare-next-release/")
        response = self.admin.prepare_next_release_active(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            PackageRelease.all_objects.filter(package=self.package).count(), 1
        )


class PackageAdminChangeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_superuser("admin", "admin@example.com", "pw")
        self.client.force_login(User.objects.get(username="admin"))
        self.package = Package.objects.get(name="arthexis")

    def test_prepare_next_release_button_visible_on_change_view(self):
        response = self.client.get(
            reverse("admin:core_package_change", args=[self.package.pk])
        )
        self.assertContains(response, "Prepare next Release")


class TodoDoneTests(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_superuser("admin", "admin@example.com", "pw")
        self.client.force_login(User.objects.get(username="admin"))

    def test_mark_done_sets_timestamp(self):
        todo = Todo.objects.create(request="Task", is_seed_data=True)
        resp = self.client.post(reverse("todo-done", args=[todo.pk]))
        self.assertRedirects(resp, reverse("admin:index"))
        todo.refresh_from_db()
        self.assertIsNotNone(todo.done_on)
        self.assertFalse(todo.is_deleted)

    def test_mark_done_condition_failure_shows_message(self):
        todo = Todo.objects.create(
            request="Task",
            on_done_condition="1 = 0",
        )
        resp = self.client.post(reverse("todo-done", args=[todo.pk]))
        self.assertRedirects(resp, reverse("admin:index"))
        messages = [m.message for m in get_messages(resp.wsgi_request)]
        self.assertTrue(messages)
        self.assertIn("1 = 0", messages[0])
        todo.refresh_from_db()
        self.assertIsNone(todo.done_on)

    def test_mark_done_condition_invalid_expression(self):
        todo = Todo.objects.create(
            request="Task",
            on_done_condition="1; SELECT 1",
        )
        resp = self.client.post(reverse("todo-done", args=[todo.pk]))
        self.assertRedirects(resp, reverse("admin:index"))
        messages = [m.message for m in get_messages(resp.wsgi_request)]
        self.assertTrue(messages)
        self.assertIn("Semicolons", messages[0])
        todo.refresh_from_db()
        self.assertIsNone(todo.done_on)

    def test_mark_done_condition_resolves_sigils(self):
        todo = Todo.objects.create(
            request="Task",
            on_done_condition="[TEST]",
        )
        with mock.patch.object(Todo, "resolve_sigils", return_value="1 = 1") as resolver:
            resp = self.client.post(reverse("todo-done", args=[todo.pk]))
        self.assertRedirects(resp, reverse("admin:index"))
        resolver.assert_called_once_with("on_done_condition")
        todo.refresh_from_db()
        self.assertIsNotNone(todo.done_on)

    def test_mark_done_respects_next_parameter(self):
        todo = Todo.objects.create(request="Task")
        next_url = reverse("admin:index") + "?section=todos"
        resp = self.client.post(
            reverse("todo-done", args=[todo.pk]),
            {"next": next_url},
        )
        self.assertRedirects(resp, next_url, target_status_code=200)
        todo.refresh_from_db()
        self.assertIsNotNone(todo.done_on)

    def test_mark_done_rejects_external_next(self):
        todo = Todo.objects.create(request="Task")
        resp = self.client.post(
            reverse("todo-done", args=[todo.pk]),
            {"next": "https://example.com/"},
        )
        self.assertRedirects(resp, reverse("admin:index"))
        todo.refresh_from_db()
        self.assertIsNotNone(todo.done_on)


class TodoFocusViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_superuser("admin", "admin@example.com", "pw")
        self.client.force_login(User.objects.get(username="admin"))

    def test_focus_view_renders_requested_page(self):
        todo = Todo.objects.create(request="Task", url="/docs/")
        next_url = reverse("admin:index")
        resp = self.client.get(
            f"{reverse('todo-focus', args=[todo.pk])}?next={quote(next_url)}"
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, todo.request)
        self.assertEqual(resp["X-Frame-Options"], "SAMEORIGIN")
        self.assertContains(resp, f'src="{todo.url}"')
        self.assertContains(resp, "Done")
        self.assertContains(resp, "Back")

    def test_focus_view_uses_admin_change_when_no_url(self):
        todo = Todo.objects.create(request="Task")
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        change_url = reverse("admin:core_todo_change", args=[todo.pk])
        self.assertContains(resp, f'src="{change_url}"')

    def test_focus_view_includes_open_target_button(self):
        todo = Todo.objects.create(request="Task", url="/docs/")
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        self.assertContains(resp, 'class="todo-button todo-button-open"')
        self.assertContains(resp, 'target="_blank"')
        self.assertContains(resp, 'href="/docs/"')

    def test_focus_view_sanitizes_loopback_absolute_url(self):
        todo = Todo.objects.create(
            request="Task",
            url="http://127.0.0.1:8000/docs/?section=chart",
        )
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        self.assertContains(resp, 'src="/docs/?section=chart"')

    def test_focus_view_rejects_external_absolute_url(self):
        todo = Todo.objects.create(
            request="Task",
            url="https://outside.invalid/external/",
        )
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        change_url = reverse("admin:core_todo_change", args=[todo.pk])
        self.assertContains(resp, f'src="{change_url}"')

    def test_focus_view_avoids_recursive_focus_url(self):
        todo = Todo.objects.create(request="Task")
        focus_url = reverse("todo-focus", args=[todo.pk])
        Todo.objects.filter(pk=todo.pk).update(url=focus_url)
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        change_url = reverse("admin:core_todo_change", args=[todo.pk])
        self.assertContains(resp, f'src="{change_url}"')

    def test_focus_view_avoids_recursive_focus_absolute_url(self):
        todo = Todo.objects.create(request="Task")
        focus_url = reverse("todo-focus", args=[todo.pk])
        Todo.objects.filter(pk=todo.pk).update(url=f"http://testserver{focus_url}")
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        change_url = reverse("admin:core_todo_change", args=[todo.pk])
        self.assertContains(resp, f'src="{change_url}"')

    def test_focus_view_parses_auth_directives(self):
        todo = Todo.objects.create(
            request="Task",
            url="/docs/?section=chart&_todo_auth=logout&_todo_auth=user:demo&_todo_auth=perm:core.view_user&_todo_auth=extra",
        )
        resp = self.client.get(reverse("todo-focus", args=[todo.pk]))
        self.assertContains(resp, 'src="/docs/?section=chart"')
        self.assertContains(resp, 'href="/docs/?section=chart"')
        self.assertContains(resp, "logged out")
        self.assertContains(resp, "Sign in using: demo")
        self.assertContains(resp, "Required permissions: core.view_user")
        self.assertContains(resp, "Additional authentication notes: extra")

    def test_focus_view_redirects_if_todo_completed(self):
        todo = Todo.objects.create(request="Task")
        todo.done_on = timezone.now()
        todo.save(update_fields=["done_on"])
        next_url = reverse("admin:index")
        resp = self.client.get(
            f"{reverse('todo-focus', args=[todo.pk])}?next={quote(next_url)}"
        )
        self.assertRedirects(resp, next_url, target_status_code=200)


class TodoUrlValidationTests(TestCase):
    def test_relative_url_valid(self):
        todo = Todo(request="Task", url="/path")
        todo.full_clean()  # should not raise

    def test_absolute_url_invalid(self):
        todo = Todo(request="Task", url="https://example.com/path")
        with self.assertRaises(ValidationError):
            todo.full_clean()


class TodoUniqueTests(TestCase):
    def test_request_unique_case_insensitive(self):
        Todo.objects.create(request="Task")
        with self.assertRaises(IntegrityError):
            Todo.objects.create(request="task")


class TodoAdminPermissionTests(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_superuser("admin", "admin@example.com", "pw")
        self.client.force_login(User.objects.get(username="admin"))

    def test_add_view_disallowed(self):
        resp = self.client.get(reverse("admin:core_todo_add"))
        self.assertEqual(resp.status_code, 403)

    def test_change_form_loads(self):
        todo = Todo.objects.create(request="Task")
        resp = self.client.get(reverse("admin:core_todo_change", args=[todo.pk]))
        self.assertEqual(resp.status_code, 200)
