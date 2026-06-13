# Return by Death — Setup (Re Zero RPG)

A Quick Reply kit + regex panel that reproduces Subaru's **Return by Death**:
rewind the chat to a Save Point while {{user}} alone keeps the memory of the
loop that just ended.

## Files
- `RZ_ReturnByDeath_QR.json` — Quick Reply set (4 buttons).
- `../Regex/RZ_Memory_Regex.json` — renders the `[RZMEM|…]` Loop Memory panel.
- `../Regex/RZ_ExtractMemory_Regex.json` — a **callable** regex (no auto
  placement) used by the QR via `/regex` to pull the carried-over memory out of
  the `[RZMEM|…]` marker. Import it but leave it as-is — it only runs when called.

## Install
1. **Regex:** Extensions → Regex → Import **both** `RZ_Memory_Regex.json` and
   `RZ_ExtractMemory_Regex.json`.
2. **Quick Replies:** Quick Reply settings → Import → `RZ_ReturnByDeath_QR.json`,
   then enable the set in the active QR slots so the buttons show under the chat bar.

## Confirm-on-death + native memory capture
- **Trigger:** manual. You press ☠ **Return by Death** when {{user}} dies; a
  confirm popup guards against misfires.
- **Memory:** captured **natively, no typing, no extension.** The card is
  instructed to end every death scene with an `[RZMEM|loop|save|cause|carried]`
  marker. On confirm, the QR runs `/regex name="RZ Extract Memory" {{lastMessage}}`
  to lift the `cause` + `carried` text straight out of that marker into
  `rbd_memory`, then injects it and rewinds.

## The 4 buttons
| Button | What it does |
|---|---|
| 🔖 **Set Save Point** | Stores the current message id in `rbd_save`. This is the point you rewind to. Set it at each milestone (a new "checkpoint"). |
| ☠ **Return by Death** | Confirms → bumps the death counter → auto-extracts this loop's memory from the `[RZMEM]` marker via `/regex` → appends it to a **cumulative log** (`rbd_log`) → `/inject`s the whole log into the prompt (id `rbd`) → `/cut`s every message after the Save Point → re-posts a **persistent Loop Memory panel** so you can see what happened and which loop you're on. The injected memory survives because it is **not** part of the deletable chat log. |
| 📖 **Loop Memory** | Shows the current carried-over memory + loop number. |
| 🧹 **Clear Memory** | Wipes `rbd` injection, `rbd_memory`, `rbd_deaths`, `rbd_save`. |

## Why the AI still "remembers" after deletion
Deleting messages drops them from context, so anything important must live
**outside** the chat log. This kit keeps it in:
- a chat variable `rbd_memory`, and
- a persistent prompt injection (`/inject id=rbd …`) re-applied each turn.

Both persist across the `/cut`, so the next generation sees "what {{user}}
already lived through" while NPCs reset.

## Loop Memory panel format
Have the engine print this marker (e.g. inside its death narration). The regex
turns it into the styled panel — four pipe-separated fields:

```
[RZMEM|loop|save point|cause of death|what is carried over]
```

Example:

```
[RZMEM|3|Morning in the Royal Capital slums|Elsa slaughtered everyone in the loot house at dusk|Don't enter the loot house after dark / Reinhard is nearby and can be pulled in / Felt is not an enemy]
```

The card already emits this marker automatically — a `[Return by Death Marker]`
rule was added to its `post_history_instructions`, telling it to end every death
scene with a single `[RZMEM|loop|save|cause|carried]` line.

## Note on STScript
These scripts use core commands (`/setvar`, `/getvar`, `/addvar`, `/add`,
`/buttons`, `/if`, `/regex`, `/inject`, `/flushinject`, `/cut`, `/sys`, `/popup`).
Command flags drift slightly between SillyTavern versions — if a button errors,
open it in the QR editor and adjust that one line (most often `/add` arithmetic,
the `/cut` range, or the `/regex name=…` syntax). The Loop Memory panel (regex)
is version-independent.
