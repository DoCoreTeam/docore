import os
import shutil
import sys

from domangcha.orchestration.contracts import RuntimeCapabilities


class RuntimeDetector:
    def detect(self) -> RuntimeCapabilities:
        explicit = os.environ.get("DOMANGCHA_RUNTIME", "").upper()
        if explicit:
            return self._profile(explicit)
        if os.environ.get("CODEX_CLOUD"):
            return self._profile("CODEX_CLOUD")
        if os.environ.get("CODEX_HOME") or shutil.which("codex"):
            kind = "CODEX_IDE" if os.environ.get("TERM_PROGRAM", "").lower() in {"vscode", "cursor"} else "CODEX_LOCAL"
            return self._profile(kind)
        if os.environ.get("CLAUDE_PROJECT_DIR") or shutil.which("claude"):
            return self._profile("CLAUDE_CODE")
        return self._profile("UNKNOWN")

    @staticmethod
    def _profile(kind: str) -> RuntimeCapabilities:
        interactive = sys.stdin.isatty() and kind != "CODEX_CLOUD"
        return RuntimeCapabilities(
            runtime=kind,
            interactive_approval=interactive,
            background_execution=kind == "CODEX_CLOUD",
            subagents=kind in {"CLAUDE_CODE", "CODEX_LOCAL", "CODEX_IDE", "CODEX_CLOUD"},
            hooks=kind in {"CLAUDE_CODE", "CODEX_LOCAL", "CODEX_IDE"},
            shell=kind != "UNKNOWN",
            network=kind != "UNKNOWN",
            browser=kind in {"CLAUDE_CODE", "CODEX_LOCAL", "CODEX_IDE"},
            checkpointing=True,
            parallelism=4 if kind != "UNKNOWN" else 1,
            workspace_write=kind != "UNKNOWN",
        )
