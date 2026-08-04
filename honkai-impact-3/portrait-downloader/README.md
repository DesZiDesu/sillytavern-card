# Honkai Impact 3 — Portrait Downloader

Standalone browser downloader for Honkai Impact 3 battlesuit artwork, designed as the collection step before importing the images into the local SillyTavern gallery.

## Open the downloader

Development preview:

```text
https://raw.githack.com/DesZiDesu/sillytavern-card/feat/hi3-portrait-downloader/honkai-impact-3/portrait-downloader/index.html
```

After the pull request is merged:

```text
https://raw.githack.com/DesZiDesu/sillytavern-card/main/honkai-impact-3/portrait-downloader/index.html
```

## Available collections

- **Square thumbnails** — 400×400 where available; recommended for a face-focused gallery.
- **Vertical portraits** — approximately 148×260.
- **Battlesuit icons** — approximately 208×184.
- **Profile avatars** — approximately 172×148.

The page queries the `Battlesuit Images` categories from the Official Honkai Impact 3 Wiki through its MediaWiki API, shows the current files, and exports selected or all images as a ZIP. The ZIP also contains `manifest.json` and a source note, which makes the later repository import reproducible.

## Import workflow

1. Open the RawGitHack page.
2. Leave **Square thumbnails** selected for HSR-like square portraits, or choose another collection.
3. Press **Download all as ZIP**.
4. Send the downloaded ZIP back for normalization, naming, local embedding, and gallery creation under `honkai-impact-3/portraits/`.

## Rights and source

The downloader does not claim ownership or relicense the artwork. Honkai Impact 3 game artwork and related trademarks belong to HoYoverse. The wiki indexes the source files and provides the metadata used by this utility. Use the downloaded material for personal/reference purposes and retain the generated source manifest.
