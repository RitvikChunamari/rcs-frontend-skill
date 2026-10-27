"""Portable stdlib smoke tests for the bundled inventory helper."""
import json
import tempfile
import unittest
from pathlib import Path
from inspect_project import markdown, scan


class InventoryTests(unittest.TestCase):
    def test_detects_framework_scripts_and_clues(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text(json.dumps({
                "name": "demo", "scripts": {"test": "vitest run"},
                "dependencies": {"react": "*", "gsap": "*"},
                "devDependencies": {"@playwright/test": "*"}
            }))
            (root / "src").mkdir()
            (root / "src" / "main.tsx").write_text("fetch('/api/projects'); gsap.to('.hero', {});")
            (root / "node_modules").mkdir()
            (root / "node_modules" / "bad.js").write_text("webgl aria-hidden")
            report = scan(root)
            self.assertIn("React", report["libraries_detected"])
            self.assertIn("GSAP", report["libraries_detected"])
            self.assertIn("Playwright", report["libraries_detected"])
            self.assertEqual(report["source_file_counts"][".tsx"], 1)
            self.assertIn("src/main.tsx", report["clue_files"]["API calls (fetch/axios/GraphQL)"])
            self.assertIn("demo", markdown(report))

    def test_empty_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = scan(Path(tmp))
            self.assertEqual(report["libraries_detected"], [])
            self.assertEqual(report["source_file_counts"], {})


if __name__ == "__main__":
    unittest.main()
