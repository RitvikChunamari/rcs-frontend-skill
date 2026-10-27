# Mandatory QA: test the actual experience

Use the project's existing tooling first. Never claim results of commands that did not run. Automated accessibility checks are useful but cannot establish full WCAG compliance without manual review.

## Test pyramid and evidence

| Gate | Minimum verification | Tools/examples | Evidence |
|---|---|---|---|
| Static | Install/build/typecheck/lint pass or documented baseline exceptions | Project's package scripts, TypeScript, ESLint | Exact commands + exit codes |
| Functional | Main navigations, forms, filters, auth, back/forward, real API writes/reads | Playwright/Cypress, component tests | Tests and route/state coverage |
| Accessibility | WCAG 2.2 AA target, labels/contrast/keyboard/focus/reduced motion/manual screen-reader smoke | axe-core, @axe-core/playwright, Accessibility Insights, WAVE | Violations + fixed items + manual findings |
| Visual | Desktop/tablet/mobile screenshots, UI states, fonts, image crops, overflow, dark mode | Playwright `toHaveScreenshot`, visual compare | Baseline and reviewed screenshots |
| Motion | No layout jank, memory leaks, stuck pins, ghost listeners, blocked scroll; touch/keyboard/reduced motion | Browser devtools, performance recordings | Tested animations + device |
| Performance | Real LCP/INP/CLS where field metrics exist; lab Lighthouse as diagnostic | Lighthouse, Chrome DevTools, web-vitals | Values, device, network, field vs lab |
| Integration | API payloads, auth, permissions, stale fetch, rollback, error/retry, streams | Devtools network, contract tests, E2E | Status cases covered |
| Security & robustness | No exposed secrets, XSS sinks, route permission assumptions, offline errors, mobile crash | Static review + runtime checks | Severity and resolution |

## Browser matrix and page states

At minimum review:
- Viewports: small mobile 320-390, medium 768, laptop 1280-1440, large desktop; expand for app targets.
- Browsers: Chromium, WebKit, Firefox when test tooling permits; real Safari/Chrome on target devices if available.
- States: first load, after fonts/image loaded, hover, keyboard focus, modal, empty, validation failure, 401/403, API 500, offline/slow network, scrolled midpoint and page end.
- System: reduced motion, coarse pointer/touch, 200% zoom, dark mode if supported, no WebGL or blocked canvas.

## Concrete Playwright test examples (adapt paths and selectors)

```ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('home accessible and navigable', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('main')).toBeVisible();
  await page.keyboard.press('Tab');
  const scan = await new AxeBuilder({ page }).analyze();
  expect(scan.violations).toEqual([]);
});

test('layout has no document overflow at mobile size', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 812 });
  await page.goto('/');
  const overflows = await page.evaluate(() =>
    document.documentElement.scrollWidth > window.innerWidth + 1
  );
  expect(overflows).toBe(false);
});

test('reduced motion keeps content and controls accessible', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto('/');
  await expect(page.locator('main')).toBeVisible();
});
```

`page` and paths should be configured against the actual test server. Treat these as **starting points**; they do not cover keyboard focus-return, screen-reader semantics, route transitions, backend mutation and custom interactions. Use snapshots only in stable screenshot environments: https://playwright.dev/docs/test-snapshots . Accessibility guidance: https://playwright.dev/docs/accessibility-testing .

## Core Web Vitals and performance

Good field targets at p75: LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1. Source: https://web.dev/articles/vitals . These field metrics differ from Lighthouse lab-only approximations. Segment mobile/desktop. Look at JS execution, long tasks, media/font loading, compositing, layout and WebGL GPU cost. Do not report a good Lighthouse score as proof of good field INP.

Typical acceptance criteria (adjust to product constraints): no hydration/console errors; zero critical/serious known new a11y violations; no horizontal overflow; keyboard main flow works; real API responses match UI; interaction never blocks core task; reduced motion removes nonessential movement; no newly introduced major performance regression.

## Visual QA process

1. Save baseline screenshots for important states before editing where possible.
2. Build and serve the actual app; capture matching viewports and scroll positions.
3. Compare against creative brief and user-approved references for hierarchy, optical spacing, typography, colors, media and interactions.
4. Fix one class of issue at a time, re-render and repeat.
5. Capture at least one second-state screenshot (modal, open menu, scrolled chapter, card hover, or error). A hero screenshot alone is insufficient.

## Failure triage priority

P0 broken core function, data loss, auth/security flaw, inaccessible primary task -> block release. P1 broken on target device, severe motion/scroll trap, screen unreadable, major API failure -> fix before ship. P2 visual/interaction inconsistency -> refine. P3 optional flair -> defer. No aesthetic goal overrides P0/P1.

## Honest final report format

`Verified`: exact command, browser, device, success/failure.
`Visual review`: pages, states, viewports inspected.
`Backend`: endpoints exercised + statuses.
`Performance`: lab/field numbers *only if measured*, environment.
`Limitations`: not run, blocked, unavailable tools, remaining risks.

## Visual-style-specific gate

Apply the 12-style acceptance matrix in [style-composition.md](style-composition.md) after the base test pyramid. Check contrast over moving glass/aurora, keyboard semantics for physical knobs and faux windows, pin/scene teardown for immersive scrolling, marquee pause in maximalism, real data labels for cyberpunk, responsive reading order for Swiss and Bento, and actual low-motion/static experiences for every style. Distinctiveness never overrides task success or measurable responsiveness.
