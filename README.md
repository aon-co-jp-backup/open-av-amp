# open-av-amp — SV-VER1 — Surround AV amplifier / サラウンド AV アンプ / Surround-AV-Verstärker / AV-ресивер объёмного звука

Reference design (not a product). Python calculations, not SPICE or bench measurements. Figures: `surround_balanced.jpg` (fully balanced), `surround_unbalanced.jpg`, `surround_sim.jpg` (5 test/debug rounds); all in `surround-av-amp.pdf`.
IMAX Enhanced, Dolby and DTS certification need licences and were not done. 4DX is a cinema system without a home standard; this design offers tactile (bass-shaker) outputs and a control port for a similar feel.

## 日本語
- 構成: HDMI 2.1 入力 6 系統 (eARC)、Dolby Atmos・DTS:X (IMAX Enhanced 対応を想定) の 11.2.4 処理、DAC 12ch (AK4191 + BD34302 を 6 組)、触覚ハイブリッド音量 VER6、パワーアンプ 11ch (7.1.4)。
- 完全バランス版 (全 12ch を差動のまま処理) とアンバランス版 (DAC 直後に差動→単相) の 2 種類。どちらも、モノラルのサブウーファー端子 (RCA + XLR) を 2 系統 (低雑音 0.28µV の改良版)、触覚 (4DX 風) 出力 2ch、ヘッドホン、PRE OUT を持ちます。
- 配線: チャンネルごとに DAC→ボリューム→パワーを一直線 (約 40mm)、グランド面を直下に敷き、隣の経路と 25mm あける (集中配置の 180mm 比で誘導・クロストーク 約 −21dB、計算)。
- 発熱: 全 11ch を Class AB にすると 4Ω で約 1128W。フロント L/C/R だけ Class AB、他 8ch をクラス D にすると約 533W (映画の平均は約 138W) → 温度制御ファンで処理。
- 音質・耐久: ジッタ 0.3ps で SNR 約 148dB、電解コンデンサは別筐体 45°C 以下 (約 73 年)、ラッチングリレー、非接触磁気エンコーダ 2 重の音量ノブ (約 17 年)。
- 未実施: 実機測定、HDMI 認証、各社の認証、過渡応答、THD。

## English
- Layout: six HDMI 2.1 inputs (eARC), Dolby Atmos and DTS:X (aimed at IMAX Enhanced) 11.2.4 processing, a 12-channel DAC (six AK4191 + BD34302 pairs), the VER6 haptic hybrid volume, an 11-channel power amplifier (7.1.4).
- Two versions: fully balanced (all 12 channels stay differential) and unbalanced (differential to single-ended right after the DAC). Both have two mono subwoofer outputs (RCA + XLR, the low-noise 0.28 uV version), two tactile (4DX-style) channels, headphones and PRE OUT.
- Wiring: one straight line per channel, DAC to volume to power stage (about 40 mm), a ground plane beneath and 25 mm to the neighbour (about 21 dB less pick-up and crosstalk than a 180 mm central layout, calculated).
- Heat: all 11 channels in Class AB dissipate about 1128 W at 4 ohm; with only front L/C/R in Class AB and 8 channels in Class D it is about 533 W (about 138 W for the film average), handled by a temperature-controlled fan.
- Sound and durability: 0.3 ps jitter gives about 148 dB SNR, the electrolytic capacitors sit in a separate case at 45 C or below (about 73 years), latching relays, and the volume knob with two non-contact magnetic encoders (about 17 years).
- Not done: bench measurements, HDMI compliance, vendor certifications, transient response, THD.

