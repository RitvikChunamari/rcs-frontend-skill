# Backend alignment and resilient product flows

The frontend must reflect backend reality. UI/backend integration is part of experience design, not a final wiring pass.

## Before editing any API-driven UI

1. Trace route -> screen -> state/hook -> network client -> actual endpoint -> schema -> auth/session. Find existing OpenAPI/GraphQL/protobuf/Zod/TypeScript schemas and error types.
2. Enumerate entities/permissions/relationships/derived values. Define read/write contract: HTTP method, path, headers, request/response, pagination/cursors, filtering/sorting, authentication/CSRF, caching, idempotency and retry semantics.
3. Map UI states: initial, loading, partial, empty, optimistic/pending, success, validation error, 401/403, 404, 409/422, 429, 5xx, offline and timeout. If backend contract is unknown, identify the gap instead of guessing.
4. Confirm the backend is running and reachable in authorized test environments. Distinguish a network error from a design bug.

## Implement correctly

- Centralize fetch/client and typed parsing, not duplicated endpoint strings in components. Validate server responses where risk demands; TypeScript alone cannot validate network JSON at runtime.
- Never pretend a network mutation succeeded before receiving confirmation. Optimistic UI is allowed with a specified rollback/reconciliation path; disable or deduplicate submissions appropriately.
- Debounce typeahead at appropriate boundaries; cancel stale requests or use request keys; handle race conditions for search/filter/sort; avoid out-of-order presentation.
- Protect session, CSRF, CORS boundaries, XSS sinks, secrets and privileged actions. Permission-based UX never substitutes for server authorization.
- For files and media: handle upload progress, size/type validation, resumability if backend supports, preview/accessibility, error cancellation and storage rules.
- For real-time/AI responses: preserve stream ordering, abort, reconnect, partial/error state, moderation/permission handling where required; do not animate streamed text so aggressively that it becomes unreadable.
- Respect source-of-truth values and formatting (dates/timezones, units, currency, pagination totals). Do not invent success metrics or demo content for production routes.
- Support rollback/recovery, retry with backoff for safe idempotent requests, and clear explanation of recoverable vs terminal failure.
- Preserve existing API shape unless endpoint migrations are explicitly authorized and coordinated.

## Contract review template

| UI action | Backend contract | Success UI | Failure/recovery | Test |
|---|---|---|---|---|
| Save profile | `PATCH /profile` with validated payload | Updated canonical values + confirmation | Field-level errors; no silent loss | Successful and 422 response |
| Search projects | `GET /projects?q=&cursor=` | Results, count, continued pagination | Cancel stale query; offline retry | Rapid query changes, empty, 500 |
| Authenticated action | Existing auth cookie/session | Navigate to intended state | 401 re-auth; 403 permission message | Expired session, denied role |

The paths above are **illustrative only**. Do not create them unless the real backend has them.

## Verification requirements

- Prefer a real development/staging backend or an explicitly approved local fixture. If mocks are used in unit/integration tests, say so clearly.
- Exercise one success and at least one error for every critical mutation; verify backend data persists after refresh/relogin where applicable.
- Assert payloads, headers and validation; check console and network for regressions. Do not regard a screenshot or visual QA as API integration proof.
