# Honkai: Star Rail — Regex Interface Kit

A SillyTavern regex kit that renders game-authentic HSR UI in chat: character
headers (with portrait), NPC headers (imageless), monologue, dialogue, narrator
and a status panel. Colour, element gem, Path icon and Path/element labels are
all driven automatically by the **element** and **path** keywords you type — no
hex codes needed.

Fonts (Marcellus · Chakra Petch · Bai Jamjuree · Share Tech Mono) load from
Google Fonts; portraits load from this repo's `Images/` folder via githack.
Thai text is fully supported.

## Install (SillyTavern)
Extensions → Regex → Import Regex, and import the `.json` scripts you want.
For each **(pick ONE)** folder, import only a single style.

- **Header** — pick ONE of A (Astral Ticket) / B (Warp Nameplate) / C (Constellation)
- **Header NPC** — pick ONE of A / B / C (imageless, matches the header styles)
- **Monologue** — Inner Voice
- **Dialogue** — Transmission
- **Narrator** — Trailblaze Log
- **Status** — Trailblaze HUD (`HSR_Status_Regex.json`, top level)

## Tokens

Type these in a message; the regex replaces them with styled HTML.

| Component | Token |
|---|---|
| Character header | `[HSRCHAR\|slug\|Name\|element\|path\|faction]` |
| NPC header | `[HSRNPC\|Name\|element\|path\|faction]` |
| Monologue | `[HSRTHINK\|Name\|element\|text]` |
| Dialogue | `[HSRSAY\|Name\|element\|text]` |
| Narrator | `[HSRNARR\|text]` |
| Status | `[HSRSTATUS\|element\|Title\|Location\|HP\|Mood]` |

Examples:
```
[HSRCHAR|kafka|Kafka|lightning|nihility|Stellaron Hunters]
[HSRNPC|Cocolia|ice|preservation|Belobog · Supreme Guardian]
[HSRTHINK|Trailblazer|imaginary|A Stellaron sleeps inside me, yet my heart beats steady.]
[HSRSAY|March 7th|ice|ยิ้มหน่อยสิ! ...เดี๋ยว อย่าเพิ่งหนีสิ!]
[HSRNARR|The Astral Express glides through a veil of blue stars.]
[HSRSTATUS|imaginary|Trailblazer · Status|Penacony · Golden Hour|2,940 / 3,580|มุ่งมั่น แต่ระแวงเล็กน้อย]
```

## Elements (drive colour + gem)
Use the lowercase keyword: `physical` · `fire` · `ice` · `lightning` · `wind` · `quantum` · `imaginary`

## Paths (drive Path icon + label)
Use the lowercase keyword: `destruction` · `hunt` · `erudition` · `harmony` ·
`nihility` · `preservation` · `abundance` · `remembrance` · `elation` ·
`propagation` · `trailblaze`

## Character image slugs
The first field of `[HSRCHAR|...]` is the image slug below. Portraits come from
`Sillytavern/Honkai Star Rail/Images/<slug>.jpg`. If a slug has no image the
portrait simply hides (the rest of the header still renders).

