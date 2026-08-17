from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List

from .graph import GraphDefinition, GraphDefinitionError


class ValidationError(RuntimeError):
    pass


def _guarded(label: str, check: Callable[[], List[str]]) -> List[str]:
    """Report a broken repository as a validation error, never as a traceback."""
    try:
        return check()
    except ValidationError as exc:
        return [str(exc)]
    except (KeyError, TypeError, ValueError) as exc:
        return ["%s check aborted: %s: %s" % (label, type(exc).__name__, exc)]


class RepositoryValidator:
    def __init__(self, root: Path):
        self.root = root

    def validate_manifests(self) -> List[str]:
        return _guarded("manifest", self._check_manifests)

    def validate_versions(self) -> List[str]:
        return _guarded("version", self._check_versions)

    def _check_manifests(self) -> List[str]:
        errors = []
        agents = self._json("domangcha/manifests/agents.json")["roles"]
        actual_agents = {p.stem for p in (self.root / "domangcha/agents").glob("dc-*.md")}
        manifest_agents = {item["id"] for item in agents}
        if actual_agents != manifest_agents:
            errors.append("agent manifest mismatch")
        commands = set(self._json("domangcha/manifests/commands.json")["commands"])
        actual_commands = {p.stem for p in (self.root / "domangcha/commands").glob("ceo*.md")}
        if commands != actual_commands:
            errors.append("command manifest mismatch")
        return errors

    def _check_versions(self) -> List[str]:
        version = self._text("domangcha/VERSION").strip()
        errors = []
        manifest = self._json("domangcha/manifests/versions.json")
        for surface in manifest["surfaces"]:
            name, kind = surface["file"], surface["kind"]
            path = self.root / name
            if not path.exists():
                errors.append(name + " missing")
                continue
            if kind == "json":
                valid = self._json(name).get(surface["key"]) == version
            else:
                content = path.read_text()
                if kind == "shell":
                    pattern = r'^' + re.escape(surface["key"]) + r'="' + re.escape(version) + r'"$'
                elif kind == "header":
                    pattern = r"^# DOMANGCHA v" + re.escape(version) + r"\b"
                else:
                    pattern = r"version-" + re.escape(version) + r"\b"
                valid = bool(re.search(pattern, content, re.M))
            if not valid:
                errors.append(name + " version mismatch")
        return errors

    def validate_graphs(self) -> List[str]:
        errors = []
        for path in sorted((self.root / "domangcha/graphs").glob("*.json")):
            try:
                GraphDefinition.from_path(path)
            except (GraphDefinitionError, KeyError, TypeError, ValueError) as exc:
                errors.append(path.name + ": " + str(exc))
        return errors

    def validate_line_limits(self, paths: Iterable[Path], limit: int = 300) -> List[str]:
        exempt = {"install.sh"}
        errors = []
        for path in paths:
            if "insane-search" in path.parts or path.name in exempt or path.suffix not in {".py", ".js", ".ts", ".tsx", ".sh"}:
                continue
            count = len(path.read_text(errors="replace").splitlines())
            if count > limit:
                errors.append("%s:%d" % (path, count))
        return errors

    def assert_builder_reviewer(self, executions: List[Dict[str, Any]]) -> None:
        writers = {x["actor"] for x in executions if x.get("action") == "write"}
        reviewers = {x["actor"] for x in executions if x.get("action") == "review"}
        if writers.intersection(reviewers):
            raise ValidationError("builder and reviewer identities overlap")

    def _text(self, relative: str) -> str:
        try:
            return (self.root / relative).read_text()
        except FileNotFoundError:
            raise ValidationError(relative + " missing") from None
        except OSError as exc:
            raise ValidationError(relative + " unreadable: " + str(exc.strerror)) from None

    def _json(self, relative: str) -> Dict[str, Any]:
        try:
            return json.loads(self._text(relative))
        except json.JSONDecodeError as exc:
            raise ValidationError(relative + " invalid json: " + str(exc)) from None
