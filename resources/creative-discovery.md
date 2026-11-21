# Where to discover creative tools

These 15 sources cover different parts of the search. Start with Codrops for browser motion demos, STASH for production credits, Blender Extensions for installable tools, or the Coding Train showcase for editable sketches. The [source index](creative-discovery.csv) includes a real example for every source. Links and feed formats were checked on November 21, 2026.

## Feeds and machine-readable catalogs

| Publisher | Endpoint | What it yields |
| --- | --- | --- |
| [Codrops Creative Hub](https://tympanus.net/codrops/hub/tutorials/) | [RSS](https://feeds.feedburner.com/tympanus) | 10 items on the verification date. The publisher's tutorial index had newer work than the mirror. |
| [STASH](https://www.stashmedia.tv/) | [RSS](https://www.stashmedia.tv/feed/) | Art direction and studio credits for animated spots. |
| [BlenderNation](https://www.blendernation.com/) | [RSS](https://www.blendernation.com/feed/) | Blender films, add-ons and process breakdowns. |
| [fxguide](https://www.fxguide.com/) | [RSS](https://www.fxguide.com/feed/) | Artist interviews and detailed VFX breakdowns. |
| [Animation World Network: AnimationWorld](https://www.awn.com/animationworld) | [RSS](https://www.awn.com/animationworld/rss.xml) | Studio animation, stop motion and production interviews. |
| [Blender Extensions](https://extensions.blender.org/add-ons/) | [JSON API](https://extensions.blender.org/api/v1/extensions/) | Request JSON with the HTTP header `Accept: application/json` to read add-on metadata. |
| [Processing Contributions](https://github.com/processing/processing-contributions) | [YAML catalog](https://raw.githubusercontent.com/processing/processing-contributions/main/contributions.yaml) | Filter the publisher's contribution records by type, category and status. |

## Directories and showcases

| Source | What to look for | Follow a lead |
| --- | --- | --- |
| [Awesome Creative Coding](https://github.com/terkelg/awesome-creative-coding) | Generative-art libraries and visual programming frameworks | [Example](https://github.com/mattdesl/canvas-sketch) |
| [Awesome Motion Skills](https://github.com/iart-ai/awesome-motion-skills) | Agent workflows for animation, explainers and kinetic typography | [Example](https://github.com/iart-ai/motion-design-skills) |
| [p5.js Libraries](https://p5js.org/libraries/directory/) | p5.js capture, export and shader libraries | [Example](https://github.com/tapioca24/p5.capture) |
| [VIDVOX ISF Files](https://github.com/Vidvox/ISF-Files) | Individual GLSL effects and their input controls | [Example](https://github.com/Vidvox/ISF-Files/blob/master/ISF/Kaleidoscope.fs) |
| [FFmpeg Filters](https://ffmpeg.org/ffmpeg-filters.html) | Named FFmpeg filters with parameters and examples | [Example](https://ffmpeg.org/ffmpeg-filters.html#xfade) |
| [Motionographer](https://motionographer.com/) | Motion studios, title sequences and production credits | [Example](https://motionographer.com/2026/10/21/the-flowers-look-back-teamlab-at-offf-barcelona-2026/) |
| [CreativeApplications.Net](https://www.creativeapplications.net/) | Experimental audiovisual instruments and installations | [Example](https://www.creativeapplications.net/member/toneveld-a-growing-collection-of-browser-based-sound-machines/) |
| [The Coding Train Passenger Showcase](https://thecodingtrain.com/showcase) | Community sketches you can inspect and remix | [Example](https://editor.p5js.org/camii06/sketches/jL6IvVK2U) |

## Find small projects and forks on GitHub

These searches use topic, star, fork and archive filters. A star range helps surface projects at different stages. Read the implementation and license at the source before adding an entry.

- [Small creative-coding repositories, newest updates first](https://github.com/search?type=repositories&q=topic%3Acreative-coding%20stars%3A0..25%20archived%3Afalse%20fork%3Atrue%20sort%3Aupdated)
- [Established motion-graphics projects, most stars first](https://github.com/search?type=repositories&q=topic%3Amotion-graphics%20archived%3Afalse%20stars%3A%3E%3D100%20sort%3Astars)
- [Creative-coding forks, newest updates first](https://github.com/search?type=repositories&q=topic%3Acreative-coding%20fork%3Aonly%20archived%3Afalse%20sort%3Aupdated)
- [Small video-editing projects, newest updates first](https://github.com/search?type=repositories&q=topic%3Avideo-editing%20archived%3Afalse%20stars%3A0..75%20sort%3Aupdated)

When a fork appears, check its parent and the changes it contributes. For example, [BigTwoFly/PixelFx](https://github.com/BigTwoFly/PixelFx) points back to [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx), the source listed in the project catalog.

## Query the source index locally

```bash
skill-dir sources
skill-dir sources shaders
skill-dir sources --has-feed --format json
```

The last command returns publisher URLs and notes for five RSS feeds, one JSON API and one YAML catalog. An empty `feed_url` means a browse link is available. The `example_url` may lead to a project, a source file, a runnable sketch or a production write-up.
