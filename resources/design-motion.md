# Design skills and motion graphics

Use the [searchable repository index](design-motion.csv) to find an agent skill or a tool for a specific creative task. Each skill links to its actual `SKILL.md`. Each tool links to upstream documentation for the capability listed. The evidence links point to the revisions reviewed.

| Creative task | Where to start | What to expect |
| --- | --- | --- |
| Establish a visual system | [Stitch Design System Extraction](https://github.com/google-labs-code/stitch-skills/blob/62fdcd679747aca0792e5dd6591b10ddfad56825/plugins/stitch-design/skills/extract-design-md/SKILL.md) and [Anthropic Canvas Design](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/canvas-design/SKILL.md) | Extract a project's existing tokens and styles into `DESIGN.md`, or create a static poster as PNG or PDF. |
| Review typography and accessibility | [Typography Audit](https://github.com/mblode/agent-skills/blob/ff9805a3dabf4529f4d88f6b3f09c5a33cb0fcb6/skills/typography-audit/SKILL.md) and [Web Quality Accessibility](https://github.com/addyosmani/web-quality-skills/blob/afa8da942115f2961fdbfa80807ea0b232ff6c00/skills/accessibility/SKILL.md) | Check type scale, line length and font loading, then inspect keyboard behavior and accessibility-tree results. |
| Plan a storyboard | [Scenario Storyboards](https://github.com/scenario-labs/skills/blob/932df7551696a7c5c5381ad8be50f5214cedafc8/skills/scenario-storyboards/SKILL.md) | Turn a shot list into a sequence of panels with recurring characters and locations. Image generation uses Scenario’s hosted service. |
| Animate a title | [GSAP Plugins](https://github.com/greensock/gsap-skills/blob/aed9cfd3277740755f6bfc1155c7aa645403b760/skills/gsap-plugins/SKILL.md), [Coldtype](https://github.com/coldtype/coldtype/blob/a74948904732aee2071158a44ed47688e0ee607a/README.md) and [Kinetype](https://github.com/Amarel-Taylor-Scott/kinetype/blob/b50e8ec0df4e94d468a1461dac7040583dd2c81c/README.md) | Use GSAP for animated text in the browser, Coldtype for programmable letterforms in Python, or Kinetype for a seeded social-video reel. |
| Time graphics to narration | [Motion Canvas](https://github.com/motion-canvas/motion-canvas/blob/7b91435c301d530351dcf5ebb91dd139c002e405/README.md) and [Remotion Best Practices](https://github.com/remotion-dev/skills/blob/6f55706d1069e512430582ad86e4e57dc07afe1b/skills/remotion-best-practices/SKILL.md) | Motion Canvas previews a TypeScript animation against audio. The Remotion skill points React video authors to guidance on composition, captions and rendering. |
| Composite a shot or plan an edit | [Natron](https://github.com/NatronGitHub/Natron/blob/8408ee1d378d7d6df7b6a6218c31c5f1d2da8ab5/README.md) and [cutlist](https://github.com/Amarel-Taylor-Scott/cutlist/blob/4d2f9c3c5ab8dcbdfc57fc71b69218ee4e33467d/README.md) | Natron composites image layers and effects through a node graph. For a simple trim, cutlist turns keep ranges into an FFmpeg command and an edit timeline. |

### More production workflows

| What you have | What you need | Start here |
| --- | --- | --- |
| Four pixel-art views of a character | A rotating sprite preview | [Sprite Stacking](https://github.com/danielwh2/sprite-stacking/blob/6fecdfd0d6e5a0595f979550e05f4b1fcde550fe/skills/sprite-stacking/SKILL.md) builds the stacked slices. [Pixelorama](https://github.com/Orama-Interactive/Pixelorama/blob/5609dbacff4daa4c4cc4752d501e2549f40dfe6e/README.md) edits layered frames and exports sprite sheets. |
| A recorded voice and a drawn character | Timed dialogue animation | [Rhubarb Lip Sync](https://github.com/DanielSWolf/rhubarb-lip-sync/blob/9b9573cd21b253c9ba58739bbd1aa0b50b991bff/README.adoc) supplies mouth-shape cues. [Rigby2D](https://github.com/jaisurya-dev-art/rigby2d/blob/1971cf5e2d4c7e6e2b60891dd692f91454420a7d/README.md) rigs layered artwork for posing and animation. |
| A source article or short brief | A vertical explainer or storyboard | [Papercut Explainer](https://github.com/0xS4N4TG/papercut-explainer/blob/8d791944453f4e4b2d79322016762464173b1829/skills/papercut-explainer/SKILL.md) produces a cut-paper reel with Remotion. [Krita Storyboard Docker](https://github.com/KDE/krita/blob/ecb3fdea0ef581560d69fa0a1ef739277c252b34/plugins/dockers/storyboarddocker/StoryboardDockerDock.cpp) lays out timed panels for PDF or SVG review. |
| Cards, puppets or other physical models | A stop-motion shot | [Tahoma2D](https://github.com/tahoma2d/tahoma2d/blob/0ca33cb8af95d8b1648889d336e50e23dd9cfb2b/toonz/sources/stopmotion/stopmotioncontroller.h) captures camera frames with live view and onion skinning. |
| A table of measurements | An animated chart or a scientific figure | [gganimate](https://github.com/thomasp85/gganimate/blob/16129a6fbec4d8cf881056f18570da205894f227/README.md) controls how marks move as data changes. [Scientific Visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/ec59a29a03d5c40f73ab40878df04860bc00e876/skills/scientific-visualization/SKILL.md) covers uncertainty and print export. |
| A Figma design node | Components that fit an existing codebase | [Figma Design to Code](https://github.com/openai/plugins/blob/981b02c0c44058b595f3b4180002c3ae3c806d40/plugins/figma/skills/figma-design-to-code/SKILL.md) uses a Figma MCP connection and the project's component and token conventions. |
| A transcript or picture-locked edit | A handoff to an editor or distributor | [StoryToolkitAI](https://github.com/octimot/StoryToolkitAI/blob/91ab42b11f509aa84bb3801a5a1ba31cf5cf74cb/README.md) builds a paper edit from transcript excerpts. [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/f101411e11968d3255488f4aaccf041d965a2148/README.md) exchanges edit decisions and media references. [Netflix Photon](https://github.com/Netflix/photon/blob/76d6762737026a98bae6d73c01a4a5e7a53bf4a1/README.md) validates IMF delivery files. |

For project leads beyond this catalog, browse the [creative discovery sources and feeds](creative-discovery.md).

### Search from the CLI

```bash
skill-dir resources --kind skill typography
skill-dir resources --kind tool kinetic typography
skill-dir resources --kind skill storyboard --format json
```

The CSV records a license for the listed skill or tool. Some upstream repositories bundle assets under additional terms. The Remotion skill collection's license is recorded as `Unspecified` because its reviewed revision did not declare one.

### Connect the work to ta-amps seed packs

Three proposal packs describe artifacts you can keep between production steps.

| Stage | Pack | Useful artifact |
| --- | --- | --- |
| Plan | [Video showcase](https://github.com/ta-amps/seed-packs-library-of-nouns-and-verbs/blob/24b7d2970de959cd4b4bdb5c33f6a45cc9c9326b/packs/video-showcase/README.md) | A script and storyboard for the shots you want to produce. |
| Time the narration | [Narrated explainer video](https://github.com/ta-amps/seed-packs-library-of-nouns-and-verbs/blob/24b7d2970de959cd4b4bdb5c33f6a45cc9c9326b/packs/narrated-explainer-video/README.md) | A frame-based plan for scenes and captions. |
| Review the render | [Frame-by-frame video QA](https://github.com/ta-amps/seed-packs-library-of-nouns-and-verbs/blob/24b7d2970de959cd4b4bdb5c33f6a45cc9c9326b/packs/frame-by-frame-video-qa/README.md) | Findings about problems such as caption collisions, clipped text and frozen frames. |

These are workflow templates. The skill or tool you choose determines how you generate and render the media.
