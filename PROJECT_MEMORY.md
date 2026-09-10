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
  - **Battery Cell Telemetry**: Individual cell voltages 1 to 16 (`cellVolt1`–`cellVolt16`), `maxCellVoltage`, `minCellVoltage`, min/max cell number indices (`minCellVoltageNum`, `maxCellVoltageNum`), and `dvCells` ("dV Cells" delta voltage in mV). Automatic normalization from V/mV and dual-source extraction (`cellVolt{i}` / `bmsVoltageList`).
- [x] **Phase 3 100% OpenAPI Remote Control & Services Complete**:
  - **`select` Platform (5 entities)**: `operatedMode`, `energyPriority`, `zeroExportFunction`, `acOutputRatedFrequency`, `batteryModel`.
  - **`number` Platform (11 entities)**: `batteryMaxChargedCurrent`, `batteryMaxDischargeCurrent`, `batteryOnGridDischargeDepthSoc`, `batteryOffGridDischargeDepthSoc`, `batteryChargedVoltage`, `batteryFloatingChargedVoltage`, `gridChargeCurrent`, `genChargeCurrent`, `genAutoStartChargeSoc`, `genAutoExitChargeSoc`, `zeroExportAdjustmentPower`.
  - **`switch` Platform (10 entities)**: `gridChargeEnable`, `buzzerEnable`, `lcdBacklightEnable`, `remoteOnOffEnable`, `remoteOutputOnOffControl`, `antiIslandingDetectionEnable`, `gridPeakShavingEnable`, `timeOfUseEnable`, `genChargeEnable`, `overLoadProtectionResetEnable`.
  - **Home Assistant Custom Services (`services.yaml`)**: `set_device_setting`, `set_eco_rule`, `query_energy_data`, `query_history_data`.
  - **Historical & Energy API Methods (`api.py`)**: `get_device_energy_data()` and `get_device_history_data()`.
- [x] **Phase 4 Telemetry Expansion & UI Controls Config**:
  - **Inverter Battery Telemetry**: `batteryPower` ($W$), `batteryChargingPower` ($W$, $\ge 0$), `batteryDischargingPower` ($W$, $\ge 0$), `batteryVoltage` ($V$), `batteryCurrent` ($A$), `bmsCommunicationStatus` ("Connected" / "Disconnected"), and Battery Port 2 metrics.
  - **HA Energy Dashboard Integration**: `energyBatteryChargeTotal` ($kWh$), `energyBatteryDischargeTotal` ($kWh$), `energyLoadToday` ($kWh$), `energyLoadTotal` ($kWh$), `energyPvToday`, and `energyPvTotal` ($kWh$) with `state_class: total_increasing`.
  - **Full Grid & Backup EPS Currents/Voltages**: L1-L3 currents, L2-L3 backup voltages, backup output frequency, and apparent power ($VA$).
  - **Configurable Polling Interval**: UI Options Flow (10-600s, default 120s) with immediate first query upon HA boot.
  - **Graceful Permission Degradation**: Code 2001528 handling to prevent log spam and skip unpermitted controls for standard accounts.
  - **README Attribution**: Updated to acknowledge vibe coding by Google Antigravity.
- [x] **Phase 5 Full Telemetry & Battery Cell Optimization (Option B)**:
  - **Individual Battery Cell Voltages (1-16)**: `cellVolt1` through `cellVolt16` in mV with automatic V/mV normalization, string unit stripping (`V`/`mV`), JSON/CSV list decoders, multi-key aliases (`cellVolt01`, `cellVoltage01`, etc.), and refined availability check (entities stay available unless cell index exceeds physical `cellCount` on 15S packs). Added diagnostic logging (`_LOGGER.info` / `_LOGGER.debug`) of battery snapshot keys.
  - **BMS Current Limits & Metadata**: `chargeLimitCurrent` (`BMSLCCurr`), `dischargeLimitCurrent` (`BMSLDCurr`), `cellCount` (`cellNumber`), probe indices (`maxCellTempNum`, `minCellTempNum`), `batteryType` (`batTyStr`), and `connectedInverterSn` (`invSn`).
  - **Complete HA Energy Dashboard Integration**: Grid feed-in energy (`energyGridFeedToday`, `energyGridFeedTotal`), Grid import energy (`energyGridImportToday`, `energyGridImportTotal`), daily battery energy (`energyBatteryChargeToday`, `energyBatteryDischargeToday`), and multi-case cumulative energy (`eBatCharTotal` / `ebatCharTotal` / `bat1CharTotal`, `eBatDisCharTotal` / `ebatDischarTotal` / `bat1DisCharTotal`) with `TOTAL_INCREASING`.
  - **Smart Load Port Telemetry**: `smartLoadPower`, `smartLoadVoltage`, `smartLoadCurrent`, `smartLoadFrequency`, `smartLoadEnergyToday`, `smartLoadEnergyTotal` (disabled by default).
  - **Generator & Periodic Aggregates**: Generator energies (`energyGenToday`, `energyGenTotal`, `genPowerL2`, `genPowerL3`), periodic monthly/yearly metrics (`energyPvMonth`, `energyPvYear`, `energyLoadMonth`, `energyLoadYear`, `energyGridFeedMonth`, `energyGridFeedYear`, etc.).
  - **Inverter Diagnostics**: `meterLinkStatus`, `totalEmsCapacity` (Ah), and `workModeStr`.
- [x] Publication and hosting on GitHub public repository `https://github.com/smilebob/felicity_solar_hacs`.

---

## ⚠️ Technical Gotchas
- **SSL Certificate Chain**: Felicity Solar servers omit intermediate CAs; all sessions use `create_felicity_client_session()` with SSL verification disabled for Felicity domains only.
- **Dynamic Device Model**: `modelName` is dynamically parsed from `deviceModel`, `model` or `productTypeEnum`.
- **HA Energy Rules**: To appear in the HA Energy Dashboard power dropdown, an entity MUST have both `device_class: power` AND `state_class: measurement`.
- **Remote Setting Targets**: All remote parameter controls and custom services target inverter serial numbers, not standalone battery pack serial numbers. Control entities are instantiated only when settings are permitted and available.
- **OpenAPI Permission 2001528**: Standard end-user accounts lack OpenAPI access; unpermitted queries are automatically silenced after one notification to avoid log spam.
- **Update Interval**: Default is 120s with immediate query upon integration boot; configurable via Home Assistant Options Flow.