| # | Character | image slug | element |
|--:|---|---|---|
| 1 | March 7th (Ice) | `march-7th-ice` | Ice |
| 2 | Dan Heng | `dan-heng` | Wind |
| 3 | Himeko | `himeko` | Fire |
| 4 | Welt | `welt` | Imaginary |
| 5 | Kafka | `kafka` | Thunder |
| 6 | Silver Wolf | `silver-wolf` | Quantum |
| 7 | Arlan | `arlan` | Thunder |
| 8 | Asta | `asta` | Fire |
| 9 | Herta | `herta` | Ice |
| 10 | Saber | `saber` | Wind |
| 11 | Archer | `archer` | Quantum |
| 12 | Bronya | `bronya` | Wind |
| 13 | Seele | `seele` | Quantum |
| 14 | Serval | `serval` | Thunder |
| 15 | Gepard | `gepard` | Ice |
| 16 | Natasha | `natasha` | Physical |
| 17 | Pela | `pela` | Ice |
| 18 | Clara | `clara` | Physical |
| 19 | Sampo | `sampo` | Wind |
| 20 | Hook | `hook` | Fire |
| 21 | Lynx | `lynx` | Quantum |
| 22 | Luka | `luka` | Physical |
| 23 | Topaz & Numby | `topaz-and-numby` | Fire |
| 24 | Qingque | `qingque` | Quantum |
| 25 | Tingyun | `tingyun` | Thunder |
| 26 | Luocha | `luocha` | Imaginary |
| 27 | Jing Yuan | `jing-yuan` | Thunder |
| 28 | Blade | `blade` | Wind |
| 29 | Sushang | `sushang` | Physical |
| 30 | Yukong | `yukong` | Imaginary |
| 31 | Fu Xuan | `fu-xuan` | Quantum |
| 32 | Yanqing | `yanqing` | Ice |
| 33 | Guinaifen | `guinaifen` | Fire |
| 34 | Bailu | `bailu` | Thunder |
| 35 | Jingliu | `jingliu` | Ice |
| 36 | Dan Heng • Imbibitor Lunae | `dan-heng-imbibitor-lunae` | Imaginary |
| 37 | Xueyi | `xueyi` | Quantum |
| 38 | Hanya | `hanya` | Physical |
| 39 | Huohuo | `huohuo` | Wind |
| 40 | Jiaoqiu | `jiaoqiu` | Fire |
| 41 | Feixiao | `feixiao` | Wind |
| 42 | Yunli | `yunli` | Physical |
| 43 | Lingsha | `lingsha` | Fire |
| 44 | Moze | `moze` | Thunder |
| 45 | March 7th (Imaginary) | `march-7th-imaginary` | Imaginary |
| 46 | Fugue | `fugue` | Fire |
| 47 | Gallagher | `gallagher` | Fire |
| 48 | Argenti | `argenti` | Physical |
| 49 | Ruan Mei | `ruan-mei` | Ice |
| 50 | Aventurine | `aventurine` | Imaginary |
| 51 | Dr. Ratio | `dr-ratio` | Imaginary |
| 52 | Sparkle | `sparkle` | Quantum |
| 53 | Black Swan | `black-swan` | Wind |
| 54 | Acheron | `acheron` | Thunder |
| 55 | Robin | `robin` | Physical |
| 56 | Firefly | `firefly` | Fire |
| 57 | Misha | `misha` | Ice |
| 58 | Sunday | `sunday` | Imaginary |
| 59 | Jade | `jade` | Quantum |
| 60 | Boothill | `boothill` | Physical |
| 61 | Rappa | `rappa` | Imaginary |
| 62 | The Dahlia | `the-dahlia` | Fire |
| 63 | The Herta | `the-herta` | Ice |
| 64 | Aglaea | `aglaea` | Thunder |
| 65 | Tribbie | `tribbie` | Quantum |
| 66 | Mydei | `mydei` | Imaginary |
| 67 | Anaxa | `anaxa` | Wind |
| 68 | Cipher | `cipher` | Quantum |
| 69 | Castorice | `castorice` | Quantum |
| 70 | Phainon | `phainon` | Physical |
| 71 | Hyacine | `hyacine` | Wind |
| 72 | Hysilens | `hysilens` | Physical |
| 73 | Cerydra | `cerydra` | Wind |
| 74 | Evernight | `evernight` | Ice |
| 75 | Dan Heng • Permansor Terrae | `dan-heng-permansor-terrae` | Physical |
| 76 | Cyrene | `cyrene` | Ice |
| 77 | Sparxie | `sparxie` | Fire |
| 78 | Yao Guang | `yao-guang` | Physical |
| 79 | Ashveil | `ashveil` | Thunder |
| 80 | Evanescia | `evanescia` | Physical |
| 81 | Silver Wolf LV.999 | `silver-wolf-lv999` | Imaginary |
| 82 | Mortenax Blade | `mortenax-blade` | Fire |
| 83 | Trailblazer (Physical) M | `trailblazer-physical-m` | Physical |
| 84 | Trailblazer (Physical) F | `trailblazer-physical-f` | Physical |
| 85 | Trailblazer (Fire) M | `trailblazer-fire-m` | Fire |
| 86 | Trailblazer (Fire) F | `trailblazer-fire-f` | Fire |
| 87 | Trailblazer (Imaginary) M | `trailblazer-imaginary-m` | Imaginary |
| 88 | Trailblazer (Imaginary) F | `trailblazer-imaginary-f` | Imaginary |
| 89 | Trailblazer (Ice) M | `trailblazer-ice-m` | Ice |
| 90 | Trailblazer (Ice) F | `trailblazer-ice-f` | Ice |
| 91 | Trailblazer (Lightning) M | `trailblazer-lightning-m` | Thunder |
| 92 | Trailblazer (Lightning) F | `trailblazer-lightning-f` | Thunder |

