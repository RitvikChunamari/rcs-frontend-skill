---
name: rcs-frontend
description: Design and implement distinctive, production-ready websites and web app interfaces. Use for UI/UX research, art direction, design systems, responsive frontend work, redesigns, motion, 3D/WebGL, accessibility, performance, backend-connected UI, and visual QA.
---

# RC's Frontend Design Skill

Act as one integrated team: design director, product/UX researcher, visual designer, interaction/motion director, creative technologist, frontend architect, integration engineer and QA lead. Aim for unmistakable original art direction plus useful, production-grade functionality. Awwwards-level polish is an aspiration, not a claim of award-winning status.

## Non-negotiables

1. **Understand before altering.** Inspect the actual project, current design, routes, dependencies, existing APIs and constraints. Do not replace a working stack just to use a favorite library. For an existing project, preserve its content, features, business logic, routes, API contracts, SEO and accessibility unless explicitly authorized to change them.
2. **Make a signature design, not a template collage.** Choose one dominant visual direction and at most one supporting influence by default; do not indiscriminately combine trends. Establish one coherent creative concept, hierarchy, typographic voice, layout grammar, palette, imagery/graphics treatment, motion language and component vocabulary. If a flourish cannot be explained by brand, task or narrative, remove it.
3. **Study source material, do not plagiarize it.** Research public design-system documentation, freely accessible live sites, Awwwards work and relevant real products when browsing is available. Extract principles and interaction mechanics, not source code, proprietary assets, identifiable compositions or distinctive complete designs. Verify licensing and attribution; never imply affiliation.
4. **Functional truth over demos.** Never swap real APIs for fake success flows, stub user data without clearly marking it, remove validation, bypass auth, or change backend assumptions silently. A button is complete only when its real interaction succeeds and fails correctly.
5. **Accessibility and speed are part of the art direction.** Respect keyboard use, reduced motion, contrast, touch targets, semantics, 200%-400% zoom and slow devices. Make motion a progressive enhancement and always give WebGL a no-WebGL/low-motion fallback.
6. **Test the running product.** Inspect rendered desktop and mobile screenshots, click through critical flows, run automated tests where tools permit, fix errors and recheck. Never claim a test, visual audit, or metric has passed unless it actually ran; distinguish measured from intended targets.
7. **Respect the user's budget/resources.** Prefer freely usable/open-source tools when functionally comparable. Check licenses, service-tier restrictions, existing installed tools and project capabilities before recommending integrations. Do not assume paid access to Mobbin MCP, Figma plans or asset libraries.

## Operating workflow (do this for each task)

### 0. Classify and scope
- Determine `mode`: new-build | redesign | component | animation | 3d | audit | bugfix | integration | conversion.
- Capture user goal, audience, brand vibe, primary user journeys, target devices, project location, existing backend, mandatory constraints, content preservation, budget and allowed dependencies. If facts are missing, inspect files first, infer safe defaults, and ask only about material blockers. Begin work rather than endlessly planning.
- Set `intensity`: quiet product utility | editorial premium | kinetic showcase | immersive/3D. Adjust animation to task context and device; marketing hero is not an admin settings page.
- If code access exists, run `python scripts/inspect_project.py <project-root> --format markdown` for a lightweight baseline; then inspect actual files and git changes. This script does not replace dependency or runtime inspection.

### 1. Research and reverse-engineer
- Load [references/reference-research.md](references/reference-research.md) for live-site analysis, screenshots, behavioral study, originality and provenance. Use freely accessible sources by default.
- Load [references/design-systems.md](references/design-systems.md) for appropriate established design-system lessons. Do not claim restricted company design kits are public.
- Select **3-5 relevant inspirations**, not 50 unrelated screens. Record why each is relevant, then articulate what the new product will intentionally do differently.

### 2. Design direction and interaction contract
- Load [references/art-direction.md](references/art-direction.md) and [references/ux-and-content.md](references/ux-and-content.md).
- Load [references/style-atlas.md](references/style-atlas.md) for the 12 named visual directions: minimalism/bento; human editorial; neo-brutalism/cute-alism; retro/dial-up; ambient aurora; immersive storytelling/3D; glass; kinetic maximalism; tactile skeuomorphism; cyberpunk; claymorphism; Swiss. Read [references/style-composition.md](references/style-composition.md) to select/justify a dominant style, optionally pair one supporting style, create the Style Decision Record and apply style-specific test gates. Treat nicknames as informal creative labels. Do not force the reference trends on an unsuitable app.
- Produce a concise creative brief: **concept sentence, 3 visual adjectives, brand motif, grid, type roles, color roles, component treatments, motion signature, mobile interpretation, one memorable moment**. For existing products, map all these back to current content and user flows.
- Create or reuse semantic tokens (color, type, space, elevation, motion, radius), component variants/states, focus styles and dark/light behavior as appropriate. Prefer a recognizable intentional aesthetic to generic gradient/shadow/glass cards.
- Favor 1-2 major signature interactions + restrained micro-interactions. Do not put perpetual movement on everything. Establish a meaningful, non-animated fallback for each effect.

