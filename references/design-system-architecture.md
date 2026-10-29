# Design-system architecture and governance

Read when building new systems, refactoring inconsistent products, supporting multiple themes/brands, Figma-to-code translation or distributing components. The goal is not a giant UI kit: it is a compact system that makes deliberate design repeatable.

## System layering

1. **Foundations**: color primitives, typography, spacing, grid, radii, border widths, shadows, motion, icon rules, focus, breakpoints and container policies.
2. **Semantic roles**: background canvas/surface/raised, text primary/muted/inverse, border, link, focus, feedback/error/warning/success, motion enter/exit. Semantic usage must survive theme changes.
3. **Components**: headless behavior + visual variants + states + responsive rules. Preserve behavior semantics and avoid duplicated tokens per component.
4. **Patterns**: form, dialog, nav, search, onboarding, chart, editorial project case, hero, notifications, data grids; patterns document coordination and behavior.
5. **Experiences**: authored pages combine patterns with editorial rhythm and content. Do not make every screen look like a cloned component catalog.

## Tokens and modes

Use JSON/Style Dictionary/DTCG-compatible token exchange only when the project benefits from tool interchange. **DTCG 2025.10** is a community-group format, not a W3C Recommendation. A small project may need only CSS variables. Keep token meaning stable, and resist a token for every one-off value.

Illustrative token hierarchy:

```css
:root {
  --color-ink-900: #121821;
  --color-paper-100: #f8f7f4;
  --color-signal-500: #f15b42;
  --surface-page: var(--color-paper-100);
  --text-primary: var(--color-ink-900);
  --focus-ring: var(--color-signal-500);
  --space-1: .25rem;
  --space-2: .5rem;
  --space-4: 1rem;
  --radius-control: .45rem;
  --motion-quick: 160ms;
}
```

The palette above is an example, not a prescribed style. Use semantic variants for dark mode/high contrast and functional state colors. Avoid semantic tokens that are just arbitrary hex labels.

## Component contract

For each core component, record: responsibility, inputs, states, slots, default keyboard behavior, accessible name, content constraints, layout variants, animation policy, theme rules and corresponding test. Define disabled vs read-only; loading actions, focus return and form errors. Ensure focus remains understandable in dialogs/menus. Prefer native semantics and proven accessible primitives over hand-built ARIA.

## Governance and drift control

- A component change requires a use-case or recurring pain, not speculative abstraction.
- Track component consumers; version breaking API changes; provide migration notes.
- Maintain representative Storybook examples or equivalent playground for default, empty, error, long text, keyboard, dark and narrow conditions.
- Create a screenshot baseline for at least one realistic page per theme, not only isolated atoms.
- When Figma is available, reconcile variable names/typography/layout but verify browser rendering rather than assuming 1:1 fidelity.
- Prefer accessible open-source components (Radix/React Aria/Ariakit etc.) chosen selectively. A design system should express the product's voice, not default library styling.

## Evaluating major-company systems

Study Apple HIG for interaction conventions and modality, Material 3 for components/adaptive design, Fluent for cross-platform density, Carbon for enterprise consistency, Spectrum for rich application patterns, Polaris for commerce admin, Primer for developer tools. Meta/Netflix and others can provide observed product patterns, not necessarily public authoritative reusable design systems. Never label imitation as compliance, and do not copy trademarked visual identities.

Official format: https://www.designtokens.org/tr/2025.10/format/
