import os
import unittest
from unittest.mock import patch

from domangcha.adapters.model_policy import ModelPolicy, ModelResolver
from domangcha.adapters.runtime import RuntimeDetector


class RuntimeTests(unittest.TestCase):
    def test_explicit_runtime_profiles_preserve_checkpointing(self):
        for runtime in ("CLAUDE_CODE", "CODEX_LOCAL", "CODEX_IDE", "CODEX_CLOUD", "UNKNOWN"):
            with self.subTest(runtime=runtime), patch.dict(os.environ, {"DOMANGCHA_RUNTIME": runtime}, clear=False):
                profile = RuntimeDetector().detect()
                self.assertEqual(profile.runtime, runtime)
                self.assertTrue(profile.checkpointing)

    def test_cloud_does_not_require_interactive_approval(self):
        with patch.dict(os.environ, {"DOMANGCHA_RUNTIME": "CODEX_CLOUD"}, clear=False):
            self.assertFalse(RuntimeDetector().detect().interactive_approval)

    def test_unknown_model_is_tolerated(self):
        self.assertIsNone(ModelResolver().resolve(ModelPolicy.HIGH_REASONING))


if __name__ == "__main__":
    unittest.main()
