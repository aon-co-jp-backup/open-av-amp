# SV-VER11 — SV-VER10 + ハイブリッド音量 (クリック式 0.5dB ⇄ 滑らか式 0.01dB) / Hybrid volume

> Translation note / 翻訳について: English text written by an AI; not checked by native speakers. 英文は AI が書いたもので、ネイティブ確認は未実施です。
> Status / 位置づけ: design proposal, calculation only (scripts/SV-VER11, [volume_calc.py](https://github.com/aon-co-jp/open-network-amp/blob/main/scripts/volume/volume_calc.py)); no hardware verification. 設計案 (計算のみ)、実機未検証。

Figure / 図: `volume_hybrid.jpg`. Spec / 仕様: [VOLUME-STEP-SPEC.md](https://github.com/aon-co-jp/open-network-amp/blob/main/VOLUME-STEP-SPEC.md) (open-network-amp VER8)。

## 日本語
- SV-VER10 (電源入力まで) に、音量ノブのハイブリッド化を加えました。SW6 で切替: ON = クリック式 (モーターのクリック感、1 クリック = 0.5dB、5dB ごとに強いクリック)、OFF = クリック無しの静かで滑らかな式 (0.01dB 刻み)。
- 全 12ch (11.2.4 の 11ch + 予備) を差動のまま、各 ch・各脚に 2 進ラダー (0.5/1/2/4/8/16/32/64dB のラッチ式リレー 8 本) を置き、1 つのノブで連動。リレーは 12ch × 2 脚 × 8 本 = 192 本。
- 滑らか式はリレー位置 (0.5dB 単位) の間 ±0.25dB を FPGA の 32bit デジタル微調整で埋める (失うビット 約 0.04bit)。SW5 (ビットパーフェクト) のときは 0.5dB 分解能。
- 未確認: 192 本のリレーの実装面積・コスト、全 ch の連動精度、リレー切替時の段差とミュート、実機測定。

## English
- SV-VER10 (up to the power input) plus a hybrid volume knob. SW6 selects: ON = clicky (motor feel, one click = 0.5 dB, a stronger click every 5 dB); OFF = quiet, smooth, no clicks (0.01 dB steps).
- All 12 channels stay differential; each channel and leg gets a binary ladder (eight latching relays, 0.5/1/2/4/8/16/32/64 dB), driven together by one knob: 12 ch x 2 legs x 8 = 192 relays.
- Smooth mode fills the +-0.25 dB between relay positions (0.5 dB grid) with a 32-bit digital trim (about 0.04 bit lost). With SW5 (bit-perfect) the resolution is 0.5 dB.
- Not verified: board area and cost of 192 relays, channel tracking, level steps and muting at relay switching, bench measurements.
