import math
SDIR = r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad"
exec(open(SDIR + r"\plot_helpers.py", encoding="utf-8").read())
c = {}
exec(open(SDIR + r"\sv6_calc.py", encoding="utf-8").read().replace('if __name__ == "__main__":', 'if False:'), c)
GR, BL, RD, PU, OR = (25, 115, 60), (30, 70, 180), (190, 30, 30), (120, 60, 160), (200, 120, 20)
text(3, 127, "SV-VER6 TEST / DEBUG: Android・Wi-Fi・Bluetooth・LAN・ブラウザ  Android, Wi-Fi, Bluetooth, LAN and browser", 2.3, INK, "la", True)
text(3, 123.6, "Python による設計計算 (SPICE・実機測定ではありません)。仮定: ネットワークの実効速度、SoC 8W、デジタル側 合計 15W (5V 3A)。 Python design calculations with assumed throughputs and loads.", 1.2, GRY)
# 1) bit rates against the link capacities
mx, my = plot(8, 72, 62, 108, 0, 8, 0, 150, False, "① 転送する量 (Mbps) とリンクの実効速度  Bit rate needed vs link capacity", "", "Mbps")
for i, (n, r) in enumerate(c["RATES"]):
    d.rectangle([*P(mx(0.2 + i), my(r)), *P(mx(0.2 + i + 0.7), my(0))], fill=GR if r < 70 else (OR if r < 130 else RD))
    text(mx(0.55 + i), my(r) + 1.6, "%.0f" % r, 0.9, INK, "mm", True)
for n, cap in c["LINKS"]:
    line([(mx(0), my(min(cap, 150))), (mx(8), my(min(cap, 150)))], BL if cap > 100 else RD, int(LW * .5))
legend(12, 106, [("棒: 左から 音声2ch / 192k / Atmos / 1536k / DSD1024 / 4K / UHD BD", GR, False), ("線: Wi-Fi 2.4G 70 (赤) / 5G 450 以上 / LAN 940", RD, False)])
# 2) heat of the linear regulator for the digital rail
mx, my = plot(70, 72, 124, 108, 6, 13, 0, 24, False, "② デジタル側 5V 3A の線形レギュレータ損失 (W)  Regulator loss vs input voltage", "レギュレータの入力電圧 (V)", "W")
curve(mx, my, [(v / 10.0, c["loss_lin"](v / 10.0)) for v in range(60, 131)], RD)
text(mx(12), my(c["loss_lin"](12)) + 1.8, "12V: %.0fW" % c["loss_lin"](12), 1.0, RD, "mm", True)
text(mx(6.8), my(c["loss_lin"](6.8)) - 2.0, "6.8V 専用巻線: %.1fW" % c["loss_lin"](6.8), 1.0, GR, "lm", True)
# 3) junction temperature of the SoC
mx, my = plot(132, 72, 192, 108, 2, 16, 40, 170, False, "③ SoC の接合部温度 (°C) と放熱 (°C/W)  SoC junction temperature", "熱抵抗 (°C/W)", "°C")
curve(mx, my, [(th, c["tj"](th)) for th in range(2, 17)], PU)
line([(mx(2), my(105)), (mx(16), my(105))], RD, int(LW * .6))
text(mx(15.8), my(105) + 2.0, "目標上限 105°C", 1.0, RD, "rm")
text(mx(5), my(c["tj"](5)) - 2.5, "5°C/W: %.0f°C" % c["tj"](5), 1.0, GR, "mm", True)
text(6, 62, "結果 (全文は下の 8 言語の説明)  Results (full text in 8 languages below)", 1.5, INK, "la", True)
rows = ["TEST 1: 2.4GHz の Wi-Fi (実効 約 70Mbps) では PCM 1536k (約 98Mbps)・DSD1024 (約 90Mbps)・UHD BD 級 (128Mbps) が足りない → 5/6GHz か有線 LAN。",
        "TEST 2 [不具合]: デジタル側 15W を 12V から線形レギュレータにすると 約 21W の熱 → 専用の 6.8V 巻線 (外付けリニア電源) にして 約 5.4W。",
        "TEST 3: SoC 8W は 放熱 5°C/W 以下で 80°C、放熱なし (15°C/W) だと 160°C → ヒートシンクが必要。",
        "TEST 4 [注意]: Wi-Fi/Bluetooth は 無線モジュールを背面の端に、アナログ段から離してシールド。LAN は絶縁トランス (1.5kVrms) でグランドループを切る。"]
y = 59.5
for r_ in rows:
    text(6, y, r_, 1.05, INK, "la"); y -= 2.3
img = img.resize((W * S // 2, H * S // 2), Image.LANCZOS)
out = SDIR + r"\surround_v6_sim.jpg"
img.save(out, "JPEG", quality=92, dpi=(300, 300))
print(out, round(y, 1))
