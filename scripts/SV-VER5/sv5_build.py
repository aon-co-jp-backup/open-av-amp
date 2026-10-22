import os, re
from PIL import Image, ImageDraw, ImageFont
SD = r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad"
g = {}
exec(open(SD + r"\v7_calc.py", encoding="utf-8").read().replace('if __name__ == "__main__":', 'if False:'), g)
avg = g["avg_w"](g["need"](100))
d_ch = g["pd_D"](avg)                      # class D heat per channel at the average listening level
all_d = 11 * d_ch
opt = 2 * g["heat_H"] + 9 * d_ch
v = {"alld": all_d, "opt": opt, "kall": g["kwh"](all_d), "kopt": g["kwh"](opt), "hh2": 2 * g["heat_H"], "dch": d_ch, "ph": g["P_H"]}
LANG8 = ["ja", "en", "en-GB", "ru", "uk", "de", "it", "fr"]
NAME8 = {"ja": "日本語", "en": "English (US)", "en-GB": "English (UK)", "ru": "Русский", "uk": "Українська", "de": "Deutsch", "it": "Italiano", "fr": "Français"}
T = {
 "title": {
  "ja": "SV-VER5 — サラウンド AV アンプを VER7 に合わせた版", "en": "SV-VER5 — the surround AV amplifier aligned with VER7", "en-GB": "SV-VER5 — the surround AV amplifier aligned with VER7",
  "ru": "SV-VER5 — AV-усилитель объёмного звука, согласованный с VER7", "uk": "SV-VER5 — AV-підсилювач об'ємного звучання, узгоджений із VER7", "de": "SV-VER5 — der Surround-AV-Verstärker, an VER7 angeglichen",
  "it": "SV-VER5 — l'amplificatore AV surround allineato a VER7", "fr": "SV-VER5 — l'amplificateur AV surround aligné sur VER7"},
 "base": {
  "ja": "SV-VER4 (全 11ch アナログ入力クラスD、外付けリニア DC 電源・R コア) を、VER7 の考え方に合わせました。全 11ch は VER7 の改良クラスD アナログ版 (ゾベルで 16Ω のピークを 7.6dB → 0.7dB)。ホームシアターの映画は 小音量から大音量まであり、全 11ch をクラスD にすると 平均 約 85dB でもアンプ全体の発熱は約 %(alld).0fW、年 約 %(kall).0fkWh で済みます。",
  "en": "SV-VER4 (all 11 channels in analog-input Class D, external linear DC supply with R-core) is aligned with the VER7 approach. All 11 channels use the improved VER7 analog Class D (a Zobel cuts the 16 ohm peak from 7.6 dB to 0.7 dB). Films run from quiet to loud, and with all 11 channels in Class D the whole amplifier dissipates only about %(alld).0f W at about 85 dB average, about %(kall).0f kWh a year.",
  "en-GB": "SV-VER4 (all 11 channels in analogue-input Class D, external linear DC supply with R-core) is aligned with the VER7 approach. All 11 channels use the improved VER7 analogue Class D (a Zobel cuts the 16 ohm peak from 7.6 dB to 0.7 dB). Films run from quiet to loud, and with all 11 channels in Class D the whole amplifier dissipates only about %(alld).0f W at about 85 dB average, about %(kall).0f kWh a year.",
  "ru": "SV-VER4 (все 11 каналов класса D с аналоговым входом, внешний линейный блок питания с R-сердечником) согласован с подходом VER7. Все 11 каналов используют улучшенный аналоговый класс D из VER7 (цепь Цобеля снижает пик АЧХ на нагрузке 16 Ом с 7,6 дБ до 0,7 дБ). Фильмы идут от тихих сцен до громких, и при классе D во всех 11 каналах весь усилитель рассеивает лишь около %(alld).0f Вт при среднем уровне около 85 дБ, около %(kall).0f кВт·ч в год.",
  "uk": "SV-VER4 (усі 11 каналів класу D з аналоговим входом, зовнішній лінійний блок живлення з R-осердям) узгоджено з підходом VER7. Усі 11 каналів виконано за схемою покращеного аналогового класу D із VER7 (ланцюг Цобеля знижує пік на 16 Ом із 7,6 дБ до 0,7 дБ). Фільми містять і тихі, і гучні сцени, і за класу D в усіх 11 каналах весь підсилювач виділяє лише близько %(alld).0f Вт за середнього рівня близько 85 дБ, близько %(kall).0f кВт·год на рік.",
  "de": "SV-VER4 (alle 11 Kanäle Klasse D mit Analogeingang, externes lineares Netzteil mit R-Kern) wurde an den Ansatz von VER7 angeglichen. Alle 11 Kanäle verwenden den verbesserten analogen Klasse-D-Verstärker von VER7 (ein Zobel senkt die Spitze an 16 Ω von 7,6 dB auf 0,7 dB). Filme reichen von leise bis laut; mit Klasse D in allen 11 Kanälen gibt der gesamte Verstärker bei etwa 85 dB im Mittel nur etwa %(alld).0f W ab, etwa %(kall).0f kWh im Jahr.",
  "it": "SV-VER4 (tutti gli 11 canali in classe D con ingresso analogico, alimentatore lineare esterno con nucleo R) è allineato all'approccio di VER7. Tutti gli 11 canali usano la classe D analogica migliorata di VER7 (uno Zobel riduce il picco su 16 ohm da 7,6 dB a 0,7 dB). I film spaziano dai volumi bassi a quelli alti e con la classe D su tutti gli 11 canali l'intero amplificatore dissipa solo circa %(alld).0f W a circa 85 dB di media, circa %(kall).0f kWh all'anno.",
  "fr": "SV-VER4 (11 canaux en classe D à entrée analogique, alimentation linéaire externe à noyau R) est aligné sur l'approche de VER7. Les 11 canaux utilisent la classe D analogique améliorée de VER7 (un réseau de Zobel ramène le pic sous 16 ohms de 7,6 dB à 0,7 dB). Les films vont du faible au fort volume et, avec la classe D sur les 11 canaux, tout l'amplificateur ne dissipe qu'environ %(alld).0f W à environ 85 dB de moyenne, environ %(kall).0f kWh par an."},
 "opt": {
  "ja": "オプション (フロント L/R だけ VER7 の A級+AB級): 9W までは A級、超えると自動で AB級 (最大 100W)。2ch のアイドル発熱は %(hh2).0fW、他の 9ch はクラスD のまま、全体の平均発熱は約 %(opt).0fW、年 約 %(kopt).0fkWh (全 D の約 7 倍)。ステレオ音楽の音質を重視する人向けで、発熱とファンの音が増えるため、通常はクラスD 全チャンネルを推奨します。",
  "en": "Option (only the front L/R in the VER7 Class A + AB): Class A up to 9 W, automatically Class AB above (up to 100 W). The two channels idle at %(hh2).0f W; the other nine stay in Class D, and the average heat of the whole amplifier is about %(opt).0f W, about %(kopt).0f kWh a year (about seven times all-Class-D). It is for people who value stereo-music sound; because it adds heat and fan noise, all-Class-D is the normal recommendation.",
  "en-GB": "Option (only the front L/R in the VER7 Class A + AB): Class A up to 9 W, automatically Class AB above (up to 100 W). The two channels idle at %(hh2).0f W; the other nine stay in Class D, and the average heat of the whole amplifier is about %(opt).0f W, about %(kopt).0f kWh a year (about seven times all-Class-D). It is for people who value the sound of stereo music; because it adds heat and fan noise, all-Class-D is the normal recommendation.",
  "ru": "Опция (только фронтальные L/R в VER7 класса A + AB): класс A до 9 Вт, выше автоматически класс AB (до 100 Вт). Два канала в покое выделяют %(hh2).0f Вт; остальные девять остаются в классе D, среднее тепловыделение всего усилителя около %(opt).0f Вт, около %(kopt).0f кВт·ч в год (примерно в семь раз больше, чем при классе D везде). Для тех, кто ценит звук стереомузыки; из-за тепла и шума вентилятора обычно рекомендуется класс D во всех каналах.",
  "uk": "Опція (лише фронтальні L/R у VER7 класу A + AB): клас A до 9 Вт, вище автоматично клас AB (до 100 Вт). Два канали в спокої виділяють %(hh2).0f Вт; решта дев'ять залишаються в класі D, середнє тепловиділення всього підсилювача близько %(opt).0f Вт, близько %(kopt).0f кВт·год на рік (приблизно у сім разів більше, ніж за класу D скрізь). Для тих, хто цінує звук стереомузики; через тепло та шум вентилятора зазвичай рекомендується клас D в усіх каналах.",
  "de": "Option (nur Front L/R im VER7-Klasse-A-plus-AB): Klasse A bis 9 W, darüber automatisch Klasse AB (bis 100 W). Die zwei Kanäle ziehen im Leerlauf %(hh2).0f W; die übrigen neun bleiben in Klasse D, die mittlere Wärme des ganzen Verstärkers beträgt etwa %(opt).0f W, etwa %(kopt).0f kWh im Jahr (etwa das Siebenfache von reinem Klasse D). Für alle, denen der Klang von Stereomusik wichtig ist; wegen Wärme und Lüftergeräusch wird normalerweise durchgehend Klasse D empfohlen.",
  "it": "Opzione (solo i frontali L/R nella classe A + AB di VER7): classe A fino a 9 W, sopra passa automaticamente in classe AB (fino a 100 W). I due canali a riposo dissipano %(hh2).0f W; gli altri nove restano in classe D, il calore medio dell'intero amplificatore è di circa %(opt).0f W, circa %(kopt).0f kWh all'anno (circa sette volte la sola classe D). È per chi apprezza il suono della musica stereo; poiché aggiunge calore e rumore della ventola, di norma si consiglia la classe D su tutti i canali.",
  "fr": "Option (seulement les avant L/R dans la classe A + AB de VER7) : classe A jusqu'à 9 W, puis classe AB automatiquement au-delà (jusqu'à 100 W). Les deux canaux dissipent %(hh2).0f W au repos ; les neuf autres restent en classe D, la chaleur moyenne de tout l'amplificateur est d'environ %(opt).0f W, environ %(kopt).0f kWh par an (environ sept fois la classe D seule). Elle s'adresse à ceux qui apprécient le son de la musique stéréo ; comme elle ajoute de la chaleur et du bruit de ventilateur, la classe D sur tous les canaux est la recommandation normale."},
 "rest": {
  "ja": "共通 (VER7 と同じ): 配線は入力→出力へ一方向 約 40mm、グランド面、0.1µF は 2mm 以内、0.1% 薄膜・C0G/フィルム、DC ケーブル 6mm² 0.8m、電解 63V・別筐体 (約 52 年)。電源はパワー段が非安定の大容量コンデンサ、アナログ・クロックは低雑音リニア。IMAX Enhanced・Dolby・DTS の認証は未取得、4DX 風の触覚出力 2ch は SV-VER1 のまま。未実施: 実機測定・HDMI 認証・聴感評価。",
  "en": "Common (as in VER7): one-way signal flow of about 40 mm, a ground plane, 0.1 uF within 2 mm, 0.1% thin-film and C0G / film parts, a 6 mm2 0.8 m DC cable, 63 V electrolytics in a separate case (about 52 years). The power-stage rails are unregulated large capacitor banks; analog and clock rails are low-noise linear. IMAX Enhanced, Dolby and DTS certification is not obtained, and the two 4DX-style tactile outputs are as in SV-VER1. Not done: bench measurements, HDMI certification, listening tests.",
  "en-GB": "Common (as in VER7): one-way signal flow of about 40 mm, an earth plane, 0.1 uF within 2 mm, 0.1% thin-film and C0G / film parts, a 6 mm2 0.8 m DC cable, 63 V electrolytics in a separate case (about 52 years). The power-stage rails are unregulated large capacitor banks; analogue and clock rails are low-noise linear. IMAX Enhanced, Dolby and DTS certification has not been obtained, and the two 4DX-style tactile outputs are as in SV-VER1. Not done: bench measurements, HDMI certification, listening tests.",
  "ru": "Общее (как в VER7): сигнал идёт в одном направлении по трассе около 40 мм, земляной полигон, блокировочные конденсаторы 0,1 мкФ в пределах 2 мм, тонкоплёночные резисторы 0,1 % и конденсаторы C0G / плёночные, кабель постоянного тока 6 мм² длиной 0,8 м, электролитические конденсаторы на 63 В в отдельном корпусе (около 52 лет). Шины питания выходного каскада — нестабилизированные, с батареями больших конденсаторов; питание аналоговой части и тактового генератора — малошумящее линейное. Сертификация IMAX Enhanced, Dolby и DTS не получена, два тактильных выхода в стиле 4DX — как в SV-VER1. Не выполнено: измерения на образце, сертификация HDMI, прослушивание.",
  "uk": "Спільне (як у VER7): тракт сигналу односпрямований, завдовжки близько 40 мм, земляна площина, конденсатори 0,1 мкФ не далі ніж 2 мм від виводів, тонкоплівкові резистори 0,1 % і конденсатори C0G / плівкові, кабель постійного струму 6 мм² завдовжки 0,8 м, електролітичні конденсатори на 63 В в окремому корпусі (близько 52 років). Шини силового каскаду — нестабілізовані батареї великих конденсаторів; аналогова частина та тактовий генератор живляться від малошумних лінійних стабілізаторів. Сертифікацію IMAX Enhanced, Dolby і DTS не отримано, два тактильні виходи в стилі 4DX залишено такими ж, як у SV-VER1. Не виконано: вимірювання на реальному зразку, сертифікація HDMI, прослуховування.",
  "de": "Gemeinsam (wie in VER7): Signalfluss in nur einer Richtung auf etwa 40 mm, Massefläche, 0,1 µF innerhalb von 2 mm vom Bauteil, 0,1-%-Dünnschicht- und C0G-/Folienbauteile, DC-Kabel 6 mm² bei 0,8 m, 63-V-Elektrolytkondensatoren in einem getrennten Gehäuse (etwa 52 Jahre). Die Endstufen-Versorgungsschienen werden aus ungeregelten, großen Kondensatorbänken gespeist; Analogteil und Takt werden rauscharm linear versorgt. Eine Zertifizierung für IMAX Enhanced, Dolby und DTS liegt nicht vor; die zwei 4DX-artigen Haptikausgänge entsprechen SV-VER1. Nicht durchgeführt: Messungen, HDMI-Zertifizierung, Hörtests.",
  "it": "Comune (come in VER7): flusso del segnale in un solo verso per circa 40 mm, piano di massa, 0,1 µF entro 2 mm, componenti a film sottile 0,1% e C0G / a film, cavo di alimentazione in c.c. da 6 mm², lungo 0,8 m, condensatori elettrolitici da 63 V in un contenitore separato (circa 52 anni). Le linee di alimentazione dello stadio di potenza sono non stabilizzate, con grandi banchi di condensatori; le alimentazioni dell'analogico e del clock sono lineari a basso rumore. La certificazione IMAX Enhanced, Dolby e DTS non è stata ottenuta e le due uscite tattili in stile 4DX sono come in SV-VER1. Non eseguito: misure, certificazione HDMI, prove d'ascolto.",
  "fr": "Commun (comme VER7) : signal circulant dans un seul sens sur environ 40 mm, plan de masse, 0,1 µF à moins de 2 mm, composants à couche mince 0,1 % et C0G / à film, câble d'alimentation continue de 6 mm², long de 0,8 m, électrolytiques de 63 V dans un boîtier séparé (environ 52 ans). Les rails de l'étage de puissance sont des batteries de condensateurs non régulées ; les alimentations analogiques et d'horloge sont linéaires à faible bruit. La certification IMAX Enhanced, Dolby et DTS n'est pas obtenue et les deux sorties tactiles de type 4DX restent identiques à celles de SV-VER1. Non réalisé : mesures, certification HDMI, écoute."},
}
import re as _re
def _dec(L, t):
    return _re.sub(r"(?<=\d)\.(?=\d)", ",", t) if L in ("ru", "uk", "de", "it", "fr") else t
