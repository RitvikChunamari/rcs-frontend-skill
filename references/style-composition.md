# Visual direction selection, hybridization and acceptance tests

Read `style-atlas.md` first. Use this guide before building a visual system or accepting a style-heavy redesign. **Aim for a purposeful signature, not a sampler plate of trends.**

## 1. Choose the style by user and product evidence

Write a short Style Decision Record (SDR):

```text
Audience and primary jobs:
Brand attributes (3):
Content density and available real assets:
Primary style (one) and rationale:
Secondary influence (optional; one) and rationale:
Explicit rejected styles (two) and why:
Grid / type / palette / imagery / material / motion rules:
Hero signature and recurring visual grammar:
Motion budget, device constraints, fallback behavior:
Expected UX/performance risks and mitigations:
UI states and real backend journeys affected:
Test plan and evidence required:
```

Use the following 0-3 rubric across 3 plausible directions (scoring is a **deliberation tool**, not a machine-generated aesthetic truth):

| Criterion | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Brand and audience match | Misaligned | Fragile link | Relevant | Naturally expressive |
| Task clarity and content fit | Obscures task | Frequent friction | Mostly usable | Highlights important action |
| Available original assets and writing | Needs invented assets | Several placeholders | Sufficient | Assets carry the narrative |
| Accessibility and motion adaptability | Major barriers | Workarounds | Feasible | Accessible by design |
| Performance feasibility | Heavy/unknown | High cost | Manageable | Efficient by default |
| Distinctiveness vs generic templates | Stock look | Trend clone | Characterful | Ownable concept |

Hard gate: refuse any style that requires inaccessible task flows, fabricated content, or broken API behavior, even if it wins on visuals. For small tool-oriented apps prefer content/interaction clarity; save cinematic animation for public-facing showcase moments.

## 2. Distinctive combinations (examples, not recipes to copy)

| Dominant + secondary | Coherent result | Limit or avoid |
|---|---|---|
| Swiss + Human Editorial | disciplined index/grid with human narrative photography and expressive type | maintain reading order; avoid oversized copy covering body content |
| Minimalism/Bento + Tactile | clean utility with one physical interaction motif | do not 3D-render every card; preserve form semantics |
| Human Editorial + Immersive 3D | chapter-based story with a single exploratory product object | image/poster fallback, semantic narrative without JS |
| Neo-Brutalist + Cute-alism | sharp structural frame plus rounded character accents | no random pastel and neon collisions or cartoon UI overload |
| Retro + Cyberpunk | selected era-specific retrofuturistic console | avoid fake security dialogs and confusing OS clones |
| Ambient Aurora + Glass | atmospheric background with one readable floating control surface | limit blur/filters and support opaque fallback |
| Kinetic Maximalism + Swiss | loud typographic rhythm kept coherent by an exact grid | no perpetual motion on functional tasks |
| Claymorphism + Bento | approachable teaching/onboarding cards with tactile feedback | no low-contrast pastel text or oversized useless boxes |
| Cyberpunk + Swiss | precise technical index with one signal color | fake meaningless telemetry disallowed |
| Minimalism + Story-Driven 3D | quiet content shell and one isolated cinematic feature | maintain fast first paint, no compulsory 3D |

Avoid combining two highly dominant materials (full-page glass + clay + hard-shadows), two competing eras, or three animated identities. Create uniqueness by expressive typography, content-specific graphics, and meaningful motion rather than stacking styles.

## 3. Turn style into an implementable system

Deliver these *before* animation code:

1. **Composition:** establish columns, max content measure, gutters, breakpoints/container query behavior, optical alignment and content order. Specify which sections use full bleed and why.
2. **Typography:** select readable text family, deliberate display family if justified, typescale (`clamp` with sensible minimum), type contrast, line-height, wrapping/hyphenation, and multilingual fallback fonts.
3. **Color semantics:** define background/surface/text/muted/action/focus/error/success tokens. Decorative colors never substitute for status labels. Check combinations *over real backgrounds*, including animated and translucent panels.
4. **Depth/material:** pick *one* main material system: flat planes, editorial paper, tactile shadows, hard-shadows, translucent glass, or spatial rendering. Define elevation and interactive states independently of decoration.
5. **Motion identity:** define entry/on-scroll/hover/press/route transition rules, staggering, easing, duration, offscreen teardown, interrupt handling, no-motion equivalent and CPU/GPU fallback. Avoid automatic marquees unless content remains available when paused.
6. **Data reality:** map cards, filters, counters, diagnostics and CTAs to actual API data or clearly authored content. Include loading/empty/error/auth and long-value states.
7. **Images/3D:** inventory source rights, alternate text or decorative status, responsive crops, compression, lazy loading, GPU budget, poster fallback and environment failure behavior.

