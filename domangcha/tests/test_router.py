import unittest

from domangcha.orchestration.contracts import Route
from domangcha.orchestration.intent import IntentNormalizer
from domangcha.orchestration.router import TaskRouter


class RouterTests(unittest.TestCase):
    def setUp(self):
        self.normalizer = IntentNormalizer()
        self.router = TaskRouter()

    def route(self, request):
        return self.router.route(self.normalizer.normalize(request)).route

    def test_simple_explanation_is_direct(self):
        self.assertEqual(self.route("Explain this architecture"), Route.DIRECT)

    def test_formatting_is_direct(self):
        self.assertEqual(self.route("이 문서를 요약하고 정리해줘"), Route.DIRECT)

    def test_bug_fix_is_loop(self):
        self.assertEqual(self.route("Fix this bug and iterate until tests pass"), Route.LOOP)

    def test_trivial_one_file_edit_is_direct(self):
        self.assertEqual(self.route("Update one file"), Route.DIRECT)

    def test_architecture_is_graph(self):
        self.assertEqual(self.route("전체 아키텍처를 리팩터링해줘"), Route.GRAPH)

    def test_security_is_graph(self):
        self.assertEqual(self.route("Update auth security permissions"), Route.GRAPH)

    def test_full_stack_is_graph(self):
        self.assertEqual(self.route("database schema + API + frontend UI 구현"), Route.GRAPH)

    def test_destructive_requires_approval(self):
        result = self.router.route(self.normalizer.normalize("Drop the database schema"))
        self.assertEqual(result.route, Route.GRAPH)
        self.assertTrue(result.approval_required)

    def test_destructive_migration_requires_graph_approval(self):
        result = self.router.route(self.normalizer.normalize("Run a destructive migration"))
        self.assertEqual(result.route, Route.GRAPH)
        self.assertTrue(result.approval_required)

    def test_parallel_research_build_is_graph(self):
        self.assertEqual(self.route("parallel research and build"), Route.GRAPH)

    def test_invalid_llm_proposal_is_ignored(self):
        intent = {"read_only": False, "signals": ["mutation"]}
        result = self.router.route(intent, {"proposed_route": "CHAOS"})
        self.assertEqual(result.route, Route.LOOP)

    def test_llm_cannot_lower_route(self):
        intent = {"read_only": False, "signals": ["security"]}
        result = self.router.route(intent, {"proposed_route": "DIRECT"})
        self.assertEqual(result.route, Route.GRAPH)

    def test_escalation(self):
        self.assertEqual(self.router.escalate(Route.DIRECT, "test failure").route, Route.LOOP)
        self.assertEqual(self.router.escalate(Route.LOOP, "parallel work").route, Route.GRAPH)


if __name__ == "__main__":
    unittest.main()
