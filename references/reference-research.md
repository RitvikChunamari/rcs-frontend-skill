# Reference research: systematic reverse-engineering without cloning

## Where to look

- **Creative websites / motion / 3D:** https://www.awwwards.com/websites/ , https://www.cssdesignawards.com/ , https://www.siteinspire.com/ , https://godly.website/ , https://www.hoverstat.es/ , https://www.behance.net/ ; search by project type, interactive technique and date. Awwwards is inspiration, **not proof** of UX, accessibility or performance quality.
- **Shipped UX flows and screen libraries:** use freely accessible product sites, public case studies, and public views such as https://pageflows.com/ . Treat commercial libraries as optional only when the user already has authorized access; never make them a dependency.
- **Graphic/creative technology studies:** https://tympanus.net/codrops/ , https://www.shadertoy.com/ (check licenses), https://threejs.org/examples/ , https://www.figma.com/community/ (check asset licenses).
- **Systematic patterns:** https://www.designsystems.com/ , official component docs. For people using custom component galleries, inspect implementation and terms before adoption.

## Research protocol for each of 3-5 references

1. **Capture evidence, don't just view thumbnails.** If browser tools exist, open the live site; capture home, navigation, one internal page, mobile layout and a complete user journey. Read interaction text. Observe initial load and content before animations complete.
2. **Record visual anatomy.** Hero proportions, baseline/grid columns/gutters, type size/line-height/weight/optical alignment, contrast, negative space, image crop, masks, compositing, transitions between sections, composition at desktop/tablet/mobile.
3. **Record behavior by phase.** Trigger (click, hover, pointer, scroll, touch, state change), delay/duration, easing (estimate), transforms, overlap, staggering, pinning, scrub, thresholds, velocity response, exit and reverse. Note what happens with reduced motion and keyboard/touch.
4. **Infer the likely technique only when justified.** Is it CSS transform, SVG stroke/mask, GSAP timeline, ScrollTrigger pin, Lenis sync, Canvas2D, WebGL/Three, displacement shader, video, Rive? If source isn't accessible, label technique as a hypothesis.
5. **Inspect quality.** Accessibility, semantic navigation, GPU/battery impact, heavy images, scroll traps, text selection, anchor links, interaction responsiveness, cumulative layout shift. A website with a beautiful effect may still be a bad pattern to reproduce.
6. **Extract transferable rules** into a small reference matrix and invent an alternative execution suited to the product. Never copy protected imagery, logos, wording, code or recognizable pixel-specific composition.

### Example reference matrix

| Source observation | Underlying rule | Original interpretation | Failure mode |
|---|---|---|---|
| Big off-grid headings reveal project imagery | Typography acts as masking & navigation | Project title reflows with an original split-typographic system | Hard to read on mobile |
| Scene transforms through scroll | One cohesive spatial narrative | Single hero 3D object responds to progress; fallback static illustration | GPU bottleneck, motion discomfort |
| Horizontal work gallery | Focus on editorial sequencing | Native horizontal cards with snap and obvious keyboard arrows | Trap wheel scroll or hide controls |
| Cinematic page transitions | Route continuity and orientation | Lightweight shared-element transition with immediate interactive readiness | Delays actual navigation |

## Browsing decision tree

- Have browser access? Inspect live behavior and capture images/video where permitted; if tools support devtools, inspect CSS, network, console and performance profiles.
- Only screenshots? Decompose visible layout and state explicitly; don't pretend to know scroll choreography or underlying implementation.
- No browsing? Use user-provided references and documented design principles; flag inspiration as unverified.
- Asked to replicate a particular page? Clarify whether exact reproduction is permitted/owned; match intended **function and general style**, not third-party distinctive expression, unless user has rights to the source.

## Originality filter

Write down: (a) what the inspiration does, (b) why it works, (c) how this product's concept should differ. Demand at least **three intentional differences** (type language, layout logic, interactive metaphor, color/graphics system, storytelling or UX behavior) from any one source. Avoid generically copying current trend bundles: multicolor neon gradients + floating glassmorphic cards + particle cursor + slow scroll + infinite reveal transitions.
