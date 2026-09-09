from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional


def workspace(payload: Dict[str, Any]) -> Path:
    return Path(payload.get("cwd") or os.getcwd()).resolve()


def load_engine(root: Path):
    candidates = [
        root,
        Path.home() / ".domangcha",
        Path(__file__).resolve().parents[3],
    ]
    for candidate in candidates:
        if (candidate / "domangcha" / "engine.py").exists():
            sys.path.insert(0, str(candidate))
            from domangcha.orchestration.execution import ExecutionCoordinator
            return ExecutionCoordinator
    raise RuntimeError("DOMANGCHA engine is not installed; run npx domangcha outside a project")


def coordinator(root: Path):
    return load_engine(root)(root)


def reporter(root: Path, lang: Optional[str] = None):
    """Shared human-facing status renderer; None when the engine is unavailable."""
    try:
        load_engine(root)
        from domangcha.orchestration.status import StatusReporter

        return StatusReporter(lang)
    except Exception:
        return None


def session_path(root: Path, session_id: str) -> Path:
    safe = "".join(ch for ch in session_id if ch.isalnum() or ch in "-_") or "unknown"
    return root / ".domangcha" / "codex" / "sessions" / (safe + ".json")


def read_json(path: Path) -> Dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def write_json(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def active_session(root: Path, session_id: str) -> Dict[str, Any]:
    return read_json(session_path(root, session_id))


def save_session(root: Path, session_id: str, value: Dict[str, Any]) -> None:
    write_json(session_path(root, session_id), value)


def hook_payload() -> Dict[str, Any]:
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, TypeError):
        return {}


def checkpoint(root: Path, task_id: str) -> Dict[str, Any]:
    return coordinator(root).checkpoints.read(task_id)


def update_checkpoint(root: Path, task_id: str, state: Dict[str, Any]) -> None:
    coordinator(root).checkpoints.write(task_id, state)


def find_session_for_task(root: Path, task_id: str) -> Optional[Path]:
    folder = root / ".domangcha" / "codex" / "sessions"
    if not folder.exists():
        return None
    for path in folder.glob("*.json"):
        if read_json(path).get("task_id") == task_id:
            return path
    return None
