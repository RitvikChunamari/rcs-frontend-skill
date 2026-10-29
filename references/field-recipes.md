# Worked field recipes: executing the skill in actual projects

These are *method examples*, not claims about completed projects or fabricated measurements.

## Recipe A: flagship Swiss-editorial developer portfolio

Input: existing site and content; user wants stronger craft and motion, explicitly no new experience/projects/case studies/images.
1. Inventory current routes, text, images, navigation, data, SEO, critical links.
2. Select a concept such as **technical precision expressed as a modern editorial index**. Preserve content; improve composition rather than inventing impact metrics.
3. Establish type-led twelve-column axes, restrained monochrome palette plus single distinctive accent, large display typography, precise indexes/captions, art-directed project crop and line rules.
4. Choose one signature reveal: project card morphs from index/grid position to immersive feature panel. Avoid taking over native navigation; touch invokes same destination, reduced-motion swaps immediately.
5. Verify project links, keyboard card access, 320/375 mobile heading wrap, scroll restoration and long titles, layout shift during fonts/images, no 3D required.
6. Capture before/after screenshots and review both at the same viewport; log what changed and any weaker areas.

## Recipe B: high-density SaaS dashboard

Input: current application with real API, filtering, data tables, user permissions.
1. Map actual data shapes and roles. Identify where users spend time; do not create imaginary business KPIs.
2. Select clear product utility as primary, with restrained editorial data hierarchy. Use tokenized color roles, accessible tables, contrast and clear visual grouping.
3. Prioritize onboarding/no data, stale/loading, filter keyboard operation, pagination, 403/500 recovery, screen-reader accessible charts/tables.
4. Use micro-motion for feedback and state continuity, not animated aurora backgrounds that obscure data. Preserve backend semantics.
5. Test primary task, expired session, slow 3G/CPU if tools permit, first-load skeleton CLS, 200% zoom and high density on small laptops.

## Recipe C: premium 3D product reveal

Input: licensed product model, user wants interaction-led storytelling.
1. Ask whether user needs to manipulate the model or only observe a cinematic presentation; start with images/video if interactivity adds little.
2. Storyboard scroll chapters: overview → detail → function → purchase/action. Ensure info and CTA remain accessible even without 3D.
3. Optimize glTF assets, texture sizes, lighting, camera path and mobile framing. Use adaptive resolution and a static poster/no-WebGL alternative.
4. Implement responsive GSAP contexts and one source of scroll truth; avoid scroll-jacking, broken anchor navigation and orphaned animation listeners.
5. Validate GPU/CPU behavior, model load failure, reduced-motion, keyboard alternatives, route cleanup and real purchase API if present.

## Recipe D: app redesign with real backend and identity

Input: modernize UI while preserving API and features.
1. Snapshot current endpoints and verify one successful mutation and error response before edits.
2. Refine semantic design system and component states. Document why visual changes preserve old data contracts.
3. Implement visual redesign one component/flow at a time; prevent generic all-purple/glass treatment by choosing a product-specific motif.
4. Run old and new workflows against the same fixture/staging contracts; inspect data persistence after reload; test keyboard and responsive states.
5. Release only with changed routes/files, test evidence, clear known issues and rollback plan.
