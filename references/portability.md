# Install / portability across coding agents

A single ZIP or folder **does not install globally into every agent automatically**. Distribution is portable; loading rules vary by platform and version. Use the agent's official skill importer/skill directory if it supports `SKILL.md`. Keep references and scripts next to the entrypoint; do not paste all files into system prompts.

## Recommended structure

```text
rcs-frontend/
  SKILL.md
  references/*.md
  scripts/inspect_project.py
  assets/AGENTS.md
  agents/openai.yaml
```

## Use with agent types

- **Agents with Skills support:** install/import this entire folder per agent's current official UI or documented skill path. Select personal/global scope if supported; otherwise add it to workspace scope. Confirm the tool really loads `SKILL.md` and linked references.
- **Agents reading `AGENTS.md`:** use the small `assets/AGENTS.md` adapter in the repository root or an officially supported global instruction file. Update its `path/to/rcs-frontend` pointer to where the directory actually lives. Its instructions tell the agent to load `SKILL.md` and referenced files on demand.
- **Agents using a rules UI:** paste the adapter text, change paths and configure the tool to read the skill. Do not assume a nonexistent "+ Global" button or identical UI across products.
- **Agents lacking file read/browser:** paste the core `SKILL.md` text into their custom instructions if allowed; they will not automatically have access to reference documents, live sites, tooling or tests. Do not claim full functionality.

## Shared knowledge without duplicated models

A project-level `AGENTS.md` or equivalent rules file and one shared skill folder can make different coding agents use consistent quality standards. This **does not** synchronize their chat memory, model usage limits, authenticated connectors, installed browser tools or hidden state. To maintain continuity, write design decisions to project files and keep changes in version control/local backups.

## Useful optional agent integration

- Browser/DevTools MCP for live-page evidence.
- Figma MCP for real design tokens and layout.
- Mobbin MCP only with appropriate plan access.
- Playwright and axe accessibility tools installed in the project/test environment.
- Documentation search for version-specific APIs.

Agent availability and feature names change; verify current documentation. Always test install with a simple request: "Audit the home page, show the selected creative thesis, trace its main API action, and list the mandatory QA gates from RC's Frontend Skill." The agent should load the skill without inventing access to unavailable tools.

## Premium edition note

The full skill has optional deep references and templates. Do **not** paste all references into a model's global prompt; load them per task. Example if a coding agent supports skills CLI: `npx skills add OWNER/rcs-frontend-skill -g` once the owner has published it. This is only a possible installer, not proof a particular app supports it. Verify with the target agent's documentation. Core skill ID remains `rcs-frontend` (lowercase, hyphenated); visible brand remains **RC's Frontend Skill**.
