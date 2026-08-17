"""Compares this source repository with the installed runtime.

install.sh copies a subset of the repository into ~/.domangcha, and every
project except this one runs that copy. Fixing the source without redeploying
therefore leaves the fix inert, and the two VERSION files still agree, so a
version check cannot see it. Only file content can. This report is read-only
and never fails a build: drift before a release is normal, not an error.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_INSTALL = Path.home() / ".domangcha" / "domangcha"
DEPLOYED_PARTS = ("engine.py", "VERSION", "orchestration", "adapters", "manifests", "graphs", "policies")
IGNORED_NAMES = {"__pycache__", ".DS_Store"}


def _ignored(path: Path) -> bool:
    return path.suffix == ".pyc" or bool(IGNORED_NAMES.intersection(path.parts))


def _deployed_files(base: Path) -> Dict[str, Path]:
    found: Dict[str, Path] = {}
    for part in DEPLOYED_PARTS:
        target = base / part
        if target.is_file():
            found[part] = target
        elif target.is_dir():
            for path in sorted(target.rglob("*")):
                if path.is_file() and not _ignored(path):
                    found[str(path.relative_to(base))] = path
    return found


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _version(base: Path) -> str:
    try:
        return (base / "VERSION").read_text().strip()
    except OSError:
        return "unknown"


class DeploymentInspector:
    """Reports which deployed files differ between source and installed runtime."""

    def __init__(self, root: Path, install: Optional[Path] = None):
        self.source = Path(root) / "domangcha"
        self.install = Path(install) if install is not None else DEFAULT_INSTALL

    def report(self) -> Dict[str, Any]:
        base = {
            "install_path": str(self.install),
            "source_version": _version(self.source),
            "installed_version": _version(self.install),
        }
        if not self.install.is_dir():
            return {**base, "installed": False, "changed": [], "missing": []}
        installed = _deployed_files(self.install)
        changed: List[str] = []
        missing: List[str] = []
        for name, path in sorted(_deployed_files(self.source).items()):
            counterpart = installed.get(name)
            if counterpart is None:
                missing.append(name)
            elif _digest(path) != _digest(counterpart):
                changed.append(name)
        return {**base, "installed": True, "changed": changed, "missing": missing}
