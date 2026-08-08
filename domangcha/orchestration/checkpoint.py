from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from .security import redact


class CheckpointStore:
    VERSION = 1

    def __init__(self, root: Path):
        self.root = root

    def write(self, task_id: str, state: Dict[str, Any]) -> Path:
        self.root.mkdir(parents=True, exist_ok=True)
        path = self.root / (task_id + ".json")
        payload = redact(dict(state))
        payload["checkpoint_version"] = self.VERSION
        payload["updated_at"] = datetime.now(timezone.utc).isoformat()
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(str(tmp), str(path))
        return path

    def read(self, task_id: str) -> Dict[str, Any]:
        path = self.root / (task_id + ".json")
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("checkpoint_version") != self.VERSION:
            raise ValueError("incompatible checkpoint version")
        return data
