# Backend-connected frontend: advanced reliability playbook

Read when frontend work touches data, permissions, mutations, uploads, search, realtime/streaming, payments, sensitive account states or distributed async workflows. A beautiful interface that lies about success is defective.

## Before editing

Create a dependency map `screen → state/source → endpoint/event → auth → success/error → persistence`. Inspect actual routes, generated API types, schemas, auth middleware and error conventions. Avoid renaming DTO fields or inventing endpoints. Surface unknowns instead of silently mocking production functionality.

## Every mutation needs an honest lifecycle

`idle → validating → submitting → [confirmed | rejected | network error]`, with cancellation/duplicate-submit and retry semantics. If using optimistic updates, retain previous state, isolate request identity, rollback on conflict/error, and prevent stale responses from overwriting newer decisions. For destructive actions use explicit confirmation or undo policies appropriate to stakes.

Examples to test for a save action: valid payload; client invalid input; 401 expired session; 403 role denied; 409 conflict; 422 field failure; 429 throttling; 500 server error; offline; timeout; duplicate clicks; page refresh; navigation mid-submit; success persistence. Exercise applicable cases; not every system uses every status.

## Data and UI composition

- Distinguish `not loaded`, `loaded empty`, `stale`, `partial`, `errored`, `permission denied`; do not render stale data as definitive success.
- Keep loading skeletons layout-stable, with measured visual geometry. Announce async completion where relevant without spamming live regions.
- Search/autocomplete must handle debounce, cancellation, sequence identity, pagination and no-results. Preserve keyboard semantics in combobox/listbox implementations.
- For realtime and SSE/WebSockets: define sequence/order, dedupe, resume/reconnect/backoff, visibility throttling, stream cleanup, buffering and empty/failed connection states. Verify actual backend protocol; avoid treating every transport as interchangeable.
- For uploads: progress, file type/size checks, resumable support when backend provides it, cancellation, actionable failures and secure content handling.
- For auth: never expose tokens/client secrets; rely on verified server-side authorization. Handle expired session and deep-link flows. Avoid route-only permission logic.

## Contract testing

Match API fixtures to real schemas (OpenAPI/GraphQL/generated types if present). Add at least one happy and failure contract test per critical mutation; use E2E against staging for an agreed smoke path if available. Distinguish unit mocks from real network proof in the final report. Assert persisted data after reload when appropriate.

## Performance of data-intensive pages

Use measured pagination/virtualization for large datasets, avoid unnecessary state churn, throttle high-frequency streams, keep 3D scenes from blocking form responsiveness, and inspect large payload cost. The UI's most important task must remain responsive when background effects are disabled.

## Handoff spec

For every changed flow record the endpoint/event, request and response shape, auth requirement, client ownership of validation, error mapping, user-visible states, retry/rollback strategy, and tests run. Never conceal a pending backend implementation behind a polished demo.
