import tempfile
import time
import unittest
from pathlib import Path

from domangcha.orchestration.checkpoint import CheckpointStore
from domangcha.orchestration.contracts import Budget, EdgeSpec, GraphState, NodeSpec, NodeType, Route, RunStatus
from domangcha.orchestration.graph import GraphDefinition, GraphDefinitionError, GraphExecutor


class GraphTests(unittest.TestCase):
    def state(self):
        return GraphState("task-1", "request", {}, Route.GRAPH)

    def test_human_gate_pauses_and_resumes(self):
        graph = GraphDefinition(
            "g", "1", "start",
            [NodeSpec("start", NodeType.DETERMINISTIC), NodeSpec("approve", NodeType.HUMAN_GATE), NodeSpec("done", NodeType.DETERMINISTIC)],
            [EdgeSpec("start", "approve"), EdgeSpec("approve", "done")],
        )
        executor = GraphExecutor({"DETERMINISTIC": lambda *_: {"outcome": "ok"}})
        state = executor.run(graph, self.state())
        self.assertEqual(state.status, RunStatus.WAITING_FOR_APPROVAL)
        state.approvals["approve"] = {"status": "APPROVED"}
        state = executor.run(graph, state)
        self.assertEqual(state.status, RunStatus.COMPLETED)

    def test_rejected_human_gate_aborts(self):
        graph = GraphDefinition("g", "1", "approve", [NodeSpec("approve", NodeType.HUMAN_GATE)], [])
        state = self.state()
        state.approvals["approve"] = {"status": "REJECTED"}
        self.assertEqual(GraphExecutor({}).run(graph, state).status, RunStatus.ABORTED)

    def test_checkpoint_redacts_secrets(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = CheckpointStore(Path(tmp))
            store.write("task", {"api_key": "hidden", "value": 1})
            self.assertEqual(store.read("task")["api_key"], "[REDACTED]")

    def test_checkpoint_redacts_secret_in_prompt(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = CheckpointStore(Path(tmp))
            store.write("task", {"request": "use api_key=sk-supersecretvalue"})
            self.assertNotIn("supersecret", store.read("task")["request"])

    def test_incompatible_checkpoint_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "task.json"
            path.write_text('{"checkpoint_version": 999}')
            with self.assertRaises(ValueError):
                CheckpointStore(Path(tmp)).read("task")

    def test_unreachable_node_rejected(self):
        graph = GraphDefinition("g", "1", "a", [NodeSpec("a", NodeType.DETERMINISTIC), NodeSpec("b", NodeType.DETERMINISTIC)], [])
        with self.assertRaises(GraphDefinitionError):
            graph.validate()

    def test_versioned_graph_loads(self):
        path = Path(__file__).resolve().parents[1] / "graphs/full_pipeline.json"
        self.assertEqual(GraphDefinition.from_path(path).id, "domangcha-full-pipeline")

    def test_node_retry(self):
        calls = {"n": 0}
        def flaky(*_):
            calls["n"] += 1
            if calls["n"] == 1:
                raise RuntimeError("injected")
            return {"outcome": "ok"}
        graph = GraphDefinition("g", "1", "work", [NodeSpec("work", NodeType.TOOL, max_attempts=2)], [])
        result = GraphExecutor({"work": flaky}).run(graph, self.state())
        self.assertEqual(result.status, RunStatus.COMPLETED)
        self.assertEqual(calls["n"], 2)

    def test_fallback(self):
        graph = GraphDefinition(
            "g", "1", "work",
            [NodeSpec("work", NodeType.TOOL, fallback_destination="repair"), NodeSpec("repair", NodeType.DETERMINISTIC)],
            [EdgeSpec("work", "repair")],
        )
        handlers = {"work": lambda *_: (_ for _ in ()).throw(RuntimeError("500")), "repair": lambda *_: {"outcome": "ok"}}
        result = GraphExecutor(handlers).run(graph, self.state())
        self.assertEqual(result.status, RunStatus.COMPLETED)
        self.assertIn("repair", result.completed_nodes)

    def test_timeout_fails_without_silent_success(self):
        graph = GraphDefinition("g", "1", "slow", [NodeSpec("slow", NodeType.TOOL, timeout_seconds=0.01)], [])
        result = GraphExecutor({"slow": lambda *_: time.sleep(0.05)}).run(graph, self.state())
        self.assertEqual(result.status, RunStatus.FAILED)

    def test_best_effort_partial_wave(self):
        wave = GraphExecutor.execute_wave({
            "good": lambda: 1,
            "bad": lambda: (_ for _ in ()).throw(RuntimeError("injected")),
        }, strategy="BEST_EFFORT")
        self.assertTrue(wave["ok"])
        self.assertIn("bad", wave["errors"])

    def test_any_waits_for_a_success_after_failure(self):
        wave = GraphExecutor.execute_wave({
            "bad": lambda: (_ for _ in ()).throw(RuntimeError("injected")),
            "good": lambda: 1,
        }, strategy="ANY")
        self.assertTrue(wave["ok"])

    def test_optional_branch_failure_does_not_fail_all_join(self):
        wave = GraphExecutor.execute_wave({
            "required": lambda: 1,
            "optional": lambda: (_ for _ in ()).throw(RuntimeError("optional failed")),
        }, strategy="ALL", required_branches=["required"])
        self.assertTrue(wave["ok"])

    def test_branch_timeout_is_recorded(self):
        wave = GraphExecutor.execute_wave({
            "good": lambda: 1,
            "hung": lambda: time.sleep(0.05),
        }, strategy="BEST_EFFORT", timeout_seconds=0.01)
        self.assertTrue(wave["ok"])
        self.assertEqual(wave["errors"]["hung"], "timeout_or_cancelled")

    def test_unmatched_edge_is_failure(self):
        graph = GraphDefinition(
            "g", "1", "validate",
            [NodeSpec("validate", NodeType.VALIDATOR), NodeSpec("done", NodeType.DETERMINISTIC)],
            [EdgeSpec("validate", "done", guard="ok")],
        )
        result = GraphExecutor({"validate": lambda *_: {"outcome": "unknown"}}).run(graph, self.state())
        self.assertEqual(result.status, RunStatus.FAILED)

    def test_tool_budget_exhaustion(self):
        state = self.state()
        state.budget = Budget(tool_calls=0)
        graph = GraphDefinition("g", "1", "tool", [NodeSpec("tool", NodeType.TOOL)], [])
        result = GraphExecutor({"tool": lambda *_: {"outcome": "ok"}}).run(graph, state)
        self.assertEqual(result.status, RunStatus.BUDGET_EXHAUSTED)
        self.assertIn("budget exhausted", result.errors[-1]["error"])

    def test_wall_time_budget_exhaustion(self):
        state = self.state()
        state.budget = Budget(wall_seconds=0)
        graph = GraphDefinition("g", "1", "node", [NodeSpec("node", NodeType.DETERMINISTIC)], [])
        result = GraphExecutor({"node": lambda *_: {"outcome": "ok"}}).run(graph, state)
        self.assertEqual(result.status, RunStatus.BUDGET_EXHAUSTED)

    def test_node_receives_only_declared_state_slice(self):
        observed = {}
        def handler(context, _node):
            observed.update(context)
            return {"outcome": "ok"}
        graph = GraphDefinition("g", "1", "node", [NodeSpec("node", NodeType.TOOL, input_fields=["task_id"])], [])
        GraphExecutor({"node": handler}).run(graph, self.state())
        self.assertEqual(set(observed), {"task_id"})

    def test_malformed_node_output_is_rejected(self):
        node = NodeSpec(
            "node", NodeType.LLM,
            output_schema={"required": ["outcome"], "properties": {"outcome": {"type": "string"}}},
        )
        graph = GraphDefinition("g", "1", "node", [node], [])
        result = GraphExecutor({"node": lambda *_: {"wrong": True}}).run(graph, self.state())
        self.assertEqual(result.status, RunStatus.FAILED)
