import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TEMPLATES = ROOT / "domangcha" / "loop" / "templates"
ENFORCER = ROOT / "domangcha" / "hooks" / "domangcha-ceo-enforcer.py"

TEMPLATE_FILES = [
    Path("LOOP.md"),
    Path("CLAUDE.md"),
    Path("LOOP.en.md"),
    Path("CLAUDE.en.md"),
    Path("scripts/loop.mjs"),
    Path(".claude/commands/plan.md"),
    Path(".claude/commands/loop.md"),
    Path(".claude/commands/policy.md"),
    Path(".cursor/rules/loop.mdc"),
]


def node_available():
    node = shutil.which("node")
    if not node:
        return False
    out = subprocess.run([node, "-v"], capture_output=True, text=True).stdout.strip()
    major, minor = (int(x) for x in out.lstrip("v").split(".")[:2])
    return (major, minor) >= (22, 13)


class TemplatePayloadTests(unittest.TestCase):
    def test_every_installed_template_ships_with_the_package(self):
        missing = [str(rel) for rel in TEMPLATE_FILES if not (TEMPLATES / rel).exists()]
        self.assertEqual(missing, [])

    def test_package_files_allowlist_covers_the_loop_templates(self):
        allowed = json.loads((ROOT / "package.json").read_text())["files"]
        self.assertTrue(any(entry.rstrip("/") == "domangcha" for entry in allowed))
        self.assertTrue(any(entry.rstrip("/") == "bin" for entry in allowed))

    def test_installer_entrypoints_stay_executable(self):
        for name in ("domangcha.sh", "domangcha-loop.mjs"):
            self.assertTrue(os.access(ROOT / "bin" / name, os.X_OK), name)

    def test_lightweight_default_never_writes_into_the_home_harness(self):
        """v2 global installs and v3 project installs must not share a path."""
        source = (ROOT / "bin" / "domangcha-loop.mjs").read_text()
        self.assertNotIn(".claude/agents", source)
        self.assertNotIn("homedir", source)


class VersionSurfaceTests(unittest.TestCase):
    def test_loop_cli_constant_matches_the_version_file(self):
        version = (ROOT / "domangcha" / "VERSION").read_text().strip()
        source = (TEMPLATES / "scripts" / "loop.mjs").read_text()
        pattern = re.compile(r'^const KIT_VERSION = "%s";$' % re.escape(version), re.M)
        self.assertRegex(source, pattern)

    def test_template_headers_match_the_version_file(self):
        version = (ROOT / "domangcha" / "VERSION").read_text().strip()
        for rel in (Path("LOOP.md"), Path("CLAUDE.md"), Path("LOOP.en.md"), Path("CLAUDE.en.md")):
            head = (TEMPLATES / rel).read_text().splitlines()[0]
            self.assertTrue(head.startswith("# DOMANGCHA v%s" % version), (rel, head))


class GlobalHookDeferralTests(unittest.TestCase):
    def _run(self, project_root, prompt="로그인 고쳐줘"):
        return subprocess.run(
            ["python3", str(ENFORCER)],
            input=json.dumps({"prompt": prompt}),
            env=dict(os.environ, CLAUDE_PROJECT_DIR=str(project_root)),
            text=True,
            capture_output=True,
            check=False,
        ).stdout

    def test_a_ceo_command_still_reaches_the_router_inside_a_loop_project(self):
        """Plain language stays in the loop; /ceo is how you ask for the harness."""
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / ".loop").mkdir()
            (project / "scripts").mkdir()
            (project / "scripts" / "loop.mjs").write_text("// stub\n")
            output = self._run(project, prompt="/ceo 결제 리팩터링")
        self.assertIn("ADAPTIVE ROUTER", output)
        self.assertIn("/ceo", output)

    def test_router_yields_to_a_project_running_the_lightweight_loop(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / ".loop").mkdir()
            (project / "scripts").mkdir()
            (project / "scripts" / "loop.mjs").write_text("// stub\n")
            output = self._run(project)
        self.assertIn("프로젝트 루프", output)
        self.assertNotIn("ADAPTIVE ROUTER", output)

    def test_router_still_owns_projects_without_the_lightweight_loop(self):
        with tempfile.TemporaryDirectory() as folder:
            output = self._run(Path(folder))
        self.assertIn("ADAPTIVE ROUTER", output)

    def test_half_installed_project_does_not_silence_the_router(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / ".loop").mkdir()
            output = self._run(project)
        self.assertIn("ADAPTIVE ROUTER", output)


