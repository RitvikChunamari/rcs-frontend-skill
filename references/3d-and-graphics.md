# Creative technology: interactive 3D, motion graphics and shaders

## Define the scene's job

Choose a specific reason: product comprehension, spatial identity, interaction affordance or storytelling. Define one hero object/scene with clear camera position, light design, material language, composition and animation beats. If a video, SVG or CSS perspective satisfies the goal, avoid costly WebGL.

## Tool choices

- Three.js: https://threejs.org/docs/ for engine-level WebGL/3D and a renderer that fits the environment.
- React Three Fiber: https://r3f.docs.pmnd.rs/ for React component scene architecture. Match R3F major version to React version (check current docs); use Drei only for needed helpers.
- Spline: https://spline.design/ for prototyping authored scenes; verify editor/export plan, embedding performance and commercial terms before relying on it.
- Blender: https://www.blender.org/ free authoring of mesh, textures, animation; export optimized glTF/GLB as appropriate.
- Rive: https://rive.app/ for interactive state-driven vector animations; verify current licensing/tooling and runtime capabilities.
- Lottie/dotlottie: https://lottiefiles.com/ , https://dotlottie.io/ ; inspect export features and individual asset licenses.
- SVG / CSS / Canvas2D: first choice for typography-as-graphic, precise illustrations and small interactive shaders that don't need actual 3D.
- Shadertoy / Codrops for studies: https://www.shadertoy.com/ , https://tympanus.net/codrops/ ; study principles rather than copying shader source/assets without permission.

## Scene craft

- Compose 3D using typographic and UI grid rules: camera FOV, negative space, object crop, color/material mood, consistent key/fill/rim lighting, balanced roughness/specular response, purposeful post-processing.
- Prefer authored geometry/optimized glTF; compress meshes/textures (Draco/Meshopt/KTX2 where supported), use limited lights/shadows, correct color management, clamp resolution on mobile, cache/dispose resources.
- Avoid running a high-DPR continuous render loop for an effectively static image. Use demand-driven rendering when appropriate; pause offscreen/in hidden tabs, reduce quality and effects on weak devices.
- Maintain interaction hit testing, pointer capture, keyboard alternative and a semantic description of meaningful scene content.
- Guarantee a static poster/alternate image and content visibility when WebGL is unsupported, loading, timed out, blocked, or reduced-motion is enabled.
- All interactive 3D is additive: preserve actual heading, button, content and form elements as accessible DOM when possible.

## Performance budget planning

Document scene count, GPU-heavy effects, target logical resolution/DPR, triangle/material/texture budget, model download size, main-thread work and render loop policy. Use actual measurements on mid/low-end mobile hardware; don't claim 60fps without measuring dropped frames and thermal/battery behavior.

## Visual approval checklist

Check silhouette at phone width, texture seams, readability over objects, quality under dark/light, anti-aliasing, offscreen load/unload, resize, no WebGL, touch drag and keyboard alternative. Compare stills from matching camera and state before and after optimization.