## Deutsch
- Aufbau: sechs HDMI-2.1-Eingänge (eARC), Dolby Atmos und DTS:X (auf IMAX Enhanced ausgelegt) 11.2.4, 12-Kanal-DAC (sechs Paare AK4191 + BD34302), haptischer Hybrid-Lautstärkeregler VER6, 11-Kanal-Endstufe (7.1.4).
- Zwei Versionen: voll symmetrisch (alle 12 Kanäle bleiben differenziell) und unsymmetrisch. Beide haben zwei Mono-Subwoofer-Ausgänge (RCA + XLR, rauscharme Version 0,28 µV), zwei Haptikkanäle (4DX-artig), Kopfhörer und PRE OUT.
- Verdrahtung: je Kanal eine gerade Linie DAC, Lautstärke, Endstufe (etwa 40 mm), Massefläche darunter, 25 mm zum Nachbarn (etwa 21 dB weniger Einstreuung und Übersprechen als bei 180 mm zentralem Aufbau, berechnet).
- Wärme: Alle 11 Kanäle in Klasse AB ergeben etwa 1128 W an 4 Ω; nur Front L/C/R in Klasse AB und 8 Kanäle in Klasse D: etwa 533 W (Filmdurchschnitt etwa 138 W), mit temperaturgeregeltem Lüfter.
- Klang und Haltbarkeit: 0,3 ps Jitter ergeben etwa 148 dB SNR, Elektrolytkondensatoren im getrennten Gehäuse bei höchstens 45 °C (etwa 73 Jahre), Latching-Relais, Lautstärkeknopf mit zwei berührungslosen Magnetencodern (etwa 17 Jahre).
- Nicht durchgeführt: Messungen, HDMI-Konformität, Zertifizierungen, Einschwingverhalten, THD.

## Русский
- Состав: шесть входов HDMI 2.1 (eARC), обработка Dolby Atmos и DTS:X (в расчёте на IMAX Enhanced) 11.2.4, 12-канальный ЦАП (шесть пар AK4191 + BD34302), тактильный гибридный регулятор громкости VER6, 11-канальный усилитель (7.1.4).
- Две версии: полностью сбалансированная (все 12 каналов остаются дифференциальными) и несбалансированная. В обеих два моно-выхода сабвуфера (RCA + XLR, малошумящая версия 0,28 мкВ), два тактильных канала (в духе 4DX), наушники и PRE OUT.
- Разводка: для каждого канала одна прямая линия ЦАП, регулятор громкости, усилитель (около 40 мм), слой земли под ней, 25 мм до соседа (наводка и перекрёстные помехи примерно на 21 дБ меньше, чем при центральной компоновке 180 мм, расчёт).
- Нагрев: все 11 каналов в классе AB — около 1128 Вт на 4 Ом; только фронтальные L/C/R в классе AB и 8 каналов в классе D — около 533 Вт (среднее для фильма около 138 Вт), вентилятор с термоуправлением.
- Звук и долговечность: джиттер 0,3 пс даёт SNR около 148 дБ, электролитические конденсаторы в отдельном корпусе при 45 °C или ниже (около 73 лет), реле с защёлкой, ручка громкости с двумя бесконтактными магнитными энкодерами (около 17 лет).
- Не выполнено: измерения, проверка HDMI, сертификации, переходные процессы, КНИ.

