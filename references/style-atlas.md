# Visual style atlas: 12 production-ready art directions

Use this as a **decision library**, not a set of presets to apply indiscriminately. Read with `art-direction.md`, `ux-and-content.md`, and `style-composition.md`. The terms **Cute-alism** and **Dial-Up Delight** are informal creative descriptors; do not present them as standards, universally agreed categories, or verified current market-leading trends. Each profile is a hypothesis to validate against brand, audience, content, actual assets, devices, and usability tests.

Choose a **dominant style** and at most **one secondary influence** for most production projects. Do not combine all 12. For each style specify: brand reason, layout grammar, typographic roles, 2-4 color roles, image/material language, interaction principles, mobile re-composition, low-motion state, accessibility risk, performance budget, and evidence of improvement.

## 1. Minimalism + Bento Grid

- **Voice / best fit:** confident, calm, legible; product/SAAS platforms, analytics dashboards, corporate sites, premium utility, restrained portfolios. Minimalism and Bento are separable: a minimal page need not be tiled; a Bento dashboard may be dense.
- **Visual grammar:** edited content, negative space, type-driven hierarchy, proportional or modular CSS Grid; 2-5 asymmetrically weighted cards with deliberate information priorities; use tiles only when they improve chunking. Establish 8px/4px rhythmic increments as a *starting rule*, not dogma.
- **Implementation:** CSS Grid (`minmax`, `repeat`, `subgrid` if target support), container queries, semantic cards and tokens; use actual data, avoid fake dashboards. Keep the DOM reading order logical if the visual ordering changes.
- **Motion / responsive:** restrained stagger-on-entry only where it aids sequence; card affordance via subtle border/color, not perpetual bobbing. On mobile, reflow to single-column or meaningful rows; do not convert important actions to hidden panels.
- **Avoid:** ubiquitous 3-by-3 card collages, random 24px radii and empty tiles, entire sites enclosed in cards, extreme whitespace that delays key tasks.
- **QA:** hierarchy at 5-second glance; content density and empty states; tab order vs visual order; long translated labels; mobile tile reading order.

## 2. Human Editorial

- **Voice / best fit:** narrative, thoughtful, tactile; fashion, high-end lifestyle, agencies, culture, journals, distinctive portfolios.
- **Visual grammar:** deliberate asymmetry, magazine spreads, expressive serif headlines paired with legible text faces, asymmetrical captions, folio/index details, purposeful image cropping and long-form reading rhythm. The *actual* photography/copy is the art direction.
- **Implementation:** varied CSS Grid spans and typographic scale, well-composed responsive image sources, readable line length, explicit media rights, no text burned into images when semantic text works.
- **Motion / responsive:** reveal imagery/typography at chapter beats; pin only where narrative benefits; preserve scannability, a working table of contents and keyboard anchors. On mobile, re-author sequence rather than shrinking the magazine spread.
- **Avoid:** fake luxury caused by thin gray text, image-heavy pages without image quality, inaccessible microtype, meaningless italic typography everywhere.
- **QA:** 200% zoom, image focal points, 320px heading wraps, contrast, reading sequence, image load stability, alt text.

## 3. Neo-Brutalism + playful 'Cute-alism'

- **Voice / best fit:** rebellious, confident, youthful; event sites, creative studios, indie tools, expressive brands. Cute-alism here means pairing a structural brutalist grid with soft, rounded, playful illustration/detail, **not** adding kawaii decoration to every button.
- **Visual grammar:** thick borders, near-hard shadows, assertive typography, constrained high-saturation palette, sharp modular layout; optional rounded mascot/shape forms act as the controlled contrasting element.
- **Implementation:** CSS border/shadow and intentionally consistent 2D offsets; explicit focus-visible states distinguish clicks; pair loud blocks with quiet neutral surfaces for complex forms.
- **Motion / responsive:** snap-like transitions, button downshift, restrained hand-drawn jiggle where brand appropriate; keep functional labels stable. Make oversize type wrap deliberately on small devices.
- **Avoid:** neon as a substitute for concept, inconsistent thick shadows, seizure-risk flash/glitch, illegible color combinations, cute graphics that obstruct tasks.
- **QA:** normal and large text contrast, keyboard focus on bold borders, touch targets, screen-reader names for illustrated controls.

## 4. Retro Nostalgia + 'Dial-Up Delight'

