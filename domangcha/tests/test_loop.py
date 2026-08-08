import unittest

from domangcha.orchestration.contracts import RunStatus
from domangcha.orchestration.loop import LoopExecutor, LoopState


class LoopTests(unittest.TestCase):
    def test_iterates_until_valid(self):
        counter = {"n": 0}

        def execute(_plan):
            counter["n"] += 1
            return {"n": counter["n"]}

        state = LoopExecutor().run(lambda _: {}, execute, lambda x: {"ok": x["n"] == 2, "progress": x["n"]})
        self.assertEqual(state.status, RunStatus.COMPLETED)
        self.assertEqual(state.iteration, 2)

    def test_repeated_error_breaks(self):
        def fail(_plan):
            raise RuntimeError("same error")

        state = LoopExecutor(max_same_error=2).run(lambda _: {}, fail, lambda _: {"ok": False})
        self.assertEqual(state.status, RunStatus.FAILED)
        self.assertEqual(state.repeated_error_count, 2)

    def test_budget_exhaustion(self):
        state = LoopState(max_iterations=1)
        result = LoopExecutor().run(lambda _: {}, lambda _: {}, lambda _: {"ok": False}, state)
        self.assertEqual(result.status, RunStatus.BUDGET_EXHAUSTED)

    def test_model_call_budget_exhaustion(self):
        state = LoopState(max_model_calls=0)
        result = LoopExecutor().run(
            lambda _: {},
            lambda _: {"_usage": {"model_calls": 1}},
            lambda _: {"ok": True},
            state,
        )
        self.assertEqual(result.status, RunStatus.BUDGET_EXHAUSTED)
