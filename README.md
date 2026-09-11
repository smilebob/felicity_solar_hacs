# ☀️ Felicity Solar, FSolar & FelicityESS for Home Assistant (HACS Integration)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/smilebob/felicity_solar_hacs)
[![GitHub Release](https://img.shields.io/github/v/release/smilebob/felicity_solar_hacs?style=for-the-badge&color=brightgreen)](https://github.com/smilebob/felicity_solar_hacs/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![HA Compatibility](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-blue.svg?style=for-the-badge&logo=home-assistant)](https://www.home-assistant.io)
[![Python Version](https://img.shields.io/badge/Python-3.12%2B-yellow.svg?style=for-the-badge&logo=python)](https://www.python.org)

> [!NOTE]
> **Community Extended Fork & Attribution**  
> This integration is an enhanced community fork based on the foundation created by **[Matheus Tavares Trindade](https://github.com/matheustavarestrindade/felicity_solar_hacs)**.  
> This **Smilebob Edition** adds extensive enterprise & community features and was largely **vibe coded with [Antigravity](https://deepmind.google/) (Google DeepMind's agentic AI coding assistant)**: OpenAPI hardening, dynamic model & firmware identification, Dual/Quad MPPT, 3-phase EPS/Grid telemetry, battery charge/discharge decomposition, configurable polling options, full Home Assistant Energy Dashboard integration, and extended BMS cell diagnostics.

---

## 🌟 Overview: The Ultimate Felicity Solar / FSolar / FelicityESS Integration

Welcome to the most complete **Home Assistant integration** for **Felicity Solar (FelicitySolar)**, **FSolar**, and **FelicityESS** energy systems! 

Whether you manage your solar installation through the **Shine Felicity Solar cloud**, the **FSolar app**, or the **FelicityESS mobile application**, this custom component communicates directly with the cloud OpenAPI backend (`shine-api.felicitysolar.com`) to bring full telemetry, diagnostics, and bidirectional remote control directly into **Home Assistant (HACS)**.

Monitor your **T-REX hybrid inverters**, **High-Frequency (HF) / Low-Frequency (LF) inverters**, and **Lithium Battery Packs (BMS 48V / 51.2V LiFePO4)** in real-time, with automatic discovery, zero YAML configuration, and seamless plug-and-play setup with the **Home Assistant Energy Dashboard**.

---

## 📱 Compatibility: Felicity Solar, FSolar & FelicityESS Ecosystems

If you use any of the official Felicity monitoring applications or portals, your setup is **100% compatible**:

| Platform / App | Compatibility | Connection Method |
| :--- | :---: | :--- |
| **Shine Felicity Solar** (`shine.felicitysolar.com`) | ✅ Supported | Cloud OpenAPI REST API (Email + Password) |
| **FSolar App** (iOS / Android) | ✅ Supported | Shared cloud backend accounts |
| **FelicityESS App** (iOS / Android) | ✅ Supported | Shared cloud backend accounts |
| **Felicity Shine Cloud Web Portal** | ✅ Supported | Automatic device and telemetry discovery |

### ⚡ Supported Hardware
* **Hybrid Inverters**: Felicity Solar T-REX Series (`T-REX-6KLP1G01`, `T-REX-8K`, `T-REX-10K`, `T-REX-12KLP1G01`, etc.), IVGM series, single-phase & three-phase hybrid inverters.
* **Off-Grid & Solar Inverters**: High Frequency (HF) & Low Frequency (LF) inverters.
* **Lithium Battery Storage (BMS)**: 48V / 51.2V LiFePO4 Battery Packs (`LPBF`, `LPBA`, `FLS48100`, `LUX-X-48100LG01`, and all CAN/RS485 connected BMS units).
* **Grid & Dataloggers**: WiFi/Ethernet smart dataloggers, external CT clamps, Eastron/Chint energy meters, and Smart Load ports.

---

## ✨ Features & Capabilities

### ⚡ 1. Solar Production & Smart Tracking (Dual & Quad MPPT)
* Dedicated individual string telemetry: **PV1, PV2, PV3, and PV4** (Voltage, Current, Power).
* **PV Total Power** intelligent calculation: dynamically sums active string powers if aggregate telemetry is missing.
* **Rated Power (kW)**: Automatically scaled in kilowatts (`kW`) with regex fallback from the inverter model nameplate.
* **Inverter Work Mode**: Real-time human-readable operating states (`Power On`, `Standby`, `Bypass`, `Off-Grid`, `Fault`, `Line Mode`, `PV Charge`, `Gen Mode`, `Turn Off`).

### 🔋 2. Lithium Battery Pack & BMS Telemetry
* **Global Battery Metrics**: Voltage, Current, SOC (%), SOH (%), Power (W), Capacity (Ah), and Rated Energy (kWh).
* **Remaining Battery Energy (kWh)**: Multi-key fallback cascade, preventing false 0 values.
* **BMS Communication Status**: Clear `Connected` / `Disconnected` status sensor for real-time link monitoring.
* **Aggregated Cell Monitoring**: Max Cell Voltage (mV), Min Cell Voltage (mV), Max/Min Cell probe numbers, and `dV Cells` (delta voltage in mV for cell balancing health).
* **Individual Cell Voltages (Cells 1 to 16)**: Automatic V/mV normalization, string unit stripping, and clean availability handling.
* **BMS Operating Limits**: Dynamic charge voltage limit (`BMSLCVolt`), discharge voltage limit (`BMSLDVolt`), charge current limit (`BMSLCCurr`), and discharge current limit (`BMSLDCurr`).
* **Thermal Probes**: Cell temperatures 1–4, plus min/max pack temperatures.

### 📊 3. 100% Home Assistant Energy Dashboard Ready
All production and grid exchange sensors use `state_class: total_increasing` and `device_class: energy` for instant 1-click inclusion in your **Home Assistant Energy Dashboard**:
* **Solar Production**: `energyPvToday`, `energyPvTotal`.
* **Battery Charge & Discharge**: `energyBatteryChargeToday`, `energyBatteryChargeTotal`, `energyBatteryDischargeToday`, `energyBatteryDischargeTotal`.
* **Grid Feed-in / Export**: `energyGridFeedToday`, `energyGridFeedTotal`.
* **Grid Import / Consumption**: `energyGridImportToday`, `energyGridImportTotal`.
* **Home Load Consumption**: `energyLoadToday`, `energyLoadTotal`.

### 🎛️ 4. Full Remote Control & Inverter Parameters (OpenAPI)
Control inverter parameters directly from Home Assistant cards, automations, or Node-RED:
* **Select Entities (`select`)**:
  * `Work Mode` (General, Backup, Eco, Gen)
  * `Energy Priority` (Battery First, Load First)
  * `Zero Export Mode` (To Load, To CT)
  * `AC Output Frequency` (50 Hz, 60 Hz)
  * `Battery Model Type` (User Defined, Lithium, LPBF, LPBA)
* **Number Entities (`number`)**:
  * Battery Max Charge Current (1–200 A) & Discharge Current (5–200 A)
  * On-Grid Discharge Depth SOC (10–100%) & Off-Grid Discharge Depth SOC (0–100%)
  * Charge Voltage (48–60 V) & Floating Charge Voltage (48–60 V)
  * Grid Charge Current Limit & Generator Charge Current Limit
  * Zero-Export Adjustment Power & Generator Auto Start/Stop SOC
* **Switch Entities (`switch`)**:
  * `Grid Charge Enable`, `Buzzer Enable`, `LCD Backlight Enable`, `Inverter Remote Standby`, `AC Output Relay Control`, `Anti-Islanding Protection`, `Grid Peak Shaving`, `Time of Use (TOU) Enable`, `Generator Charge Enable`, `Overload Auto-Reset`.

### 🔌 5. Home Assistant Services (`services.yaml`)
* `felicity_solar.set_device_setting`: Send custom parameter payloads to your inverter.
* `felicity_solar.set_eco_rule`: Program automated Time-of-Use (TOU) or ECO schedules (Rules 1 to 6) with customizable start/stop times, power, and target SOC.
* `felicity_solar.query_energy_data`: Query historical production/consumption aggregates by day, month, year, or lifetime.
* `felicity_solar.query_history_data`: Query real-time historical snapshot records.

### 🌐 6. Smart Load, Generator & 3-Phase Grid Telemetry
* **3-Phase Metrics**: Monophase and 3-Phase (L1, L2, L3) voltages, currents, and powers for both Grid and Backup (EPS) ports.
* **Smart Load Port**: Dedicated power, voltage, current, frequency, and daily/total energies.
* **Generator Support**: Generator active power, voltage, frequency, and daily/total generator production metrics.

### 🛡️ 7. Reliability, Internationalization & Polish
* **Configurable Polling Interval**: Adjust update frequency from 10 to 600 seconds via the Home Assistant Options Flow (default 120s).
* **Multi-Language Support**: Full native translations in **English** and **French** (`en`, `fr`).
* **Silent & Resilient Logging**: Intelligent log throttling eliminates log spam when individual BMS cell telemetry is not streamed by the cloud.
* **Auto-Reauthentication (`reauth`)**: Automatic prompt to update credentials if your password changes.

---

## 🚀 Installation

### Option A: Via HACS (Recommended)

1. Make sure you have **[HACS](https://hacs.xyz/)** installed in Home Assistant.
2. In Home Assistant, open **HACS** > **Integrations**.
3. Click the top-right menu (three vertical dots) and select **Custom repositories**.
4. Paste the repository URL:
   ```text
   https://github.com/smilebob/felicity_solar_hacs
   ```
   Select **Integration** as the category and click **Add**.
5. Find **Felicity Solar (Smilebob Edition)** in HACS and click **Download**.
6. **Restart Home Assistant**.

### Option B: Manual Installation

1. Download the latest release `.zip` or clone this repository:
   ```bash
   git clone https://github.com/smilebob/felicity_solar_hacs.git
   ```
2. Copy the `custom_components/felicity_solar` folder into your Home Assistant directory:
   `<config>/custom_components/felicity_solar`
3. **Restart Home Assistant**.

---

## ⚙️ Configuration

1. In Home Assistant, navigate to **Settings** > **Devices & Services**.
2. Click **+ Add Integration** in the bottom-right corner.
3. Search for **Felicity Solar** (or **FelicitySolar / FSolar / FelicityESS**).
4. Enter your credentials:
   * **Email**: The email address of your Shine Felicity Solar / FSolar / FelicityESS account.
   * **Password**: Your account password.
5. Click **Submit**. Your inverters and battery packs will be automatically discovered with all sensors created!

---

## 📈 Home Assistant Energy Dashboard Setup

To configure the native **Energy Dashboard** in Home Assistant (**Settings** > **Dashboards** > **Energy**):

| Energy Section | Recommended Entity |
| :--- | :--- |
| **Electricity grid (Grid consumption)** | `sensor.felicity_inverter_<SN>_grid_import_today` or `_total` |
| **Electricity grid (Return to grid)** | `sensor.felicity_inverter_<SN>_grid_feed_in_today` or `_total` |
| **Solar panels (Solar production)** | `sensor.felicity_inverter_<SN>_solar_energy_today` or `_total` |
| **Battery systems (Energy going in)** | `sensor.felicity_inverter_<SN>_battery_charge_energy_today` or `_total` |
| **Battery systems (Energy coming out)** | `sensor.felicity_inverter_<SN>_battery_discharge_energy_today` or `_total` |

---

## ❓ Frequently Asked Questions (FAQ)

### Does this integration work with the FSolar or FelicityESS mobile apps?
**Yes, absolutely.** The FSolar app, FelicityESS app, and Shine Felicity Solar web portal all share the same cloud backend. Your existing login credentials work directly with this integration.

### Why do some individual battery cell voltages show as "Unavailable"?
Certain Felicity Solar battery packs (or specific firmware revisions) stream aggregate BMS metrics (`maxCellVoltage`, `minCellVoltage`, `dV Cells`, `bmsCommunicationStatus`), but do not transmit individual per-cell voltages over the cloud API. The integration detects this cleanly, avoids log spam, and marks unstreamed cells as unavailable while keeping all aggregate metrics fully functional.

### How do I change the polling update frequency?
Go to **Settings** > **Devices & Services** > **Felicity Solar** > **Configure**. You can adjust the update interval anywhere between **10 seconds** and **600 seconds** (default: 120s).

---

## 📄 License

Distributed under the **[MIT License](LICENSE)**.

---

## 👨‍💻 Credits & Author Attribution

### 🌟 Original Creator
This integration was originally conceived, designed, and created by **Matheus Tavares Trindade**:
* **GitHub:** [@matheustavarestrindade](https://github.com/matheustavarestrindade)
* **LinkedIn:** [Matheus Tavares Trindade](https://www.linkedin.com/in/matheus-tavares-trindade/)
* **Website:** [matheustavarestrindade.com](https://matheustavarestrindade.com)
* **Original Repository:** [matheustavarestrindade/felicity_solar_hacs](https://github.com/matheustavarestrindade/felicity_solar_hacs)

### 🤝 Extended Fork Maintainers & Contributors
* **[Pierre / @smilebob](https://github.com/smilebob)** (Smilebob Edition): Architecture, maintenance, enterprise extensions, and testing.
* **Google Antigravity**: Agentic AI pair programmer that vibe coded the major extensions, diagnostics, OpenAPI refactoring, and sensors of this edition.
* **[Fábio Matavelli / @fabiomatavelli](https://github.com/fabiomatavelli)**: Lithium battery telemetry contributions (PR #1).
* **[viprosite/vue-element-admin-simple](https://github.com/viprosite/vue-element-admin-simple)**: Essential frontend reference for Felicity Solar dashboard data structures (`actualIVGM.vue`, `actualBattery.vue`).
* **[johanmeijer/grott](https://github.com/johanmeijer/grott)**: Open-source solar telemetry mapping standards.
