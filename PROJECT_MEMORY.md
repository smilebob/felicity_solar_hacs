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
- [x] Official rename to **Felicity Solar (Smilebob Edition)**.
- [x] Complete support for **Felicity T-REX-6KLP1G01** inverters and all hybrid/HF/LF models.
- [x] **Dynamic inverter model display** in Home Assistant device registry (e.g. `Felicity T-Rex-6Klp1G01` instead of `High Frequency Inverter`).
- [x] **`Rated Power`** sensor in **`kW`** (`native_unit_of_measurement=UnitOfPower.KILO_WATT`) with auto-scaling (Watts -> kW) and Regex fallback parsing from model name (e.g., `T-REX-6KLP1G01` -> `6.0 kW`).
- [x] Support for **2 solar strings / MPPT trackers (PV1 & PV2)**.
- [x] **Extended Lithium Battery Pack Sensors** (Integrated PR #1 from `matheustavarestrindade` / `@fabiomatavelli`): Power, Charging State, Min/Max Temp, Cell Temperatures (1-4), Cell Voltages, Capacity (Ah), WiFi Signal (dBm), Charge/Discharge Limit Voltages.
- [x] **100% Home Assistant Energy Dashboard Compatibility** (`device_class: power`, `state_class: measurement`).
- [x] Publication and hosting on GitHub public repo `https://github.com/smilebob/felicity_solar_hacs`.

---

## ⚠️ Technical Gotchas
- **Dynamic Device Model**: `modelName` is dynamically parsed from `deviceModel`, `model` or `productTypeEnum`.
- **HA Energy Rules**: To appear in the HA Energy Dashboard power dropdown, an entity MUST have both `device_class: power` AND `state_class: measurement`.
