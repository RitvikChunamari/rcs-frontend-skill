# Design-system research and transfer rules

Read when the project needs a systematic design language, large UI kit, company design influences or token/component architecture. These are **principle references**, not permission to replicate trade dress. Official/public documentation is preferred; a consumer brand's public product UI is not equivalent to an open component system.

## Core systems: what to learn

| Source | Documentation | Borrow the method, not the identity |
|---|---|---|
| Apple Human Interface Guidelines | https://developer.apple.com/design/human-interface-guidelines/ | Purpose, focus, interaction familiarity, touch ergonomics, legibility, spatial hierarchy, platform adaptation, meaningful delight, native patterns. |
| Google Material Design 3 | https://m3.material.io/ | Adaptive layouts, semantic color, dynamic themes, state/feedback, shape, interaction consistency, content hierarchy. |
| Microsoft Fluent 2 | https://fluent2.microsoft.design/ | Token-to-component mapping, cross-platform UI, density, accessibility, coherent control behavior. |
| IBM Carbon | https://carbondesignsystem.com/ | Enterprise patterns, accessible tables/forms, dense data presentation, systematic spacing and data visualization. |
| Adobe Spectrum | https://spectrum.adobe.com/ | Expressive but dependable tool UIs, adaptive density, accessible color and typography systems. |
| Atlassian | https://atlassian.design/ | Design foundations, predictable interactive states, work-management navigation and design-to-code alignment. |
| Shopify Polaris | https://shopify.dev/docs/api/polaris | Merchant tasks, information hierarchy, commerce admin consistency, platform-specific components; verify current product surface before implementation. |
| GitHub Primer | https://primer.style/ | Developers' workflows, semantic tokens, scalable components, themes, status and feedback. |
| Salesforce Lightning | https://www.lightningdesignsystem.com/ | Complex enterprise objects, forms, data density, accessibility and operational workflows. |
| Ant Design | https://ant.design/ | Data-heavy CRUD patterns, component contracts and interface consistency; customize brand instead of cloning defaults. |
| Base Web (Uber) | https://baseweb.design/ | Component API design, extensible theme architecture, accessible web components. |
| USWDS | https://designsystem.digital.gov/ | Plain-language tasks, accessibility, critical-journey reliability and robust forms. |

## Product experiences requiring careful interpretation

- **Meta / Facebook / Instagram / WhatsApp:** inspect public, current products and official published design content; learn from graph navigation, reactions, content hierarchy, threaded conversations, continuity and fast feedback. Do not assert there is one publicly downloadable, comprehensive 'Meta design system' encompassing all products. Respect privacy and cultural sensitivity.
- **Netflix / Hawkins:** reported cross-platform/internal design system with shared tokens across consumer and professional experiences; much of the implementation is not publicly available. Study consumer experiences for content-led visual hierarchy, focus, motion/cross-device navigation and personalization; do not claim access to proprietary Hawkins tokens or source. Background: https://learn.thedesignsystem.guide/p/how-netflix-builds-design-systems
- **Spotify / Encore:** publicly shared thought leadership on scaling coherent music product systems across platforms; do not infer proprietary library details from public screenshots. Related: https://www.designsystems.com/
- **Airbnb, Stripe, Linear, Notion, Vercel:** use public, observable flows to reason about clarity, trust, typography, timing, feedback and content density. Avoid treating screenshots as component APIs.

## System selection heuristic

1. Evaluate task: consumer creation vs enterprise operations vs editorial storytelling vs native mobile.
2. Use **at most 1 dominant foundation** plus compatible concepts from other systems; no wholesale fusion of Apple glass, Material shape, Carbon density and Netflix red.
3. Establish theme tokens: `color.*`, `typography.*`, `space.*`, `radius.*`, `shadow.*`, `motion.*`, `zIndex.*`, `breakpoint.*`. Add semantic tokens like `surface`, `text-muted`, `focus-ring`, `danger`, `success`.
4. Define component variants, hover/active/focus-visible/disabled/loading/error/success/empty and responsive states.
5. Keep design tokens synchronized with implemented CSS, Figma variables and component props when tool access allows.
6. Prefer testing actual user flows over assuming a popular design system guarantees good UX.

## Brand translation example

Brief: an editorial portfolio with Swiss typography and cinematic motion. Use Apple-level restraint and familiar controls, IBM-level typographic and grid discipline, Netflix-level content focus; **do not** port system-branded chrome. Invent a distinct typographic lockup, contrast rhythm, grid asymmetry and one project-card signature interaction.
