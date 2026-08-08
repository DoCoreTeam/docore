import unittest
from pathlib import Path

from domangcha.orchestration.validation import RepositoryValidator, ValidationError


ROOT = Path(__file__).resolve().parents[2]


class ValidationTests(unittest.TestCase):
    def test_manifests_match_files(self):
        self.assertEqual(RepositoryValidator(ROOT).validate_manifests(), [])

    def test_graph_definitions_are_valid(self):
        self.assertEqual(RepositoryValidator(ROOT).validate_graphs(), [])

    def test_hand_maintained_source_line_limits(self):
        paths = [path for path in (ROOT / "domangcha").rglob("*") if path.is_file()]
        self.assertEqual(RepositoryValidator(ROOT).validate_line_limits(paths), [])

    def test_builder_reviewer_separation(self):
        with self.assertRaises(ValidationError):
            RepositoryValidator(ROOT).assert_builder_reviewer([
                {"actor": "dc-dev-be", "action": "write"},
                {"actor": "dc-dev-be", "action": "review"},
            ])
