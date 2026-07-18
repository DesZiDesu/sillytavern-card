# Universal Smartphone v2

An interactive in-universe smartphone for SillyTavern, rendered from a single
`<PHONE>{…}</PHONE>` JSON state the AI emits. It covers **Chat, Social, Shop,
Bank, Contacts and Settings** in one widget.

This folder adds a **User-Side UI regex** so that *your own* phone actions render
as UI too (not plain text), and makes all displayed times follow **roleplay time**
instead of the real-world clock.

## Files

| File | Affects | What it does |
|------|---------|--------------|
| `Regex/Universal_Smartphone_v2.json` | AI Output + User Input | The phone itself (renders the `<PHONE>` state). Lightly patched — see *Time fix* below. |
| `Regex/Universal_Smartphone_v2_UserSide.json` | **User Input** | **NEW.** Renders the messages/actions the phone sends *as you* inside the **same phone UI** as the main regex. |
| `Lorebook/Phone [LB].json` | World Info | The AI-side phone lorebook — the unified `<PHONE>` smartphone protocol (schema, screens, send-formats) plus companion device systems (Banking, NEXUS social, chat messenger, Nokia, call kernel, book reader). Keyed on phone/app triggers; the Smartphone entry includes the **in-world time** rules. |

Import the two regexes in **SillyTavern → Extensions → Regex** (they're
independent — keep both enabled), and the lorebook as a **World Info / Lorebook**
so the AI knows how to emit the `<PHONE>` state.

## The problem this solves

The phone works like this:

1. The AI outputs a `<PHONE>` block → the main regex draws the interactive phone.
2. When you tap **Send** inside the phone (a chat, a like, an order, a transfer…),
   the widget types a compact text block into your message box and sends it as
   **you**, e.g.:

   ```
   [ Chat: Quincy ]
   ─────────────────────────────────
   1. hii Quincy!! did you eat yet?
   ─────────────────────────────────
   Saturday, Jul 18  21:47
   ```

Previously that block showed on **your** side as raw plain text. The AI still
needs to read that text (so it isn't changed in the prompt), but now it is
**displayed inside the very same phone** — same frame, notch, status bar,
wallpaper, bubbles and list rows as the main regex. It looks like your phone
showing the screen you just acted on, auto-sized to the content.

### What the User-Side regex renders

It reuses the main phone's own CSS and components, so every feature matches:

- **Chat** → the chat thread with your blue outgoing bubbles (per message), each
  stamped with the in-world time, under the contact's nav bar.
- **Social** → the feed: a new post renders as a real post card; likes / comments
  / replies / shares render as list rows with an icon.
- **Shop** → the "Order Placed" screen with cart-item rows and the total.
- **Bank** → the "Transfer Sent" screen with debit transaction rows (red) + total.
- **Contacts** → the contact list with the newly added contact.

It is **display-only** (`markdownOnly`), so the AI still receives the original
text and understands exactly what you did — you just see the phone screen instead
of raw text.

## Time fix — roleplay time, not real-world time

All times shown for **your** sent messages come from the in-world clock in the
footer of the sent block (`date  time`), which the phone fills from the `time`
and `date` fields **you set in the `<PHONE>` state** — never from
`new Date()`. So if the story clock says `21:47`, your sent bubbles read `21:47`.

The main phone regex was also patched so the *pre-send preview* is consistent:

- `ts()` now accepts a plain roleplay clock string like `"21:47"` (and still
  parses ISO timestamps), instead of only real-world ISO dates.
- Pending (not-yet-sent) chat bubbles are stamped with the in-world clock
  (`state.time`) instead of the real-world time.

### For accurate in-world time, keep the AI's `<PHONE>` state honest

The clock is whatever the AI writes — there is no live clock. To keep everything
in roleplay time, the `<PHONE>` state should always carry the current in-world
values:

```json
{
  "time": "21:47",
  "date": "Saturday, Jul 18",
  "chats": {
    "quincy": [
      { "from": "quincy", "text": "hi!", "ts": "21:30" },
      { "from": "self",   "text": "hey", "ts": "21:47" }
    ]
  }
}
```

`ts` may be either the in-world `"HH:MM"` clock or a full ISO 8601 timestamp —
both display as in-world time. Advancing `time`/`date` as the scene moves keeps
the phone on story time.
