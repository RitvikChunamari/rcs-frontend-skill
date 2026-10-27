# Production frontend engineering

## Repo-first rule

1. Inspect `package.json`, lockfile, scripts, tsconfig, router, layouts, CSS/toolchain, test setup, .env.example (never disclose actual secrets), services, hooks, API clients and existing component conventions.
2. Run repository's own verification commands to establish baseline; record pre-existing failures separately.
3. Prefer extending existing tokens/components. Avoid broad rewrites, framework migrations, new state libraries or dependencies unless justified by measurable value.
4. Inspect source data ownership and route boundaries. No architecture refactor that accidentally changes server/client rendering, cache semantics or SEO.

## System architecture

- Separate primitives, composites, features, views, app shell and data adapters where the existing codebase supports it. Keep style primitives themable and typed.
- Use CSS custom properties/tokens as an implementation source of truth; adopt project token tooling if present. Semantic tokens, never magic hard-coded color copies per component.
- Use fluid type/layout carefully (`clamp`, container queries, Grid/Flex) with testable minimums. Keep scrolling native when practical. Prevent horizontal overflow at small widths.
- Prefer semantic native controls. For complex widgets, adopt established accessible primitives if available (Radix, React Aria, Ariakit, Headless UI etc.) and style them cohesively.
- Ensure React effects and animation libraries clean up on route unmount, dependency changes and breakpoint changes. No ghost listeners/tweens or leaked requestAnimationFrame loops.
- Use types/validators at trust boundaries. Component props should express valid variants and states; avoid untyped `any` and implicit stringly typed workflows.
- Keep client bundles small: code-split scene editors, heavy motion, charts and 3D; lazy-load below-the-fold content but protect LCP. Optimize fonts (preload only critical), imagery, media sizes and responsive sources.
- Keep routing/caching/prefetch honest; never render a rich visual as a blocking barrier to interactivity. Error boundaries around unstable scenes and data regions.

## Framework-specific guidance

- React/Next: respect server vs client boundaries; isolate interactive components, choose streaming carefully, avoid hydration mismatch, use stable keys, avoid expensive context-wide rerenders.
- Vue/Nuxt: use composables, transitions and SSR lifecycle properly; clean up client-only effects and DOM listeners.
- Svelte/SvelteKit: prefer native reactivity and action/lifecycle practices; respect server load/action boundaries.
- Plain HTML/CSS/JS: build progressively enhanced semantic HTML first, then attach effects with cleanup; don't import a full framework for one card reveal.
- Native app design tasks: adapt Apple's/Material platform conventions and native technologies, don't force web implementation practices blindly.

## Component completion definition

For every interactive component: normal/hover/pressed/focus/disabled/loading/empty/error/success, touch and keyboard access, screen-reader name, contrast, responsive layout, and state with actual backend data. Document only relevant variants, not hypothetical ones.

## Prefer compatible stacks

| Need | Start with | Escalate when |
|---|---|---|
| Simple hover/reveal | CSS transforms, opacity, `prefers-reduced-motion` | Choreography needs a timeline or responsive orchestration |
| Small React layout transitions | Motion (`motion.dev`) or existing library | Complex scroll-linked choreography |
| Scroll narratives | GSAP ScrollTrigger | Add Lenis only for genuinely improved synchronized smooth-scrolling |
| Page transitions | Native View Transitions if supported; router patterns | Complex interruptible shared-element sequences |
| Decorative vector scene | SVG/CSS/Canvas2D | Real depth/shading/projection requires WebGL |
| Spatial interaction | Three.js / React Three Fiber | Check fallback/perf first; avoid WebGL for a basic icon |

## Engineering hygiene

Keep no broken links or CTA dead ends. Honor existing lint/formatter conventions. Protect user data, avoid analytics without consent, do not expose secrets in client bundles. Prefer safe DOM APIs over raw HTML injection. Ensure all runtime dependencies are declared/pinned through lockfile, and verify license and maintenance.