@unittest.skipUnless(node_available(), "Node 22.13+ required for node:sqlite")
class LoopRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.project = Path(self.folder.name)
        (self.project / "scripts").mkdir()
        shutil.copy(TEMPLATES / "scripts" / "loop.mjs", self.project / "scripts" / "loop.mjs")
        self.loop("init", "--project", "sample")

    def tearDown(self):
        self.folder.cleanup()

    def loop(self, *args, stdin=""):
        result = subprocess.run(
            ["node", "scripts/loop.mjs", *args],
            cwd=self.project,
            input=stdin,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_init_creates_the_policy_ledger(self):
        self.assertTrue((self.project / ".loop" / "POLICY.md").exists())

    def test_a_plain_prompt_carries_the_protocol_without_a_slash_command(self):
        output = self.loop("hook", "prompt", stdin=json.dumps({"prompt": "로그인 화면 만들어줘"}))
        self.assertIn("지시 기록", output)
        self.assertIn("LOOP.md 1절", output)

    def test_a_promoted_policy_is_reinjected_on_every_later_prompt(self):
        self.loop("policy", "add", "--title", "i18n", "--rule", "메시지 파일을 함께 고친다")
        output = self.loop("hook", "prompt", stdin=json.dumps({"prompt": "이어서"}))
        self.assertIn("P001", output)
        self.assertIn("메시지 파일을 함께 고친다", output)

    def test_a_promoted_policy_survives_a_context_reset(self):
        self.loop("policy", "add", "--title", "i18n", "--rule", "메시지 파일을 함께 고친다")
        self.assertIn("P001", self.loop("resume"))

    def test_retired_policies_stop_being_injected(self):
        self.loop("policy", "add", "--title", "i18n", "--rule", "메시지 파일을 함께 고친다")
        self.loop("policy", "retire", "P001", "--reason", "구조 변경")
        self.assertNotIn("P001 i18n", self.loop("resume"))

    def test_a_ceo_prompt_offers_the_harness_instead_of_planning(self):
        output = self.loop("hook", "prompt", stdin=json.dumps({"prompt": "/ceo refactor everything"}))
        self.assertIn("/ceo", output)
        self.assertNotIn("LOOP.md 1절", output)


@unittest.skipUnless(node_available(), "Node 22.13+ required for node:sqlite")
class BilingualTests(unittest.TestCase):
    """An English project must not be handed Korean output or a Korean plan schema."""

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.project = Path(self.folder.name)
        (self.project / "scripts").mkdir()
        shutil.copy(TEMPLATES / "scripts" / "loop.mjs", self.project / "scripts" / "loop.mjs")
        self.loop("init", "--project", "sample", "--lang", "en")

    def tearDown(self):
        self.folder.cleanup()

    def loop(self, *args, stdin="", expect=0):
        result = subprocess.run(
            ["node", "scripts/loop.mjs", *args],
            cwd=self.project, input=stdin, text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, expect, result.stderr or result.stdout)
        return result.stdout

    def _english_plan(self):
        self.loop("plan", "new", "--title", "Login", "--instruction", "ins_0001", "--target", "v0.2.0")
        path = self.project / ".loop" / "PLAN.md"
        text = path.read_text()
        for placeholder, value in [
            ("- (what the user gets when this plan is done, 1-3 lines)", "- users can sign in"),
            ('- (what this plan does not do, or "none")', "- social login"),
            ("- (documents this whole plan must follow; for UI items name the design system INDEX path)", "- none"),
            ("### I01 (item title)", "### I01 Login form"),
            ('Scope: (files or directories to change; mark new files "new")', "Scope: src/login.js new"),
            ("- (a command and its expected result, e.g. pnpm test profile passes)", "- node -e \"1\" exits 0"),
            ("- (an observable condition, e.g. GET /api/profile returns 401 when unauthenticated)", "- empty password rejected"),
        ]:
            text = text.replace(placeholder, value)
        path.write_text(text)

    def test_the_plan_template_is_written_in_english(self):
        self._english_plan()
        self.assertIn("Plan ID:", (self.project / ".loop" / "PLAN.md").read_text())

    def test_an_english_plan_passes_check_and_confirm(self):
        self._english_plan()
        self.assertIn("plan check passed", self.loop("plan", "check"))
        self.assertIn("is active", self.loop("plan", "confirm"))

    def test_english_output_carries_no_korean(self):
        self._english_plan()
        self.loop("plan", "confirm")
        text = self.loop("start", "I01") + self.loop("resume")
        self.assertFalse(re.search(r"[가-힣]", text), text)

    def test_the_progress_card_reports_iteration_and_room(self):
        self._english_plan()
        self.loop("plan", "confirm")
        card = [x for x in self.loop("resume").splitlines() if x.startswith("🔁")]
        self.assertEqual(len(card), 1, self.loop("resume"))
        self.assertIn("items 0/1", card[0])
        self.assertIn("retries left", card[0])

    def test_a_korean_plan_still_parses_after_switching_to_english(self):
        """The parser reads both editions, so an existing plan survives the switch."""
        self.loop("config", "set", "lang", "ko")
        self.loop("plan", "new", "--title", "로그인", "--instruction", "ins_0001", "--target", "v0.2.0")
        self.loop("config", "set", "lang", "en")
        self.assertIn("P0001", self.loop("resume"))


if __name__ == "__main__":
    unittest.main()
