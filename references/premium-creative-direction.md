# Premium creative-director protocol

Load for ambiguous briefs, major redesigns, flagship landing pages, identity-heavy interfaces and design critiques. Design quality is the *coherence of decisions under constraints*, not the number of effects.

## 1. Extract the real design problem

Record the **user promise**, audience, top task, competitive sameness, brand personality, visual constraints, content inventory, and measurable success. Distinguish: facts observed in code/product; facts supplied by user; hypotheses needing verification. For redesigns, inventory protected routes, copy, imagery and interactions before drawing.

Produce a one-sentence thesis in this form: `For [audience], this should feel like [mental model] because [product truth], expressed through [visual mechanism], without compromising [primary task].`

## 2. Create three meaningfully different directions (only when task scale warrants)

For each, specify **concept / layout grammar / typographic voice / palette / graphic motif / signature interaction / engineering cost / risks**. Three directions must differ structurally, not just in accent color. Compare against the existing brand and user journeys; choose one, optionally borrow one supporting trait from another. If user has already selected a style, honor it and skip forced alternatives.

Use this decision matrix (1-5): brand fit 25%, user clarity 25%, differentiation 20%, maintainability 15%, production feasibility 15%. Treat a high score as a prioritization aid, not objective proof. Exclude any direction that obscures content, inaccessible interactions, or cannot be built within constraints.

## 3. Define a visual grammar (tokens are not enough)

Document the repeatable decisions that make a screen unmistakable:
- **Compositional signature:** which edge is aligned, how negative space works, density cadence (e.g. 2 quiet panels then one dramatic spread), where asymmetry is permissible.
- **Typography:** display and body families, size/clamp policy, heading line-break behavior, width/measure, metadata treatment, numeral style.
- **Palette:** neutral foundation, functional semantic colors, single expressive accent; contrast checks against actual backgrounds.
- **Material:** flat editorial paper, refined glass, physical device, ink, anodized metal, etc. Define shadow/light *source* and consistent radius/stroke rules.
- **Image language:** original art direction, crop/perspective, lighting, subject placement, source provenance and rights.
- **Motion voice:** precise/inertial/playful/cinematic; preferred duration families; trigger; reduced-motion substitute. Use motion to communicate a model of the system.
- **State vocabulary:** empty/loading/disabled/success/errors look like part of the same brand, not imported generic patterns.

## 4. Construct a signature moment without compromising the product

Choose one hero/high-impact transformation that teaches or reveals something **specific**. Example: a service's data structure unfolds into a graphic system; a portfolio project card opens into an editorial spread with continuity. Avoid effect-for-effect's-sake, copycat layouts, infinite cursor-chasers and decorative preloader gates. Progressive enhancement must leave content available when JavaScript/animation/WebGL fails where practical.

## 5. Screen-by-screen critique ritual

Evaluate three distances: (a) blurred/thumbnail, hierarchy and contrast; (b) 1:1 screenshot, alignment and type craft; (c) interactive browser, affordances, feedback and flow. At each size ask:
1. What is the *first* thing perceived, and should it be?
2. Is the next step clear without needing motion to explain it?
3. Can any two decorative choices be removed to make the concept stronger?
4. Is the dominant rhythm intentional or merely repetitive cards?
5. Are backgrounds, image crops and reading contrast excellent on mobile?
6. Which part looks like a component library's default? Redesign that part.
7. Could this be mistaken for a near-clone? Rework its structure or storytelling.

Always critique at least one key screen **twice** after implementation; compare actual before/after images and record a specific correction. Avoid pretending design quality is measurable from source code alone.

## 6. Decision record

Use `assets/templates/creative-direction-brief.md` as an editable project artifact. Record rejected directions, tradeoffs, licensing/asset assumptions and reasons. For the next agent, put lasting decisions in project docs rather than relying on chat memory.
