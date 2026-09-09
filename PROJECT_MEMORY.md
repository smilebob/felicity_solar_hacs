# 🧠 Global Project Memory: Felicity Solar (Smilebob Edition)

> **Last Updated**: 2026-09-09 | **Status**: Active / Production (Dynamic Model Support, Battery Sensors & Rated Power OK)

## 🎯 Overview & Goal
- **Description**: Custom Home Assistant component (HACS) to monitor Felicity Solar equipment (T-REX-6KLP1G01 hybrid inverters with dual MPPT, HF/LF inverters, and Lithium Battery Packs) with dynamic model identification and Rated Power sensor support.
- **GitHub Repository**: `https://github.com/smilebob/felicity_solar_hacs`
- **Tech Stack**: Home Assistant Core, Python 3.12+, `aiohttp`, `PyCryptodome`, `PyJWT`
- **Global Entry Point**: `custom_components/felicity_solar/__init__.py`

---

## 🚀 Essential Commands
| Action | Command | Note |
| :--- | :--- | :--- |
| **Syntax Verification** | `python3 -m py_compile custom_components/felicity_solar/*.py` | Standalone validation |
| **Git Push** | `git push origin main` | Automatic HACS deployment |

---

## 🗺️ Component Index (Mapping)
| Directory / Module | Role & Responsibility | Detailed Documentation |
| :--- | :--- | :--- |
| `custom_components/felicity_solar/` | Home Assistant integration component (API, Coordinator, Sensors, ConfigFlow) | [MEMORY.md](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/MEMORY.md) |

---

## 📌 Current State & Features Implemented
### ✅ Implemented & Verified
- [x] **Phase 1 OpenAPI Hardening Complete**: Refresh token support (`/openApi/sec/refreshToken`), granular API error codes, hardware firmware version (`sw_version`).
- [x] **Phase 2 Advanced Telemetry Complete**:
  - **Quad MPPT Support**: `pv3` and `pv4` voltage, current, and power.
  - **3-Phase Grid & Backup Telemetry**: L1, L2, L3 voltages and powers (`acGridPowerL1..3`, `acBackupPowerL1..3`).
  - **External CT Clamp & Generator**: `ctPower`, `meterPower`, `genPower`, `genVoltage`, `genFrequency`.
  - **Alarm & Fault Sensors (`/openApi/data/deviceDataWarn/{deviceSn}`)**: `warnCount` ("Active Warning Count") and `lastWarnMsg` ("Last Warning Message").
- [x] **Phase 3 100% OpenAPI Remote Control & Services Complete**:
  - **`select` Platform (5 entities)**: `operatedMode`, `energyPriority`, `zeroExportFunction`, `acOutputRatedFrequency`, `batteryModel`.
  - **`number` Platform (11 entities)**: `batteryMaxChargedCurrent`, `batteryMaxDischargeCurrent`, `batteryOnGridDischargeDepthSoc`, `batteryOffGridDischargeDepthSoc`, `batteryChargedVoltage`, `batteryFloatingChargedVoltage`, `gridChargeCurrent`, `genChargeCurrent`, `genAutoStartChargeSoc`, `genAutoExitChargeSoc`, `zeroExportAdjustmentPower`.
  - **`switch` Platform (10 entities)**: `gridChargeEnable`, `buzzerEnable`, `lcdBacklightEnable`, `remoteOnOffEnable`, `remoteOutputOnOffControl`, `antiIslandingDetectionEnable`, `gridPeakShavingEnable`, `timeOfUseEnable`, `genChargeEnable`, `overLoadProtectionResetEnable`.
  - **Home Assistant Custom Services (`services.yaml`)**: `set_device_setting`, `set_eco_rule`, `query_energy_data`, `query_history_data`.
  - **Historical & Energy API Methods (`api.py`)**: `get_device_energy_data()` and `get_device_history_data()`.
- [x] **100% Home Assistant Energy Dashboard Compatibility** (`device_class: power`, `state_class: measurement`).
- [x] Publication and hosting on GitHub public repository `https://github.com/smilebob/felicity_solar_hacs`.

---

## ⚠️ Technical Gotchas
- **SSL Certificate Chain**: Felicity Solar servers omit intermediate CAs; all sessions use `create_felicity_client_session()` with SSL verification disabled for Felicity domains only.
- **Dynamic Device Model**: `modelName` is dynamically parsed from `deviceModel`, `model` or `productTypeEnum`.
- **HA Energy Rules**: To appear in the HA Energy Dashboard power dropdown, an entity MUST have both `device_class: power` AND `state_class: measurement`.
- **Remote Setting Targets**: All remote parameter controls and custom services target inverter serial numbers, not standalone battery pack serial numbers.
