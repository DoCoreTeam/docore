import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional


class EventWriter:
    def __init__(self, path: Optional[Path] = None):
        self.path = path

    def emit(self, event: str, **fields: Any) -> Dict[str, Any]:
        record = {"event": event, "at": datetime.now(timezone.utc).isoformat(), **fields}
        if self.path:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record
