# Repository guidance

Keep this portable agent skill free to use and independent of paid services. Preserve the `SKILL.md` entrypoint, validate local links, and run the repository checks before committing changes.

## Validation

Run:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 -m compileall -q scripts
```

Do not claim browser, accessibility, performance, or visual validation unless it actually ran against a rendered target project.