---
**Newest: [SV-VER10](SV-VER10)** — SV-VER9 plus the power input (100-240 V auto-ranging, 50/60 Hz, device recognition over the power line at connection time only, 120 Hz only when both sides support it, optional 20 A connector; design proposal). **Before: [SV-VER9](SV-VER9)** — the block diagrams show the volume and the two gains (low and high) in 1 dB steps with three modes on both the speaker and the headphone outputs (HP-VER4). **Before: [SV-VER8](SV-VER8)** — the block diagrams now show the front-panel headphone amplifier (HP-VER3), the ON/OFF switches for the speaker, headphone and subwoofer outputs, and the gain and volume controls (1 dB steps, three modes). **Before: [SV-VER7](SV-VER7)** — SV-VER6 plus the front-panel headphone amplifier (3.5 / 4.4 / 6.35 mm, XLR stereo 4-pin and two mono 3-pin, gain adjustment). **Before: [SV-VER6](SV-VER6)** — Android OS (Android TV / Google TV), browser with HDMI image output, Wi-Fi 8 (internet, image and audio transfer), Bluetooth 6 and LAN; each figure carries the 8-language explanation. **Before: [SV-VER5](SV-VER5)** — aligned with VER7: all 11 channels in improved analog-input Class D only; manual in 8 languages (JA, EN-US, EN-UK, RU, UK, DE, IT, FR). **Before: [SV-VER4](SV-VER4)** — supply, R-core and chassis re-verified (power rails unregulated large capacitors, analog/digital linear-regulated, 1.0 kVA R-core). **Before: [SV-VER3](SV-VER3)** — external linear DC supply with R-core transformers, aluminium + wood chassis (ideas from SPEC). **Before: [SV-VER2](SV-VER2)** — all 11 channels in analog-input Class D (heat about 309 W worst case instead of 533 W), with an output-filter damper. SV-VER1 stays as the earlier version.

