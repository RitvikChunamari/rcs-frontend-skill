# Premium release gates and review protocol

Use alongside testing-and-quality.md and scorecard.md. These gates are **evidence-based**. A portable skill cannot pre-certify an app. A screenshot alone cannot prove usability, integration, accessibility or performance.

## Gate P0: preservation and truthful scope

For an existing app, show baseline routes/data/content and the changed files. A change that silently removes a feature, auth, data or required asset **blocks release**. Show explicit permissions for new pages, altered content, new paid services or new library costs.

## Gate P1: visual precision

Review *actual* screenshots at 320/375/768/1024/1440 as applicable, plus long text, dark/light, keyboard focus and functional empty/error states. Detect clipping, accidental horizontal scroll, line breaks, spacing drift, repeated generic modules, weak focal hierarchy, low-res images, broken composition. Require at least one documented correction from first render; screenshots may be captured via browser agent or project tooling.

## Gate P2: user path and real APIs

Critical navigation, primary form/action, and a representative error path must work. Test an API response from the real/dev backend when possible. Failed mutations must never say success; network errors provide recovery. Verify keyboard and touch parity on essential actions.

## Gate P3: accessibility (WCAG 2.2 AA target)

Automated axe plus manual: Tab/Shift-Tab, Enter/Space/Escape, visible focus not obscured, logical heading tree, noncolor status, live status, labels/errors, modality, zoom 200%-400%, hover/touch equivalence, reduced motion, target size policy. Check contrast on the **actual composited background**, especially glass/aurora/video. WCAG 2.2 minimum pointer targets are not a blanket 44px rule: apply the normative criterion/exceptions; using 44px as an ergonomic design target can still be helpful. If screen reader not tested, report untested.

## Gate P4: performance and robustness

Field Core Web Vitals p75 **targets**: LCP <= 2.5s; INP <= 200ms; CLS <= .1 (separately on mobile/desktop where data exists). Lab Lighthouse is an investigation aid, not a substitute for field p75. For motion/3D, inspect frame times, scroll stutter, GPU cost, memory leaks, load/asset budgets and no-WebGL behavior on low-end devices. Record environment, not a made-up universal FPS.

## Gate P5: cross-platform interaction

Test Chromium + WebKit + Firefox where feasible; prioritize target devices. Verify pointer/touch, coarse hover capability, reduced-motion, route unmount, back/forward, refresh, orientation and offline behavior. Test the running app rather than merely checking JSX/CSS.

## Evidence structure

Use `assets/templates/quality-report.md`. Optionally feed machine-checked evidence JSON to `python scripts/quality_gate.py path/to/evidence.json`; it marks missing evidence as `not_run`, never treats unchecked boxes as passes. Quality gate output cannot prove all design quality; human visual review remains essential.

## Blocker vs warning

Blocker: broken primary task, fabricated backend success, inaccessible essential action, clear privacy/security regression, major navigation/data loss, nonrecoverable rendering failure on supported devices. Warning: weaker typographic rhythm, lower-than-target lab scores, decorative detail disagreement, or lower-priority secondary issues. Do not call a blocker a warning to inflate completion score.

## No self-awarded Awwwards certifications

Use creative scorecards for iteration, not as objective claims of being number one or awards. Reports identify observed issues and tests that *ran* versus tests *planned*.

Sources: https://www.w3.org/TR/wcag/ ; https://web.dev/articles/vitals ; https://playwright.dev/docs/test-snapshots
