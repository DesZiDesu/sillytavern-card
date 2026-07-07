/**
 * Pixiv personal proxy — Cloudflare Worker
 * ----------------------------------------
 * Personal-use bridge that lets your own website search Pixiv and load its
 * images (Pixiv has no public API, no CORS, and blocks image hotlinking).
 *
 * SETUP (once, ~3 minutes):
 *   1. Create a free account at https://dash.cloudflare.com
 *   2. Workers & Pages -> Create -> Worker -> paste this whole file -> Deploy
 *   3. Copy your worker URL (https://<name>.<account>.workers.dev)
 *      and paste it into pixiv-finder.html's Options.
 *
 * OPTIONAL (recommended) — Settings -> Variables & Secrets:
 *   ACCESS_KEY     any password you invent. Requests must then include
 *                  ?key=<that password>; stops strangers using your worker.
 *   PIXIV_SESSION  your PHPSESSID cookie value from pixiv.net (log in,
 *                  DevTools -> Application -> Cookies -> PHPSESSID).
 *                  Enables R-18 results and full account-level search.
 *
 * NOTES: personal use only. Pixiv's ToS does not allow third-party clients;
 * keep traffic low, don't share your worker URL publicly, and don't
 * redistribute artists' work. Session cookies expire every few weeks —
 * just paste a fresh one when R-18 stops working.
 */

const UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36";

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "*",
};

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", ...CORS },
  });
}

function pixivHeaders(env) {
  const h = {
    "User-Agent": UA,
    "Referer": "https://www.pixiv.net/",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
  };
  if (env.PIXIV_SESSION) h["Cookie"] = "PHPSESSID=" + env.PIXIV_SESSION;
  return h;
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (req.method === "OPTIONS") return new Response(null, { headers: CORS });

    // optional shared-secret gate
    if (env.ACCESS_KEY && url.searchParams.get("key") !== env.ACCESS_KEY) {
      return json({ error: true, message: "bad or missing ?key=" }, 403);
    }

    try {
      // ---------- search: /search?word=...&page=1&mode=all|safe|r18&smode=s_tag|s_tag_full
      if (url.pathname === "/search") {
        const word = (url.searchParams.get("word") || "").trim();
        if (!word) return json({ error: true, message: "missing ?word=" }, 400);
        const page = url.searchParams.get("page") || "1";
        let mode = url.searchParams.get("mode") || "safe";
        if (!["all", "safe", "r18"].includes(mode)) mode = "safe";
        if (mode === "r18" && !env.PIXIV_SESSION)
          return json({ error: true, message: "r18 needs PIXIV_SESSION secret on the worker" }, 400);
        const smode = url.searchParams.get("smode") === "s_tag_full" ? "s_tag_full" : "s_tag";
        const target =
          "https://www.pixiv.net/ajax/search/artworks/" + encodeURIComponent(word) +
          "?word=" + encodeURIComponent(word) +
          "&order=date_d&mode=" + mode + "&p=" + encodeURIComponent(page) +
          "&s_mode=" + smode + "&type=all&lang=en";
        const r = await fetch(target, { headers: pixivHeaders(env) });
        if (!r.ok) return json({ error: true, message: "pixiv answered " + r.status }, 502);
        const data = await r.json();
        const bucket = data?.body?.illustManga || data?.body?.illust || {};
        const items = (bucket.data || [])
          .filter((x) => x && x.id && x.url)
          .map((x) => ({
            id: x.id, title: x.title, thumb: x.url,
            user: x.userName, userId: x.userId,
            pages: x.pageCount || 1, r18: x.xRestrict > 0,
            tags: x.tags || [], w: x.width, h: x.height,
          }));
        return json({ error: false, total: bucket.total || items.length, items });
      }

      // ---------- illust pages: /illust?id=12345
      if (url.pathname === "/illust") {
        const id = (url.searchParams.get("id") || "").replace(/\D/g, "");
        if (!id) return json({ error: true, message: "missing ?id=" }, 400);
        const r = await fetch(
          "https://www.pixiv.net/ajax/illust/" + id + "/pages?lang=en",
          { headers: pixivHeaders(env) }
        );
        if (!r.ok) return json({ error: true, message: "pixiv answered " + r.status }, 502);
        const data = await r.json();
        const pages = (data?.body || []).map((p) => ({
          original: p.urls?.original, regular: p.urls?.regular,
          small: p.urls?.small, w: p.width, h: p.height,
        }));
        return json({ error: false, id, pages });
      }

      // ---------- image proxy: /image?url=<i.pximg.net url>
      if (url.pathname === "/image") {
        const target = url.searchParams.get("url") || "";
        let t;
        try { t = new URL(target); } catch { return json({ error: true, message: "bad url" }, 400); }
        if (!t.hostname.endsWith(".pximg.net"))
          return json({ error: true, message: "only pximg.net urls allowed" }, 400);
        const r = await fetch(t.toString(), {
          headers: { "User-Agent": UA, "Referer": "https://www.pixiv.net/" },
          cf: { cacheEverything: true, cacheTtl: 86400 },
        });
        if (!r.ok) return json({ error: true, message: "pximg answered " + r.status }, 502);
        const h = new Headers(CORS);
        h.set("content-type", r.headers.get("content-type") || "image/jpeg");
        h.set("cache-control", "public, max-age=86400");
        const cd = url.searchParams.get("dl");
        if (cd) h.set("content-disposition", 'attachment; filename="' + cd.replace(/[^\w.\-]+/g, "_") + '"');
        return new Response(r.body, { status: 200, headers: h });
      }

      return json({ error: true, message: "routes: /search /illust /image" }, 404);
    } catch (e) {
      return json({ error: true, message: String(e) }, 500);
    }
  },
};
