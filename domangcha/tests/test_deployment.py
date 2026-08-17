import shutil
import tempfile
import unittest
from pathlib import Path

from domangcha.orchestration.deployment import DEPLOYED_PARTS, DeploymentInspector


ROOT = Path(__file__).resolve().parents[2]


def deploy(destination: Path) -> Path:
    """Mirror what install.sh copies into ~/.domangcha/domangcha."""
    source = ROOT / "domangcha"
    destination.mkdir(parents=True)
    for part in DEPLOYED_PARTS:
        origin = source / part
        if origin.is_dir():
            shutil.copytree(origin, destination / part)
        else:
            shutil.copy2(origin, destination / part)
    return destination


class DeploymentInspectorTests(unittest.TestCase):
    def test_absent_runtime_is_reported_as_not_installed(self):
        with tempfile.TemporaryDirectory() as folder:
            report = DeploymentInspector(ROOT, Path(folder) / "absent").report()
        self.assertFalse(report["installed"])
        self.assertEqual(report["changed"], [])
        self.assertEqual(report["missing"], [])

    def test_freshly_deployed_runtime_has_no_drift(self):
        with tempfile.TemporaryDirectory() as folder:
            install = deploy(Path(folder) / "domangcha")
            report = DeploymentInspector(ROOT, install).report()
        self.assertTrue(report["installed"])
        self.assertEqual(report["changed"], [])
        self.assertEqual(report["missing"], [])

    def test_stale_file_is_reported_even_when_versions_match(self):
        with tempfile.TemporaryDirectory() as folder:
            install = deploy(Path(folder) / "domangcha")
            stale = install / "orchestration/validation.py"
            stale.write_text(stale.read_text() + "\n# stale\n")
            report = DeploymentInspector(ROOT, install).report()
        self.assertEqual(report["changed"], ["orchestration/validation.py"])
        self.assertEqual(report["source_version"], report["installed_version"])

    def test_undeployed_file_is_reported_as_missing(self):
        with tempfile.TemporaryDirectory() as folder:
            install = deploy(Path(folder) / "domangcha")
            (install / "engine.py").unlink()
            report = DeploymentInspector(ROOT, install).report()
        self.assertEqual(report["missing"], ["engine.py"])

    def test_compiled_artifacts_are_not_drift(self):
        with tempfile.TemporaryDirectory() as folder:
            install = deploy(Path(folder) / "domangcha")
            cache = install / "orchestration/__pycache__"
            cache.mkdir(exist_ok=True)
            (cache / "validation.cpython-39.pyc").write_bytes(b"\x00")
            report = DeploymentInspector(ROOT, install).report()
        self.assertEqual(report["changed"], [])
        self.assertEqual(report["missing"], [])


if __name__ == "__main__":
    unittest.main()
