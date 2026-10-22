import math
# ------------------------------------------------ 1) bit rates (Mbps) of what travels over the network
RATES = [
    ("音声 2ch 44.1k/16", 44.1e3 * 16 * 2 / 1e6),
    ("PCM 2ch 192k/24", 192e3 * 24 * 2 / 1e6),
    ("Atmos 11.2.4 PCM 48k/24 (13ch)", 48e3 * 24 * 13 / 1e6),
    ("PCM 2ch 1536k/32", 1536e3 * 32 * 2 / 1e6),
    ("DSD1024 2ch", 1024 * 44.1e3 * 2 / 1e6),
    ("4K HDR 動画 (ストリーミング)", 40.0),
    ("4K UHD Blu-ray 級", 128.0),
]
# effective (not nominal) throughput assumed for each link, Mbps
LINKS = [("Wi-Fi 2.4GHz", 70.0), ("Wi-Fi 5GHz", 450.0), ("Wi-Fi 6/7/8 (6GHz)", 1200.0), ("有線 LAN GbE", 940.0)]
# ------------------------------------------------ 2) digital-side power (5 V rail) and the linear regulator heat
P_SOC, P_WIFI_BT, P_LAN, P_HDMI, P_MISC = 8.0, 3.0, 1.0, 2.0, 1.0
P_DIG = P_SOC + P_WIFI_BT + P_LAN + P_HDMI + P_MISC
I_DIG = P_DIG / 5.0
loss_lin = lambda vin: (vin - 5.0) * I_DIG
# ------------------------------------------------ 3) SoC junction temperature
tj = lambda theta_ja, p=P_SOC, tamb=40.0: tamb + p * theta_ja
if __name__ == "__main__":
    for n, r in RATES: print(n, round(r, 1))
    print("digital", P_DIG, "W", round(I_DIG, 2), "A")
    for v in (12.0, 9.0, 6.8): print("Vin", v, "loss", round(loss_lin(v), 1), "W")
    for th in (3, 5, 8, 15): print("theta", th, "Tj", round(tj(th), 0))
