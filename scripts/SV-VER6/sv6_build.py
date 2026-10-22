import os, re, shutil
from PIL import Image, ImageDraw, ImageFont
SD = r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad"
exec(open(SD + "/sv6_texts.py", encoding="utf-8").read())
D = SD + "/avamp/SV-VER6"
FIGDIR = D + "/figures-only"
os.makedirs(FIGDIR, exist_ok=True)
_re = re
dec = lambda L, t: _re.sub(r"(?<=\d)\.(?=\d)", ",", t) if L in ("ru", "uk", "de", "it", "fr") else t
W, pad = 3200, 60
colw = (W - 3 * pad) // 2
FS = 34
REG = ImageFont.truetype("C:/Windows/Fonts/meiryo.ttc", FS)
HD = ImageFont.truetype("C:/Windows/Fonts/meiryob.ttc", int(FS * 1.2))
BIG = ImageFont.truetype("C:/Windows/Fonts/meiryob.ttc", int(FS * 1.5))
TOK = re.compile(r"[\x21-\x7e\u00a0-\u024f\u0400-\u04ff]+|\s|.", re.S)


def wrap(t, font, width):
    out, cur = [], ""
    for tk in TOK.findall(t):
        if font.getlength(cur + tk) > width and cur.strip():
            out.append(cur.rstrip()); cur = tk.lstrip()
        else:
            cur += tk
    out.append(cur.rstrip())
    return out


hh = lambda lines: sum(int(f.size * 1.45) for _, f in lines) + 40


def text_panel(keys, heading):
    blocks = []
    for L in LANG8:
        lines = [(NAME8[L], HD)]
        for k in keys:
            t = TITLE[L] if k == "title" else T[k][L]
            for ln in wrap(dec(L, t), REG, colw):
                lines.append((ln, REG))
            lines.append(("", REG))
        blocks.append(lines)
    rows = [(blocks[i], blocks[i + 1]) for i in range(0, 8, 2)]
    TH = 140 + sum(max(hh(a), hh(b)) for a, b in rows) + pad
    panel = Image.new("RGB", (W, TH), "white")
    d = ImageDraw.Draw(panel)
    d.text((pad, 40), heading, font=BIG, fill=(20, 30, 60))
    y = 140
    for a, b in rows:
        for col, lines in enumerate((a, b)):
            x, yy = pad + col * (colw + pad), y
            for t, f in lines:
                d.text((x, yy), t, font=f, fill=(20, 30, 60) if f is HD else (40, 40, 40)); yy += int(f.size * 1.45)
        y += max(hh(a), hh(b))
    return panel


def compose(fn, keys, heading):
    src = SD + "/" + fn
    shutil.copy(src, FIGDIR + "/" + fn)
    fig = Image.open(src).convert("RGB")
    fig = fig.resize((W, int(fig.height * W / fig.width)))
    panel = text_panel(keys, heading)
    img = Image.new("RGB", (W, fig.height + panel.height), "white")
    img.paste(fig, (0, 0)); img.paste(panel, (0, fig.height))
    img.save(D + "/" + fn, "JPEG", quality=88, dpi=(300, 300))
    print(fn, img.size)


compose("surround_v6_balanced.jpg", ["os", "net", "rf", "rest"], "SV-VER6 全段バランス / Fully balanced — 説明 / Explanation (8 languages)")
compose("surround_v6_unbalanced.jpg", ["os", "net", "rf", "rest"], "SV-VER6 アンバランス / Unbalanced — 説明 / Explanation (8 languages)")
compose("surround_v6_sim.jpg", ["sim", "net", "rest"], "SV-VER6 仮想シミュレーション / Virtual simulation — 説明 / Explanation (8 languages)")
man = text_panel(["title", "os", "net", "sim", "rf", "rest"], "SV-VER6 説明書 / Manual (日本語 · English US/UK · Русский · Українська · Deutsch · Italiano · Français)")
man.save(D + "/manual-sv6.jpg", "JPEG", quality=90, dpi=(300, 300))
man.save(D + "/manual-sv6.pdf", resolution=300)
md = ["# SV-VER6 — %s\n" % TITLE["ja"],
      "\n> Translation note / 翻訳について: the non-Japanese texts were written by an AI and then proofread by independent AI reviewers for the earlier versions; the new SV-VER6 texts have only been written by an AI and have NOT been checked by human native speakers. 日本語以外の文章は AI が書いたもので、ネイティブスピーカー (人間) による確認は未実施です。\n",
      "Figures: `surround_v6_balanced.jpg`, `surround_v6_unbalanced.jpg`, `surround_v6_sim.jpg` (each with the 8-language explanation below the figure; bare figures in `figures-only/`), `manual-sv6.jpg` / `manual-sv6.pdf`, `surround-av-amp-v6.pdf`. Reference design, Python calculations, not bench measurements.\n"]
for L in LANG8:
    md.append("## %s\n" % NAME8[L]); md.append("**%s**\n" % TITLE[L])
    for k in ("os", "net", "sim", "rf", "rest"):
        md.append("- " + dec(L, T[k][L]))
    md.append("")
open(D + "/README.md", "w", encoding="utf-8").write("\n".join(md))
ns = ("surround_v6_balanced.jpg", "surround_v6_unbalanced.jpg", "surround_v6_sim.jpg", "manual-sv6.jpg")
ims = [Image.open(D + "/" + n).convert("RGB") for n in ns]
ims[0].save(D + "/surround-av-amp-v6.pdf", save_all=True, append_images=ims[1:], resolution=300)
print("done")
