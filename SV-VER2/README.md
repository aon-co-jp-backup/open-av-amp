# SV-VER2 — all-Class-D (analog input) surround AV amplifier / 全 11ch アナログ入力クラス D / Alle 11 Kanäle Klasse D mit Analogeingang / Все 11 каналов класса D с аналоговым входом

SV-VER2 is SV-VER1 with all 11 power channels changed to Class D with analog input (Eigentakt-type, self-oscillating with feedback). Everything else (HDMI 2.1, Atmos / DTS:X 11.2.4, 12-channel AK4191 + BD34302 DAC, VER6 haptic hybrid volume, two improved mono subwoofer outputs, two tactile channels, balanced and unbalanced versions) is unchanged.
Figures: `surround_v2_balanced.jpg`, `surround_v2_unbalanced.jpg`, `surround_v2_sim.jpg` (4 test/debug rounds), all in `surround-av-amp-v2.pdf`. Python calculations, not SPICE or bench measurements. IMAX Enhanced / Dolby / DTS certification was not done; 4DX is a cinema system, so tactile outputs and a control port give a similar feel.

## 日本語
- 変更: 全 11ch を、アナログ入力のクラス D (Eigentakt 型の自己発振 + 負帰還) にしました。
- 発熱: 最悪 約 309W (4Ω)。SV-VER1 の混成は 約 533W、全 Class AB は 約 1128W。映画の平均は約 19W、待機は約 16W (全 AB は 約 99W)。
- 音質の問題と対策: 出力 LC フィルタ (22µH / 0.47µF、共振 約 49kHz) は、16Ω のような軽い負荷だと高域が約 7.6dB 持ち上がります。出力に RC ダンピング (ゾベル) を足して約 0.7dB に抑えます (計算)。
- 注意: 「クラス D のほうが必ず音がよい」とは言えず、フィルタ・電源・配線次第です。スイッチング ノイズを入れないよう、パワー段は筐体の外側に置き、シールド板で DAC / ボリュームと仕切ります。
- 未実施: 実機測定 (THD・雑音・出力インピーダンス・EMI)、HDMI と各社の認証、過渡応答。

## English
- Change: all 11 channels are now Class D with analog input (Eigentakt-type, self-oscillating with feedback).
- Heat: about 309 W worst case (4 ohm), versus about 533 W for the SV-VER1 mix and about 1128 W for all Class AB. The film average is about 19 W and idle about 16 W (all-AB about 99 W).
- Sound issue and fix: the output LC filter (22 uH / 0.47 uF, resonance about 49 kHz) lifts the treble by about 7.6 dB into a light load such as 16 ohm. An RC damper (Zobel) at the output holds it to about 0.7 dB (calculated).
- Caution: Class D is not automatically better sounding; the filter, supply and wiring decide. To keep switching noise out, the power stage sits at the outside of the chassis behind a shield plate from the DAC and volume.
- Not done: bench measurements (THD, noise, output impedance, EMI), HDMI and vendor certifications, transient response.

## Deutsch
- Änderung: Alle 11 Kanäle sind jetzt Klasse D mit Analogeingang (Eigentakt-Typ, selbstschwingend mit Gegenkopplung).
- Wärme: im ungünstigsten Fall etwa 309 W (4 Ω), gegenüber etwa 533 W bei der Mischung von SV-VER1 und etwa 1128 W bei reiner Klasse AB. Filmdurchschnitt etwa 19 W, Leerlauf etwa 16 W (alle AB etwa 99 W).
- Klangproblem und Abhilfe: Der LC-Ausgangsfilter (22 µH / 0,47 µF, Resonanz etwa 49 kHz) hebt die Höhen an leichter Last wie 16 Ω um etwa 7,6 dB an. Ein RC-Dämpfungsglied (Zobel) am Ausgang hält es bei etwa 0,7 dB (berechnet).
- Hinweis: Klasse D klingt nicht automatisch besser; Filter, Versorgung und Verdrahtung entscheiden. Die Endstufe sitzt außen im Gehäuse hinter einer Schirmwand zu DAC und Lautstärkeregler.
- Nicht durchgeführt: Messungen (THD, Rauschen, Ausgangsimpedanz, EMV), HDMI- und Herstellerzertifizierungen, Einschwingverhalten.

## Русский
- Изменение: все 11 каналов теперь класса D с аналоговым входом (тип Eigentakt, самовозбуждение с обратной связью).
- Нагрев: в худшем случае около 309 Вт (4 Ом) против около 533 Вт у смешанного варианта SV-VER1 и около 1128 Вт при классе AB везде. Среднее для фильма около 19 Вт, в покое около 16 Вт (все AB около 99 Вт).
- Проблема со звуком и решение: выходной LC-фильтр (22 мкГн / 0,47 мкФ, резонанс около 49 кГц) при лёгкой нагрузке, например 16 Ом, поднимает верха примерно на 7,6 дБ. RC-демпфер (цепь Цобеля) на выходе удерживает подъём около 0,7 дБ (расчёт).
- Примечание: класс D не всегда звучит лучше сам по себе; решают фильтр, питание и разводка. Силовой каскад стоит снаружи корпуса за экраном от ЦАП и регулятора громкости.
- Не выполнено: измерения (КНИ, шум, выходное сопротивление, ЭМС), проверка HDMI и сертификации, переходные процессы.
