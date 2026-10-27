# Curated resource registry (verify APIs, plans and licenses at use time)

This is a **discovery map**, not a mandate to install every tool. URLs and service tiers can change. Preference: existing project stack and free/open-source resources first; check licenses on fonts, code, components, scenes and assets.

## Design systems and product research

- Apple HIG: https://developer.apple.com/design/human-interface-guidelines/
- Google Material: https://m3.material.io/
- IBM Carbon: https://carbondesignsystem.com/ ; Carbon MCP may require an IBMid/OAuth: https://www.carbondesignsystem.com/getting-started/carbon-mcp/onboarding-and-setup
- Microsoft Fluent 2: https://fluent2.microsoft.design/
- Adobe Spectrum: https://spectrum.adobe.com/
- Atlassian: https://atlassian.design/
- GitHub Primer: https://primer.style/
- Shopify Polaris: https://shopify.dev/docs/api/polaris
- Other system examples: https://www.lightningdesignsystem.com/ , https://ant.design/ , https://baseweb.design/ , https://designsystem.digital.gov/
- Awwwards: https://www.awwwards.com/websites/ ; Mobbin: https://mobbin.com/ ; Page Flows: https://pageflows.com/ ; Codrops: https://tympanus.net/codrops/ ; Figma design systems: https://www.designsystems.com/

## Visual-style and trend references

- Twelve-style implementation guide: `style-atlas.md`; selection and validation: `style-composition.md`.
- Tilda taxonomy and examples: https://tilda.education/en/web-design-styles (Swiss, editorial, minimal, brutalist, retro and bento).
- Figma web trend overview: https://www.figma.com/resource-library/web-design-trends/ (immersive 3D, motion, bold type, maximalism, retrofuturism, neo-brutalism, neumorphism).
- Refero style taxonomy: https://styles.refero.design/ ; examples may be curated or access-limited.
- Treat 'Cute-alism' and 'Dial-Up Delight' as informal creative labels; avoid claiming official standards or market rank.

## Core frontend

- React / Next, Vue / Nuxt, Svelte / SvelteKit: choose based on the existing app, not trends.
- CSS: MDN https://developer.mozilla.org/en-US/docs/Web/CSS ; use Grid, container queries, clamp, transitions, masks and View Transitions where supported.
- Accessibility primitives: https://www.radix-ui.com/primitives , https://react-spectrum.adobe.com/react-aria/ , https://ariakit.org/ , https://headlessui.com/ .
- Component starters (customize; check terms): https://ui.shadcn.com/ , https://www.aceternity.com/ , https://magicui.design/ , https://www.reactbits.dev/ , https://www.motion-primitives.com/ , https://www.threeui.com/ . Some catalogs mix free and paid components or carry per-component dependencies; verify individually.
- Iconography: https://lucide.dev/ , https://iconify.design/ ; verify icon sets' individual licenses.
- Typography: https://fonts.google.com/ , https://fontsource.org/ ; verify commercial licenses and avoid loading entire variable font inventories.

## Motion and interaction

- GSAP / ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ ; check current GSAP licensing if distributing/commercially using plugins.
- Lenis: https://github.com/darkroomengineering/lenis ; smooth scrolling only when it improves the product.
- Motion: https://motion.dev/docs/react ; animation/layout on React, and JS animation tools.
- Theatre.js: https://www.theatrejs.com/ ; timeline/creative scene authoring, verify maintenance and licensing.
- Rive: https://rive.app/ ; interactive motion authoring, plan/runtime terms can vary.
- Lottie/dotlottie: https://dotlottie.io/ ; use appropriately licensed animation assets.

## 3D, shaders, graphics

- Three.js: https://threejs.org/ ; React Three Fiber: https://r3f.docs.pmnd.rs/ ; Drei: https://drei.docs.pmnd.rs/
- Blender: https://www.blender.org/ ; glTF standard: https://www.khronos.org/gltf/
- Spline: https://spline.design/ ; shader studies: https://www.shadertoy.com/ ; WebGL fundamentals: https://webglfundamentals.org/ ; 3D web tutorials: https://tympanus.net/codrops/
- GSAP/CSS/SVG and Canvas2D often outperform heavy 3D for a flat creative effect; prototype the cheapest representation first.

## Testing / performance / design ops

- Playwright: https://playwright.dev/ ; Axe: https://www.deque.com/axe/ ; Lighthouse: https://developer.chrome.com/docs/lighthouse/ ; Core Web Vitals: https://web.dev/articles/vitals
- Accessibility standard: https://www.w3.org/TR/WCAG22/ ; Accessibility Insights: https://accessibilityinsights.io/
- Storybook: https://storybook.js.org/ ; Chromatic: https://www.chromatic.com/ (paid tier possible); open-source visual regression through Playwright screenshots preferred when budget constrained.
- Figma: https://www.figma.com/ ; official MCP/docs: https://developers.figma.com/ ; not universally free/accessible.

## MCP / integration guidance

Do not assume a connector is installed or grant it capabilities it does not have. Where authorized, use:
- Figma MCP for actual design frames/variables and implementation context.
- Mobbin MCP for real flows if the user's plan includes access; official page says MCP is Pro/Team: https://mobbin.com/mcp
- Browser automation/Chrome DevTools MCP for navigation, screenshots, live CSS/network/performance evidence.
- Context7 or official developer documentation for precise version-specific library APIs.
- shadcn/other component MCP only when the selected component truly fits design intent and license.
- Git tools/local files for code and test runs. Never require a user to publish a local repository before working.

## Selection rubric

For each proposed third-party tool ask: (1) existing equivalent? (2) extra JS/GPU cost? (3) keyboard/reduced-motion support? (4) stable version/docs? (5) license and free-plan restrictions? (6) removal/cleanup complexity? (7) visual fit with art direction? Install only when benefit exceeds long-term cost.
