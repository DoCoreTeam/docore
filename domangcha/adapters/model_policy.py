from enum import Enum
from typing import Dict, Optional


class ModelPolicy(str, Enum):
    HIGH_REASONING = "HIGH_REASONING"
    BALANCED = "BALANCED"
    FAST_CHEAP = "FAST_CHEAP"
    LONG_CONTEXT = "LONG_CONTEXT"
    REVIEW = "REVIEW"


class ModelResolver:
    def __init__(self, mappings: Optional[Dict[str, str]] = None):
        self.mappings = mappings or {}

    def resolve(self, policy: ModelPolicy) -> Optional[str]:
        return self.mappings.get(policy.value)