- **Voice / best fit:** playful digital memory, independent culture, games, music, apparel, portfolio storytelling. 'Dial-Up Delight' is a working nickname for late-1990s/Y2K web and desktop-inspired layering.
- **Visual grammar:** pixel glyphs, system-window chrome, browser-in-browser frames, sticker/collage motifs, desktop icons, authentic era-specific typography; choose one era (e.g. early desktop or Y2K) rather than mixing every decade.
- **Implementation:** build window-like components with real semantic controls, not screenshots of interfaces; use sprite atlases and optimized pixel assets only if required; limit faux cursors to explicitly decorative contexts.
- **Motion / responsive:** playful window open/close and loading metaphors with honest progress; no simulated system alerts, phishing-like popups, autoplay audio or fake functionality. On mobile, stack virtual windows without obscuring core actions.
- **Avoid:** copying OS trademarks/icons without permission, fake warning dialogs, tiny type, excessive texture, cursor trails that interfere with pointers.
- **QA:** keyboard window controls, visible real vs decorative affordances, mobile viewport overflow, cursor/device compatibility, animation opt-out.

## 5. Ambient Tech + Aurora

- **Voice / best fit:** calm, aspirational tech; AI/wellness/finance premium marketing, immersive tool landing pages (less suitable for high-density enterprise forms).
- **Visual grammar:** softly integrated color fields, custom aurora gradients, restrained luminous edges, subtle grain, measured blur, large stable typography and quiet foreground panels.
- **Implementation:** CSS layered radial gradients/pseudo-elements before canvas/shaders; one modest animation layer rather than multiple expensive full-screen blurs. Put text on a stable contrast-protected surface; add `prefers-contrast` and no-transparency alternatives where supported.
- **Motion / responsive:** slow, low-amplitude lighting; pause animation offscreen and when user requests reduced motion. Avoid full-screen shader loops on low-power phones.
- **Avoid:** generic purple/orange 'AI glow', blurry text, gradient backgrounds behind every card, continuous GPU-heavy animation.
- **QA:** text contrast over every frame, battery/GPU behavior, dark/light surfaces, mobile legibility, no-motion static background.

## 6. Story-Driven + Immersive 3D

- **Voice / best fit:** product launch narrative, premium commerce, museums, cinematic portfolios, technical product explainers with a meaningful object/story.
- **Visual grammar:** chapter-based narrative, strong still frame before action, considered camera path, scene states coordinated with content, occasional scroll-driven type scale; 3D must clarify the product or story.
- **Implementation:** use GSAP/ScrollTrigger for justified timelines and Three.js/R3F only if simpler CSS/SVG/video cannot deliver the experience. Cap draw calls/polygon/texture budgets; compressed GLB/glTF; lazy-load 3D below first meaningful content. Use a good static image/poster alternative.
- **Motion / responsive:** vertical scrolling remains usable; if horizontal chapters are used, provide clear progress and keyboard navigation; never make key information available *only* on scrub. On touch devices use reduced camera path and safe gestures.
- **Avoid:** scroll-jacking, pin traps, fixed-height scroll scenes that break browser back/forward, WebGL required for CTA, dizzying camera movement.
- **QA:** 320px and landscape; reduced motion, no WebGL, scene teardown, battery/load, pinned-section correctness, text visible before JS initializes.

## 7. Glassmorphism + Frost

- **Voice / best fit:** layered dashboards, translucent overlays, selective premium controls, scenic/mobile-first app shells.
- **Visual grammar:** translucent foreground sheets, carefully controlled background separation, thin keylines, tonal elevation. Treat transparency as a material *accent*, not a full design system.
- **Implementation:** `backdrop-filter` only with opaque/translucent **fallback** colors; define tokens for blur, tint, border and readable foregrounds; avoid nesting multiple full-window filtered surfaces. Test behavior over bright, busy, and moving backgrounds.
- **Motion / responsive:** fade/tint changes as panels surface; avoid blur animation and opacity layering on every scroll. Increase opacity or switch to solid surfaces on small/low-end devices.
- **Avoid:** white-on-glass low contrast, unnecessary overlays, frosted controls indistinguishable from disabled ones, expensive repeated backdrop filters.
- **QA:** both supported/unsupported browser behavior, contrast at all scroll states, focus indicators, GPU compositing, background imagery changes.

## 8. Kinetic Maximalism

- **Voice / best fit:** bold promotional campaigns, festivals, avant-garde agencies, experimental music and fashion.
- **Visual grammar:** dense typographic rhythm, impactful display fonts, graphic collage, layered directional geometry, strong visual 'rests' so the hierarchy can breathe. Maximalism is a carefully directed composition, *not* unlimited motion.
- **Implementation:** organize complexity through grid and z-index tokens; use a text hierarchy and semantic main content underneath animated visual layers. Keep heavy assets within a budget; use CSS/SVG before perpetual canvas.
- **Motion / responsive:** marquee loops, kinetic type, controlled collision/overlap and scroll reversals as only a small number of signature moments; pause/stop repeating movement and honor reduced-motion.
- **Avoid:** all regions moving at once, false CTAs buried in graphics, migraine-trigger flashes, unbounded autoplay, content displaced by typography.
- **QA:** reading and CTA scan time, visual order, pause/stop, keyboard, contrast amid overlays, mobile performance and static mode.

## 9. Tactile Skeuomorphism / Neo-Skeuomorphism

