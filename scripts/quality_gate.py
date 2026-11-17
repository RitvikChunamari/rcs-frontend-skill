#!/usr/bin/env python3
"""Summarize manually supplied evidence. Never performs or fabricates product tests."""
import argparse
import json
from pathlib import Path

REQUIRED = ("preservation", "visual", "functionality", "backend", "accessibility", "performance", "responsiveness")
STATUSES = {"pass", "fail", "warning", "not_run", "not_applicable"}


def evaluate(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("gates"), dict):
        raise ValueError("Expected a JSON object with a 'gates' object")
    gates = payload["gates"]
    planned = payload.get("required_gates", [])
    if not isinstance(planned, list) or any(
        not isinstance(name, str) or not name.strip() for name in planned
    ):
        raise ValueError("required_gates must be a list of nonempty gate names")
    if any(not isinstance(name, str) or not name.strip() for name in gates):
        raise ValueError("Gate names must be nonempty strings")
    # Preserve base requirements and evaluate every supplied gate, including tests.
    names = dict.fromkeys([*REQUIRED, *planned, *gates])
    results = {}
    reasons = {}
    for gate in names:
        detail = gates.get(gate, {})
        if not isinstance(detail, dict):
            raise ValueError(f"Gate {gate} must be an object")
        status = detail.get("status", "not_run")
        if not isinstance(status, str) or status not in STATUSES:
            raise ValueError(f"Invalid status for {gate}: {status}")
        evidence = detail.get("evidence", [])
        if not isinstance(evidence, list) or any(not isinstance(x, str) for x in evidence):
            raise ValueError(f"Gate {gate} evidence must be a list of strings")
        if status == "pass" and not [x for x in evidence if x.strip()]:
            status = "not_run"  # A claim without evidence is never passing.
        if status == "not_applicable":
            reason = detail.get("reason", "")
            if not isinstance(reason, str):
                raise ValueError(f"Gate {gate} reason must be a string")
            if reason.strip():
                reasons[gate] = reason.strip()
            else:
                status = "not_run"
        results[gate] = status
    if any(status == "fail" for status in results.values()):
        verdict, code = "BLOCKED", 1
    elif any(status == "not_run" for status in results.values()):
        verdict, code = "NOT VERIFIED", 2
    elif any(status == "warning" for status in results.values()):
        verdict, code = "CONDITIONAL / REVIEW WARNINGS", 2
    else:
        verdict, code = "ALL APPLICABLE DOCUMENTED GATES PASS (human verification still required)", 0
    return {"project": payload.get("project", "unnamed"), "verdict": verdict, "gates": results,
            "applicability_reasons": reasons,
            "disclaimer": "Evidence is user-supplied. Tool verifies completeness, not whether test claims are true."}, code


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("evidence_json", type=Path)
    p.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = p.parse_args()
    try:
        result, code = evaluate(json.loads(args.evidence_json.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        p.error(str(error))
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"# Quality evidence: {result['project']}\n\nVerdict: **{result['verdict']}**")
        for key, value in result["gates"].items():
            print(f"- {key}: {value}")
            if key in result["applicability_reasons"]:
                print(f"  Reason: {result['applicability_reasons'][key]}")
        print("\n" + result["disclaimer"])
    raise SystemExit(code)


if __name__ == "__main__":
    main()
