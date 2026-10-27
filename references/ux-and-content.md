# UX, content, responsive and inclusive interaction

## User-journey contract

Before pixels: identify the top 3 user intents and success criteria. Map entry -> decision -> action -> feedback -> recovery for each. Make actual task completion fast. Use real labels, specific microcopy, plain error text, progressive disclosure and predictable navigation. The dramatic moment must not interrupt the user's primary goal.

## Information architecture

- Organize content by users' mental models and existing product entities; test labels against the provided content.
- Prominent state and navigation cues; avoid hidden mystery navigation as the only path.
- Preserve browser Back, deep linking, scroll restoration, anchors, standard keyboard shortcuts where applicable.
- For product-heavy apps, maintain search, filtering, sorting and pagination semantics and accessible result counts.
- Design empty/loading/error/partial/offline/auth-expired/success states **before** making the polished happy path.

## Inclusion and accessibility review

- Target WCAG 2.2 AA; semantic landmarks, heading order, accessible names/descriptions, correctly associated form labels, inline validation, focus order/visible focus, no keyboard traps.
- Ensure interactive roles follow behaviors: button for action, link for navigation. Support Esc close, focus return in dialogs, aria-live where necessary without spam.
- Contrast and legibility across all interaction states; distinguish status with more than color. Avoid hover-only interactions; maintain pointer and touch equivalents and adequate hit areas.
- Test reduced-motion, zoom to 200%-400%, text resize, high contrast and system dark mode if supported. Motion alone never conveys state.
- Keep 3D/Canvas content supplementary or provide equivalent semantic controls, accessible explanations and fallback.
- Consider localization (RTL, long strings, cultural meanings), privacy and consent for tracking/recording/telemetry.

## Content craft

Write honest product-specific copy with real nouns and verbs; do not invent case studies, credentials, revenue, user reviews, data points or client names. Tune language to brand while keeping instructions and errors unambiguous. Ensure typographic treatment survives long real text, truncation, dynamic content and translation.

## UX verification tasks

- Complete key journeys with keyboard alone, including navigation, settings, forms and dismissible overlays.
- Complete primary journey with touch-sized viewport, slow network and a validation failure.
- Compare content across loading, success, empty, malformed response, expired session and 5xx.
- Confirm clear escape paths, disabled conditions and error recovery; never strand user behind a loader or animation.
