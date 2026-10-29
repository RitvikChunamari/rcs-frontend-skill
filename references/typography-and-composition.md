# Typography, grids and optical finish lab

Use for premium editorial sites, typography-first design, dashboard information density, localization, responsive treatment and screenshot polishing.

## Typesetting specification

- Create **five semantic levels** before assigning pixel sizes: display, section heading, body, annotation/metadata, numeric/data. Give each a weight, tracking, line height, measure and role. Make hierarchy visible even without color.
- Choose a family for a *reason*: optical sizes, numeral forms, multilingual coverage, legibility under 14-16px, weight variety, licensing, variable-font payload. Do not use a trendy serif merely because the page says editorial.
- Aim for body line lengths around 45-75 characters for uninterrupted prose, adjusted for script, font and display width. Test actual copy, CJK, accented names, and 200%-400% zoom.
- Prefer natural wrapping with `text-wrap: balance` for short headings only where supported; avoid brittle manual `<br>`-style breaks. Use intentional `max-width` in `ch` or `rem` when it helps.
- Watch **rivers, widows, awkward rag**, punctuation hanging, numerals misaligned, letterspacing of uppercase metadata, and long URL/button overflow. Optically align round letters and asymmetric logos.
- Scale type by *container and content*, not a magical global size multiplier. Use `clamp()` with conservative min/max; inspect actual breakpoints.

## Grid engineering

- Start with content-first columns (often 4/8/12, not mandatory); define margin and gutter bands. Provide baseline rhythm for type and media rather than forcing every item into a rigid box.
- Use `grid-template-columns: repeat(12, minmax(0, 1fr))` only when the design truly benefits. CSS subgrid can align nested content; verify supported targets. For reusable cards, use container queries rather than viewport-only breakpoints.
- For Swiss composition: asymmetry still follows a repeatable grid. Place display type, captions and imagery on shared axes; test optical balance by squinting at the screenshot.
- Editorial image stories require deliberate **crop and caption semantics**. Preserve meaningful focal points, avoid cropping faces/text, and give captions a typographic role.
- Break the grid *once with intention* to create an editorial moment; keep task forms, settings and dense data predictable.

## Example fluid type (adapt per brand)

```css
:root {
  --font-display: 'Display Sans', system-ui, sans-serif;
  --font-body: 'Body Sans', system-ui, sans-serif;
  --type-body: clamp(1rem, 0.98rem + 0.15vw, 1.125rem);
  --type-display: clamp(3.2rem, 2.1rem + 5.3vw, 7.5rem);
}
.prose { max-inline-size: 68ch; line-height: 1.62; }
.display { font: 650 var(--type-display)/0.99 var(--font-display); letter-spacing: -0.045em; text-wrap: balance; }
@media (max-width: 38rem) { .display { letter-spacing: -0.025em; } }
```

This is a starting pattern, not a universal preferred font, ratio or pixel setting.

## Optical QA

At 320/375/768/1024/1440 and content extremes examine: headline rag, paragraph density, font loading shifts, captions, table numerals, baseline line-up, uneven button padding, card aspect ratios and art-directed crops. Test at 200% zoom. Compare mobile and desktop as separately composed surfaces. `font-display`, preload and fallback metric alignment should be evaluated with real Lighthouse/DevTools observations.

Reference: MDN container queries https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries
