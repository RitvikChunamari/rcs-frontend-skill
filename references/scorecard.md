# Creative and engineering scorecard

Score each dimension 0-5 based on evidence, never solely gut feel. Weighted percentage is guidance for iteration, **not** a scientific benchmark, official award or objective ranking.

| Dimension | Weight | A 5/5 requires |
|---|---:|---|
| Distinctiveness / art direction | 18 | Recognizable concept, coherent visual language, does not resemble a default template |
| Hierarchy / graphic craft | 14 | Intentional typography, spacing, composition, image craft, optical finish |
| UX / task clarity | 15 | Key journeys self-evident, feedback/recovery strong, no interface puzzles |
| Motion / tactile behavior | 12 | Original, purpose-driven, coherent, interruptible, reduced-motion compatible |
| Responsive / cross-device | 10 | Carefully re-composed small/large layouts, no hidden interactions or overflow |
| Frontend quality / maintainability | 10 | Project-aligned code, tokens/components, no regressions, sensible bundles |
| Backend integration / state truth | 9 | Real data, auth/permissions, error and success correctly handled |
| Accessibility | 7 | Automated + manual validation, practical keyboard and screen reader support |
| Performance / robustness | 5 | Measured or honestly noted, good loading/interactivity/stability |

## Release rules

- Do not mark an implementation "done" with broken critical journeys, newly introduced high-impact accessibility failures or silent data/API errors regardless of score.
- If any criterion scores under 3, identify remediation before increasing decorative complexity.
- Favor **one excellent memorable moment** over many mediocre effects. Functionality and accessibility are constraints, not optional low-weight tradeoffs.
- Make improvement evidence-backed: screenshots compared, test results, user feedback or measurable UX/performance where available.

## Final self-critique questions

1. Would the interface still be recognizable without the accent color and illustrations?
2. Does the typography and layout express the product's personality rather than the library's defaults?
3. Is each animation serving orientation, affordance, feedback or narrative?
4. Are mobile and reduced-motion versions equally usable, not merely degraded?
5. Are controls bound to real backend behavior and genuinely resilient to failures?
6. Can the user understand the page within seconds and finish their main task?
7. Do observed screenshots show enough quality to justify the design claims?
