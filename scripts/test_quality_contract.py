"""Regressions for declared test gates and applicability in release evidence."""
import unittest

from quality_gate import REQUIRED, evaluate


def complete_report():
    return {"gates": {
        name: {"status": "pass", "evidence": ["review/log.txt"]}
        for name in REQUIRED
    }}


class QualityContractTests(unittest.TestCase):
    def test_failed_unit_tests_block_an_otherwise_complete_report(self):
        payload = complete_report()
        payload["gates"]["unit_tests"] = {
            "status": "fail", "evidence": ["pytest: validation boundary failed"]
        }
        report, code = evaluate(payload)
        self.assertEqual(code, 1)
        self.assertEqual(report["gates"]["unit_tests"], "fail")

    def test_planned_gate_cannot_disappear_from_release_report(self):
        payload = complete_report()
        payload["required_gates"] = ["unit_tests", "critique"]
        report, code = evaluate(payload)
        self.assertEqual(code, 2)
        self.assertEqual(report["gates"]["critique"], "not_run")

    def test_static_site_can_explain_absent_backend(self):
        payload = complete_report()
        payload["gates"]["backend"] = {
            "status": "not_applicable",
            "reason": "Static documentation page with no backend calls.",
        }
        report, code = evaluate(payload)
        self.assertEqual(code, 0)
        self.assertEqual(report["gates"]["backend"], "not_applicable")

    def test_omitted_applicability_reason_is_unverified(self):
        payload = complete_report()
        payload["gates"]["backend"] = {"status": "not_applicable"}
        report, code = evaluate(payload)
        self.assertEqual(code, 2)
        self.assertEqual(report["gates"]["backend"], "not_run")

    def test_extra_pass_still_needs_evidence(self):
        payload = complete_report()
        payload["gates"]["critique"] = {"status": "pass", "evidence": ["  "]}
        report, code = evaluate(payload)
        self.assertEqual(code, 2)
        self.assertEqual(report["gates"]["critique"], "not_run")

    def test_empty_plan_keeps_base_gates_required(self):
        report, code = evaluate({"gates": {}, "required_gates": []})
        self.assertEqual(code, 2)
        self.assertEqual(set(report["gates"]), set(REQUIRED))

    def test_malformed_gate_names_and_requirements_rejected(self):
        for required in ["unit_tests", [None], [" "], {}]:
            with self.subTest(required=required), self.assertRaises(ValueError):
                evaluate({"gates": {}, "required_gates": required})

    def test_non_string_status_has_clear_validation_error(self):
        with self.assertRaises(ValueError):
            evaluate({"gates": {"visual": {"status": []}}})


if __name__ == "__main__":
    unittest.main()