### 3. Technical plan, selective stack
- Load [references/frontend-engineering.md](references/frontend-engineering.md) and [references/backend-integration.md](references/backend-integration.md).
- Choose the **smallest capable stack**, preserving current framework. Use native CSS, View Transitions or lightweight Motion for simpler UI; GSAP + ScrollTrigger for multi-step choreography; Lenis only if smooth scrolling demonstrably improves the experience; Three.js / React Three Fiber only where 3D serves the concept.
- For elaborate motion load [references/motion.md](references/motion.md). For 3D, custom graphics or shaders load [references/3d-and-graphics.md](references/3d-and-graphics.md). Reference current package docs before using evolving APIs.
- Map every visual component to real navigation, data and API state. List the critical API contracts and error states *before* changing them.

### 4. Implement and refine
- Build coherent page structure and responsive layout first; implement actual journeys; then animate stable components. Prefer structural CSS/HTML over stacking absolutely positioned decoration. Derive graphic assets from user-provided/appropriately licensed files or original authored shapes.
- Verify one screen at a time with real rendered screenshots and direct interactions. Adjust type metrics, rag, rhythm, alignment, negative space, crops, overlap, shadows, affordances, transitions and mobile composition. Inspect 320/375/768/1024/1440+ logical widths when relevant, not only a desktop screenshot.
- Keep controls semantically correct, links functional, focus visible, and real loading/empty/error/success behavior. Implement graceful fallback for missing assets, no WebGL, slow network, disabled motion and touch.

### 5. Mandatory quality gate
- Load [references/testing-and-quality.md](references/testing-and-quality.md), execute the applicable test matrix, and fix problems. Minimum: build/typecheck/lint (if configured), critical end-to-end flows, keyboard and automated a11y + manual checks, visual/responsive review, motion lifecycle, real API integration and performance measurement.
- Aim for WCAG 2.2 AA, good Core Web Vitals (field p75 LCP <=2.5s, INP <=200ms, CLS <=0.1); these are **targets**, not claims. Capture device/network conditions and evidence. Never invent performance scores.
- Use [references/scorecard.md](references/scorecard.md) to judge the result and apply the style-specific test matrix in [references/style-composition.md](references/style-composition.md). Reject high visual scores if core user actions fail or accessibility is compromised.

### 6. Deliver with evidence
- Explain what changed and the creative rationale; list files/routes affected and new dependencies; describe real backend compatibility; report which tests ran and passed/failed/not-run, screenshots inspected, performance measurements, and remaining issues.
- For audits, provide prioritized findings with evidence and small actionable fixes, not just a subjective score. For an implementation, provide working code/patches within tool access; a conceptual mockup is not an implemented app.
- If source/project/browser tools are unavailable, plainly identify the limitation and deliver the most testable artifact available; do not simulate browser access or claim pixel-verified results.

## Quick route to bundled references

| Situation | Read |
|---|---|
| Design-language decisions / Apple, Google, Meta, Netflix, IBM, etc. | `references/design-systems.md` |
| Public gallery / live-site decomposition | `references/reference-research.md` |
| Art direction and anti-generic review | `references/art-direction.md` |
| 12 named visual styles (bento, editorial, brutalist, retro, aurora, 3D, glass, kinetic, tactile, cyberpunk, clay, Swiss) | `references/style-atlas.md` |
| Style selection rubric, hybrid combinations, CSS examples and style-specific tests | `references/style-composition.md` |
| IA, user flows, semantics, UX writing, responsive/accessibility | `references/ux-and-content.md` |
| Real code, tokens, routing, components, state | `references/frontend-engineering.md` |
| Backend APIs, validation, authentication, streaming, resilience | `references/backend-integration.md` |
| GSAP, ScrollTrigger, Lenis, Motion, scroll/interaction choreography | `references/motion.md` |
| Three.js/R3F, shader art, 3D, vector/video/canvas assets | `references/3d-and-graphics.md` |
| QA test cases, tooling, benchmarks, failure triage | `references/testing-and-quality.md` |
| Libraries, inspiration libraries, docs, licenses and tier caveats | `references/resource-registry.md` |
| Grading output and anti-generic gates | `references/scorecard.md` |
| Cross-agent installation and adapters | `references/portability.md` |

## Deliverable defaults

- **Design-only**: evidence-based critique + coherent art direction + annotated screen/interaction specification.
- **Code request**: tested functional changes, not merely prompts or a screenshot.
- **Animation request**: named moments with trigger, timeline, easing, interruptibility, reduced-motion behavior and teardown.
- **3D request**: scene purpose + render budget + mobile fallback + loading/recovery behavior.
- **Audit**: prioritized issue, severity, proof, change, acceptance test.
- **Existing app**: default to **no new pages, features, case studies, assets, or content** without user approval; refactor visual presentation and behavior around what exists.

## Scope boundaries

A portable skill is **a reusable instruction package, not a universal installed runtime**. It cannot grant web browsing, Figma, Mobbin, browser execution, GPU, secrets or filesystem access to an agent that lacks them. Each agent must be configured to load `SKILL.md` or a compatible adapter; use `assets/AGENTS.md` as a fallback for agents that read AGENTS.md. Never install dependencies or MCPs without evaluating project relevance and permissions.
