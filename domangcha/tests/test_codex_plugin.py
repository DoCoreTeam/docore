import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PLUGIN = ROOT / "plugins" / "domangcha"


def invoke(script, payload, cwd):
    return subprocess.run(
        ["python3", str(PLUGIN / "scripts" / script)],
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        cwd=cwd,
        check=False,
    )


class CodexPluginTests(unittest.TestCase):
    def test_manifest_and_hooks_exist(self):
        manifest = json.loads((PLUGIN / ".codex-plugin/plugin.json").read_text())
        hooks = json.loads((PLUGIN / "hooks/hooks.json").read_text())
        self.assertEqual(manifest["name"], "domangcha")
        self.assertIn("UserPromptSubmit", hooks["hooks"])
        self.assertIn("Stop", hooks["hooks"])

    def test_hook_driven_loop_completion(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            base = {"cwd": folder, "session_id": "session-1"}
            started = invoke("user_prompt.py", {**base, "prompt": "Fix this bug and run tests"}, root)
            self.assertEqual(started.returncode, 0, started.stderr)
            context = json.loads(started.stdout)["hookSpecificOutput"]["additionalContext"]
            self.assertIn("route=LOOP", context)
            task_id = context.split("task_id=", 1)[1].split(" ", 1)[0]

            mutation = invoke("tool_event.py", {
                **base,
                "hook_event_name": "PostToolUse",
                "tool_name": "apply_patch",
                "tool_input": {"command": "patch"},
                "tool_response": {"ok": True},
            }, root)
            self.assertEqual(mutation.returncode, 0)
            validation = invoke("tool_event.py", {
                **base,
                "hook_event_name": "PostToolUse",
                "tool_name": "Bash",
                "tool_input": {"command": "python3 -m unittest"},
                "tool_response": {"exit_code": 0},
            }, root)
            self.assertEqual(validation.returncode, 0)

            completed = subprocess.run([
                "python3", str(PLUGIN / "scripts/control.py"), "complete",
                "--task-id", task_id, "--workspace", folder, "--summary", "fixed",
            ], text=True, capture_output=True, cwd=root, check=False)
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            stopped = invoke("stop.py", {**base, "hook_event_name": "Stop"}, root)
            self.assertEqual(json.loads(stopped.stdout), {})

    def test_stop_continues_without_evidence(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            base = {"cwd": folder, "session_id": "session-2"}
            invoke("user_prompt.py", {**base, "prompt": "Refactor this iteratively"}, root)
            invoke("tool_event.py", {
                **base,
                "hook_event_name": "PostToolUse",
                "tool_name": "apply_patch",
                "tool_input": {"command": "patch"},
                "tool_response": {"ok": True},
            }, root)
            stopped = invoke("stop.py", {**base, "hook_event_name": "Stop"}, root)
            result = json.loads(stopped.stdout)
            self.assertEqual(result["decision"], "block")
            self.assertIn("validation", result["reason"])

            continued = invoke("user_prompt.py", {**base, "prompt": result["reason"]}, root)
            context = json.loads(continued.stdout)["hookSpecificOutput"]["additionalContext"]
            original = json.loads((root / ".domangcha/codex/sessions/session-2.json").read_text())
            self.assertIn("task_id=" + original["task_id"], context)
            checkpoints = list((root / ".domangcha/checkpoints").glob("*.json"))
            self.assertEqual(len(checkpoints), 1)

    def test_direct_task_closes_before_next_prompt(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            base = {"cwd": folder, "session_id": "session-3"}
            first = invoke("user_prompt.py", {**base, "prompt": "Explain this function"}, root)
            first_context = json.loads(first.stdout)["hookSpecificOutput"]["additionalContext"]
            first_id = first_context.split("task_id=", 1)[1].split(" ", 1)[0]
            invoke("stop.py", {**base, "hook_event_name": "Stop"}, root)
            second = invoke("user_prompt.py", {**base, "prompt": "Format this text"}, root)
            second_context = json.loads(second.stdout)["hookSpecificOutput"]["additionalContext"]
            second_id = second_context.split("task_id=", 1)[1].split(" ", 1)[0]
            self.assertNotEqual(first_id, second_id)


if __name__ == "__main__":
    unittest.main()
