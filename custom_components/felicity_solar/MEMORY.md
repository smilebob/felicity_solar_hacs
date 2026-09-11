# 📦 Module Memory: Felicity Solar Component (`custom_components/felicity_solar/`)

> **Directory**: `custom_components/felicity_solar/` | **Last Updated**: 2026-09-09

## 🎯 Role & Responsibility
Contains the Home Assistant integration code: Felicity Shine REST API client, DataUpdateCoordinator, UI ConfigFlow, and dynamic sensor entities for inverters and batteries.

---

## 🗂️ Key Files & Components
| File / Module | Role | Key Inputs / Outputs |
| :--- | :--- | :--- |
| [`__init__.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/__init__.py) | Component Entry Point & Services | Registers platforms (sensor, select, number, switch) & 4 HA services |
| [`api.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/api.py) | Felicity Shine REST API Client | RSA login, JWT refresh token, telemetry snapshots, warnings, settings, energy queries |
| [`coordinator.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/coordinator.py) | Polling & Device Discovery | `_async_update_data()`: Inverter & battery telemetry + remote settings queries |
| [`config_flow.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/config_flow.py) | UI Configuration Flow | Email, password, update interval setup |
| [`sensor.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/sensor.py) | Sensor Platform | Dynamic sensor entity factory |
| [`sensors_inverter.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/sensors_inverter.py) | Inverter Sensors (105) | Grid Feed-In/Import energies (HA Energy Dashboard), daily/monthly/yearly battery & PV energies, Smart Load port, generator energies & L2-L3 powers, meter status, EMS capacity, native work mode, plus all previous telemetry |
| [`sensors_battery.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/sensors_battery.py) | Battery Sensors (49) | Voltage, current, SOC, SOH, individual cell voltages 1–16 (mV with V/mV auto-detect & clean availability), cell min/max mV & probe IDs, dV Cells (mV), cell temps (1-4), BMS charge/discharge current limits, sanitized cell count, battery type, BMS status, connected inverter SN |
| [`select.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/select.py) | Select Controls (5) | `Work Mode`, `Energy Priority`, `Zero Export Mode`, `AC Output Freq`, `Battery Model` |
| [`number.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/number.py) | Number Controls (11) | Charge/discharge currents, discharge depth SOC, charge/float volts, generator limits |
| [`switch.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/switch.py) | Switch Controls (10) | `Grid Charge`, `Buzzer`, `LCD Backlight`, `Remote Standby`, `AC Output Relay`, etc. |
| [`services.yaml`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/services.yaml) | HA Service Schemas | UI definitions for `set_device_setting`, `set_eco_rule`, `query_energy_data`, `query_history_data` |

---

## 🔄 Dependencies & Data Flow
- **External API**: Shine Felicity Solar OpenAPI (`https://shine-api.felicitysolar.com`).
- **Data Flow**:
  - `FelicitySolarCoordinator` polls `get_device_snapshot()`, `get_device_basic_info()`, `get_device_warnings()`, and `get_device_settings()`.
  - Stored in `coordinator.data[device_sn]` with separate `"data"` (telemetry) and `"settings"` (controls) dictionaries.
  - Entities inherit from `CoordinatorEntity` and update state reactively or optimistically.
  - Controls dispatch writes to `FelicitySolarAPI.set_device_setting()`, followed by `async_request_refresh()`.

---

## ⚠️ Technical Gotchas
- **SSL Certificate Chain**: Felicity servers serve leaf certificates missing intermediate CAs (`SSLCertVerificationError`). All HTTP calls must use `create_felicity_client_session()` which disables verification specifically for this integration.
- **Dynamic Model Identification**: Never hardcode model strings; read dynamically from `deviceModel` or `modelName`.
- **API Return Codes**: `998`/`999` (token expired, triggers re-auth), `1006051` (device unreachable), `2001528` (permission denied on OpenAPI layer; automatically halts unpermitted calls to silence log spam).
- **Target Inverter Controls**: Parameter writes (`/openApi/cmd/deviceSetting`) target inverter serial numbers, not standalone battery pack serial numbers. Control entities are instantiated only when settings are permitted and available.
- **Update Interval**: Default is 120s with immediate query upon integration boot; configurable via Home Assistant Options Flow.
