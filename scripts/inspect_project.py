#!/usr/bin/env python3
"""Create a cautious, dependency-free inventory of a frontend project.

It never opens .env/secrets or modifies the project. Keyword flags are clues, not
proof of functionality. It deliberately ignores generated/dependency directories.
"""
from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from pathlib import Path

SKIP_DIRS = {
    ".git", ".next", ".nuxt", ".output", ".svelte-kit", "build", "dist", "coverage",
    "node_modules", ".venv", "venv", "vendor", ".turbo", ".cache", "storybook-static",
}
CODE_EXTS = {".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html", ".css", ".scss", ".sass"}
LIBRARIES = {
    "react": "React", "next": "Next.js", "vue": "Vue", "nuxt": "Nuxt",
    "svelte": "Svelte", "@sveltejs/kit": "SvelteKit", "astro": "Astro",
    "vite": "Vite", "tailwindcss": "Tailwind", "@playwright/test": "Playwright",
    "@axe-core/playwright": "axe Playwright", "gsap": "GSAP", "lenis": "Lenis",
    "motion": "Motion", "framer-motion": "Framer Motion", "three": "Three.js",
    "@react-three/fiber": "React Three Fiber", "@react-three/drei": "Drei",
    "@radix-ui/react-dialog": "Radix primitives", "@tanstack/react-query": "TanStack Query",
    "zod": "Zod", "@storybook/react": "Storybook", "vitest": "Vitest",
    "cypress": "Cypress", "axios": "Axios",
}
CLUES = {
    "API calls (fetch/axios/GraphQL)": ("fetch(", "axios.", "graphql", "usequery(", "usemutation("),
    "Potential routes": ("approuter", "browserrouter", "createbrowserrouter", "routedefinition", "<route", "load("),
    "Motion (GSAP/WAAPI/CSS)": ("scrolltrigger", "gsap.", ".animate(", "@keyframes", "animation:"),
    "Media/WebGL": ("<canvas", "webgl", "three.", "<video", "useframe("),
    "Accessibility/reduced motion": ("prefers-reduced-motion", "aria-", "focus-visible", "useReducedMotion"),
    "Error and loading states": ("isloading", "loading", "onerror", "errorboundary", "iserror"),
}


def scan(root: Path) -> dict:
    if not root.is_dir():
        raise ValueError(f"Not a project directory: {root}")
    package_path = root / "package.json"
    pkg = {}
    if package_path.exists():
        try:
            pkg = json.loads(package_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            pkg = {}
    deps = {}
    deps.update(pkg.get("dependencies", {}) if isinstance(pkg.get("dependencies"), dict) else {})
    deps.update(pkg.get("devDependencies", {}) if isinstance(pkg.get("devDependencies"), dict) else {})

    scripts = pkg.get("scripts", {}) if isinstance(pkg.get("scripts"), dict) else {}
    files = Counter()
    matched = {key: [] for key in CLUES}
    checked_files = 0
    # Avoid symlinks that may lead outside project. Exclude large/minified files.
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        for filename in sorted(filenames):
            p = Path(dirpath, filename)
            if p.is_symlink() or p.suffix.lower() not in CODE_EXTS:
                continue
            files[p.suffix.lower()] += 1
            if checked_files >= 5000 or p.stat().st_size > 256_000:
                continue
            checked_files += 1
            try:
                text = p.read_text(encoding="utf-8").lower()
            except (OSError, UnicodeDecodeError):
                continue
            relative = p.relative_to(root).as_posix()
            for name, needles in CLUES.items():
                if any(n.lower() in text for n in needles) and len(matched[name]) < 12:
                    matched[name].append(relative)

    lockfiles = [name for name in ("package-lock.json", "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb") if (root / name).exists()]
    return {
        "project": root.name,
        "package": pkg.get("name"),
        "package_manager_lockfiles": lockfiles,
        "libraries_detected": sorted({pretty for package, pretty in LIBRARIES.items() if package in deps}),
        "package_scripts": scripts,
        "source_file_counts": dict(sorted(files.items())),
        "source_files_sampled_for_clues": checked_files,
        "clue_files": matched,
        "limitations": [
            "Heuristic keyword inventory only; inspect actual routes, contracts and runtime behavior.",
            "Skipped dependencies/generated dirs, hidden dirs, symlinks, source files >256 KB; capped at 5000 inspected files.",
            "Did not read environment files, run the app, evaluate security, or verify QA.",
        ],
    }


def markdown(report: dict) -> str:
    lines = [f"# Frontend project inventory: {report['project']}", "",
             f"Package: `{report['package'] or 'not identified'}`",
             f"Lockfiles: {', '.join(report['package_manager_lockfiles']) or 'none found'}",
             f"Libraries: {', '.join(report['libraries_detected']) or 'none detected in package.json'}", "",
             "## Available package scripts"]
    for name, cmd in report["package_scripts"].items():
        lines.append(f"- `{name}`: `{cmd}`")
    if not report["package_scripts"]:
        lines.append("- None found")
    lines.extend(["", "## Source file counts"])
    for ext, count in report["source_file_counts"].items():
        lines.append(f"- `{ext}`: {count}")
    lines.extend(["", "## Search clues (not verified functionality)"])
    for clue, samples in report["clue_files"].items():
        lines.append(f"- **{clue}**: {', '.join('`' + p + '`' for p in samples) if samples else 'No obvious pattern found'}")
    lines.extend(["", "## Limitations"])
    lines.extend(f"- {limitation}" for limitation in report["limitations"])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", default=".")
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    args = parser.parse_args()
    try:
        report = scan(Path(args.project_root).expanduser().resolve())
    except (ValueError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, indent=2) if args.format == "json" else markdown(report), end="")


if __name__ == "__main__":
    main()