Files: [`SV-VER1/`](SV-VER1) (figures JPG + PDF), scripts in [`scripts/SV-VER1/`](scripts/SV-VER1) (saved per version). Related: [open-network-amp](https://github.com/aon-co-jp/open-network-amp) (integrated amplifier VER1-VER6). Home page: https://audiocafe.tokyo/

## API 方針: REST 全廃・gRPC / Connect へ (2026-11-04)

### 日本語
- **REST は全廃する。新しい API は REST で作らない。** ブラウザや `curl` から呼ぶ API は **Connect の単純呼び出し**(`POST /<パッケージ>.<Service>/<Method>`、`content-type: application/json`、本文は JSON)、サービス間は **gRPC / gRPC-web**(RPoem の管理API `open_runo.admin.v1.Admin` と同じ流儀)。ストリーミングは、必要になってから。
- **既存の REST は、触るときに順に移す。** 移したら旧 REST の経路は消す。移行が終わるまで残るが、**新規には追加しない**。
- **JSON は RS-JSON に統一**する(読み込みは `from_str_secure` / `parse_secure` でサイズ・深さ・重複キーの上限つき、書き出しは `rust_json::fast`)。ブラウザの WASM に `prost` は入れない(サイズが増えるため)。
- **例外(自分たちの API ではなく、相手の規格が決めているもの)**: ACME、OAuth/OIDC のコールバック、第三者(GitHub など)からの Webhook、ヘルスチェック、静的ファイル配信、OTLP など。これらは規格どおりの HTTP を受ける。
- 参考実装: `RPoem`(`open_runo.admin.v1.Admin`)、`open-easy-web`(`server/src/connect.rs`、`proto/open_easy_web/admin/v1/admin.proto`)。
- ※ このリポジトリのコードが既に方針どおりかどうかは、各リポジトリの現状による。この節は方針の記録であり、コードの変更を意味しない。

### English
- **REST is being abolished. New APIs are not built as REST.** APIs called from browsers or `curl` use **Connect unary calls** (`POST /<package>.<Service>/<Method>`, `content-type: application/json`, JSON body); service-to-service calls use **gRPC / gRPC-web** (the same style as RPoem's admin API `open_runo.admin.v1.Admin`). Streaming only when it is actually needed.
- **Existing REST endpoints are migrated one by one, when they are touched.** The old REST route is removed once migrated. Until migration is finished they remain, but **no new ones are added**.
- **JSON is unified on RS-JSON**: reading with `from_str_secure` / `parse_secure` (size, depth and duplicate-key limits), writing with `rust_json::fast`. `prost` is not put into browser WASM (it would grow the binary).
- **Exceptions (shapes dictated by someone else's standard, not our own API)**: ACME, OAuth/OIDC callbacks, webhooks from third parties (e.g. GitHub), health checks, static file serving, OTLP, and so on. These accept plain HTTP as the standard requires.
- Reference implementations: `RPoem` (`open_runo.admin.v1.Admin`) and `open-easy-web` (`server/src/connect.rs`, `proto/open_easy_web/admin/v1/admin.proto`).
- Note: whether the code in a given repository already follows this policy depends on that repository. This section records the policy; it does not mean the code has been changed.

### Deutsch (KI-Übersetzung, noch nicht von Muttersprachlern geprüft)
- **REST wird abgeschafft. Neue APIs werden nicht als REST gebaut.** APIs, die aus dem Browser oder mit `curl` aufgerufen werden, nutzen **Connect-Unary-Aufrufe** (`POST /<Paket>.<Service>/<Methode>`, `content-type: application/json`, JSON-Body); zwischen Diensten gilt **gRPC / gRPC-web** (wie bei der Admin-API von RPoem, `open_runo.admin.v1.Admin`). Streaming erst, wenn es wirklich nötig ist.
- **Bestehende REST-Endpunkte werden einzeln migriert, sobald man sie anfasst.** Nach der Migration wird die alte REST-Route entfernt. Bis dahin bleiben sie bestehen, es werden aber **keine neuen hinzugefügt**.
- **JSON wird auf RS-JSON vereinheitlicht**: Lesen mit `from_str_secure` / `parse_secure` (Grenzen für Größe, Tiefe und doppelte Schlüssel), Schreiben mit `rust_json::fast`. `prost` kommt nicht in Browser-WASM (die Datei würde größer).
- **Ausnahmen (Formate, die ein fremder Standard vorgibt, nicht unsere eigene API)**: ACME, OAuth/OIDC-Callbacks, Webhooks von Dritten (z. B. GitHub), Health-Checks, statische Dateien, OTLP usw. Diese nehmen schlichtes HTTP entgegen, wie es der Standard verlangt.
- Referenzimplementierungen: `RPoem` (`open_runo.admin.v1.Admin`) und `open-easy-web` (`server/src/connect.rs`, `proto/open_easy_web/admin/v1/admin.proto`).
- Hinweis: Ob der Code eines Repositorys diese Richtlinie schon befolgt, hängt vom jeweiligen Repository ab. Dieser Abschnitt hält die Richtlinie fest; er bedeutet nicht, dass der Code bereits geändert wurde.

### Русский (машинный перевод, носителями языка ещё не проверен)
- **REST полностью отменяется. Новые API не создаются как REST.** API, вызываемые из браузера или через `curl`, используют **унарные вызовы Connect** (`POST /<пакет>.<Service>/<Method>`, `content-type: application/json`, тело — JSON); между сервисами — **gRPC / gRPC-web** (так же, как административный API RPoem, `open_runo.admin.v1.Admin`). Потоковая передача — только когда она действительно нужна.
- **Существующие REST-эндпоинты переносятся по одному, когда до них доходят руки.** После переноса старый REST-маршрут удаляется. До завершения переноса они остаются, но **новые не добавляются**.
- **JSON унифицируется на RS-JSON**: чтение через `from_str_secure` / `parse_secure` (ограничения на размер, глубину и повторяющиеся ключи), запись через `rust_json::fast`. `prost` не добавляется в браузерный WASM (размер вырос бы).
- **Исключения (форматы, заданные чужим стандартом, а не наш собственный API)**: ACME, обратные вызовы OAuth/OIDC, вебхуки сторонних сервисов (например, GitHub), проверки работоспособности, раздача статических файлов, OTLP и т. п. Они принимают обычный HTTP, как требует стандарт.
- Эталонные реализации: `RPoem` (`open_runo.admin.v1.Admin`) и `open-easy-web` (`server/src/connect.rs`, `proto/open_easy_web/admin/v1/admin.proto`).
- Примечание: соответствует ли код конкретного репозитория этой политике, зависит от самого репозитория. Этот раздел фиксирует политику и не означает, что код уже изменён.
