# HI3 Message UI — Valkyrja Operations V3

A single-install SillyTavern Regex package for Honkai Impact 3rd conversation rendering.

## Install

Import HI3 Message UI V3 Package.json once. It contains all four Regex entries:

- Character Header — V3 Valkyrja Data
- NPC Header — V3 Auxiliary Contact
- Dialogue — V3 Voice Link
- Monologue — V3 Cognitive Trace

Do not import both the package and the individual source entries at the same time, or the same marker can be rendered twice.

## Marker contract

[HI3CHAR|gallery-stem|Name|type|Battlesuit|Faction]
[HI3NPC|Name|type|Role|Faction]
[HI3SAY|Name|type|text]
[HI3THINK|Name|type|text]

Character Header example:

[HI3CHAR|040_Herrscher_of_Flamescion_(Avatar)|Kiana Kaslana|psy|Herrscher of Flamescion|Schicksal · Hyperion]

The first HI3CHAR field is the exact filename stem from Honkai Impact 3rd/Gallery/; the Regex appends .png. The gallery image is loaded first from:

Honkai Impact 3rd/Gallery/<gallery-stem>.png

If an older marker still uses an assets/ui/portraits/ stem, the header keeps a compatibility fallback after the gallery request fails.

## Rendering contract

- One marker per line is recommended.
- markdownOnly: true
- runOnEdit: true
- placement [1,2]
- Character Header loads a gallery image.
- NPC Header never contains or requests an image.
- Dialogue uses the light V3 command surface.
- Monologue uses the dark V3 cognitive/combat surface.
- Supported accent types: bio, psy, mech, qua, img, sd, neutral.
- Keep | and ] out of field values.
