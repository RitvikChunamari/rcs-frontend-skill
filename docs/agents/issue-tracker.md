# Issue tracker: GitHub

Issues and specs for this repository live as GitHub issues. Use the `gh` CLI for operations.

## Conventions

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --json number,title,body,labels,comments`
- List: `gh issue list --state open --json number,title,body,labels,comments`
- Comment: `gh issue comment <number> --body "..."`
- Label: `gh issue edit <number> --add-label "..."` or `--remove-label "..."`
- Close: `gh issue close <number> --comment "..."`

Infer the repository from `git remote -v`; `gh` does this automatically inside a clone.

## Pull requests as a triage surface

**PRs as a request surface: no.**

GitHub shares one number space across issues and pull requests. Resolve an ambiguous number with `gh pr view <number>` and fall back to `gh issue view <number>`.

## Skill terminology

- When a skill says **publish to the issue tracker**, create a GitHub issue.
- When a skill says **fetch the relevant ticket**, read the corresponding GitHub issue.

## Wayfinding operations

When a wayfinding workflow is used, represent its map as a GitHub issue and its tickets as child issues where GitHub sub-issues are available. Otherwise, link children from a task list and include `Part of #<map>` in each child.

Use native GitHub issue dependencies when available. Where dependencies are unavailable, put `Blocked by: #<number>` at the top of the blocked issue. A ticket becomes ready only after every blocker is closed and the ticket is unassigned.
