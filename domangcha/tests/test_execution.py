import tempfile
import unittest
from pathlib import Path

from domangcha.orchestration.contracts import Route
from domangcha.orchestration.execution import ExecutionCoordinator


class ExecutionTests(unittest.TestCase):
    def test_state_preserving_escalation(self):
        with tempfile.TemporaryDirectory() as tmp:
            coordinator = ExecutionCoordinator(Path(tmp))
            state = coordinator.start("Explain this")
            task_id = state.task_id
            self.assertEqual(state.route, Route.DIRECT)
            state = coordinator.escalate(state, "dependency found")
            self.assertEqual(state.task_id, task_id)
            self.assertEqual(state.route, Route.LOOP)
            self.assertEqual(len(state.route_history), 2)
            loaded = coordinator.load(task_id)
            self.assertEqual(loaded.route, Route.LOOP)
            self.assertEqual(loaded.task_id, task_id)

    def test_rejected_approval_aborts(self):
        with tempfile.TemporaryDirectory() as tmp:
            coordinator = ExecutionCoordinator(Path(tmp))
            state = coordinator.start("Drop the database")
            saved = coordinator.approve(state.task_id, "migration", False)
            self.assertEqual(saved["status"], "ABORTED")
