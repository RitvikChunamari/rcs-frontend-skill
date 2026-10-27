# Contributing to RC's Frontend Skill

Thanks for helping improve a freely usable, portable frontend skill.

## Scope

We welcome corrections, official design-system links, original design patterns, style recipes, browser/performance/a11y tests, more precise API-integration guidance, and agent installation notes tested against a real version. Small, well-evidenced changes are preferable to an enormous unverified resource list.

## Before opening a pull request

1. Check existing issues and open a focused issue for substantial changes.
2. Keep the top-level `SKILL.md` actionable and concise; put deeper information in a relevant `references/*.md` file.
3. Include specific constraints, when-to-use / when-not-to-use advice, implementation pitfalls, fallbacks, and evidence when adding a design technique.
4. Don't add material copied from a proprietary design system, website source, paywalled screenshot collection, third-party assets or brand artwork without adequate permission. Summarize principles and link to sources.
5. Never submit secrets, user data, API tokens, access credentials, or unlicensed files.
6. Test locally:

   ```bash
   python -m unittest discover -s scripts -p 'test_*.py' -v
   python scripts/validate_skill.py
   ```

7. Describe the change and tests in your pull request. Claim only checks you actually ran.

## Contribution guidelines

- Prefer accessible, performant, maintainable solutions to maximal effects.
- Include reduced-motion, touch/mobile, low-performance and keyboard considerations for relevant motion/3D proposals.
- Do not misrepresent unofficial creative terms as established standards.
- Avoid endorsements or affiliation claims with referenced commercial products.
- Preserve existing functionality and follow the project's general safety and originality rules.

Contributions are offered under the repository's MIT license.
