import re
from typing import Any, Dict


class IntentNormalizer:
    """Deterministic normalization; semantic enrichment is optional downstream."""

    def normalize(self, request: str) -> Dict[str, Any]:
        compact = re.sub(r"\s+", " ", request).strip()
        lowered = compact.lower()
        return {
            "request": compact,
            "read_only": self._read_only(lowered),
            "explicit_command": self._command(lowered),
            "signals": sorted(self._signals(lowered)),
            "estimated_files": self._file_hint(lowered),
        }

    @staticmethod
    def _command(text: str) -> str:
        match = re.search(r"/(ceo(?:-[a-z]+)?)\b", text)
        return match.group(1) if match else ""

    @staticmethod
    def _read_only(text: str) -> bool:
        mutating = (
            "implement", "fix", "create", "add", "remove", "delete", "update",
            "refactor", "migrate", "deploy", "구현", "수정", "고쳐", "추가",
            "삭제", "변경", "만들", "배포", "마이그레이션", "리팩터",
        )
        readonly = (
            "explain", "summarize", "format", "what", "why", "how", "review",
            "설명", "요약", "정리", "조회", "알려", "검토",
        )
        return any(x in text for x in readonly) and not any(x in text for x in mutating)

    @staticmethod
    def _signals(text: str) -> set:
        groups = {
            "mutation": ("implement", "fix", "create", "update", "구현", "수정", "추가", "변경"),
            "database": ("database", "schema", "migration", "db ", "데이터베이스", "스키마", "마이그레이션"),
            "api": (" api", "endpoint", "public contract", "엔드포인트"),
            "frontend": ("frontend", "ui", "page", "component", "프론트", "화면", "컴포넌트"),
            "security": ("security", "auth", "permission", "secret", "보안", "인증", "인가", "권한"),
            "destructive": ("drop ", "truncate", "destroy", "destructive", "irreversible", "삭제", "파괴", "되돌릴 수 없"),
            "architecture": ("architecture", "cross-cutting", "refactor all", "아키텍처", "전체 리팩터"),
            "parallel": ("parallel", "multi-agent", "fan-out", "병렬", "멀티에이전트"),
            "resume": ("checkpoint", "resume", "long-running", "체크포인트", "재개", "장기 실행"),
            "external": ("webhook", "external api", "payment", "deploy", "외부 api", "결제", "배포"),
            "iterative": ("iterate", "debug", "refactor", "loop", "반복", "디버그", "리팩터", "루프"),
        }
        return {name for name, words in groups.items() if any(word in text for word in words)}

    @staticmethod
    def _file_hint(text: str) -> int:
        if any(x in text for x in ("one file", "single file", "한 파일", "파일 하나", "1개 파일")):
            return 1
        match = re.search(r"(\d+)\s*(?:files?|개\s*파일)", text)
        return int(match.group(1)) if match else 0
