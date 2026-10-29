#!/usr/bin/env python3
"""Read-only, heuristic CSS consistency inventory. Not a browser/a11y compliance test."""
import argparse
import collections
import json
from pathlib import Path
import re

SKIP = {"node_modules", ".git", "dist", "build", ".next", "coverage", "vendor", ".venv"}
EXTENSIONS = {".css", ".scss", ".sass", ".less"}
COLOR = re.compile(r"(?<![\w-])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})(?![\w-])")
TOKEN = re.compile(r"(?m)(--[a-zA-Z][\w-]*)\s*:")
FONT = re.compile(r"font-family\s*:\s*([^;{}]+)", re.I)
PIXELS = re.compile(r"(?<![\w.])(?:[1-9]\d{0,3})(?:\.\d+)?px\b")


def audit(root, max_files=1500):
    root = Path(root)
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    colors = collections.Counter()
    tokens = collections.Counter()
    fonts = collections.Counter()
    sizes = collections.Counter()
    files = 0
    reduced = 0
    container = 0
    keyframes = 0
    failures = []
    for path in root.rglob("*"):
        if any(part in SKIP or part.startswith(".git") for part in path.relative_to(root).parts):
            continue
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        files += 1
        if files > max_files:
            failures.append(f"Stopped at {max_files} files to limit scan")
            break
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            failures.append(f"Unreadable: {path.relative_to(root)}")
            continue
        content = re.sub(r"/\*.*?\*/", "", content, flags=re.S)
        colors.update(x.lower() for x in COLOR.findall(content))
        tokens.update(TOKEN.findall(content))
        fonts.update(" ".join(x.strip().split()) for x in FONT.findall(content))
        sizes.update(PIXELS.findall(content))
        reduced += len(re.findall(r"prefers-reduced-motion", content, re.I))
        container += len(re.findall(r"@container\b", content, re.I))
        keyframes += len(re.findall(r"@(?:-webkit-)?keyframes\b", content, re.I))
    observations = []
    if files == 0:
        observations.append("No standalone CSS-family files found; inspect CSS-in-JS/Tailwind separately.")
    if files and not tokens:
        observations.append("No CSS custom-property declarations found in scanned files; inspect other token sources.")
    if len(colors) >= 12:
        observations.append("Many unique literal hex colors; review whether semantic tokens reduce accidental drift.")
    if keyframes and not reduced:
        observations.append("CSS keyframes exist but no prefers-reduced-motion query found in scanned files; verify motion policy elsewhere.")
    return {
        "root": str(root), "css_files_scanned": min(files, max_files),
        "unique_hex_colors": len(colors), "top_hex_colors": colors.most_common(20),
        "custom_property_declarations": sum(tokens.values()), "top_token_names": tokens.most_common(20),
        "font_family_declarations": fonts.most_common(12), "top_pixel_literals": sizes.most_common(15),
        "reduced_motion_mentions": reduced, "container_queries": container, "keyframes": keyframes,
        "observations": observations, "scan_warnings": failures,
        "disclaimer": "Static heuristics only. Does not measure rendered quality, brand coherence, WCAG compliance or performance."
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("project", help="Project directory")
    p.add_argument("--format", choices=["json", "markdown"], default="markdown")
    args = p.parse_args()
    result = audit(args.project)
    if args.format == "json":
        print(json.dumps(result, indent=2))
        return
    print(f"# CSS design consistency inventory: {result['root']}")
    for key in ("css_files_scanned", "unique_hex_colors", "custom_property_declarations", "reduced_motion_mentions", "container_queries", "keyframes"):
        print(f"- {key.replace('_', ' ').capitalize()}: {result[key]}")
    print("- Top colors: " + ", ".join(f"{c} ({n})" for c, n in result["top_hex_colors"][:10]))
    print("- Fonts: " + ", ".join(f"{c} ({n})" for c, n in result["font_family_declarations"][:8]))
    for s in result["observations"] + result["scan_warnings"]:
        print(f"- Review: {s}")
    print("\n" + result["disclaimer"])


if __name__ == "__main__":
    main()
