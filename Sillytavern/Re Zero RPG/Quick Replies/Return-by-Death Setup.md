# Return by Death — Setup (Re Zero RPG)

A Quick Reply kit + regex panel that reproduces Subaru's **Return by Death**:
rewind the chat to a Save Point while {{user}} alone keeps the memory of the
loop that just ended.

## Files
- `RZ_ReturnByDeath_QR.json` — Quick Reply set (4 buttons).
- `../Regex/RZ_Memory_Regex.json` — renders the `[RZMEM|…]` Loop Memory panel.

## Install
1. **Regex:** Extensions → Regex → Import → `RZ_Memory_Regex.json`.
2. **Quick Replies:** Quick Reply settings → Import → `RZ_ReturnByDeath_QR.json`,
   then enable the set in the active QR slots so the buttons show under the chat bar.

## The 4 buttons
| Button | What it does |
|---|---|
| 🔖 **Set Save Point** | Stores the current message id in `rbd_save`. This is the point you rewind to. Set it at each milestone (a new "checkpoint"). |
| ☠ **Return by Death** | Confirms → bumps the death counter → asks what {{user}} carries over → `/inject`s that memory into the prompt (id `rbd`) → `/cut`s every message after the Save Point. The world resets; the injected memory survives because it is **not** part of the deletable chat log. |
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

You can ask the card to append this block automatically by adding a line to the
card's output rules (post_history_instructions), e.g. *"On {{user}}'s death,
end the death scene with a single `[RZMEM|loop|save|cause|carried]` marker."*

## Note on STScript
These scripts use core commands (`/setvar`, `/getvar`, `/addvar`, `/add`,
`/buttons`, `/input`, `/inject`, `/flushinject`, `/cut`, `/sys`, `/popup`).
Command flags drift slightly between SillyTavern versions — if a button errors,
open it in the QR editor and adjust that one line (most often `/add` arithmetic
or the `/cut` range). The Loop Memory panel (regex) is version-independent.
