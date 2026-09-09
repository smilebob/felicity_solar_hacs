# ☀️ Felicity Solar for Home Assistant (Smilebob Edition)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/smilebob/felicity_solar_hacs)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> [!NOTE]
> **Community Extended Fork & Original Author Attribution**  
> This integration is an extended community fork based on the original work created by **[Matheus Tavares Trindade](https://github.com/matheustavarestrindade/felicity_solar_hacs)**.  
> All core architectural credits belong to the original author. This edition adds community enhancements: OpenAPI hardening, dynamic model & firmware identification, Dual/Quad MPPT, 3-phase telemetry, and lithium battery telemetry from PR #1 by Fábio Matavelli.

A comprehensive custom integration for Home Assistant to monitor your Felicity Solar setup. This integration securely connects to the Shine Felicity Solar OpenAPI to fetch real-time telemetry for your **T-REX hybrid inverters**, **High Frequency (HF) / Low Frequency (LF) / IVGM inverters**, and **Lithium Battery Packs (BMS)**, automatically creating native Home Assistant sensors and supporting the built-in Energy Dashboard.

---

## ✨ Features

- **UI Configuration & Auto-Discovery:** Seamless setup via the Home Assistant UI (no YAML required). Automatically discovers all inverters and batteries linked to your account.
- **Dynamic Model & Firmware Identification:** Detects the exact inverter model (e.g., `Felicity T-Rex-6Klp1G01`) and displays hardware firmware version (`sw_version`) in the HA Device Registry.
- **Solar Tracking (Dual & Quad MPPT):**
  - Dedicated sensors for strings **PV1 & PV2**, plus optional **PV3 & PV4** (Voltage, Current, Power).
  - **PV Total Power** smart calculation (automatically sums active strings if total power is missing).
- **Rated Power Sensor (kW):** Automatically normalized in kilowatts (`kW`) with auto-scaling and fallback regex parsing from model name.
- **Inverter Work Mode Sensor:** Real-time human-readable operating states (`Power On`, `Standby`, `Bypass`, `Off-Grid`, `Fault`, `Line Mode`, `PV Charge`, `Gen Mode`, `Turn Off`).
- **3-Phase & Grid Telemetry:** Monophase and 3-Phase (L1, L2, L3) voltages and powers for both Grid and Backup Loads.
- **External CT Clamp & Generator:** Monitors external CT power (`ctPower`), home load (`meterPower`), and generator metrics (`genPower`, `genFrequency`).
- **Active Alarms & Diagnostics:** Real-time active warning counter and latest diagnostic message from `/openApi/data/deviceDataWarn/`.
- **Extended Lithium Battery Pack Telemetry (PR #1):**
  - Voltage, Current, SOC, SOH, and BMS Power.
  - Charging state (`Charging`, `Discharging`, `Idle`, `Unknown`).
  - Cell temperatures (4 individual cell sensors, min & max temperatures).
  - Individual cell voltages (min and max cell millivolts).
  - Charge & discharge voltage limits, capacity (Ah), remaining energy (kWh), and WiFi signal strength (dBm).
- **Hardened Authentication & Session Management:**
  - Automated **Refresh Token** (`/openApi/sec/refreshToken`) renewal to prevent unnecessary RSA scraping.
  - Granular API error code handling (`999`/`998` auto-reconnect, `1002006` wrong password, `1002001` inactive account).
- **100% Home Assistant Energy Dashboard Ready:** Features `total_increasing` energy sensors (`energyPvToday`, `totalEnergy`) ready to plug directly into the Energy Dashboard.

---

## 🛠️ Installation

### Method 1: HACS (Recommended)

1. Open Home Assistant and navigate to **HACS**.
2. Click the three dots in the top right corner and select **Custom repositories**.
3. Add repository: `https://github.com/smilebob/felicity_solar_hacs` with Category: **Integration**.
4. Click **Add**, find **Felicity Solar (Smilebob Edition)** in the list, and click **Download**.
5. **Restart Home Assistant**.

### Method 2: Manual Installation

1. Download the latest release from [Releases](https://github.com/smilebob/felicity_solar_hacs/releases).
2. Copy the `custom_components/felicity_solar` directory into your Home Assistant `/config/custom_components/` directory.
3. **Restart Home Assistant**.

---

## ⚙️ Configuration

1. In Home Assistant, go to **Settings** > **Devices & Services**.
2. Click **+ Add Integration** in the bottom right corner.
3. Search for **Felicity Solar**.
4. Enter your Shine Felicity Solar credentials (Email and Password).
5. The integration will authenticate, initialize session tokens, and automatically register your devices!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Original Author & Credits

### 🌟 Original Creator
This integration was originally conceived, designed, and created by **Matheus Tavares Trindade**:
- **GitHub:** [@matheustavarestrindade](https://github.com/matheustavarestrindade)
- **LinkedIn:** [Matheus Tavares Trindade](https://www.linkedin.com/in/matheus-tavares-trindade/)
- **Website:** [matheustavarestrindade.com](https://matheustavarestrindade.com)
- **Original Repository:** [matheustavarestrindade/felicity_solar_hacs](https://github.com/matheustavarestrindade/felicity_solar_hacs)

### 🤝 Extended Fork Maintainers & Contributors
- **[Pierre / @smilebob](https://github.com/smilebob)** (Smilebob Edition): Maintenance, OpenAPI hardening, dynamic model & firmware identification, Dual/Quad MPPT, 3-phase, CT clamp, and work mode support.
- **[Fábio Matavelli / @fabiomatavelli](https://github.com/fabiomatavelli)**: Additional lithium battery telemetry enhancements (PR #1).

