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
| `Regex/Universal_Smartphone_v2_UserSide.json` | **User Input** | **NEW.** Renders the messages/actions the phone sends *as you* into a phone-style "Sent" card. |

Import both in **SillyTavern → Extensions → Regex** (they're independent — the
new one does not replace the old one). Keep them both enabled.

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
**displayed** as a matching phone UI card on your side.

### What the User-Side regex renders

Every phone feature that sends a message as you is covered:

- **Chat** → blue outgoing message bubbles (per message), with the in-world time.
- **Social** → a row per action: ❤️ like · 💬 comment · ↩️ reply · ✍️ new post · 🔁 share.
- **Shop** → an itemised order receipt with the total.
- **Bank** → transfer cards (recipient · note · amount) with the total sent.
- **Contacts** → an "added to contacts" card.

It is **display-only** (`markdownOnly`), so the AI still receives the original
text and understands exactly what you did — you just see a nice card instead of
raw text.

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