OUT = SD + r"\sv5out"
os.makedirs(OUT, exist_ok=True)
md = ["# SV-VER5 — %s\n" % T["title"]["ja"], "Figures: `surround_v5_balanced.jpg`, `surround_v5_unbalanced.jpg`, `manual-sv5.jpg` / `manual-sv5.pdf` (8-language manual), `surround-av-amp-v5.pdf`. Reference design, Python calculations (see VER7 and SV-VER2 / SV-VER4), not bench measurements.\n"]
for L in LANG8:
    md.append("## %s\n" % NAME8[L]); md.append("**%s**\n" % T["title"][L])
    for k in ("base", "rest"):
        md.append("- " + (T[k][L] % v if "%(" in T[k][L] else T[k][L]))
    md.append("")
open(OUT + r"\README.md", "w", encoding="utf-8").write("\n".join(md))
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
    out.append(cur.rstrip()); return out
blocks = []
for L in LANG8:
    lines = [(NAME8[L] + " — SV-VER5", HD)]
    for k in ("title", "base", "rest"):
        t = T[k][L] % v if "%(" in T[k][L] else T[k][L]
        for ln in wrap(t, REG, colw): lines.append((ln, REG))
        lines.append(("", REG))
    blocks.append(lines)
hh = lambda lines: sum(int(f.size * 1.45) for _, f in lines) + 40
rows = [(blocks[i], blocks[i + 1]) for i in range(0, 8, 2)]
H = 140 + sum(max(hh(a), hh(b)) for a, b in rows) + pad
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)
d.text((pad, 40), "SV-VER5 説明書 / Manual — 日本語 · English (US/UK) · Русский · Українська · Deutsch · Italiano · Français", font=BIG, fill=(20, 30, 60))
y = 140
for a, b in rows:
    for col, lines in enumerate((a, b)):
        x, yy = pad + col * (colw + pad), y
        for t, f in lines:
            d.text((x, yy), t, font=f, fill=(20, 30, 60) if f is HD else (40, 40, 40)); yy += int(f.size * 1.45)
    y += max(hh(a), hh(b))
img.save(OUT + r"\manual-sv5.jpg", "JPEG", quality=90, dpi=(300, 300))
img.save(OUT + r"\manual-sv5.pdf", resolution=300)
print(img.size, {k: round(x, 1) for k, x in v.items()})
