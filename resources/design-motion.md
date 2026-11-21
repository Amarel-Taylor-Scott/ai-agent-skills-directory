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
