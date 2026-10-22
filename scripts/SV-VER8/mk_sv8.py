import re
# 1) the figure
b = open("surround_v7_block_body.py", encoding="utf-8").read()
b = b.replace("SV-VER7", "SV-VER8").replace("surround_v7_%s.jpg", "surround_v8_%s.jpg")
i = b.index('box(150, 34, 198, 62,')
j = b.index("\n", i)
b = b[:i] + 'box(150, 34, 198, 62, [L("ヘッドホン (前面) HP-VER3", 1.05, True), L("3.5 / 4.4 / 6.35mm / XLR", 0.85), L("(ステレオ4ピン + モノラル3ピン×2)", 0.8), L("ゲイン・音量 各 1dB 刻み 3 モード", 0.85), L("ON/OFF スイッチ (SP・HP・SUB)", 0.85), L("PRE OUT 11.2ch " + ("XLR" if BAL else "RCA"), 0.85)], ANA)' + b[j:]
b = b.replace('L("I/V → LPF → ボリューム → バッファ", 1.15, True)', 'L("I/V → LPF → 音量・ゲイン → バッファ", 1.1, True)')
b = b.replace('L("ラッチングリレー + 0.1% 薄膜抵抗 (ラダー)", 1.0)', 'L("音量・ゲインは 1dB 刻み 3 モード (ANALOG / DIGITAL / A+D)", 0.95), L("ラッチングリレー + 0.1% 薄膜抵抗", 0.95)')
k = b.index('box(66, 6, 198, 30,')
b = b[:k] + b[k:].replace('L("配線を短く・耐久・音質 設計メモ Design notes", 1.3, True),', 'L("配線を短く・耐久・音質 設計メモ Design notes", 1.3, True),\n  L("前面: スピーカー・ヘッドホン・サブウーファーの出力は各々 ON/OFF スイッチ (非接触スイッチ + 密閉リレー)。ゲインと音量はスピーカー用・ヘッドホン用 各 1dB 刻み 3 モード", 0.95),', 1)
open("surround_v8_block_body.py", "w", encoding="utf-8").write(b)
# 2) texts: update the headphone sentence of the AV amplifier
t = open("sv7_texts_add.py", encoding="utf-8").read()
pairs = [
 ("ゲイン調整つき: アナログ 0 / +6 / +12 / +18dB とデジタルゲインの 2 種類で、ヘッドホンの抵抗を検出して自動推奨する。", "ゲインと音量は 1dB 刻み・3 モードで調整でき (下記)、ヘッドホンの抵抗を検出してゲインを自動推奨する。"),
 ("With gain adjustment: analog 0 / +6 / +12 / +18 dB and a digital gain, with an automatic recommendation from the detected headphone resistance.", "Gain and volume are adjusted in 1 dB steps with three modes (see below), with an automatic gain recommendation from the detected headphone resistance."),
 ("С регулировкой усиления: аналоговое 0 / +6 / +12 / +18 дБ и цифровое, с автоматической рекомендацией по определённому сопротивлению наушников.", "Усиление и громкость регулируются с шагом 1 дБ в трёх режимах (ниже), с автоматической рекомендацией усиления по определённому сопротивлению наушников."),
 ("З регулюванням підсилення: аналогове 0 / +6 / +12 / +18 дБ і цифрове, з автоматичною рекомендацією за визначеним опором навушників.", "Підсилення та гучність регулюються з кроком 1 дБ у трьох режимах (нижче), з автоматичною рекомендацією підсилення за визначеним опором навушників."),
 ("Mit Verstärkungseinstellung: analog 0 / +6 / +12 / +18 dB und digital, mit automatischer Empfehlung aus dem erkannten Kopfhörerwiderstand.", "Verstärkung und Lautstärke werden in 1-dB-Schritten mit drei Modi eingestellt (siehe unten), mit automatischer Verstärkungsempfehlung aus dem erkannten Kopfhörerwiderstand."),
 ("Con regolazione del guadagno: analogico 0 / +6 / +12 / +18 dB e digitale, con raccomandazione automatica dalla resistenza rilevata della cuffia.", "Guadagno e volume si regolano a passi di 1 dB in tre modi (vedi sotto), con raccomandazione automatica del guadagno dalla resistenza rilevata della cuffia."),
 ("Avec réglage du gain : analogique 0 / +6 / +12 / +18 dB et numérique, avec recommandation automatique à partir de la résistance détectée du casque.", "Le gain et le volume se règlent par pas de 1 dB en trois modes (voir ci-dessous), avec recommandation automatique du gain à partir de la résistance détectée du casque."),
]
n = 0
for a, c in pairs:
    if a in t:
        t = t.replace(a, c); n += 1
    else:
        print("MISSING", a[:40])
t = t.replace("HP-VER2", "HP-VER3")
if "T_G3" not in t:
    t = 'exec(open(SD + "/g3_texts.py", encoding="utf-8").read())\nT["g3"] = T_G3["g3"]\n' + t
open("sv8_texts_add.py", "w", encoding="utf-8").write(t)
print(n, "of", len(pairs))
# 3) the build script
s = open("sv7_build.py", encoding="utf-8").read()
s = s.replace("SV-VER7", "SV-VER8").replace("surround_v7_", "surround_v8_").replace("manual-sv7", "manual-sv8").replace("avamp/SV-VER7", "avamp/SV-VER8").replace("surround-av-amp-v7", "surround-av-amp-v8").replace("sv7_texts_add.py", "sv8_texts_add.py")
s = s.replace('["hp", "sw", "os", "net", "rf", "rest"]', '["hp", "sw", "g3", "os", "net", "rf", "rest"]').replace('["title", "hp", "sw", "os", "net", "sim", "rf", "rest"]', '["title", "hp", "sw", "g3", "os", "net", "sim", "rf", "rest"]').replace('for k in ("hp", "sw", "os", "net", "sim", "rf", "rest"):', 'for k in ("hp", "sw", "g3", "os", "net", "sim", "rf", "rest"):')
s = s.replace("(see SV-VER6 and HP-VER2)", "(see SV-VER6, HP-VER2 and HP-VER3)")
open("sv8_build.py", "w", encoding="utf-8").write(s)
