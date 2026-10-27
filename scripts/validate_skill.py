#!/usr/bin/env python3
"""Minimal self-check for the portable agent skill (stdlib only)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REQUIRED = ["SKILL.md", "README.md", "LICENSE", "agents/openai.yaml",
            "assets/AGENTS.md", "references/style-atlas.md",
            "references/style-composition.md", "references/testing-and-quality.md"]


def validate():
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Missing required file: {rel}")
    if not SKILL.is_file():
        return errors
    content = SKILL.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
    if not frontmatter:
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        for field in ("name", "description"):
            if not re.search(rf"(?m)^{field}:\s*\S", frontmatter.group(1)):
                errors.append(f"Missing frontmatter field: {field}")
        if not re.search(r"(?m)^name: rcs-frontend\s*$", frontmatter.group(1)):
            errors.append("Skill name must match rcs-frontend")
    docs = [SKILL, *sorted((ROOT / "references").glob("*.md"))]
    for doc in docs:
        for rel in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", doc.read_text(encoding="utf-8")):
            if "://" not in rel and not rel.startswith(("mailto:", "#")):
                if not (doc.parent / rel).is_file():
                    errors.append(f"Broken local link: {doc.relative_to(ROOT)} -> {rel}")
    return errors


if __name__ == "__main__":
    failures = validate()
    for failure in failures:
        print(f"ERROR: {failure}", file=sys.stderr)
    if failures:
        raise SystemExit(1)
    print("Skill structure, frontmatter and local reference links: OK")
