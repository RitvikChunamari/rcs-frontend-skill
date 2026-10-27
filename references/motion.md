# Motion direction and implementation

## First design the choreography

Every motion moment should have: purpose, trigger, target/state, duration/easing, interruption, focus/touch behavior, reversed/exit state and reduced-motion alternative. Describe a timeline at a high level before coding it. The page should remain usable if animation fails to initialize.

| Motion role | Recommended approach | Guardrail |
|---|---|---|
| Hover/press feedback | CSS transitions or existing primitive | Keep immediate, intuitive, no hover-only information |
| Stateful layout swap | Motion layout/shared elements | Focus continuity; no stale layout measurements |
| Scroll-triggered reveal | IntersectionObserver/CSS or GSAP ScrollTrigger | Don't reveal everything; preserve text visibility |
| Scroll-scrub story/pin | GSAP timeline + ScrollTrigger | Avoid scroll traps, overlong pinning and dead zones |
| Smooth scrolling | Lenis when justified | Native fallback, anchors, keyboard, touch, modal and focus behavior |
| Complex page choreography | Coordinated GSAP timelines | Cleanup on navigation; respect interruption and loading |
| Character/brand vector animation | Rive/Lottie/dotlottie after license check | Lightweight load, static fallback, correct playback behavior |

## Animation language parameters (defaults, not laws)

- Micro-feedback around 120-250ms; component entrance around 300-600ms; scene-to-scene transitions depend on narrative. Ease and distance by perceived weight; use critically damped springs for direct manipulation, not theatrical stagger on routine data.
- Animate composited `transform`/`opacity` when feasible. Avoid continuous layout thrash, large blur/filter repaints or always-on effects on low-powered devices.
- Limit to a **small motion vocabulary** (e.g. masked typographic reveal + project image parallax + one chapter scene morph). Variety comes from content and choreography, not unrelated easings.
- Scroll indicators should reflect real progress. Long pinning/velocity-dependent effects need meaningful content and escape paths.

## GSAP / ScrollTrigger / Lenis: correct lifecycle

- Source: https://gsap.com/docs/v3/Plugins/ScrollTrigger/ and https://gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/
- In React use proper scope/cleanup (`@gsap/react` or `gsap.context` / revert); in Vue/Svelte use framework lifecycle cleanup. Avoid duplicate ScrollTriggers under StrictMode/navigation.
- For Lenis use current https://github.com/darkroomengineering/lenis documentation; when integrating GSAP, synchronize on Lenis scroll updates and ONE animation clock. Avoid having both `autoRaf` and a separate ticker driving the same instance. Always destroy listeners/tickers on unmount.
- If changing layout after images/fonts load, refresh measurements deliberately. Test sticky/pinned sections across resize/orientation and nested scrollers.
- By default honor `prefers-reduced-motion`, including disabling smooth interpolation and scroll scrubbing when it is uncomfortable. Keep semantic route changes immediate and keyboard focus visible.

## Example GSAP + Lenis (framework-agnostic pseudocode, adapt versions)

```js
import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis({ autoRaf: false, anchors: true });
lenis.on('scroll', ScrollTrigger.update);
const tick = (seconds) => lenis.raf(seconds * 1000);
gsap.ticker.add(tick);

// On route/component teardown:
function teardown() {
  gsap.ticker.remove(tick);
  lenis.destroy();
  // Revert only animations/ScrollTriggers owned by this component/context.
}
```

Before shipping, verify reduced-motion behavior on the actual installed Lenis version, confirm one ticker, preserve nested modal scroll and anchor navigation. `gsap.ticker.lagSmoothing(0)` is documented for integration but changes global ticker behavior; add only when justified and restore appropriately in shared apps.

## Awwwards-inspired effects worth dissecting

- Typographic masks / split text: preserve accessible real heading, avoid permanently wrapped single letters for screen readers.
- Image reveal: original image art direction + `clip-path`/mask plus parallax; prevent giant repaints and large unoptimized images.
- Scroll-controlled project-card transformations: animate a coherent card to detail transition; ensure clickable cards still work on touch/keyboard.
- Magnetic buttons / pointer trails: require strong purpose, disable on coarse pointers and reduced motion, never obstruct hit targets.
- Horizontal galleries: use actual accessible controls, scroll snap, visible focus and clear progress; never hijack the only scroll mechanism.
- Chapter-to-chapter 3D transformations: synchronize scene with scroll timeline; offer still-image equivalent and route cleanup.
