# Choose a direction from the actual brief

Use for a new visual system or a requested redesign. Read the existing page and project design notes first. A style name is a starting point; the result must explain how this particular product works.

## Resolve who sets the direction

1. **User-directed.** Follow supplied styles, examples, fonts and exclusions. Interpret references as attributes to study. A request for a specific look takes precedence over your category preferences.
2. **Combined.** If the user names a combination, assign each influence a job. Otherwise add a supporting influence only when it solves a concrete need. Start with one lead and one support. If the user explicitly requests more, bound each to a role or region and resolve conflicts before building.
3. **Context-chosen.** With no requested style, preserve an existing coherent system for additions and refinements. For a new project or an authorized replacement, infer a direction from the evidence below. State the choice and reason, then proceed.

Existing visual evidence includes the running UI, tokens, assets and established components even if DESIGN.md is absent. A stale document loses to confirmed current code and user decisions. Record a local amendment when authorized; do not overwrite unrelated design decisions.

## Build the evidence before the look

For the target screen, identify these six factors. Mark inferred facts and unknowns.

| Factor | Decision it changes |
|---|---|
| Primary activity and task frequency | Navigation, density, hierarchy and acceptable interruption |
| Audience, reading ability and use context | Language, type scale, input methods and familiarity |
| Actual content and available licensed assets | Whether type, product imagery, photography or data carries the design |
| Platform, viewport and assistive needs | Interaction patterns, reflow, focus, motion and contrast |
| Existing brand/system and user constraints | What must persist and where expression is allowed |
| Device, delivery and maintenance budget | Font/media sizes, rendering complexity and dependency choices |

Separate screens within one product. A music editor and its promotional homepage may need different density and motion while sharing type and color roles. Product categories supply hypotheses, not automatic palettes or layouts. Do not infer personality, color or capabilities merely from words such as “AI,” “finance,” or “luxury.”

When the activity and audience are known, missing aesthetic preferences are permission to choose provisionally. Ask a focused question only when competing interpretations change the core workflow or audience. If the product itself is unknown, clarify it before designing a fictional business. Continue inspection meanwhile.

## Compare plausible directions

Consider two or three candidates for substantial new work. For each, connect an observed fact to a layout, type, content and motion decision. Reject a candidate that needs invented proof, unreadable controls, unavailable assets or an unaffordable renderer. Then compare task clarity, content fit, brand continuity, practical delivery and distinctive expression. The rubric in [style composition](style-composition.md) can organize the comparison; its numbers are deliberation aids.

Examples are starting hypotheses, not fixed assignments.

| Evidence in the brief | Plausible direction | What would change the choice |
|---|---|---|
| Frequent comparison of dense operational data | Compact utility or Swiss hierarchy, clear tabular alignment, limited motion | Existing brand system, touch-only input, novice users needing more guidance |
| Long reading with citations and navigation | Typographic editorial, stable reading measure, visible document structure | A technical reference may need denser navigation and code specimens |
| A photographer has strong original images | Image-led editorial or quiet gallery, deliberately different crops | Sparse or unlicensed imagery favors a type-led composition |
| Public-service application with costly mistakes | Familiar forms, explicit progress, restrained styling | A specific public design system should govern its conventions |
| An exhibition has experimental art and a browsing audience | Kinetic or immersive storytelling with immediate access to the work | Low bandwidth or motion sensitivity calls for a static interpretation |
| Physical product with real close-up photography | Tactile detail or editorial product story | An interactive 3D object earns its cost only if it answers a user question |
| A playful learning activity | Friendly graphic forms with clear feedback | Age, literacy and accessibility determine the controls and content density |

The twelve-style atlas is a vocabulary, not a closed menu. A bespoke direction or established project system can be a better fit. Avoid random theme rotation and universal “premium” presets.

## Make combinations coherent

Specify ownership before borrowing features. For Swiss + editorial, the grid and control hierarchy might come from Swiss while image sequencing and narrative pacing supply the editorial influence. Reconcile type, contrast, spacing and state tokens once. Do not alternate unrelated component kits from section to section.

For apparently conflicting requests, preserve the requested character in an appropriate layer. A maximalist dashboard might use bold section identity around a stable data workspace. Explain the tradeoff. Do not quietly turn an explicitly expressive brief into minimalism.

## Record the decision

For substantial work, update the project's existing design brief or use [creative direction record](../assets/templates/creative-direction-brief.md). Include selection mode, evidence, assumptions, selected direction, rejected alternative, combination roles, tokens, density, motion, and the checks that would disprove the choice. A concise example:

“Chosen for this stock-management screen: a compact typographic system because staff compare quantities repeatedly on small laptops. Preserve the green status semantics. Use roomy confirmation dialogs for destructive actions. Reconsider density if the long-name and 200% zoom checks fail.”

Confirm the result against real content at desktop and mobile sizes. If the render contradicts the brief, revise the affected design decision and recheck. Keep the direction stable across subsequent screens unless new evidence or the user changes it.