- **Voice / best fit:** music/audio tools, synthesizers, instrument panels, hardware configurators, one-of-a-kind interactive portfolios.
- **Visual grammar:** physical-material analogy with directional light, restrained specular highlights, brushed metal/leather/plastic texture, inset/extruded controls and physically believable affordances.
- **Implementation:** create interaction semantics first (real input range, button, switch); skin using layered gradients, borders, box-shadows, SVG or a small texture. Use real unit markings and bounds for dials/sliders, accessible value labels and keyboard behavior.
- **Motion / responsive:** tactile spring and depression with clear state feedback, nonessential realism optional. On mobile, make controls large enough to manipulate without precision drag.
- **Avoid:** visual knobs that cannot be operated by keyboard, texture noise over labels, fake indicators, huge GPU textures for simple toggles.
- **QA:** input state equivalence (visual and accessibility tree), keyboard adjustability, touch, contrast, hit areas, screen-reader values.

## 10. Cyberpunk + Sci-Fi Tech

- **Voice / best fit:** gaming, hardware, developer experiences, futuristic concept products, cinematic AI showcases when supported by brand substance.
- **Visual grammar:** near-black field, 1-2 signal colors (cyan/magenta/acid green), hairline grids/crosshairs, instrument panel labels, angular cuts, schematic diagrams and *meaningful* status readouts.
- **Implementation:** use real diagnostics/data instead of fake code telemetry; high-contrast readable terminal-style monospace only in appropriate metadata; preserve a conventional navigation and main action.
- **Motion / responsive:** discreet scan sweeps / indicator pulses, optionally a singular glitch transition; no essential information in rapidly flashing details. Lower decoration for data entry and mobile.
- **Avoid:** fake system authority, random hexadecimal panels, nonstop glitches, illegible tiny monospace, neon green on every element.
- **QA:** color-blind use beyond hue, error state clarity, contrast, flash safety, navigation efficiency, focus states, performance with overlays.

## 11. Claymorphism + Soft 3D

- **Voice / best fit:** approachable edtech, kid-facing learning (with age-appropriate UX), onboarding, gamified utilities, warm playful experiences.
- **Visual grammar:** soft inflated forms, gentle pastel palette with *readable* foregrounds, coherent soft shadows, rounded illustrated characters, layered material cues; choose a consistent simulated light direction.
- **Implementation:** CSS-based layered shadows for cards and buttons; lightweight authored SVG illustration before WebGL; ensure each decorative 3D object has no false affordance. Clear separation between active vs disabled vs selected states.
- **Motion / responsive:** bouncy response tied to input or progress, not all components floating. Reduce movement for sensitive users and lower-end hardware.
- **Avoid:** low-contrast pastel body copy, oversized clay cards hiding information, too many floating cartoon shapes, heavy mesh assets for buttons.
- **QA:** body copy and state contrast, touch targets, disabled-vs-enabled differentiation, color vision, load and mobile reflow.

## 12. Swiss / International Typographic Style

- **Voice / best fit:** architecture, editorial information, institutional communication, technical portfolios, high-information utility and bold yet disciplined creative direction.
- **Visual grammar:** mathematically coherent grid, asymmetric placement, typographic contrast within a controlled family, clear alignment axis, restrained palette, objective labeling, large type as form; choose appropriate sans fonts rather than assume Helvetica licensing.
- **Implementation:** CSS Grid with explicit layout columns/baselines; fluid type (`clamp`) with safe line lengths; consistent indexes/section rules, careful optical corrections. Subvert one grid rule intentionally for a focal moment, not randomly.
- **Motion / responsive:** type masking, purposeful grid reflow, anchored section transitions; animation should reinforce structure. Mobile uses new grid proportions and intact reading order, not a shrunk desktop poster.
- **Avoid:** equating Swiss with generic black/white template, unreadable oversized words, illegible dense grids, multiple arbitrary alignments.
- **QA:** type at 320px and 200% zoom, content order vs reading order, headings and logical hierarchy, alignment on both desktop and mobile.

## Reference trail and limits

Treat the following as starting points for primary/secondary research, not a substitute for live inspection:
- Tilda guide (minimalism, editorial, Swiss, brutalism, retro and bento): https://tilda.education/en/web-design-styles
- Figma 2026 trend overview (3D, motion, maximalism, retrofuturism, neo-brutalism, etc.): https://www.figma.com/resource-library/web-design-trends/
- MDN CSS Grid: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout
- MDN `backdrop-filter` and compatibility caveats: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter
- MDN `prefers-reduced-motion`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion
- GSAP ScrollTrigger documentation: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- WCAG 2.2 contrast criteria: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

Do not treat marketing claims such as "increases engagement drastically" or "always loads rapidly" as established properties of an aesthetic. Effects on engagement, task completion and performance must be tested for the actual product and audience.
