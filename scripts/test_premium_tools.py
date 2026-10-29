"""Standard-library smoke tests for premium skill tools."""
import tempfile
import unittest
from pathlib import Path
from design_consistency_audit import audit
from quality_gate import evaluate, REQUIRED


class DesignAuditTests(unittest.TestCase):
    def test_scans_css_and_skips_dependencies(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "a.css").write_text(':root {--ink: #123456;} .card { color: #123456; font-family: "Inter", sans-serif; } @media (prefers-reduced-motion: reduce) {} @container (min-width: 20rem) {}')
            (root / "node_modules").mkdir()
            (root / "node_modules" / "bad.css").write_text('.x{color:#aa0000}')
            report = audit(root)
            self.assertEqual(report["css_files_scanned"], 1)
            self.assertEqual(report["unique_hex_colors"], 1)
            self.assertGreater(report["reduced_motion_mentions"], 0)
            self.assertEqual(report["container_queries"], 1)

    def test_empty_project_does_not_claim_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            report = audit(temp)
            self.assertEqual(report["css_files_scanned"], 0)
            self.assertIn("CSS-in-JS", report["observations"][0])


class QualityEvidenceTests(unittest.TestCase):
    def test_blank_pass_is_not_verified(self):
        data = {"gates": {gate: {"status": "pass", "evidence": []} for gate in REQUIRED}}
        result, code = evaluate(data)
        self.assertEqual(code, 2)
        self.assertEqual(result["gates"]["visual"], "not_run")

    def test_documented_passes(self):
        data = {"gates": {gate: {"status": "pass", "evidence": ["Test log/run id: EXAMPLE"]} for gate in REQUIRED}}
        result, code = evaluate(data)
        self.assertEqual(code, 0)
        self.assertIn("human verification", result["verdict"])

    def test_failed_gate_blocks(self):
        data = {"gates": {"functionality": {"status": "fail", "evidence": ["smoke failure"]}}}
        result, code = evaluate(data)
        self.assertEqual(code, 1)
        self.assertEqual(result["verdict"], "BLOCKED")

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            evaluate({"gates": {"visual": {"status": "perfect"}}})


if __name__ == "__main__":
    unittest.main()
