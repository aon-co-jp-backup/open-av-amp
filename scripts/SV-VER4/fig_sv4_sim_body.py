import math, textwrap
exec(open(r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad\plot_helpers.py", encoding="utf-8").read())
GR, BL, RD, PU, OR = (25, 115, 60), (30, 70, 180), (190, 30, 30), (120, 60, 160), (200, 120, 20)
V, N, PO, EFF = 45.0, 11, 100.0, 0.9
Pin = lambda frac: N * PO * frac / EFF            # input power at a fraction of full output
Pfull = Pin(1.0)
Pfilm = Pin(1 / 8.0)
Idc = lambda frac: Pin(frac) / (2 * V)            # current drawn from each rail pair (approx)
reg_loss = lambda frac, head: Idc(frac) * 2 * head  # a regulator on both rails, headroom per rail
C_BANK = 4 * 22000e-6
ripple = lambda frac, c: Idc(frac) / (2 * 100.0 * c)
text(3, 127, "SV-VER4 TEST / DEBUG: 外付けリニア電源・R コア・筐体  Linear supply, R-core, chassis", 2.3, INK, "la", True)
text(3, 123.6, "Python による設計計算 (SPICE・実機測定ではありません)。仮定: 11ch × 100W/8Ω、レール ±45V、D 級効率 90%、映画の平均 = 出力の 1/8、商用 100V 15A。", 1.3, GRY)
mx, my = plot(8, 72, 62, 108, 0, 100, 0, 300, False, "① パワー段のレールを定電圧化した場合の損失 (W)  Regulator loss", "出力 (最大の %)", "W")
curve(mx, my, [(p, reg_loss(p / 100.0, 5.0)) for p in range(1, 101)], RD)
curve(mx, my, [(p, reg_loss(p / 100.0, 0.0)) for p in range(1, 101)], GR)
legend(12, 106, [("定電圧 (余裕 5V): 最大で %.0fW" % reg_loss(1, 5.0), RD, False), ("非安定 (大容量コンデンサのみ): 0W", GR, False)])
mx, my = plot(70, 72, 124, 108, 30, 200, 0, 1.0, False, "② パワーレールのリップル/垂れ (V)  Ripple / sag vs capacitance", "容量 (mF、レール 1 組)", "V")
curve(mx, my, [(c, ripple(1 / 8.0, c / 1000.0)) for c in range(30, 201, 2)], BL)
curve(mx, my, [(c, ripple(1 / 3.0, c / 1000.0)) for c in range(30, 201, 2)], OR)
legend(76, 106, [("映画の平均 (1/8 出力)", BL, False), ("持続 1/3 出力", OR, False)])
text(mx(88), my(ripple(1 / 8.0, 0.088)) + 2.4, "88mF: %.2f V" % ripple(1 / 8.0, 0.088), 1.0, GR, "mm", True)
mx, my = plot(132, 72, 192, 108, 0, 100, 0, 1600, False, "③ 必要な VA と商用 100V 15A の限界  Mains VA needed", "出力 (最大の %)", "VA")
curve(mx, my, [(p, Pin(p / 100.0) * 1.15) for p in range(1, 101)], PU)
line([(mx(0), my(1500)), (mx(100), my(1500))], RD, int(LW * .6))
text(160, my(1500) - 2.2, "1500 VA (100V 15A)", 1.0, RD, "mm")
text(mx(33), my(Pin(1 / 3.0) * 1.15) + 2.6, "1/3: %.0f VA" % (Pin(1 / 3.0) * 1.15), 1.0, GR, "mm", True)
l1 = reg_loss(1, 5.0)
rows = [
    ("ROUND 1 (電源): SV-VER3 は 5 バンクすべてを定電圧にしていた。パワー段 (±45V) まで定電圧にすると、余裕 5V でも最大出力時に %.0fW、映画の平均でも %.0fW を電源が無駄に熱にする。→ 問題あり。" % (l1, reg_loss(1 / 8.0, 5.0)),
     "ROUND 1 (supply): SV-VER3 regulated all five banks. Regulating the power-stage rails (+-45 V) as well wastes %.0f W as heat at full output even with 5 V of headroom, and %.0f W for the film average. Problem." % (l1, reg_loss(1 / 8.0, 5.0)),
     "RUNDE 1 (Versorgung): SV-VER3 regelte alle fünf Bänke. Auch die Endstufenschienen (±45 V) zu regeln erzeugt selbst mit 5 V Reserve bei Vollaussteuerung %.0f W Verlustwärme, im Filmdurchschnitt %.0f W. Problem." % (l1, reg_loss(1 / 8.0, 5.0)),
     "РАУНД 1 (питание): в SV-VER3 были стабилизированы все пять банков. Стабилизация и силовых шин (±45 В) даёт даже при запасе 5 В потери %.0f Вт при полной мощности и %.0f Вт в среднем для фильма. Проблема." % (l1, reg_loss(1 / 8.0, 5.0))),
    ("ROUND 2 (対策): パワー段のレールは 非安定の 大容量コンデンサ (4 × 22,000µF、電解は別筐体) にし、アナログ ±15V・デジタル・DAC・クロックだけを 低雑音のリニア定電圧にする (損失は 約 数 W)。クラス D は 負帰還で 電源変動をある程度抑える。映画の平均でのレールの変動は %.2fV、持続 1/3 出力でも %.2fV (計算)。" % (ripple(1 / 8.0, C_BANK), ripple(1 / 3.0, C_BANK)),
     "ROUND 2 (fix): the power-stage rails become unregulated large capacitor banks (4 x 22,000 uF, in the separate case); only analog +-15 V, digital, DAC and clock get low-noise linear regulation (a few watts of loss). Class D feedback absorbs part of the supply variation. The rail ripple is %.2f V at the film average and %.2f V at a sustained 1/3 power (calculated)." % (ripple(1 / 8.0, C_BANK), ripple(1 / 3.0, C_BANK)),
     "RUNDE 2 (Abhilfe): Die Endstufenschienen werden ungeregelte große Kondensatorbänke (4 × 22.000 µF, im getrennten Gehäuse); nur analog ±15 V, Digital, DAC und Takt erhalten rauscharme Linearregelung (wenige Watt Verlust). Die Gegenkopplung der Klasse D fängt einen Teil der Versorgungsschwankung ab. Restwelligkeit %.2f V im Filmdurchschnitt und %.2f V bei dauerhaft 1/3 Leistung (berechnet)." % (ripple(1 / 8.0, C_BANK), ripple(1 / 3.0, C_BANK)),
     "РАУНД 2 (решение): шины силового каскада — нестабилизированные батареи больших конденсаторов (4 × 22 000 мкФ, в отдельном корпусе); малошумящая линейная стабилизация только для аналоговых ±15 В, цифровой части, ЦАП и такта (потери несколько ватт). Обратная связь класса D частично гасит колебания питания. Пульсации %.2f В в среднем для фильма и %.2f В при длительных 1/3 мощности (расчёт)." % (ripple(1 / 8.0, C_BANK), ripple(1 / 3.0, C_BANK))),
    ("ROUND 3 (R コアの容量): 全 11ch が最大出力で鳴り続けると 約 %.0fVA で、商用 100V 15A (1500VA) に近い。実際の映画・音楽は ピークだけ大きいので、R コアは 持続 1/3 出力 (約 %.0fVA) を連続で出せる 1.0kVA 級にし、ピークは コンデンサ (88mF で 10ms のピーク %.1fV の垂れ) で賄う。" % (Pfull * 1.15, Pin(1 / 3.0) * 1.15, Idc(1.0) * 0.01 / 0.088),
     "ROUND 3 (R-core size): all 11 channels at full output continuously would draw about %.0f VA, close to the 1500 VA of a 100 V 15 A mains. Real films and music are only briefly loud, so the R-core is a 1.0 kVA class that can deliver the sustained 1/3 power (about %.0f VA) and the capacitors supply the peaks (a 10 ms peak sags the 88 mF bank by %.1f V)." % (Pfull * 1.15, Pin(1 / 3.0) * 1.15, Idc(1.0) * 0.01 / 0.088),
     "RUNDE 3 (R-Kern-Größe): Alle 11 Kanäle dauerhaft bei Vollaussteuerung ziehen etwa %.0f VA, nahe den 1500 VA eines 100-V-15-A-Anschlusses. Filme und Musik sind nur kurz laut; der R-Kern ist daher ein 1,0-kVA-Typ für dauerhaft 1/3 Leistung (etwa %.0f VA), die Spitzen liefern die Kondensatoren (eine 10-ms-Spitze lässt die 88-mF-Bank um %.1f V einbrechen)." % (Pfull * 1.15, Pin(1 / 3.0) * 1.15, Idc(1.0) * 0.01 / 0.088),
     "РАУНД 3 (размер R-сердечника): все 11 каналов при полной мощности непрерывно потребляют около %.0f ВА, близко к 1500 ВА сети 100 В 15 А. Фильмы и музыка громки лишь кратковременно, поэтому R-сердечник класса 1,0 кВА держит длительные 1/3 мощности (около %.0f ВА), а пики обеспечивают конденсаторы (пик 10 мс просаживает батарею 88 мФ на %.1f В)." % (Pfull * 1.15, Pin(1 / 3.0) * 1.15, Idc(1.0) * 0.01 / 0.088)),
    ("ROUND 4 (筐体・端子): アルミ + 木のハイブリッドは 共振を抑える狙い。端子の金 / ロジウムめっきは 接触抵抗の安定のため。この 2 つは 机上の計算で 検証できない (測定が必要)。R コアの漏れ磁束は トロイダルと同程度以下とされる (一般的な目安、実測なし)。電解は 45°C 以下の別筐体で 約 73 年、他の耐久は SV-VER2 と同じ。",
     "ROUND 4 (chassis, terminals): the aluminium + wood hybrid aims to damp resonance and the gold or rhodium plating keeps the contact resistance stable. Neither can be verified by desk calculation (measurement is needed). The stray flux of an R-core is generally said to be equal to or below that of a toroid (a rule of thumb, not measured). Electrolytics in a separate case at 45 C or below last about 73 years; other durability items are as in SV-VER2.",
     "RUNDE 4 (Gehäuse, Klemmen): Das Aluminium-Holz-Hybrid soll Resonanzen dämpfen, die Gold- oder Rhodiumschicht hält den Übergangswiderstand stabil. Beides lässt sich nicht am Schreibtisch berechnen (Messung nötig). Das Streufeld eines R-Kerns gilt allgemein als gleich oder kleiner als das eines Ringkerns (Faustregel, nicht gemessen). Elektrolytkondensatoren im getrennten Gehäuse bei höchstens 45 °C halten etwa 73 Jahre; die übrige Haltbarkeit wie bei SV-VER2.",
     "РАУНД 4 (корпус, клеммы): гибрид алюминия и дерева призван гасить резонансы, золотое или родиевое покрытие стабилизирует переходное сопротивление. Ни то ни другое нельзя проверить расчётом (нужны измерения). Поле рассеяния R-сердечника принято считать равным или меньшим, чем у тороида (ориентир, не измерено). Электролиты в отдельном корпусе при 45 °C или ниже служат около 73 лет; остальная долговечность как в SV-VER2."),
    ("未実施: 実機測定 (リップル・THD・雑音・EMI)、過渡応答、筐体の共振測定、各社の認証。数値は設計用の計算と仮定。",
     "Not done: bench measurements (ripple, THD, noise, EMI), transient response, chassis resonance measurement, vendor certifications. The numbers are design calculations and assumptions.",
     "Nicht durchgeführt: Messungen (Restwelligkeit, THD, Rauschen, EMV), Einschwingverhalten, Resonanzmessung des Gehäuses, Zertifizierungen. Die Werte sind Entwurfsrechnungen und Annahmen.",
     "Не выполнено: измерения (пульсации, КНИ, шум, ЭМС), переходные процессы, измерение резонансов корпуса, сертификации. Значения — проектные расчёты и допущения."),
]
y = 64
text(6, 66.5, "TEST / DEBUG の記録 (4 回)  Log", 1.6, INK, "la", True)
for blk in rows:
    for i, t in enumerate(blk):
        for ln in textwrap.wrap(t, 190 if i else 100):
            text(6, y, ln, 0.8, INK if i == 0 else GRY, "la")
            y -= 1.22
    y -= 0.5
img = img.resize((W * S // 2, H * S // 2), Image.LANCZOS)
out = r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad\surround_v4_sim.jpg"
img.save(out, "JPEG", quality=92, dpi=(300, 300))
print(out, round(l1), round(reg_loss(1 / 8.0, 5.0)), round(ripple(1 / 8.0, C_BANK), 2), round(ripple(1 / 3.0, C_BANK), 2), round(Pfull * 1.15), round(Pin(1 / 3.0) * 1.15), round(Idc(1.0) * 0.01 / 0.088, 1), round(y, 1))
