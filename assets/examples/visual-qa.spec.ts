/**
 * EXAMPLE Playwright smoke suite, NOT a test that ran in this skill repository.
 * Copy into a target app with @playwright/test configured, set BASE_URL,
 * replace '/' and test ids with real screens, then approve snapshots.
 */
import { test, expect } from '@playwright/test';

const baseURL = process.env.BASE_URL || 'http://127.0.0.1:3000';

for (const viewport of [
  { width: 375, height: 812 },
  { width: 768, height: 1024 },
  { width: 1440, height: 900 },
]) {
  test(`homepage viewport ${viewport.width}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    await page.goto(`${baseURL}/`, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await expect(page.locator('body')).toBeVisible();
    // Compare in a stable CI environment. Review baselines manually.
    await expect(page).toHaveScreenshot(`home-${viewport.width}.png`, {
      animations: 'disabled',
      fullPage: true,
    });
    const overflows = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
    expect(overflows, 'unexpected horizontal overflow').toBe(false);
  });
}

test('reduced motion leaves content usable', async ({ page }) => {
  await page.emulateMedia({ reducedMotion: 'reduce' });
  await page.goto(`${baseURL}/`);
  await expect(page.locator('main')).toBeVisible();
  // Add real project-specific assertions for navigation and critical actions.
});
