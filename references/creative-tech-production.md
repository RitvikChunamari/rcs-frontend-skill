# Creative technology: motion, 3D, shaders and media production

Use when the user requests immersive 3D, scroll narratives, rich product visualizations, shader backgrounds, animated typography or ambitious motion. First prove that the treatment supports product meaning; then stage its production pipeline.

## Representation ladder: use the lowest-cost effective medium

1. HTML/CSS and SVG for typography, masks, gradients, icon motion and most interface transitions.
2. Canvas 2D for complex particle/paint systems where DOM element counts become expensive.
3. WebGL/WebGPU via Three.js/R3F for actual 3D perspective, materials, interactions or many draw operations. Browser/GPU coverage and fallback must be validated; WebGPU is optional, never assumed.
4. Prerendered image/sequence/video for cinematic effects that do not need interaction. Provide an accessible poster and avoid autoplay with sound.

Avoid using 3D for a visual that can be rendered faithfully with a tiny SVG/CSS treatment. No background effect may obscure buttons or intercept keyboard/pointer events.

## 3D scene production checklist

- Define hero subject and interaction before modeling. Decide camera framing, focal distance, physically plausible light logic, environment, surface/roughness, tone mapping and postprocessing *as one scene*.
- Create asset provenance: authored in Blender, licensed downloaded asset, or user-provided. Export glTF/GLB; optimize mesh/poly count, textures, material count and load order. Compress where supported (check build tooling), test texture quality in actual target devices.
- Budget *observed* frame time and resource usage. Example **planning starting points**, not standards: flagship hero desktop <=2-3MB compressed asset if feasible; mobile target lower; 60fps aspirational on target devices, 30fps minimum fallback threshold for nonessential graphics. Measure with browser performance tools rather than trusting asset sizes.
- For R3F: reuse materials/geometries, use instancing/LOD where appropriate, cap pixel ratio, render on demand when static, avoid unnecessary per-frame React state writes and heavy postprocessing. Dispose unmanaged resources and stop loops on unmount.
- Define **high, medium, low, no-WebGL** paths. On mobile/low power, choose fewer effects, smaller textures or a still illustration. Respect reduced motion (static camera, no auto-rotation) without losing labels/controls.
- 3D interaction must have 2D navigation/accessibility equivalent for essential operations; provide meaningful labels and visible controls outside canvas.

## Motion budget and choreography

Define moments by semantic group:
- `micro`: action acknowledgment; snappy, generally ~100-220ms (tune to device and brand).
- `spatial`: panels/shared elements; generally ~200-500ms, reversibility and interruption required.
- `story`: progress-driven scenes; duration tied to scrolling or deliberate actions, never force a timed wait before content.

These are design heuristics, not a compliance standard. Establish one curve family per motion voice; avoid combining spring, linear, elastic and overshoot arbitrarily. Animate opacity/transform where possible, watch compositing memory and avoid accidental `will-change` everywhere. For GSAP, scope contexts to components, kill timelines/triggers on teardown; use `gsap.matchMedia()` for responsive and reduced-motion branches. Lenis should never degrade native controls, anchor links or reduced-motion preference.

## Cinematic storyboard format

For each beat record: **trigger → subject → camera/element movement → semantic purpose → focus behavior → mobile alternative → reduced-motion static outcome → teardown**. E.g. `Project card opens → image scales within shared frame → maintain project identity → focus moves to project heading → on mobile use direct route + modest fade → reduced-motion immediate navigation`.

## Failure modes to reject

Blank loader while downloading enormous scene, excessive blur and chromatic aberration, GPU memory growth on route visits, web fonts required before content appears, smooth scroll trapping nested panels, motion sickness, scroll-controlled text that screen readers cannot encounter, idle animation competing with data entry.

Official docs: https://r3f.docs.pmnd.rs/advanced/scaling-performance ; https://gsap.com/docs/v3/Plugins/ScrollTrigger/ ; https://developer.apple.com/design/human-interface-guidelines/motion
