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


class InstallerLanguageTests(unittest.TestCase):
    """Install-time output cannot know the reader's language, so it carries both."""

    HANGUL = re.compile(r"[가-힣]")

    def test_the_loop_installer_pairs_every_korean_line_with_english(self):
        source = (ROOT / "bin" / "domangcha-loop.mjs").read_text()
        # say()/fail() take (en, ko); a bare Korean first argument would be Korean-only output.
        for call in re.findall(r"\b(?:say|fail)\(([^\n]*)", source):
            first = call.split(",")[0]
            self.assertFalse(self.HANGUL.search(first), call)

    def test_the_entrypoint_help_covers_both_languages(self):
        # Colour variables sit between the two languages, so compare with them stripped.
        plain = re.sub(r"\$\{(?:BR|DM|CY|NC)\}", "", (ROOT / "bin" / "domangcha.sh").read_text())
        self.assertIn("USAGE / 사용법", plain)
        self.assertIn("UPDATING / 업데이트", plain)

    def test_korean_is_dimmed_and_english_is_not(self):
        """Korean is there to be glanced at; English carries the message."""
        entry = (ROOT / "bin" / "domangcha.sh").read_text()
        self.assertIn("BR=$'\\033[1;37m'", entry)
        self.assertIn("DM=$'\\033[2m'", entry)
        # Colour is dropped when stdout is not a terminal, so piped output stays clean.
        self.assertIn('if [ -t 1 ] && [ -z "${NO_COLOR:-}" ]', entry)
        loop = (ROOT / "bin" / "domangcha-loop.mjs").read_text()
        self.assertIn("const dim = (t) => c('2', t);", loop)
        self.assertIn("process.stdout.isTTY && !process.env.NO_COLOR", loop)

    def test_the_harness_installer_prints_english_before_korean(self):
        source = (ROOT / "domangcha" / "install.sh").read_text()
        self.assertIn('"$label_en" "$label_ko"', source)
        reversed_labels = [
            line for line in source.splitlines()
            if re.search(r'[가-힣][^"]*/ [A-Za-z]', line)
        ]
        self.assertEqual(reversed_labels, [])


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



if __name__ == "__main__":
    unittest.main()
