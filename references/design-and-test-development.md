# Design-driven and test-driven development

Use design-driven development to establish the experience and test-driven development to protect behavior. Apply both in proportion to the change. These are agent workflows using the project's available tools, not services provided by the skill.

## Design before implementation

Before a substantial interface change, record a small design contract in the existing project brief.

- User task, success condition and factual content.
- Selected direction, explicit constraints and which screen areas it affects.
- Content order, type roles, spacing, semantic colors and responsive behavior.
- States and transitions, including loading, empty, error, success, focus, interruption and recovery where applicable.
- Acceptance evidence for each important decision.

Render a representative slice early using the real framework and realistic content. Choose the hardest useful slice, such as the comparison control plus its keyboard state, rather than always making a marketing hero. Inspect the slice before repeating it across the product. Update the contract when an observed problem changes a decision.

Define falsifiable criteria. “Elegant” alone cannot fail a test. “The heading does not collide with its neighbor at 320px; one primary action is visually dominant; a failed save retains entered data” can guide visual review and behavioral assertions. Record type character and composition as visual judgments, separately from machine-checkable behavior.

## Select the right test level

| Change or risk | Useful evidence |
|---|---|
| Parsing, validation, sorting, calculations, state transitions | Unit tests with boundary and invalid inputs |
| A dialog, form, tabs, filters or async feedback | Component tests through accessible roles and user events |
| Navigation, network mutation, auth and recovery | Integration or end-to-end tests against the configured target |
| Typography, spacing, images and responsive composition | Rendered critique, overflow checks and reviewed screenshot comparisons |
| Animation or gestures | State/lifecycle tests plus real pointer, keyboard and reduced-motion checks |

Use the existing runner and conventions. Reversible copy and CSS adjustments do not require invented unit tests. If a required runner is absent, use a suitable existing native runner or add a small free dependency only after checking relevance and project rules. If execution is impossible, leave the test status unrun.

## Red → green → refactor

For new behavior and bug fixes with testable logic:

1. Express one observable requirement as an executable test. For a bug, reproduce the reported failure.
2. Run it against the current code. Confirm that the failure describes the missing behavior, rather than a syntax error, missing dependency or broken test environment. If it already passes, inspect the requirement and setup before changing code.
3. Implement the smallest correction that makes the test pass through the normal entry point.
4. Improve structure without changing behavior. Re-run the focused tests and the relevant existing suite.
5. Check the rendered user path when the behavior is visible. A passing unit test alone cannot establish that an accessible control invokes the code correctly.

Record the failing command/result, passing command/result and any refactor. Do not describe tests written after implementation as test-first work. For an existing module, add characterization coverage only for behavior the change risks.

Useful unit cases include empty input, boundary values, duplicates, cancellation, and stale async responses. Use deterministic clocks and controlled network boundaries where appropriate. Keep assertions about outputs and user-visible state. Avoid assertions on private methods, incidental class names, arbitrary timeouts, or snapshots that merely freeze the current implementation.

## Example acceptance contract

For a comparison slider:

- At 0%, the original fills the frame. At 100%, the revised version fills it.
- Arrow keys change the percentage and accessible value together.
- Preset buttons and dragging produce the same visible endpoint.
- Layout changes preserve both images' shared coordinate system.
- Reduced motion keeps direct control.
- The visual review checks the actual clipping direction.

Unit tests can check percentage calculation when custom logic exists. A browser test must establish which image is visible. Hardcoding the wrong implementation into a matching test is not evidence.

For a save form, test validation locally, retry and stale responses at the integration boundary, and an actual save through the authorized backend before claiming the whole flow works. A mock is evidence only for the layer it controls.

## Visual regression discipline

Capture intentional baselines after visual review of the agreed direction. Keep browser, fonts, content, viewport and animation state stable. Investigate diffs before updating a baseline. Never accept a new screenshot merely to make CI pass. Geometry or screenshot checks complement inspection of hierarchy, usefulness and originality.

## Release evidence

Declare applicable extra gates before implementation, for example `design_contract`, `unit_tests`, `component_tests` and `critique`. Supply these in the evidence JSON's `required_gates` array. The checker also evaluates every gate supplied under `gates`.

Use `not_applicable` with a concrete `reason` when a check genuinely does not apply, such as backend testing for a static document. Missing tools, time, or a failed check are `not_run` or `fail`, never an exemption. The checker validates declared completeness; a reviewer still verifies logs, screenshots and applicability.

Free primary references: [Testing Library principles](https://testing-library.com/docs/guiding-principles/), [Python unittest](https://docs.python.org/3/library/unittest.html), [Playwright visual comparisons](https://playwright.dev/docs/test-snapshots).
