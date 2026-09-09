# 📦 Module Memory: Felicity Solar Component (`custom_components/felicity_solar/`)

> **Directory**: `custom_components/felicity_solar/` | **Last Updated**: 2026-09-09

## 🎯 Role & Responsibility
Contains the Home Assistant integration code: Felicity Shine REST API client, DataUpdateCoordinator, UI ConfigFlow, and dynamic sensor entities for inverters and batteries.

---

## 🗂️ Key Files & Components
| File / Module | Role | Key Inputs / Outputs |
| :--- | :--- | :--- |
| [`api.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/api.py) | Felicity Shine REST API Client | Auth RSA PKCS1_v1_5, JWT token `felicitySolarToken.json` |
| [`coordinator.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/coordinator.py) | Polling & Device Discovery | `_async_update_data()`: Extract `modelName`, `ratedPower` (kW), and extended battery telemetry |
| [`sensor.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/sensor.py) | Sensor Platform Entry Point | Dynamic entity instantiation |
| [`sensors_inverter.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/sensors_inverter.py) | Inverter Sensors | Dynamic device info (`modelName`) + `Rated Power` sensor |
| [`sensors_battery.py`](file:///home/pierre/Projets/felicity_solar_hacs/custom_components/felicity_solar/sensors_battery.py) | Battery Sensors | Voltage, Current, SOC, SOH, Power, State, Min/Max Temp, Cell Temps, Voltages, Capacity, WiFi |

---

## ⚠️ Technical Gotchas
- **Dynamic Model Identification**: The coordinator reads the exact model name (`deviceModel`) sent by Felicity Cloud. Do not hardcode `"High Frequency Inverter"` in `sensors_inverter.py`.
