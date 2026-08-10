# Lorebooks

Store SillyTavern World Info / lorebook files for the Honkai Impact 3rd bot here.

## Importable lorebook

- `Honkai Impact 3rd [LB].json` — the main HI3 lorebook with 116 entries covering cosmology, Honkai systems, Previous Era, Current Era, Part 1, Part 1.5, Part 2 through Chapter XIII, characters, factions, locations, and event-by-event A → B → C → End flows.

## Entry contract

- Constant entries intentionally use an empty `key` array and are always available.
- Non-constant entries are vectorized and include both English and Thai retrieval keywords.
- The file keeps mainline Earth, Part 1.5, Part 2, APHO, Captainverse, bubble universes, and crossover material separated by continuity rules.
- The canon cutoff is Part 2 Chapter XIII: `A Rose in a Curtsy`; future chapters must be labelled as speculation or an original continuation.

## Import notes

Import the JSON as a SillyTavern World Info / lorebook. If the companion HI3 V3 regex package is enabled, use exact gallery filename stems from `Honkai Impact 3rd/Gallery/` for `[HI3CHAR]`; the Regex appends `.png` and loads the repository gallery first. The lorebook documents `[HI3CHAR]`, `[HI3NPC]`, `[HI3SAY]`, and `[HI3THINK]` marker contracts; do not invent image URLs or filenames.

Keep authored lorebook exports and editable source notes together in this folder.
