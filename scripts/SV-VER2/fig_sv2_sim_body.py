import math, textwrap
exec(open(r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad\plot_helpers.py", encoding="utf-8").read())
GR, BL, RD, PU, OR = (25, 115, 60), (30, 70, 180), (190, 30, 30), (120, 60, 160), (200, 120, 20)
V = 45.0


def pd_ab(rl, frac=None):
    if frac is None:
        return 2 * V * V / (math.pi ** 2 * rl)
    po = frac * V * V / (2 * rl)
    vo = math.sqrt(2 * po * rl)
    return 2 * V * vo / (math.pi * rl) - vo * vo / (2 * rl)


def pd_d(rl, frac=None, eff=0.9):
    po = (V * V / (2 * rl)) * (1 if frac is None else frac)
    return po * (1 / eff - 1)


mixed = lambda rl, f=None: 3 * pd_ab(rl, f) + 8 * pd_d(rl, f)
alld = lambda rl, f=None: 11 * pd_d(rl, f)
a4, m4, d4, d8 = 11 * pd_ab(4), mixed(4), alld(4), alld(8)
fa, fm, fd = 11 * pd_ab(8, 1 / 8), mixed(8, 1 / 8), alld(8, 1 / 8)
# idle: AB bias 100 mA x 90 V per channel, class D idle about 1.5 W per channel
idle_ab, idle_d = 11 * 0.1 * 90, 11 * 1.5
L_, C_ = 22e-6, 0.47e-6
f0 = 1 / (2 * math.pi * math.sqrt(L_ * C_))


def resp(f, rl, zobel=False):
    w = 2 * math.pi * f
    zl = rl
    h = 1 / complex(1 - w * w * L_ * C_, w * L_ / zl)
    if zobel:      # 1 ohm... series RC damping across the output: adds damping, model as extra load of 10 ohm
        zl = 1 / (1 / rl + 1 / 10.0)
        h = 1 / complex(1 - w * w * L_ * C_, w * L_ / zl)
    return 20 * math.log10(abs(h))


pk16 = max(resp(f, 16) for f in range(1000, 200001, 500))
pk16z = max(resp(f, 16, True) for f in range(1000, 200001, 500))
d20_4 = resp(20000, 4)
d20_8 = resp(20000, 8)
text(3, 127, "SV-VER2 (アナログ入力のクラス D 全 11ch) TEST / DEBUG  Surround AV: all-Class-D analog-input amplifier", 2.3, INK, "la", True)
text(3, 123.6, "Python による設計計算 (SPICE・実機測定ではありません)。仮定: レール ±45V、D 級効率 90%、映画の平均 = 最大出力の 1/8、LC フィルタ 22µH / 0.47µF。", 1.3, GRY)
mx, my = plot(8, 72, 62, 108, 4, 9, 0, 1200, False, "① 11ch の最悪発熱 (W)  Worst-case heat", "負荷 (Ω)", "W")
curve(mx, my, [(r / 2, 11 * pd_ab(r / 2)) for r in range(8, 19)], RD)
curve(mx, my, [(r / 2, mixed(r / 2)) for r in range(8, 19)], OR)
curve(mx, my, [(r / 2, alld(r / 2)) for r in range(8, 19)], GR)
legend(12, 106, [("全 AB: 4Ωで %.0fW" % a4, RD, False), ("SV-VER1 混成: %.0fW" % m4, OR, False), ("SV-VER2 全クラス D: %.0fW" % d4, GR, False)])
mx, my = plot(70, 72, 124, 108, 1, 200, -12, 12, True, "② 出力 LC フィルタの応答 (22µH/0.47µF)  Output filter", "周波数 (kHz)", "dB")
for rl, col in ((4, BL), (8, GR), (16, OR)):
    curve(mx, my, [(f / 1000.0, max(-12, min(12, resp(f, rl)))) for f in range(1000, 200001, 1000)], col)
legend(76, 106, [("4Ω", BL, False), ("8Ω", GR, False), ("16Ω (ピーク %.1fdB → ダンピングで %.1fdB)" % (pk16, pk16z), OR, False)])
mx, my = plot(132, 72, 192, 108, 0, 250, 0, 100, False, "③ 効率 (出力 W、4Ω)  Efficiency vs power", "出力 (W)", "%")
curve(mx, my, [(p, 100.0 * p / (p + pd_ab(4, p / 253.0))) for p in range(2, 251, 4)], RD)
curve(mx, my, [(p, 100.0 * p / (p + pd_d(4, p / 253.0) + 1.5)) for p in range(2, 251, 4)], GR)
legend(138, 106, [("Class AB", RD, False), ("Class D (アナログ入力・Eigentakt 型)", GR, False)])
rows = [
    ("ROUND 1 (発熱): SV-VER1 の混成は最悪 %.0fW だったが、全 11ch をクラス D にすると %.0fW (4Ω)、%.0fW (8Ω)。映画の平均は %.0fW (混成 %.0fW・全 AB %.0fW)、待機時は 約 %.0fW (全 AB は %.0fW)。→ 発熱が大きく減る。" % (m4, d4, d8, fd, fm, fa, idle_d, idle_ab),
     "ROUND 1 (heat): the SV-VER1 mix was %.0f W worst case; with all 11 channels in Class D it is %.0f W at 4 ohm and %.0f W at 8 ohm. The film average is %.0f W (mix %.0f W, all-AB %.0f W) and idle is about %.0f W (all-AB %.0f W). Heat drops sharply." % (m4, d4, d8, fd, fm, fa, idle_d, idle_ab),
     "RUNDE 1 (Wärme): Die Mischung von SV-VER1 hatte im ungünstigsten Fall %.0f W; mit allen 11 Kanälen in Klasse D sind es %.0f W an 4 Ω und %.0f W an 8 Ω. Filmdurchschnitt %.0f W (Mischung %.0f W, alle AB %.0f W), Leerlauf etwa %.0f W (alle AB %.0f W). Die Wärme sinkt deutlich." % (m4, d4, d8, fd, fm, fa, idle_d, idle_ab),
     "РАУНД 1 (нагрев): смешанный вариант SV-VER1 давал %.0f Вт в худшем случае; при классе D во всех 11 каналах — %.0f Вт на 4 Ом и %.0f Вт на 8 Ом. Среднее для фильма %.0f Вт (смешанный %.0f Вт, все AB %.0f Вт), в покое около %.0f Вт (все AB %.0f Вт). Нагрев заметно снижается." % (m4, d4, d8, fd, fm, fa, idle_d, idle_ab)),
    ("ROUND 2 (音質: 出力フィルタ): LC フィルタの共振は %.0fkHz。4Ω では 20kHz で %.1fdB、8Ω では %.1fdB と平坦だが、16Ω では ピークが %.1fdB 出る。→ 問題あり: 負荷が軽いとき高域が持ち上がる。対策: 出力に RC ダンピング (ゾベル) を足すと %.1fdB に収まる (計算)。" % (f0 / 1000, d20_4, d20_8, pk16, pk16z),
     "ROUND 2 (sound, output filter): the LC filter resonates at %.0f kHz. It is flat at 20 kHz (%.1f dB at 4 ohm, %.1f dB at 8 ohm) but peaks by %.1f dB into 16 ohm. Problem: the treble lifts with a light load. Fix: an RC damper (Zobel) at the output keeps it to %.1f dB (calculated)." % (f0 / 1000, d20_4, d20_8, pk16, pk16z),
     "RUNDE 2 (Klang, Ausgangsfilter): Der LC-Filter schwingt bei %.0f kHz. Bei 20 kHz ist er flach (%.1f dB an 4 Ω, %.1f dB an 8 Ω), hebt an 16 Ω aber um %.1f dB an. Problem: Die Höhen steigen bei leichter Last. Abhilfe: ein RC-Dämpfungsglied (Zobel) am Ausgang hält es bei %.1f dB (berechnet)." % (f0 / 1000, d20_4, d20_8, pk16, pk16z),
     "РАУНД 2 (звук, выходной фильтр): LC-фильтр резонирует на %.0f кГц. На 20 кГц он ровный (%.1f дБ на 4 Ом, %.1f дБ на 8 Ом), но на 16 Ом даёт подъём %.1f дБ. Проблема: при лёгкой нагрузке поднимаются верха. Решение: RC-демпфер (цепь Цобеля) на выходе удерживает его в %.1f дБ (расчёт)." % (f0 / 1000, d20_4, d20_8, pk16, pk16z)),
    ("ROUND 3 (アナログ入力の利点): 入力をアナログのまま受ける Class D (Eigentakt 型のように 自己発振+負帰還) は、デジタル PWM 変換とそのクロックの影響を受けず、DAC の後はアナログのままです。電源の変動にも強い (PSRR は負帰還で確保、数値は仮定)。出力段は 500kHz 前後でスイッチ、各ch に実装。「必ず Class D のほうが音がよい」とは言えず、フィルタ・電源・配線次第 (上の 2 回目の対策が必要)。",
     "ROUND 3 (benefit of analog input): a Class D amplifier that takes the signal as analog (self-oscillating with feedback, like the Eigentakt type) does not depend on a digital PWM stage and its clock, and after the DAC the path stays analog. The feedback also helps against supply variation (values assumed). It switches at about 500 kHz, one module per channel. It is not automatically better sounding; the filter, supply and wiring decide (round 2 is needed).",
     "RUNDE 3 (Vorteil des Analogeingangs): Ein Klasse-D-Verstärker mit Analogeingang (selbstschwingend mit Gegenkopplung, wie der Eigentakt-Typ) hängt nicht von einer digitalen PWM-Stufe und deren Takt ab, nach dem DAC bleibt der Weg analog. Die Gegenkopplung hilft auch gegen Versorgungsschwankungen (Werte angenommen). Er schaltet bei etwa 500 kHz, ein Modul je Kanal. Er klingt nicht automatisch besser; Filter, Versorgung und Verdrahtung entscheiden (Runde 2 ist nötig).",
     "РАУНД 3 (преимущество аналогового входа): усилитель класса D с аналоговым входом (самовозбуждающийся с обратной связью, как тип Eigentakt) не зависит от цифрового ШИМ-каскада и его тактирования, после ЦАП тракт остаётся аналоговым. Обратная связь помогает и при колебаниях питания (значения приняты). Переключение около 500 кГц, один модуль на канал. Он не всегда звучит лучше сам по себе; решают фильтр, питание и разводка (нужен раунд 2)."),
    ("ROUND 4 (配線・耐久): 配線は SV-VER1 と同じ (チャンネルごとに 40mm・隣と 25mm)。クラス D は ヒートシンクが小さくなり 温度が下がるため 電解コンデンサも長持ち。スイッチング ノイズ (500kHz) がアナログに入らないよう、パワー段は 筐体の外側に置き、DAC / ボリュームと シールド板で仕切る。ファンは ほぼ回らない (静音)。",
     "ROUND 4 (wiring, durability): the wiring is the same as SV-VER1 (40 mm per channel, 25 mm to the neighbour). Class D needs a smaller heatsink and runs cooler, so the capacitors last longer. To keep the 500 kHz switching noise out of the analog part, the power stage sits at the outside of the chassis behind a shield plate from the DAC and volume. The fan hardly runs (quiet).",
     "RUNDE 4 (Verdrahtung, Haltbarkeit): Die Verdrahtung ist wie bei SV-VER1 (40 mm je Kanal, 25 mm zum Nachbarn). Klasse D braucht einen kleineren Kühlkörper und bleibt kühler, die Kondensatoren halten länger. Damit das 500-kHz-Schaltrauschen nicht in den Analogteil gelangt, sitzt die Endstufe außen im Gehäuse hinter einer Schirmwand zu DAC und Lautstärkeregler. Der Lüfter läuft kaum (leise).",
     "РАУНД 4 (разводка, долговечность): разводка как в SV-VER1 (40 мм на канал, 25 мм до соседа). Классу D нужен меньший радиатор, он холоднее, конденсаторы служат дольше. Чтобы шум переключения 500 кГц не попадал в аналоговую часть, силовой каскад стоит снаружи корпуса за экраном от ЦАП и регулятора громкости. Вентилятор почти не вращается (тихо)."),
    ("未実施: 実機測定 (THD・雑音・出力インピーダンス・EMI)、HDMI の認証、IMAX Enhanced / Dolby / DTS の認証、過渡応答。数値は設計用の計算と仮定。",
     "Not done: bench measurements (THD, noise, output impedance, EMI), HDMI compliance, IMAX Enhanced / Dolby / DTS certification, transient response. The numbers are design calculations and assumptions.",
     "Nicht durchgeführt: Messungen (THD, Rauschen, Ausgangsimpedanz, EMV), HDMI-Konformität, IMAX-Enhanced-/Dolby-/DTS-Zertifizierung, Einschwingverhalten. Die Werte sind Entwurfsrechnungen und Annahmen.",
     "Не выполнено: измерения (КНИ, шум, выходное сопротивление, ЭМС), проверка HDMI, сертификация IMAX Enhanced / Dolby / DTS, переходные процессы. Значения — проектные расчёты и допущения."),
]
y = 64
text(6, 66.5, "TEST / DEBUG の記録 (4 回)  Log", 1.6, INK, "la", True)
for blk in rows:
    for i, t in enumerate(blk):
        for ln in textwrap.wrap(t, 175 if i else 90):
            text(6, y, ln, 0.8, INK if i == 0 else GRY, "la")
            y -= 1.3
    y -= 0.5
img = img.resize((W * S // 2, H * S // 2), Image.LANCZOS)
out = r"C:\Users\noruk\AppData\Local\Temp\claude\F--runo\58accee1-c937-49c6-954f-77e9dc39b2c8\scratchpad\surround_v2_sim.jpg"
img.save(out, "JPEG", quality=92, dpi=(300, 300))
print(out, round(a4), round(m4), round(d4), round(d8), round(fd), round(fm), round(fa), round(f0), round(d20_4, 2), round(d20_8, 2), round(pk16, 1), round(pk16z, 1), round(y, 1))
