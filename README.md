<div align="center">

# RC's Frontend Design Skill

**A frontend design and implementation skill for Claude Code, Codex, Cursor, and other AI coding agents.**

*Distinctive UI/UX. Expressive motion. Thoughtful 3D. Production-grade frontend engineering.*

[Quick start](#install) · [What it does](#what-it-does) · [12 design directions](#design-style-atlas) · [Quality gates](#quality-gates) · [Contributing](CONTRIBUTING.md)

</div>

---

RC's Frontend Design Skill gives agentic coding tools an opinionated workflow for **researching, designing, implementing, connecting, and testing original interfaces**. It combines established design-system principles with editorial design, motion, creative coding, and 3D techniques without sacrificing real product behavior.

Use it as a reusable `SKILL.md` package for website design, web app UI/UX, frontend redesigns, design systems, responsive React interfaces, accessibility, animation, WebGL, and production QA. The instructions are portable: the agent adapts them to the project's existing framework and the tools it can actually access.

It is **not** a UI component library, a pretrained model, an Awwwards scraper, an API key, or a guarantee of an award-winning site. Agents still need the project files and tools necessary to implement and verify changes.

## Install

### Option A — Skills CLI (agents supported by the CLI)

Install from GitHub:

```bash
npx skills add RitvikChunamari/rcs-frontend-skill
```

To select global/personal scope for supported agents:

```bash
npx skills add RitvikChunamari/rcs-frontend-skill -g
```

The [Skills CLI](https://github.com/vercel-labs/skills) can prompt you to select compatible agents. Global install locations, supported agent names, and behavior vary by tool/version. This is **not** a single universal install to every app.

### Option B — Manual installation (no CLI necessary)

1. Download the repository's ZIP from **Code → Download ZIP**.
2. Extract it into a directory named `rcs-frontend`.
3. Import the folder into your agent's Skills UI, or move it to the tool's documented personal/global skills directory. The agent must be able to read `SKILL.md` and its sibling folders.
4. In apps supporting only custom instructions or `AGENTS.md`, use [`assets/AGENTS.md`](assets/AGENTS.md) as an adapter and update its reference path to this folder. See [`references/portability.md`](references/portability.md).
5. Confirm activation with the sample prompt below.

### Agent compatibility

| Agent or format | How to use this repository |
|---|---|
| **Claude Code** | Install through a compatible skills workflow or place the folder where Claude can discover `SKILL.md`. |
| **OpenAI Codex / ChatGPT** | Install as an Agent Skill or make the skill directory available to the agent. |
| **Cursor, OpenCode, Antigravity, and similar tools** | Use native skill support when available; otherwise adapt [`assets/AGENTS.md`](assets/AGENTS.md) to the tool's rules format. |
| **Any agent that reads instructions** | Provide `SKILL.md` and the task-relevant files under `references/`; capabilities still depend on the host agent. |

Exact installation paths and feature names change between tools and versions. Follow the agent's current official documentation, and verify that it loads the skill with the sample prompt below.

## What it does

| Discipline | What the agent is instructed to deliver |
|---|---|
| **Design research** | Deconstruct freely accessible live sites and public examples; learn from Apple, Material, Fluent, Carbon, Spectrum, and other design systems without cloning proprietary work. |
| **Art direction and UX** | Choose a defensible concept, visual system, layout, typography, content hierarchy, responsive behaviors, and interaction states. |
| **Frontend engineering** | Implement semantic, maintainable UI using the **existing project's stack** wherever practical; preserve routes, data, SEO, and behavior. |
| **Motion and interaction** | Choose CSS/WAAPI, Motion, GSAP/ScrollTrigger and Lenis **when justified**, with reduced-motion and teardown rules. |
| **3D and graphics** | Use Three.js, React Three Fiber, SVG, shaders, and creative visuals selectively, with mobile/low-end fallbacks. |
| **Backend fidelity** | Preserve actual API contracts, auth, forms, loading/error/empty states, validation, streaming, and data integrity. |
| **QA and testing** | Run relevant build/lint/type checks, Playwright and accessibility checks, keyboard testing, responsive screenshots and performance measurements where tools permit. |

### Design style atlas

The skill includes **12 directions**, each documented with selection criteria, visual primitives, motion treatments, implementation considerations, common mistakes, and style-specific QA:

| | | |
|---|---|---|
| Minimalism & Bento | Human Editorial | Neo-Brutalism & Cute-alism |
| Retro & Dial-Up Delight | Ambient Tech & Aurora | Story-Driven & Immersive 3D |
| Glassmorphism & Frost | Kinetic Maximalism | Tactile Skeuomorphism |
| Cyberpunk & Sci-Fi | Claymorphism & Soft 3D | Swiss / International Typographic Style |

See [`references/style-atlas.md`](references/style-atlas.md) and [`references/style-composition.md`](references/style-composition.md). Style labels are **creative directions**, not universal rules or guaranteed design trends. The workflow prefers one coherent dominant style and, where helpful, one complementary influence.

## Try it

After installation, ask your agent:

> Audit my current website and implement an original Swiss-editorial redesign with expressive but restrained project-card motion. Keep the existing backend, routes, copy, projects, and images intact. Verify keyboard interaction, reduced motion, mobile layouts, build, and critical flows. Report exactly what you tested.

Other examples:

- "Compare three coherent art directions for my product before implementing the most appropriate one."
- "Build a cinematic 3D product hero with a static fallback, then check mobile performance."
- "Improve the visual polish of these components without breaking existing forms or API data."
- "Research a small set of design-system examples; identify reusable principles and produce an original implementation."

## How the skill works

1. **Inspect** the real project, its routes, constraints, and backend contracts.
2. **Research** a small set of relevant inspirations and design-system references.
3. **Choose** a distinct visual thesis and document interaction behavior.
4. **Implement** real responsive screens and flows within the current stack.
5. **Animate / add 3D** only where it improves comprehension or experience.
6. **Test** usability, visuals, accessibility, backend integrity, and performance.
7. **Report evidence**: tested commands, observed outcomes, screenshots checked, and remaining caveats.

Read the [orchestrator](SKILL.md) and the on-demand [reference guides](references/). Agents should read **only the relevant guides** for the current task to conserve context.

## Quality gates

The rules target WCAG 2.2 AA, functional keyboard navigation, reduced-motion support, resilient live API workflows, and healthy Core Web Vitals. These are **targets**, not pre-certified results. Every future app must be tested independently; importing a skill does not automatically test anything.

The included project-inventory helper is read-only, requires Python 3.9+, and has no external dependencies:

```bash
python scripts/inspect_project.py /path/to/your-project --format markdown
```

To test the **skill repository itself**:

```bash
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/validate_skill.py
```

CI runs these checks on pushes and pull requests. They verify skill consistency and scripts, **not** the runtime quality of an unrelated website.

## Repository map

```text
rcs-frontend-skill/
├── SKILL.md                      # Skill entrypoint and workflow
├── README.md                     # Community docs
├── LICENSE                       # MIT
├── CONTRIBUTING.md               # Contribution guide
├── agents/openai.yaml            # ChatGPT skill UI metadata
├── assets/AGENTS.md              # Adapter for AGENTS.md/custom rules
├── references/                   # Design, motion, 3D, engineering, QA guidance
├── scripts/                      # Read-only inventory and self-checks
└── .github/workflows/            # Automated checks
```

## Sources and attribution

The skill links to official documentation, tool creators, research collections, and inspiration sources in [`references/resource-registry.md`](references/resource-registry.md), [`references/design-systems.md`](references/design-systems.md), and [`references/reference-research.md`](references/reference-research.md). Product names, brand names, and tool names remain the property of their respective owners. No affiliation with Apple, Google, Meta, Netflix, Awwwards, Mobbin, or the tool maintainers is claimed. Observe licensing, paywalls, and terms when obtaining references or assets.

## Contribute

Issues and pull requests are welcome for better design research procedures, practical patterns, maintained links, framework-specific recipes, accessibility tests, or corrections. Please read [CONTRIBUTING.md](CONTRIBUTING.md). **Do not contribute scraped proprietary assets, unlicensed screenshots, credentials, or direct clones of third-party designs.**

## License

MIT — see [LICENSE](LICENSE).
