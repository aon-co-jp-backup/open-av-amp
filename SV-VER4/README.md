# SV-VER4 — re-verified supply, R-core and chassis / 電源・Rコア・筐体の再検証 / Überprüfte Versorgung / Проверенное питание

SV-VER4 = SV-VER3 corrected by four virtual test/debug rounds (`surround_v4_sim.jpg`, Python calculations, not SPICE or bench measurements). Figures: `surround_v4_balanced.jpg`, `surround_v4_unbalanced.jpg`, `surround_v4_sim.jpg`, all in `surround-av-amp-v4.pdf`.

## 日本語
- 問題: SV-VER3 は 5 バンクすべてを定電圧にしていた。パワー段 (±45V) まで定電圧にすると、余裕 5V でも最大出力時に約 136W、映画の平均でも約 17W を電源が熱にしてしまう。
- 対策: パワー段のレールは非安定の大容量コンデンサ (4 × 22,000µF、別筐体)、アナログ ±15V・デジタル・DAC・クロックだけを低雑音のリニア定電圧にする。レールの変動は、映画の平均で約 0.10V、持続 1/3 出力で約 0.26V (計算)。
- R コア: 全 11ch が最大出力で鳴り続けると約 1406VA で 100V 15A (1500VA) に近い。持続 1/3 出力 (約 469VA) を出せる 1.0kVA 級にし、ピークはコンデンサで賄う (10ms のピークで約 1.5V の垂れ)。
- 筐体 (アルミ + 木)・端子 (金/ロジウム) は机上の計算では検証できない (測定が必要)。
- 未実施: 実機測定、過渡応答、筐体の共振測定、各社の認証。

## English
- Problem: SV-VER3 regulated all five banks. Regulating the +-45 V power rails wastes about 136 W at full output (5 V headroom) and about 17 W for the film average.
- Fix: the power-stage rails are unregulated large capacitor banks (4 x 22,000 uF, separate case); only analog +-15 V, digital, DAC and clock get low-noise linear regulation. Rail ripple is about 0.10 V at the film average and 0.26 V at a sustained 1/3 power (calculated).
- R-core: all 11 channels at full output would draw about 1406 VA, close to 1500 VA (100 V 15 A). A 1.0 kVA class core covers the sustained 1/3 power (about 469 VA) and the capacitors supply the peaks (about 1.5 V sag for a 10 ms peak).
- The aluminium + wood chassis and the gold/rhodium terminals cannot be verified by desk calculation (measurement needed).
- Not done: bench measurements, transient response, chassis resonance measurement, certifications.

## Deutsch
- Problem: SV-VER3 regelte alle fünf Bänke. Die Regelung der ±45-V-Endstufenschienen erzeugt bei Vollaussteuerung etwa 136 W (5 V Reserve) und im Filmdurchschnitt etwa 17 W Verlust.
- Abhilfe: Endstufenschienen als ungeregelte große Kondensatorbänke (4 × 22.000 µF, getrenntes Gehäuse); nur analog ±15 V, Digital, DAC und Takt rauscharm linear geregelt. Restwelligkeit etwa 0,10 V im Filmdurchschnitt, 0,26 V bei dauerhaft 1/3 Leistung (berechnet).
- R-Kern: Alle 11 Kanäle bei Vollaussteuerung ziehen etwa 1406 VA, nahe 1500 VA (100 V 15 A). Ein 1,0-kVA-Kern deckt dauerhaft 1/3 Leistung (etwa 469 VA); Spitzen liefern die Kondensatoren (etwa 1,5 V Einbruch bei 10 ms).
- Gehäuse (Aluminium-Holz) und Klemmen (Gold/Rhodium) lassen sich nicht am Schreibtisch prüfen (Messung nötig).
- Nicht durchgeführt: Messungen, Einschwingverhalten, Resonanzmessung, Zertifizierungen.

## Русский
- Проблема: в SV-VER3 были стабилизированы все пять банков. Стабилизация силовых шин ±45 В даёт около 136 Вт потерь при полной мощности (запас 5 В) и около 17 Вт в среднем для фильма.
- Решение: шины силового каскада — нестабилизированные батареи больших конденсаторов (4 × 22 000 мкФ, отдельный корпус); малошумящая линейная стабилизация только для аналоговых ±15 В, цифровой части, ЦАП и такта. Пульсации около 0,10 В в среднем для фильма и 0,26 В при длительных 1/3 мощности (расчёт).
- R-сердечник: все 11 каналов при полной мощности потребляют около 1406 ВА, близко к 1500 ВА (100 В 15 А). Сердечник класса 1,0 кВА покрывает длительные 1/3 мощности (около 469 ВА), пики обеспечивают конденсаторы (просадка около 1,5 В за 10 мс).
- Корпус (алюминий + дерево) и клеммы (золото/родий) расчётом не проверить (нужны измерения).
- Не выполнено: измерения, переходные процессы, измерение резонансов, сертификации.
