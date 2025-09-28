import os
import sys
import json
from pathlib import Path
import shutil
import subprocess
from unittest import mock

sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Package, PackageRelease, Todo, ReleaseManager


class ReleaseProgressViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        User.all_objects.filter(username="admin").delete()
        self.user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="password"
        )
        self.client = self.client_class()
        self.client.force_login(self.user)
        self.package = Package.objects.create(name="pkg", is_active=True)
        self.release = PackageRelease.objects.create(
            package=self.package,
            version="1.0",
            revision="",
        )
        self.version_path = Path("VERSION")
        self.original_version = self.version_path.read_text(encoding="utf-8")
        self.version_path.write_text(self.release.version, encoding="utf-8")
        self.addCleanup(
            lambda: self.version_path.write_text(
                self.original_version, encoding="utf-8"
            )
        )
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        lock_path = Path("locks") / f"release_publish_{self.release.pk}.json"
        if lock_path.exists():
            lock_path.unlink()
        Todo.objects.all().delete()

    def tearDown(self):
        shutil.rmtree(self.log_dir, ignore_errors=True)

    def _assign_release_manager(self):
        manager = ReleaseManager.objects.create(
            user=self.user,
            pypi_token="pypi-test-token",
        )
        self.release.release_manager = manager
        self.release.save(update_fields=["release_manager"])
        return manager

    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    def test_stale_log_removed_on_start(self, git_clean):
        log_path = self.log_dir / (f"{self.package.name}-{self.release.version}.log")
        log_path.write_text("old data")

        url = reverse("release-progress", args=[self.release.pk, "publish"])
        response = self.client.get(url)

        self.assertTrue(log_path.exists())

        response = self.client.get(f"{url}?start=1&step=0")

        self.assertTrue(log_path.exists())
        self.assertNotIn("old data", response.context["log_content"])

    def test_log_hidden_before_start(self):
        log_path = self.log_dir / (f"{self.package.name}-{self.release.version}.log")
        log_path.write_text("old data")

        url = reverse("release-progress", args=[self.release.pk, "publish"])
        response = self.client.get(url)

        self.assertEqual(response.context["log_content"], "")

    def test_non_current_release_becomes_current(self):
        other = PackageRelease.objects.create(
            package=self.package, version="2.0", revision=""
        )
        url = reverse("release-progress", args=[other.pk, "publish"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        other.refresh_from_db()
        self.assertEqual(
            self.version_path.read_text(encoding="utf-8").strip(), other.version
        )

    def test_release_sync_updates_version_file_and_package(self):
        self.package.is_active = False
        self.package.save(update_fields=["is_active"])
        self.release.version = "1.1"
        self.release.save(update_fields=["version"])
        self.version_path.write_text("1.0", encoding="utf-8")

        url = reverse("release-progress", args=[self.release.pk, "publish"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.version_path.read_text(encoding="utf-8").strip(),
            self.release.version,
        )
        self.release.refresh_from_db()
        self.assertTrue(self.release.package.is_active)

    @mock.patch("core.views.release_utils._git_clean", return_value=False)
    @mock.patch("core.views.release_utils.network_available", return_value=False)
    def test_dirty_fixtures_committed(self, net, git_clean):
        fixture_path = Path("core/fixtures/releases__packagerelease_0_1_3.json")
        if fixture_path.exists():
            original = fixture_path.read_text(encoding="utf-8")
            self.addCleanup(
                lambda original=original: fixture_path.write_text(
                    original, encoding="utf-8"
                )
            )
        else:
            fixture_path.write_text("[]", encoding="utf-8")
            self.addCleanup(lambda: fixture_path.unlink(missing_ok=True))
        fixture_path.write_text("[]", encoding="utf-8")

        def fake_run(cmd, capture_output=False, text=False, check=False, **kwargs):
            if cmd[:3] == ["git", "status", "--porcelain"]:
                return subprocess.CompletedProcess(
                    cmd, 0, stdout=f" M {fixture_path}\n", stderr=""
                )
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        with mock.patch("core.views.subprocess.run", side_effect=fake_run):
            url = reverse("release-progress", args=[self.release.pk, "publish"])
            self.client.get(f"{url}?start=1&step=0")
            response = self.client.get(f"{url}?step=1")
        self.assertEqual(response.status_code, 200)

    def test_todos_must_be_acknowledged(self):
        todo = Todo.objects.create(request="Do something", url="/admin/")
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 1,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()
        response = self.client.get(f"{url}?step=1")
        self.assertEqual(
            response.context["todos"],
            [
                {
                    "id": todo.pk,
                    "request": "Do something",
                    "url": "/admin/",
                    "request_details": "",
                }
            ],
        )
        self.assertIsNone(response.context["next_step"])
        tmp_dir = Path("tmp_todos")
        tmp_dir.mkdir(exist_ok=True)
        self.addCleanup(lambda: shutil.rmtree(tmp_dir, ignore_errors=True))
        fx = tmp_dir / f"todos__{todo.pk}.json"
        fx.write_text("[]", encoding="utf-8")
        with (
            mock.patch("core.views.TODO_FIXTURE_DIR", tmp_dir),
            mock.patch("core.views.subprocess.run"),
        ):
            self.client.get(f"{url}?ack_todos=1")
            response = self.client.get(f"{url}?step=1")
        self.assertFalse(Todo.objects.filter(is_deleted=False).exists())
        self.assertFalse(fx.exists())
        self.assertIsNone(response.context.get("todos"))
        self.assertEqual(response.context["next_step"], 2)

    def test_todo_ack_condition_failure_blocks_acknowledgement(self):
        todo = Todo.objects.create(
            request="Do something",
            on_done_condition="1 = 0",
        )
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 1,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()

        response = self.client.get(f"{url}?ack_todos=1")
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertTrue(messages)
        self.assertIn("1 = 0", messages[0])

        response = self.client.get(f"{url}?step=1")
        self.assertIsNone(response.context.get("next_step"))
        self.assertEqual(
            response.context["todos"],
            [
                {
                    "id": todo.pk,
                    "request": "Do something",
                    "url": "",
                    "request_details": "",
                }
            ],
        )

    def test_release_manager_approval_requires_input(self):
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 7,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()

        response = self.client.get(f"{url}?step=7")

        self.assertTrue(response.context["awaiting_approval"])
        self.assertIsNone(response.context["next_step"])
        self.assertFalse(response.context["approval_credentials_ready"])
        self.assertTrue(response.context["approval_credentials_missing"])
        self.assertIn(
            "Release manager publishing credentials missing",
            response.context["log_content"],
        )
        self.assertNotContains(response, 'name="approve"')
        self.assertContains(response, "Publishing credentials required")

    def test_release_manager_approval_accepts(self):
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        self._assign_release_manager()
        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 7,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()

        initial = self.client.get(f"{url}?step=7")
        self.assertTrue(initial.context["approval_credentials_ready"])
        response = self.client.get(f"{url}?approve=1&step=7")

        self.assertFalse(response.context["awaiting_approval"])
        self.assertEqual(response.context["current_step"], 8)
        self.assertEqual(response.context["next_step"], 8)
        self.assertIn(
            "Release manager approved release", response.context["log_content"]
        )

    def test_release_manager_rejection_aborts(self):
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        self._assign_release_manager()
        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 7,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()

        initial = self.client.get(f"{url}?step=7")
        self.assertTrue(initial.context["approval_credentials_ready"])
        response = self.client.get(f"{url}?reject=1&step=7")

        self.assertEqual(
            response.context["error"],
            "Release manager rejected the release. Restart required.",
        )
        self.assertFalse(response.context["awaiting_approval"])
        self.assertIsNone(response.context["next_step"])
        self.assertIn(
            "Release manager rejected release", response.context["log_content"]
        )

    @mock.patch("core.views.release_utils.network_available", return_value=False)
    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    def test_pause_publish_suspends_process(self, git_clean, net_available):
        url = reverse("release-progress", args=[self.release.pk, "publish"])
        self.client.get(url)
        self.client.get(f"{url}?start=1&step=0")
        lock_path = Path("locks") / f"release_publish_{self.release.pk}.json"
        self.assertTrue(lock_path.exists())

        response = self.client.get(f"{url}?pause=1")
        self.assertTrue(response.context["paused"])
        self.assertIsNone(response.context["next_step"])
        self.assertTrue(lock_path.exists())
        self.assertContains(response, "Continue Publish")

    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    @mock.patch("core.views.release_utils.network_available", return_value=False)
    def test_pre_release_commit(self, net, git_clean):
        original = Path("VERSION").read_text(encoding="utf-8")
        self.addCleanup(lambda: Path("VERSION").write_text(original, encoding="utf-8"))

        commands: list[list[str]] = []
        fixture_filename = "todos__create_release_pkg_1_0_1.json"

        def fake_run(cmd, capture_output=False, text=False, check=False, **kwargs):
            commands.append(cmd)
            if (
                cmd[:4] == ["git", "diff", "--cached", "--quiet"]
                and any(part.endswith(fixture_filename) for part in cmd)
            ):
                return subprocess.CompletedProcess(cmd, 1, stdout="", stderr="")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        tmp_dir = Path("tmp_todos_pre_release")
        tmp_dir.mkdir(exist_ok=True)
        self.addCleanup(lambda: shutil.rmtree(tmp_dir, ignore_errors=True))

        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 4,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()

        with mock.patch("core.views.TODO_FIXTURE_DIR", tmp_dir):
            with mock.patch("core.views.subprocess.run", side_effect=fake_run):
                url = reverse("release-progress", args=[self.release.pk, "publish"])
                response = self.client.get(f"{url}?step=4")

        self.assertIn(["scripts/generate-changelog.sh"], commands)
        self.assertEqual(response.status_code, 200)
        expected_request = "Create release pkg 1.0.1"
        todo = Todo.objects.get(request=expected_request)
        self.assertTrue(todo.is_seed_data)
        self.assertEqual(todo.url, reverse("admin:core_packagerelease_changelist"))
        self.assertIsNone(todo.done_on)
        fixture_path = tmp_dir / fixture_filename
        self.assertTrue(fixture_path.exists())
        data = json.loads(fixture_path.read_text(encoding="utf-8"))
        self.assertEqual(data[0]["fields"]["request"], expected_request)
        self.assertEqual(
            data[0]["fields"]["url"], reverse("admin:core_packagerelease_changelist")
        )

        log_path = Path("logs") / f"{self.package.name}-{self.release.version}.log"
        self.addCleanup(lambda: log_path.unlink(missing_ok=True))
        self.assertTrue(log_path.exists())
        log_content = log_path.read_text(encoding="utf-8")
        self.assertIn(
            "Regenerated CHANGELOG.rst using scripts/generate-changelog.sh",
            log_content,
        )
        self.assertIn("Staged CHANGELOG.rst for commit", log_content)
        self.assertIn(f"Added TODO: {expected_request}", log_content)
        self.assertIn(
            "Staged TODO fixture tmp_todos_pre_release/todos__create_release_pkg_1_0_1.json",
            log_content,
        )
        self.assertIn(
            "Committed TODO fixture tmp_todos_pre_release/todos__create_release_pkg_1_0_1.json",
            log_content,
        )
        self.assertEqual(
            Path("VERSION").read_text(encoding="utf-8").strip(),
            self.release.version,
        )
        self.assertIn("Execute pre-release actions", log_content)
        self.assertIn(
            f"Updated VERSION file to {self.release.version}", log_content
        )
        self.assertIn("Staged VERSION for commit", log_content)
        self.assertIn(
            "No changes detected for VERSION or CHANGELOG; skipping commit",
            log_content,
        )
        self.assertIn("Unstaged CHANGELOG.rst", log_content)
        self.assertIn("Unstaged VERSION file", log_content)
        self.assertIn("Pre-release actions complete", log_content)
        self.assertIn(
            ["git", "commit", "-m", "chore: add release TODO for pkg"], commands
        )

    @mock.patch("core.views.release_utils._git_clean", return_value=True)
    @mock.patch("core.views.release_utils.network_available", return_value=False)
    def test_pre_release_python_fallback(self, net, git_clean):
        original_version = Path("VERSION").read_text(encoding="utf-8")
        original_changelog = Path("CHANGELOG.rst").read_text(encoding="utf-8")
        self.addCleanup(
            lambda: Path("VERSION").write_text(original_version, encoding="utf-8")
        )
        self.addCleanup(
            lambda: Path("CHANGELOG.rst").write_text(
                original_changelog, encoding="utf-8"
            )
        )

        commands: list[list[str]] = []
        fixture_filename = "todos__create_release_pkg_1_0_1.json"
        changelog_entry = "- abc123 fix fallback generation"

        def fake_run(cmd, capture_output=False, text=False, check=False, **kwargs):
            commands.append(cmd)
            if cmd == ["scripts/generate-changelog.sh"]:
                err = OSError(193, "%1 is not a valid Win32 application")
                err.winerror = 193  # type: ignore[attr-defined]
                raise err
            if cmd[:3] == ["git", "describe", "--tags"]:
                return subprocess.CompletedProcess(cmd, 0, stdout="0.1.10\n", stderr="")
            if cmd[:2] == ["git", "log"]:
                return subprocess.CompletedProcess(
                    cmd, 0, stdout=f"{changelog_entry}\n", stderr=""
                )
            if (
                cmd[:3] == ["git", "diff", "--cached"]
                and any(part.endswith("CHANGELOG.rst") for part in cmd)
            ):
                return subprocess.CompletedProcess(cmd, 1, stdout="", stderr="")
            if (
                cmd[:3] == ["git", "diff", "--cached"]
                and any(part.endswith(fixture_filename) for part in cmd)
            ):
                return subprocess.CompletedProcess(cmd, 1, stdout="", stderr="")
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

        tmp_dir = Path("tmp_todos_pre_release_fallback")
        tmp_dir.mkdir(exist_ok=True)
        self.addCleanup(lambda: shutil.rmtree(tmp_dir, ignore_errors=True))

        session = self.client.session
        session_key = f"release_publish_{self.release.pk}"
        session[session_key] = {
            "step": 4,
            "log": f"{self.package.name}-{self.release.version}.log",
            "started": True,
        }
        session.save()

        with mock.patch("core.views.TODO_FIXTURE_DIR", tmp_dir):
            with mock.patch("core.views.subprocess.run", side_effect=fake_run):
                url = reverse("release-progress", args=[self.release.pk, "publish"])
                response = self.client.get(f"{url}?step=4")

        self.assertIn(["scripts/generate-changelog.sh"], commands)
        self.assertEqual(response.status_code, 200)
        log_path = Path("logs") / f"{self.package.name}-{self.release.version}.log"
        self.addCleanup(lambda: log_path.unlink(missing_ok=True))
        self.assertTrue(log_path.exists())
        log_content = log_path.read_text(encoding="utf-8")
        self.assertIn(
            "scripts/generate-changelog.sh failed: [Errno 193] %1 is not a valid Win32 application",
            log_content,
        )
        self.assertIn("Regenerated CHANGELOG.rst using Python fallback", log_content)
        self.assertIn("Staged CHANGELOG.rst for commit", log_content)
        self.assertEqual(
            Path("VERSION").read_text(encoding="utf-8").strip(),
            self.release.version,
        )
        self.assertIn(changelog_entry, Path("CHANGELOG.rst").read_text(encoding="utf-8"))
        todo = Todo.objects.get(request="Create release pkg 1.0.1")
        self.assertIsNone(todo.done_on)
        fixture_path = tmp_dir / fixture_filename
        self.assertTrue(fixture_path.exists())
        self.assertIn(
            "Committed TODO fixture tmp_todos_pre_release_fallback/"
            "todos__create_release_pkg_1_0_1.json",
            log_content,
        )
        self.assertIn("Pre-release actions complete", log_content)

    def test_todo_done_marks_timestamp(self):
        todo = Todo.objects.create(request="Task")
        url = reverse("todo-done", args=[todo.pk])
        tmp_dir = Path("tmp_todos2")
        tmp_dir.mkdir(exist_ok=True)
        self.addCleanup(lambda: shutil.rmtree(tmp_dir, ignore_errors=True))
        fx = tmp_dir / f"todos__{todo.pk}.json"
        fx.write_text("[]", encoding="utf-8")
        with mock.patch("core.views.TODO_FIXTURE_DIR", tmp_dir):
            response = self.client.post(url)
        self.assertRedirects(response, reverse("admin:index"))
        todo.refresh_from_db()
        self.assertIsNotNone(todo.done_on)
        self.assertTrue(fx.exists())
