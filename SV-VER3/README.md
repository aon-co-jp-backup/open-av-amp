# SV-VER3 — external linear DC supply, SPEC-inspired analog-input Class D / 外付けリニアDC電源 / Externes lineares Netzteil / Внешний линейный блок питания

SV-VER3 = SV-VER2 (all 11 channels in analog-input Class D) plus the changes below. The SV-VER2 test log (`../SV-VER2/surround_v2_sim.jpg`) still applies; no new simulation was run for these mechanical and supply changes. Reference design only; Python-based numbers are in SV-VER2.
Inspiration: web searches about the Japanese maker SPEC (RSA-F1 / RSA-V1: analog-input Class D, linear analog supply, R-core transformer, aluminium + wood hybrid chassis, rhodium-plated terminals). Only the ideas were taken, nothing was copied; reviews are subjective and no bench data was found.

## 日本語
- 電源: スイッチング電源を使わず、外付けのリニア DC 電源 (定電圧のアナログ電源) にします。トランスは R コア (トロイダルより巻線の自由度が高く、漏れ磁束も小さいとされる、SPEC の RSA-V1 も採用) を左右チャンネル独立に使い、5 バンク (前・後+ハイト・サブ・触覚・デジタル) に分けます。電解コンデンサは 45°C 以下の別筐体に置きます (約 73 年、計算)。
- 筐体: アルミと木のハイブリッドで共振を抑えます。端子は金またはロジウムめっきです。
- 変更なし: 全 11ch アナログ入力クラス D、触覚ハイブリッド音量 VER6、改良したモノラルサブウーファー端子 2 系統、触覚出力 2ch、完全バランス版とアンバランス版、配線 約 40mm。
- 未実施: 実機測定、各社の認証、今回の変更の再シミュレーション。

## English
- Supply: no switching supply; an external linear DC supply (regulated analog) with R-core transformers (more winding freedom and less stray flux than toroids, also used in SPEC's RSA-V1), independent per channel group, in five banks (front, rear + height, sub, tactile, digital). The electrolytic capacitors sit in a separate case at 45 C or below (about 73 years, calculated).
- Chassis: an aluminium and wood hybrid to damp resonance; gold or rhodium-plated terminals.
- Unchanged: all 11 channels in analog-input Class D, the VER6 haptic hybrid volume, two improved mono subwoofer outputs, two tactile channels, balanced and unbalanced versions, about 40 mm wiring.
- Not done: bench measurements, certifications, re-simulation of these changes.

## Deutsch
- Versorgung: kein Schaltnetzteil, sondern ein externes lineares Gleichspannungsnetzteil (geregelt, analog) mit R-Kern-Transformatoren (mehr Wicklungsfreiheit und weniger Streufluss als Ringkerne, auch im SPEC RSA-V1), unabhängig je Kanalgruppe, in fünf Bänken. Die Elektrolytkondensatoren sitzen in einem getrennten Gehäuse bei höchstens 45 °C (etwa 73 Jahre, berechnet).
- Gehäuse: Aluminium-Holz-Hybrid zur Resonanzdämpfung; Klemmen vergoldet oder rhodiniert.
- Unverändert: alle 11 Kanäle Klasse D mit Analogeingang, haptischer Hybrid-Lautstärkeregler VER6, zwei verbesserte Mono-Subwoofer-Ausgänge, zwei Haptikkanäle, etwa 40 mm Verdrahtung.
- Nicht durchgeführt: Messungen, Zertifizierungen, erneute Simulation.

## Русский
- Питание: без импульсного блока; внешний линейный блок питания постоянного тока (стабилизированный аналоговый) с R-сердечниками (больше свободы намотки и меньше поле рассеяния, чем у тороидов; применяются и в SPEC RSA-V1), независимо для групп каналов, пять банков. Электролитические конденсаторы — в отдельном корпусе при 45 °C или ниже (около 73 лет, расчёт).
- Корпус: гибрид алюминия и дерева для гашения резонансов; клеммы с золотым или родиевым покрытием.
- Без изменений: все 11 каналов класса D с аналоговым входом, тактильный гибридный регулятор громкости VER6, два улучшенных моно-выхода сабвуфера, два тактильных канала, разводка около 40 мм.
- Не выполнено: измерения, сертификации, повторное моделирование.
