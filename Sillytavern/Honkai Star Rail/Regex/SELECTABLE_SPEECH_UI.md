# HSR Selectable Speech UI

The Honkai: Star Rail speech interface is split into three independent **pick ONE** folders so users can choose one Header, one Dialogue, and one Monologue design.

## Header — pick one

Folder:

`Header (เลือกโหลดแค่อันเดียว - pick ONE)`

- `HSR_Header_A_AstralTicket_Regex.json`
- `HSR_Header_B_WarpRecord_Regex.json`
- `HSR_Header_C_DataBank_Regex.json`

All Header variants use:

`[HSRCHAR|slug|Name|element|path|faction]`

Character portraits load from the repository gallery at:

`Sillytavern/Honkai Star Rail/Images/<slug>.jpg`

The portrait is displayed on the right side of the thin header.

## Dialogue — pick one

Folder:

`Dialogue (เลือกโหลดแค่อันเดียว - pick ONE)`

- `HSR_Dialogue_A_AstralTicket_Regex.json`
- `HSR_Dialogue_B_WarpRecord_Regex.json`
- `HSR_Dialogue_C_DataBank_Regex.json`

All Dialogue variants use:

`[HSRSAY|Name|element|text]`

Dialogue contains no portrait image.

## Monologue — pick one

Folder:

`Monologue (เลือกโหลดแค่อันเดียว - pick ONE)`

- `HSR_Monologue_A_AstralTicket_Regex.json`
- `HSR_Monologue_B_WarpRecord_Regex.json`
- `HSR_Monologue_C_DataBank_Regex.json`

All Monologue variants use:

`[HSRTHINK|Name|element|text]`

Monologue contains no portrait image.

## Matching sets

- **A — Astral Ticket:** ivory HSR menu surface, gold rail and dark cinematic text panels.
- **B — Warp Record:** navy warp-result styling with violet/cyan signal accents.
- **C — Data Bank:** pale silver database header with clean information panels.

Users may mix letters, but matching A/A/A, B/B/B, or C/C/C gives the most coherent visual system.

## Preview

Open:

`Tools/previews/hsr_speech_ui_hsr_style_preview.html`

The preview renders the production regex files and gallery portraits directly from the repository.
