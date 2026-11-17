# Direction and workflow scenario checks

Use these prompts to evaluate an agent after loading the skill. Run each in a fresh project/context with the stated fixtures, capture its decision and actual output, and judge the required behavior. These are evaluation specifications, not recorded benchmark successes. Different valid visual choices can satisfy a case.

| Prompt / fixture | Expected behavior | Failure signal |
|---|---|---|
| “Build a library room-booking form for patrons on phones.” No style given. | Infer a clear form-oriented direction from the task, disclose assumptions, define validation and recovery tests. | Random trend choice, invented library claims, aesthetic questions blocking obvious progress. |
| “Add a filter to this inventory screen.” Existing tokens and components supplied. | Preserve the current system, test filtering/empty results, critique the integrated control. | Replaces the whole interface because no style was named. |
| “Use cyberpunk for this monitoring dashboard.” | Honor the direction with readable task controls and meaningful status semantics. | Silently replaces the requested look with minimalism or invents live telemetry. |
| “Swiss + editorial for a photographer's portfolio.” Licensed images supplied. | Assign grid/hierarchy and image/narrative roles, reconcile tokens and review mobile crops. | Alternates two unrelated theme kits or asks the user to choose one. |
| “Retro, tactile and kinetic for an exhibition.” | Assign bounded roles for all explicitly requested influences, keep access to content and low-motion alternatives. | Drops a requested influence without explanation or stacks effects without roles. |
| “Build a site.” Empty project. | Ask for the intended product/task, while inspecting available context. | Invents a business, audience and testimonials. |
| “Refine heading spacing.” Existing page. | Inspect computed fonts and real wraps, change spacing, verify mobile/zoom. | Adds a testing dependency solely to assert a CSS string or restyles unrelated sections. |
| “Fix negative quantities being accepted at checkout.” | Reproduce with a failing test, implement, pass/refactor, exercise the actual form and error path. | Tests only the happy path or claims red–green without running the failing test. |
| “Critique this page.” Source available, browser unavailable. | Provide bounded source findings, label visual review unverified, keep the request read-only. | Claims screenshot or contrast measurements without rendering. |
| “Create a static documentation page.” | Choose a reading-oriented system, verify navigation/reflow and explain backend testing is inapplicable. | Reports an unrun backend check as passed or creates unnecessary APIs. |

For each run record model/version, skill commit, prompt, fixtures, chosen mode, reasons, actual commands, screenshots, findings and remaining limitations. Compare choices against the brief, not exact style names. Controlled before/after studies should follow [comparison protocol](../../references/comparison-protocol.md).
