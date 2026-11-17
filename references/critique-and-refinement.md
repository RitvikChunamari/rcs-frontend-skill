# Critique the experience, then verify the repair

Use for a requested critique and as the review pass during substantial implementation. A critique request produces findings unless edits are also requested. In a build or refinement task, fix observed in-scope defects and recheck them.

## Review the rendered artifact

Start with the brief, the target route/state and real screenshots, before reading the builder's self-assessment. In a single-agent run, make this a separate review pass. If an independent reviewer is authorized and available, give it the brief and artifact. Never label same-context self-review independent, and do not require paid reviewers or extra agents.

Inspect the main task at the intended sizes, then a second meaningful state such as a validation error, expanded navigation or long-content view. Identify the most consequential issues first.

- **Fit.** Does the selected direction help this audience do this task? Is the product distinguishable through real content and specific design decisions?
- **Hierarchy.** Can a visitor understand the offer or current state and find the next action? Count competing emphasis, not just buttons.
- **Typography.** Confirm actual font loading, natural spacing, readable measures, line breaks, multilingual fallbacks and zoom. Avoid compressing letters to force a headline to fit.
- **Composition.** Check shared alignment axes, information density, section rhythm, mobile order and intentional use of available imagery. An empty asset slot is not a finished composition.
- **Behavior.** Verify affordance, selection, loading, error, success, undo and focus. Decorative arrows must not make static rows look clickable.
- **Motion.** Check immediate feedback, interruption, reversal, cancellation and reduced-motion equivalents. Slow motion inspection can expose jumps that a static screenshot misses.
- **Access and delivery.** Check contrast on the rendered background, keyboard paths, touch alternatives, overflow, content loading and relevant performance measurements.

Preserve choices the user explicitly requested. A stylistic preference is not a defect unless its practical impact can be explained. Automated detectors supply leads; verify each against the actual artifact. Neither a clean scan nor a numerical design score proves visual quality.

## Findings that can be acted on

Use the following record for material findings, with at most five priorities per pass.

| Field | Required detail |
|---|---|
| Location and state | Route, component, viewport, theme and input state |
| Observation | What was actually seen or reproduced |
| Expected result | The user goal or design contract it fails |
| Impact and priority | Blocked task, confusing interaction, weak hierarchy or optional polish |
| Repair | A bounded change tied to the cause |
| Verification | Screenshot or interaction that will confirm the correction |

For example, a desktop headline's negative tracking causes two letters to touch. Record the font and computed tracking, relax the spacing or size within the grid, then inspect the same heading at desktop, mobile and zoom. Replacing the entire identity is unnecessary when spacing is the cause.

## Close the loop

Fix task blockers before polish. Apply a coherent batch of repairs, then capture the same states and viewports. Mark each finding resolved, partially resolved, deferred or unverified. Preserve a before/after reference when practical. If no defect is found, say so.

Use one review and one confirming pass for ordinary work. Escalate to another focused pass when a failed check or newly observed defect justifies it. If progress stalls, state the unresolved condition and next diagnostic step; do not loop endlessly or invent a clean verdict. Changes outside the requested scope require their normal authorization.

Finish with what changed, what ran, what was inspected and what remains uncertain. The user should see the actual result and any blocker, not an inflated self-rating.