### Reference primitives (adapt to actual project)

**Responsive bento without DOM-order mismatch:**

```css
.bento { display: grid; grid-template-columns: repeat(12,minmax(0,1fr)); gap: clamp(12px,1.5vw,24px); }
.bento > * { grid-column: span 4; min-width: 0; }
.bento > .featured { grid-column: span 8; }
@media (max-width: 760px) { .bento > *, .bento > .featured { grid-column: 1 / -1; } }
```

**Readable glass panel with graceful opaque fallback:**

```css
.glass-panel { background: #16222e; color: #fff; border: 1px solid #5c7485; }
@supports ((backdrop-filter: blur(14px)) or (-webkit-backdrop-filter: blur(14px))) {
  .glass-panel { background: rgb(22 34 46 / 90%); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); }
}
@media (prefers-reduced-transparency: reduce) { .glass-panel { background: #16222e; backdrop-filter: none; -webkit-backdrop-filter: none; } }
```

**Reduced motion that does not hide content:**

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-loop { animation: none !important; }
  .chapter-reveal { transform: none !important; opacity: 1 !important; }
  .scroll-tween { transition: none !important; }
}
```

For GSAP timelines, implement matching JS reduced-motion branches and `revert()`/`kill()` teardown; CSS alone does not stop JS-driven animation. Never use transform/opacity to conceal essential content by default when JS may fail.

## 4. Style-sensitive test obligations

| Style | Additional evidence beyond base QA |
|---|---|
| Minimalism/Bento | DOM order matches reading order; cards meaningful; data truncation and empty state stable |
| Human Editorial | focal crop at 320px; font wrapping, captions, text zoom, reading order |
| Neo-Brutalism/Cute-alism | contrast despite saturation; hard-shadow focus clarity; animated decoration not obstructive |
| Retro / Dial-Up | faux windows do not impersonate system UI; keyboard/window and responsive state |
| Aurora Ambient | constant text contrast over full animation; GPU load + reduced motion fallback |
| Story 3D | no-WebGL poster, scroll pin teardown, touch/keyboard scene, long page / resize |
| Glassmorphism | no-filter browser; background change and high-contrast test, low-end GPU |
| Kinetic Maximalism | pause loops; accessible content order; distraction-free reading and CTA access |
| Tactile Skeuomorphism | native input semantics; control values match visual state; touch and keyboard |
| Cyberpunk | no critical info expressed only by color, readable mono and no unsafe flashes |
| Claymorphism | state discernibility, pastel contrast, accessible tactile controls |
| Swiss | asymmetry reflows under 320px/200% zoom; grids don't rearrange content illogically |

Global browser/quality gate: real screenshots in key states, actual backend E2E, WCAG 2.2 AA *target*, key interactions keyboard-accessible, color contrast at least 4.5:1 normal text and 3:1 large text unless a documented WCAG exception applies, reduced motion tested, no content hidden behind layered/scroll elements, no significant visual regression. Aim for field p75 LCP <=2.5s, INP <=200ms and CLS <=0.1. Record **measured** vs **unmeasured** separately. A style does not earn special exemptions from requirements.

## 5. Review loop: prove visual identity, not just trend conformity

Review at 3 distances: 3-second recognition (distinctive composition), 10-second information scan (task clarity), and 60-second real use (navigation, input, recovery). Compare two viable art-direction prototypes at equal content, test with target users where possible. If style does not improve perceived identity or comprehension, simplify it. Require original asset provenance and avoid copying any single reference's composition/implementation wholesale.

Useful links: https://tilda.education/en/web-design-styles ; https://www.figma.com/resource-library/web-design-trends/ ; https://www.w3.org/TR/WCAG22/ ; https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion ; https://web.dev/articles/vitals
