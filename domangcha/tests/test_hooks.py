import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HOOKS = ROOT / "domangcha" / "hooks"


def fake_home(folder):
    """A home directory whose ~/.domangcha resolves to this repository."""
    home = Path(folder) / "home"
    home.mkdir()
    (home / ".domangcha").symlink_to(ROOT)
    return home


def run_hook(name, home, payload=None, project_root=None):
    env = dict(os.environ, HOME=str(home))
    if project_root is not None:
        env["CLAUDE_PROJECT_DIR"] = str(project_root)
    return subprocess.run(
        ["bash", str(HOOKS / name)],
        input=json.dumps(payload) if payload is not None else "",
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


class StopHookTests(unittest.TestCase):
    def test_unrelated_project_keeping_its_own_version_file_is_skipped(self):
        with tempfile.TemporaryDirectory() as folder:
            home = fake_home(folder)
            app = Path(folder) / "app"
            (app / "domangcha").mkdir(parents=True)
            (app / "domangcha/VERSION").write_text("0.1.63\n")
            (app / "package.json").write_text('{"name": "app"}\n')
            result = run_hook("domangcha-stop.sh", home, project_root=app)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")

    def test_repository_shaped_project_is_still_validated(self):
        with tempfile.TemporaryDirectory() as folder:
            home = fake_home(folder)
            repo = Path(folder) / "repo"
            (repo / "domangcha/manifests").mkdir(parents=True)
            (repo / "domangcha/VERSION").write_text("2.3.0\n")
            (repo / "package.json").write_text('{"name": "repo"}\n')
            (repo / "domangcha/manifests/agents.json").write_text(
                json.dumps({"roles": [{"id": "dc-absent"}]})
            )
            result = run_hook("domangcha-stop.sh", home, project_root=repo)
        self.assertEqual(result.returncode, 2)
        self.assertIn("DOMANGCHA STOP VALIDATION FAILED", result.stderr)


class PostEditHookTests(unittest.TestCase):
    def test_project_root_search_stops_at_home(self):
        with tempfile.TemporaryDirectory() as folder:
            home = Path(folder) / "home"
            hooks = home / ".claude" / "hooks"
            hooks.mkdir(parents=True)
            (home / "package.json").write_text('{"name": "home-monorepo"}\n')
            edited = hooks / "sample.sh"
            edited.write_text("echo hook\n")
            result = run_hook(
                "domangcha-post-edit.sh",
                home,
                payload={"tool_input": {"file_path": str(edited)}},
            )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
