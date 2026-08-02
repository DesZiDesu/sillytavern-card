# Honkai: Star Rail RPG cards

Import **one card only**.

- `Honkai Star Rail RPG.json` — canonical main card using **UI A / Astral Ticket**.
- `Variants/Honkai Star Rail RPG - UI A - Astral Ticket.json` — explicit UI A copy.
- `Variants/Honkai Star Rail RPG - UI B - Warp Record.json` — coordinated UI B set.
- `Variants/Honkai Star Rail RPG - UI C - Data Bank.json` — coordinated UI C set.

Every card is self-contained and embeds:

- 81 HSR lore and system entries;
- Scene Tracker;
- one matching Header;
- one matching Monologue design;
- one matching Dialogue design;
- Status Tracker.

The former `Honkai Star Rail Tracker Systems [LB].json` file was consolidated into the main lorebook and removed. No separate lorebook or regex import is required when using one of these cards.

## GitHub portrait headers

The Header regex uses the slug from:

`[HSRCHAR|slug|Name|element|path|faction]`

It loads:

`https://raw.githubusercontent.com/DesZiDesu/sillytavern-card/main/Sillytavern/Honkai%20Star%20Rail/Images/<slug>.jpg`

with a RawGitHack fallback. The approved first message uses the verified gallery files `march-7th-ice.jpg` and `dan-heng.jpg`.

Narrator/Narrative regex is intentionally not included yet.
