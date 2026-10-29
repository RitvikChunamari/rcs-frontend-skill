# Interaction architecture and behavioral fidelity

Use for nontrivial components, animations, navigation, data mutation, onboarding, editors, multi-step workflows, touch gestures and 3D controls. A premium interface is a predictable machine with a compelling surface.

## Model the UI as states and transitions

For each critical component, write a **state table**: initial, hover (optional), focus, pressed, active, pending, success, empty, failure, disabled, offline, permission-denied. Define trigger, visuals, semantic announcement, keyboard behavior, backend effect, and recovery for each transition. Never replace actual permissions with disabled styling alone.

Example search box:

| Event | State | Result | Cancel/rollback | A11y |
|---|---|---|---|---|
| Type | editing | Update visible query immediately | Cancel prior stale request | Label persists |
| Delay or submit | loading | Issue query w/ cancellation or request identity | Abort stale query | Polite status announcement |
| Empty response | empty | Helpful no-result state | Clear/edit query | Proper status text |
| Error | error | Explain retry/refine action | Retry preserved input | Error announced |
| Click result | navigating | Use true route | Back restores relevant state | Focus/heading handled |

## Interaction contract

- **Intent:** what task is this interaction serving?
- **Trigger:** pointer, keyboard, touch, scroll, viewport, API event or time; no hover-only vital information.
- **Feedback:** how quickly does the user perceive recognition? Press, loading and completion are distinct.
- **Duration/curve:** use a consistent motion vocabulary; do not give every element a unique easing.
- **Interruption:** rapid repeated clicks, route changes and scroll reversal must not freeze UI or produce duplicate submissions.
- **State persistence:** decide whether filters, scroll position and tab selection survive navigation/refresh.
- **A11y:** native semantics, focus return, semantic live regions, keyboard path, reduced motion.
- **Backend:** request/payload/response, permission check, timeout, retries (idempotency), consistent errors.

## Motion-as-information hierarchy

Level 0: no motion for essential access. Level 1: affordance micro-feedback (press/focus). Level 2: spatial continuity (drawer, modal, page change). Level 3: editorial reveal (section narrative). Level 4: immersive 3D; only if content still usable without it. Determine the level per user journey, not per aesthetic fad.

## Scroll-driven experiences

Provide explicit entry/exit offsets, scrubbing logic, pinning boundaries and scroll ownership. Audit touch scroll, focus traversal through pinned content, browser back, anchor links and resize. Never create artificial content lock that prevents scrolling to actual information. Prefer normal document flow when the narrative doesn't require pinning. Test reduced-motion static state and keyboard navigation of horizontal sequences.

## Advanced navigation

If using View Transitions API, verify availability and route behavior; manage focus/heading semantics and reduced-motion behavior. Animated page transitions must not delay navigation semantics. Support back/forward, route refresh, direct deep-link, loading/skeleton and error boundaries.

## State-machine acceptance template

Write Given / When / Then for the success path, an edge case, a backend error, keyboard-only access, reduced motion, and a mobile touch path. Do not claim animation is finished when only the primary happy-path mouse gesture was seen.

Sources: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API ; https://playwright.dev/docs/test-assertions
