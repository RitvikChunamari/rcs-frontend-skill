#!/usr/bin/env python3
"""Summarize manually supplied evidence. Never performs or fabricates product tests."""
import argparse
import json
from pathlib import Path

REQUIRED = ("preservation", "visual", "functionality", "backend", "accessibility", "performance", "responsiveness")
STATUSES = {"pass", "fail", "warning", "not_run"}


def evaluate(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("gates"), dict):
        raise ValueError("Expected a JSON object with a 'gates' object")
    gates = payload["gates"]
    results = {}
    for gate in REQUIRED:
        detail = gates.get(gate, {})
        if not isinstance(detail, dict):
            raise ValueError(f"Gate {gate} must be an object")
        status = detail.get("status", "not_run")
        if status not in STATUSES:
            raise ValueError(f"Invalid status for {gate}: {status}")
        evidence = detail.get("evidence", [])
        if not isinstance(evidence, list) or any(not isinstance(x, str) for x in evidence):
            raise ValueError(f"Gate {gate} evidence must be a list of strings")
        if status == "pass" and not [x for x in evidence if x.strip()]:
            status = "not_run"  # A claim without evidence is never passing.
        results[gate] = status
    if any(status == "fail" for status in results.values()):
        verdict, code = "BLOCKED", 1
    elif any(status == "not_run" for status in results.values()):
        verdict, code = "NOT VERIFIED", 2
    elif any(status == "warning" for status in results.values()):
        verdict, code = "CONDITIONAL / REVIEW WARNINGS", 2
    else:
        verdict, code = "ALL DOCUMENTED GATES PASS (human verification still required)", 0
    return {"project": payload.get("project", "unnamed"), "verdict": verdict, "gates": results,
            "disclaimer": "Evidence is user-supplied. Tool verifies completeness, not whether test claims are true."}, code


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("evidence_json", type=Path)
    p.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = p.parse_args()
    result, code = evaluate(json.loads(args.evidence_json.read_text(encoding="utf-8")))
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"# Quality evidence: {result['project']}\n\nVerdict: **{result['verdict']}**")
        for key, value in result["gates"].items():
            print(f"- {key}: {value}")
        print("\n" + result["disclaimer"])
    raise SystemExit(code)


if __name__ == "__main__":
    main()
