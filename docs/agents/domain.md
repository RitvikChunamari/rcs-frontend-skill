# Domain Docs

How engineering agents should consume this repository's domain documentation before exploring or changing it.

## Before exploring, read these

- `GLOSSARY.md` at the repository root when it exists.
- Relevant architecture decision records under `docs/adr/` when they exist.

If these files do not exist, proceed silently. Domain-modeling workflows create them lazily when terms or decisions are actually resolved.

## Layout

This is a single-context repository:

```text
/
├── GLOSSARY.md
└── docs/
    └── adr/
```

## Use the glossary's vocabulary

When an issue, proposal, hypothesis, or test names a domain concept, use the term defined in `GLOSSARY.md`. Avoid synonyms the glossary explicitly rejects.

If a necessary concept is absent, reconsider whether the term belongs to the project or note the gap for a domain-modeling workflow.

## Flag ADR conflicts

If proposed work contradicts an existing ADR, surface the conflict explicitly instead of silently overriding the decision.
