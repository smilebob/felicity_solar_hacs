import json
import logging
import re
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant

from .api import FelicitySolarAPI, DeviceTypeEnum, create_felicity_client_session
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


def _safe_float(value, default=0.0):
    """Convert value to float, returning default if value is None or invalid."""
    try:
        return float(value) if value is not None and value != "" else default
    except (ValueError, TypeError):
        return default


def _safe_int(value, default=0):
    """Convert value to int, returning default if value is None or invalid."""
    try:
        return int(value) if value is not None and value != "" else default
    except (ValueError, TypeError):
        return default


def _parse_cell_voltage(value):
    """Safely parse cell voltage to millivolts (mV).

    - Strips units like 'V', 'mV', whitespace, and replaces ',' with '.'.
    - If value is in Volts (e.g. 3.325 < 100), convert to mV (3325.0).
    - If value is already in mV (e.g. 3325 >= 100), keep as mV (3325.0).
    - If value is None, 0, or invalid, return None (avoids displaying false 0 mV).
    """
    if value is None:
        return None
    if isinstance(value, str):
        clean_str = re.sub(r"(?i)\s*(?:mv|v)\s*$", "", value.strip()).replace(",", ".").strip()
        v = _safe_float(clean_str, default=None)
    else:
        v = _safe_float(value, default=None)

    if v is None or v <= 0:
        return None
    if v < 100:
        return round(v * 1000.0, 1)
    return round(v, 1)


def _extract_voltage_list(snapshot: dict) -> list:
    """Extract list of cell voltages from possible list fields in snapshot."""
    for key in (
        "bmsVoltageList",
        "cellVoltList",
        "cellVoltageList",
        "voltageList",
        "cellVoltages",
        "cellList",
        "cells",
    ):
        val = snapshot.get(key)
        if not val:
            continue
        if isinstance(val, list):
            return val
        if isinstance(val, str):
            val_str = val.strip()
            if val_str.startswith("[") and val_str.endswith("]"):
                try:
                    parsed = json.loads(val_str)
                    if isinstance(parsed, list):
                        return parsed
                except Exception:
                    pass
            for sep in (",", ";"):
                if sep in val_str:
                    items = [x.strip() for x in val_str.split(sep) if x.strip()]
                    if items:
                        return items
    return []


def _get_cell_raw_value(snapshot: dict, cell_idx: int, voltage_list: list):
    """Retrieve raw cell voltage value from snapshot dictionary or voltage list."""
    candidate_keys = (
        f"cellVolt{cell_idx}",
        f"cellVolt{cell_idx:02d}",
        f"cellvolt{cell_idx}",
        f"cellvolt{cell_idx:02d}",
        f"cellVoltage{cell_idx}",
        f"cellVoltage{cell_idx:02d}",
        f"cellvoltage{cell_idx}",
        f"cellvoltage{cell_idx:02d}",
        f"cell_volt_{cell_idx}",
        f"cell_volt{cell_idx}",
        f"bmsVolt{cell_idx}",
        f"bmsVolt{cell_idx:02d}",
        f"bms_volt_{cell_idx}",
        f"volt{cell_idx}",
        f"volt{cell_idx:02d}",
        f"cell{cell_idx}",
        f"cell{cell_idx:02d}",
    )
    for k in candidate_keys:
        if k in snapshot:
            v = snapshot[k]
            if v is not None and v != "" and v != 0 and v != "0":
                return v

    # Fallback to voltage list if key was missing or 0/None
    if len(voltage_list) >= cell_idx:
        v = voltage_list[cell_idx - 1]
        if v is not None and v != "" and v != 0 and v != "0":
            return v

    return None


def _calculate_battery_remaining_energy(
    snapshot: dict,
    batt_soc: int | None,
    batt_volt: float | None,
    batt_capacity: float | None,
    rated_energy_kwh: float | None,
) -> float | None:
    """Safely determine or calculate battery remaining energy in kWh.

    Precedence:
    1. Direct API keys for remaining energy (remainingBatteryEnergy, remainEnergy, eBatRemain, etc.)
    2. Direct API keys for remaining capacity in Ah (remainCap, etc.) multiplied by voltage
    3. Derived from ratedEnergy (kWh) and SOC: ratedEnergy * (SOC / 100)
    4. Derived from battCapacity (Ah), battVolt (V) and SOC: (Ah * V / 1000) * (SOC / 100)
    5. Returns None if undetermined (avoids displaying false 0 kWh).
    """
    # 1. Direct API keys for remaining energy
    direct_energy_keys = (
        "remainingBatteryEnergy1",
        "remainingBatteryEnergy",
        "remainBatteryEnergy1",
        "remainBatteryEnergy",
        "remainingEnergy",
        "remainEnergy",
        "eBatRemain",
        "ebatRemain",
        "surplusEnergy",
        "surplusBatteryEnergy",
        "restEnergy",
        "bmsRemainEnergy",
        "batRemainEnergy",
        "remainingPower",
    )
    for k in direct_energy_keys:
        if k in snapshot:
            val = _safe_float(snapshot[k], default=None)
            if val is not None and val > 0:
                # If value is in Wh (> 100), convert to kWh
                return round(val / 1000.0, 2) if val > 100 else round(val, 2)

    # 2. Direct API keys for remaining capacity in Ah
    direct_cap_keys = (
        "remainCap",
        "remainingCapacity",
        "remainCapacity",
        "surplusCapacity",
        "surplusCap",
        "restCap",
        "bmsRemainCapacity",
        "bmsRemainingCapacity",
        "restCapacity",
    )
    for k in direct_cap_keys:
        if k in snapshot:
            cap_val = _safe_float(snapshot[k], default=None)
            if cap_val is not None and cap_val > 0 and batt_volt is not None and batt_volt > 0:
                return round((cap_val * batt_volt) / 1000.0, 2)

    # 3. Derive from ratedEnergy and SOC
    if rated_energy_kwh is not None and rated_energy_kwh > 0 and batt_soc is not None and batt_soc >= 0:
        return round(rated_energy_kwh * (batt_soc / 100.0), 2)

    # 4. Derive from battCapacity (Ah), battVolt (V) and SOC
    if (
        batt_capacity is not None
        and batt_capacity > 0
        and batt_volt is not None
        and batt_volt > 0
        and batt_soc is not None
        and batt_soc >= 0
    ):
        nominal_kwh = (batt_capacity * batt_volt) / 1000.0
        return round(nominal_kwh * (batt_soc / 100.0), 2)

    return None


WORK_MODE_MAP = {
    0: "Power On",
    1: "Standby",
    2: "Bypass",
    3: "Off-Grid",
    4: "Fault",
    5: "Line Mode",
    6: "PV Charge",
    7: "Gen Mode",
    8: "Turn Off",
}


class FelicitySolarCoordinator(DataUpdateCoordinator):
    """Coordinator to fetch data from Felicity Solar."""

    def __init__(self, hass: HomeAssistant, email: str, password: str, update_interval: int):
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=update_interval),
        )
        self._session = create_felicity_client_session(hass)
        self.api = FelicitySolarAPI(
            email=email,
            password=password,
            session=self._session
        )
        self._unsupported_cells_logged: set[str] = set()

    async def _async_update_data(self) -> dict[str, dict]:
        """Fetch data from API for all devices."""
        try:
            _LOGGER.info("Starting data update cycle")

            # Re-auth and load devices if needed
            await self.api.initialize()

            devices_data = {}
            serial_numbers = self.api.get_devices_serial_numbers()

            if not serial_numbers:
                _LOGGER.warning("No devices found — check your Felicity Solar account or credentials")
                return devices_data

            for device_sn in serial_numbers:
                try:
                    snapshot = await self.api.get_device_snapshot(device_sn)
                    basic_info = await self.api.get_device_basic_info(device_sn)
                    warnings = await self.api.get_device_warnings(device_sn)

                    device_type = snapshot.get("productTypeEnum")
                    firmware_version = basic_info.get("firmwareVersion") or snapshot.get("firmwareVersion")
                    warn_count = len(warnings)
                    last_warn_msg = str(warnings[0].get("warnMsg") or warnings[0].get("name") or warnings[0].get("msg", "Normal")) if warnings else "Normal"

                    _LOGGER.info("Snapshot received for device %s (productTypeEnum='%s', firmware='%s', warnings=%d)", device_sn, device_type, firmware_version, warn_count)

                    is_battery = (
                        device_type == DeviceTypeEnum.LITHIUM_BATTERY_PACK
                        or (isinstance(device_type, str) and "BATTERY" in device_type.upper())
                    )

                    if is_battery:
                        state_val = _safe_int(snapshot.get("bmsChargingState"), -1)
                        if state_val == 1:
                            charging_state = "Charging"
                        elif state_val == 0:
                            charging_state = "Idle"
                        elif state_val == 2:
                            charging_state = "Discharging"
                        else:
                            charging_state = "Unknown"

                        max_cell_v = _parse_cell_voltage(snapshot.get("maxVoltage2bms"))
                        min_cell_v = _parse_cell_voltage(snapshot.get("minVoltage2bms"))

                        # Parse individual cell voltages (1 to 16) with multi-key and list decoders
                        voltage_list = _extract_voltage_list(snapshot)
                        cell_voltages = {}
                        for i in range(1, 17):
                            raw_v = _get_cell_raw_value(snapshot, i, voltage_list)
                            cell_voltages[f"cellVolt{i}"] = _parse_cell_voltage(raw_v)

                        # Fallback for max/min cell voltage from individual cells if not provided directly
                        valid_cells = [v for v in cell_voltages.values() if v is not None]
                        if max_cell_v is None and valid_cells:
                            max_cell_v = max(valid_cells)
                        if min_cell_v is None and valid_cells:
                            min_cell_v = min(valid_cells)

                        if max_cell_v is not None and min_cell_v is not None:
                            dv_cells = round(abs(max_cell_v - min_cell_v), 1)
                        else:
                            dv_cells = None

                        max_cell_num = _safe_int(snapshot.get("maxVoltageNum2bms"), default=None)
                        min_cell_num = _safe_int(snapshot.get("minVoltageNum2bms"), default=None)

                        # Diagnostics logging for battery cell telemetry
                        battery_cell_telemetry = {
                            k: v for k, v in snapshot.items()
                            if any(term in k.lower() for term in ("volt", "cell", "bms"))
                        }
                        _LOGGER.debug(
                            "Battery %s raw cell/voltage/BMS telemetry: %s",
                            device_sn,
                            battery_cell_telemetry,
                        )
                        if valid_cells:
                            _LOGGER.info(
                                "Battery %s parsed %d/16 cell voltages (min=%.1f mV, max=%.1f mV, dV=%.1f mV)",
                                device_sn,
                                len(valid_cells),
                                min_cell_v if min_cell_v is not None else 0.0,
                                max_cell_v if max_cell_v is not None else 0.0,
                                dv_cells if dv_cells is not None else 0.0,
                            )
                            self._unsupported_cells_logged.discard(device_sn)
                        else:
                            if device_sn not in self._unsupported_cells_logged:
                                self._unsupported_cells_logged.add(device_sn)
                                _LOGGER.info(
                                    "Battery %s does not report individual cell voltages via cloud API (min/max cell telemetry and dV remain active)",
                                    device_sn,
                                )
                            _LOGGER.debug(
                                "Battery %s individual cell voltages not available. Raw telemetry: %s",
                                device_sn,
                                battery_cell_telemetry,
                            )

                        batt_volt = _safe_float(snapshot.get("battVolt"), default=None)
                        batt_curr = _safe_float(snapshot.get("battCurr"), default=None)
                        batt_soc = _safe_int(snapshot.get("battSoc"), default=None)
                        batt_soh = _safe_int(snapshot.get("battSoh"), default=None)
                        batt_capacity = _safe_float(snapshot.get("battCapacity"), default=None)

                        # Derive and normalize rated energy in kWh
                        raw_rated_energy = _safe_float(snapshot.get("ratedEnergy"), default=None)
                        if raw_rated_energy is not None and raw_rated_energy > 100:
                            rated_energy_kwh = round(raw_rated_energy / 1000.0, 2)
                        elif raw_rated_energy is not None and raw_rated_energy > 0:
                            rated_energy_kwh = round(raw_rated_energy, 2)
                        elif batt_capacity is not None and batt_capacity > 0 and batt_volt is not None and batt_volt > 0:
                            rated_energy_kwh = round((batt_capacity * batt_volt) / 1000.0, 2)
                        else:
                            rated_energy_kwh = None

                        remaining_energy = _calculate_battery_remaining_energy(
                            snapshot, batt_soc, batt_volt, batt_capacity, rated_energy_kwh
                        )

                        _LOGGER.debug(
                            "Battery %s energy telemetry: remaining=%s kWh, rated=%s kWh, capacity=%s Ah, volt=%s V, soc=%s%%",
                            device_sn,
                            remaining_energy,
                            rated_energy_kwh,
                            batt_capacity,
                            batt_volt,
                            batt_soc,
                        )

                        # Derive physical cell count safely (cellNumber in API is often pack address e.g. 3)
                        raw_cell_num = _safe_int(snapshot.get("cellNumber"), default=None)
                        if raw_cell_num is not None and (raw_cell_num < 8 or (max_cell_num is not None and raw_cell_num < max_cell_num)):
                            rate_volt = _safe_float(snapshot.get("rateVolt"), default=None)
                            if (batt_volt is not None and batt_volt > 40) or (rate_volt is not None and rate_volt >= 48):
                                cell_count = 16
                            elif max_cell_num is not None and max_cell_num > 0:
                                cell_count = max(16, max_cell_num)
                            else:
                                cell_count = None
                        else:
                            cell_count = raw_cell_num

                        # BMS Communication Status for Battery
                        bms_status_str = snapshot.get("bmsFlagStr")
                        if not bms_status_str or bms_status_str == "-":
                            bms_flag_val = snapshot.get("bmsFlag")
                            if bms_flag_val is True or bms_flag_val == "true" or bms_flag_val == 1:
                                bms_status_str = "Connected"
                            elif bms_flag_val is False or bms_flag_val == "false" or bms_flag_val == 0:
                                bms_status_str = "Disconnected"
                            else:
                                bms_status_str = None

                        devices_data[device_sn] = {
                            "type": DeviceTypeEnum.LITHIUM_BATTERY_PACK,
                            "serialNumber": device_sn,
                            "firmwareVersion": firmware_version,
                            "collectorSn": basic_info.get("collectorSn"),
                            "data": {
                                "voltage": batt_volt if batt_volt is not None else 0.0,
                                "current": batt_curr if batt_curr is not None else 0.0,
                                "soc": batt_soc if batt_soc is not None else 0,
                                "soh": batt_soh if batt_soh is not None else 0,
                                "ratedEnergy": rated_energy_kwh,
                                "energyUnit": str(snapshot.get("energyUnit", "")),
                                "nameplateRatedPower": str(snapshot.get("nameplateRatedPower", "")),
                                "power": _safe_float(snapshot.get("bmsPower")),
                                "chargingState": charging_state,
                                "tempMax": _safe_float(snapshot.get("tempMax")),
                                "tempMin": _safe_float(snapshot.get("tempMin")),
                                "remainingEnergy": remaining_energy,
                                "capacity": batt_capacity if batt_capacity is not None else 0.0,
                                "maxCellVoltage": max_cell_v,
                                "minCellVoltage": min_cell_v,
                                "maxCellVoltageNum": max_cell_num,
                                "minCellVoltageNum": min_cell_num,
                                "dvCells": dv_cells,
                                **cell_voltages,
                                "emsSocAvg": _safe_int(snapshot.get("emsSocAvg")),
                                "wifiSignal": _safe_int(snapshot.get("wifiSignal")),
                                "cellTemp1": _safe_float(snapshot.get("cellTemp1"), default=None),
                                "cellTemp2": _safe_float(snapshot.get("cellTemp2"), default=None),
                                "cellTemp3": _safe_float(snapshot.get("cellTemp3"), default=None),
                                "cellTemp4": _safe_float(snapshot.get("cellTemp4"), default=None),
                                "chargeLimitVoltage": _safe_float(snapshot.get("BMSLCVolt")),
                                "dischargeLimitVoltage": _safe_float(snapshot.get("BMSLDVolt")),
                                "chargeLimitCurrent": _safe_float(snapshot.get("BMSLCCurr"), default=None),
                                "dischargeLimitCurrent": _safe_float(snapshot.get("BMSLDCurr"), default=None),
                                "cellCount": cell_count,
                                "maxCellTempNum": _safe_int(snapshot.get("maxCellTempNum"), default=None),
                                "minCellTempNum": _safe_int(snapshot.get("minBattTempNum"), default=None),
                                "batteryType": str(snapshot.get("batTyStr")) if snapshot.get("batTyStr") else None,
                                "connectedInverterSn": str(snapshot.get("invSn")) if snapshot.get("invSn") else None,
                                "bmsCommunicationStatus": bms_status_str,
                                "warnCount": warn_count,
                                "lastWarnMsg": last_warn_msg,
                            }
                        }
                    else:
                        settings = await self.api.get_device_settings(device_sn)
                        previous_settings = self.data.get(device_sn, {}).get("settings", {}) if self.data else {}
                        if not settings and previous_settings:
                            _LOGGER.info(
                                "Preserving %d cached settings for inverter %s after empty query",
                                len(previous_settings),
                                device_sn,
                            )
                            settings = previous_settings
                        elif not settings and self.api.has_openapi_permissions is not False:
                            _LOGGER.warning(
                                "Inverter %s settings are empty — remote control entities (select, number, switch) will show 'unknown'",
                                device_sn,
                            )
                        raw_model = snapshot.get("deviceModel") or snapshot.get("model") or snapshot.get("productTypeEnum") or "Solar Inverter"
                        model_display = str(raw_model).replace("_", " ").title()
                        if "Felicity" not in model_display:
                            model_display = f"Felicity {model_display}"

                        # Handle rated power calculation (stored in kW)
                        raw_rated = _safe_float(snapshot.get("ratedPower") or snapshot.get("nameplateRatedPower") or snapshot.get("ratePower"))
                        if raw_rated > 100:
                            # If value is returned in Watts (e.g. 6000), convert to kW
                            raw_rated = raw_rated / 1000.0
                        
                        # Fallback parsing from model name if API returned 0 / missing
                        if raw_rated == 0:
                            match = re.search(r"(\d+)\s*K", model_display.upper())
                            if match:
                                raw_rated = float(match.group(1))

                        # Handle PV Power calculation (raw API or sum of dual/quad MPPT)
                        pv1_power = _safe_float(snapshot.get("pv1Power") or snapshot.get("pvPower1"))
                        pv2_power = _safe_float(snapshot.get("pv2Power") or snapshot.get("pvPower2"))
                        pv3_power = _safe_float(snapshot.get("pv3Power") or snapshot.get("pvPower3"))
                        pv4_power = _safe_float(snapshot.get("pv4Power") or snapshot.get("pvPower4"))
                        raw_pv_power = _safe_float(snapshot.get("pvPower"))
                        raw_pv_total_power = _safe_float(snapshot.get("pvTotalPower"))

                        total_pv_power = raw_pv_total_power or raw_pv_power
                        if total_pv_power == 0 and (pv1_power > 0 or pv2_power > 0 or pv3_power > 0 or pv4_power > 0):
                            total_pv_power = pv1_power + pv2_power + pv3_power + pv4_power

                        # Battery charge / discharge powers calculation
                        ems_power = _safe_float(snapshot.get("emsPower"))
                        bms_state = _safe_int(snapshot.get("bmsChargingState"), -1)
                        if bms_state == 1:
                            battery_charging_power = abs(ems_power)
                            battery_discharging_power = 0.0
                        elif bms_state == 2:
                            battery_charging_power = 0.0
                            battery_discharging_power = abs(ems_power)
                        else:
                            battery_charging_power = ems_power if ems_power > 0 else 0.0
                            battery_discharging_power = abs(ems_power) if ems_power < 0 else 0.0

                        # BMS Communication Status
                        bms_flag_val = snapshot.get("bmsFlag")
                        if bms_flag_val is True or bms_flag_val == "true" or bms_flag_val == 1:
                            bms_status = "Connected"
                        elif bms_flag_val is False or bms_flag_val == "false" or bms_flag_val == 0:
                            bms_status = "Disconnected"
                        else:
                            bms_status = None

                        devices_data[device_sn] = {
                            "type": DeviceTypeEnum.HIGH_FREQUENCY_INVERTER,
                            "productTypeEnum": device_type,
                            "modelName": model_display,
                            "serialNumber": device_sn,
                            "firmwareVersion": firmware_version,
                            "collectorSn": basic_info.get("collectorSn"),
                            "settings": settings,
                            "data": {
                                "acInputVoltage": _safe_float(snapshot.get("acRInVolt")),
                                "acInputFrequency": _safe_float(snapshot.get("acRInFreq")),
                                "acInputPower": _safe_float(snapshot.get("acRInPower")),
                                "acGridCurrentL1": _safe_float(snapshot.get("acRInCurr")),
                                "acGridCurrentL2": _safe_float(snapshot.get("acSInCurr")),
                                "acGridCurrentL3": _safe_float(snapshot.get("acTInCurr")),
                                "acGridVoltageL2": _safe_float(snapshot.get("acSInVolt")),
                                "acGridVoltageL3": _safe_float(snapshot.get("acTInVolt")),
                                "acGridFrequencyL2": _safe_float(snapshot.get("acSInFreq")),
                                "acGridFrequencyL3": _safe_float(snapshot.get("acTInFreq")),
                                "acGridPowerL1": _safe_float(snapshot.get("acRInPower")),
                                "acGridPowerL2": _safe_float(snapshot.get("acSInPower")),
                                "acGridPowerL3": _safe_float(snapshot.get("acTInPower")),
                                "acTotalGridPower": _safe_float(snapshot.get("acTtlInpower") or snapshot.get("acRInPower")),
                                "acOutputVoltage": _safe_float(snapshot.get("acROutVolt")),
                                "acOutputCurrent": _safe_float(snapshot.get("acROutCurr")),
                                "acOutputFrequency": _safe_float(snapshot.get("acROutFreq")),
                                "acTotalOutputActivePower": _safe_float(snapshot.get("acTotalOutActPower")),
                                "acTotalBackupApparentPower": _safe_float(snapshot.get("acTotalOutAppaPower")),
                                "acBackupVoltageL2": _safe_float(snapshot.get("acSOutVolt")),
                                "acBackupVoltageL3": _safe_float(snapshot.get("acTOutVolt")),
                                "acBackupCurrentL1": _safe_float(snapshot.get("acROutCurr")),
                                "acBackupCurrentL2": _safe_float(snapshot.get("acSOutCurr")),
                                "acBackupCurrentL3": _safe_float(snapshot.get("acTOutCurr")),
                                "acBackupPowerL1": _safe_float(snapshot.get("acROutPower")),
                                "acBackupPowerL2": _safe_float(snapshot.get("acSOutPower")),
                                "acBackupPowerL3": _safe_float(snapshot.get("acTOutPower")),
                                "loadPercentage": _safe_float(snapshot.get("loadPercent")),
                                "pvVoltage": _safe_float(snapshot.get("pvVolt")),
                                "pvInputCurrent": _safe_float(snapshot.get("pvInCurr")),
                                "pvPower": raw_pv_power or total_pv_power,
                                "pvTotalPower": total_pv_power,
                                "pv1Voltage": _safe_float(snapshot.get("pv1Volt") or snapshot.get("pvVolt1") or snapshot.get("pvVolt")),
                                "pv1Current": _safe_float(snapshot.get("pv1InCurr") or snapshot.get("pvInCurr1") or snapshot.get("pvInCurr")),
                                "pv1Power": pv1_power or raw_pv_power,
                                "pv2Voltage": _safe_float(snapshot.get("pv2Volt") or snapshot.get("pvVolt2")),
                                "pv2Current": _safe_float(snapshot.get("pv2InCurr") or snapshot.get("pvInCurr2")),
                                "pv2Power": pv2_power,
                                "pv3Voltage": _safe_float(snapshot.get("pv3Volt") or snapshot.get("pvVolt3")),
                                "pv3Current": _safe_float(snapshot.get("pv3InCurr") or snapshot.get("pvInCurr3")),
                                "pv3Power": pv3_power,
                                "pv4Voltage": _safe_float(snapshot.get("pv4Volt") or snapshot.get("pvVolt4")),
                                "pv4Current": _safe_float(snapshot.get("pv4InCurr") or snapshot.get("pvInCurr4")),
                                "pv4Power": pv4_power,
                                "ctPower": _safe_float(snapshot.get("ctPower")),
                                "meterPower": _safe_float(snapshot.get("meterPower")),
                                "totalConsumptionPower": _safe_float(snapshot.get("totalConsumPower")),
                                "genPower": _safe_float(snapshot.get("genTotalPower") or snapshot.get("genPower")),
                                "genVoltage": _safe_float(snapshot.get("genVoltage")),
                                "genCurrent": _safe_float(snapshot.get("genCurrent")),
                                "genFrequency": _safe_float(snapshot.get("genFrequency")),
                                "batteryVoltage": _safe_float(snapshot.get("emsVoltage") or snapshot.get("battVolt")),
                                "batteryCurrent": _safe_float(snapshot.get("emsCurrent") or snapshot.get("battCurr")),
                                "batteryPower": ems_power,
                                "batteryChargingPower": round(battery_charging_power, 2),
                                "batteryDischargingPower": round(battery_discharging_power, 2),
                                "batterySoc": _safe_int(snapshot.get("emsSoc") or snapshot.get("battSoc")),
                                "bmsCommunicationStatus": bms_status,
                                "battery2Voltage": _safe_float(snapshot.get("emsVoltage2")),
                                "battery2Current": _safe_float(snapshot.get("emsCurrent2")),
                                "battery2Power": _safe_float(snapshot.get("emsPower2")),
                                "battery2Soc": _safe_int(snapshot.get("emsSoc2")),
                                "tempMax": _safe_float(snapshot.get("tempMax")),
                                "devTempMax": _safe_float(snapshot.get("devTempMax")),
                                "devTempMin": _safe_float(snapshot.get("devTempMin")),
                                "energyPvToday": _safe_float(snapshot.get("ePvToday") or snapshot.get("epvToday")),
                                "energyPvTotal": _safe_float(snapshot.get("ePvTotal")),
                                "energyPvMonth": _safe_float(snapshot.get("ePvMonth")),
                                "energyPvYear": _safe_float(snapshot.get("ePvYear")),
                                "energyLoadToday": _safe_float(snapshot.get("eLoadToday")),
                                "energyLoadTotal": _safe_float(snapshot.get("eLoadTotal")),
                                "energyLoadMonth": _safe_float(snapshot.get("eLoadMonth")),
                                "energyLoadYear": _safe_float(snapshot.get("eLoadYear")),
                                "energyGridFeedToday": _safe_float(snapshot.get("eGridFeedToday") or snapshot.get("egridFeedToday")),
                                "energyGridFeedTotal": _safe_float(snapshot.get("eGridFeedTotal") or snapshot.get("egridFeedTotal")),
                                "energyGridFeedMonth": _safe_float(snapshot.get("eGridFeedMonth") or snapshot.get("egridFeedMonth")),
                                "energyGridFeedYear": _safe_float(snapshot.get("eGridFeedYear") or snapshot.get("egridFeedYear")),
                                "energyGridImportToday": _safe_float(snapshot.get("eToday") or snapshot.get("etoday")),
                                "energyGridImportTotal": _safe_float(snapshot.get("eTotal") or snapshot.get("etotal")),
                                "energyGridImportMonth": _safe_float(snapshot.get("eMonth") or snapshot.get("emonth")),
                                "energyGridImportYear": _safe_float(snapshot.get("eYear") or snapshot.get("eyear")),
                                "energyBatteryChargeToday": _safe_float(
                                    snapshot.get("eBatCharToday") or snapshot.get("ebatCharToday") or snapshot.get("bat1CharToday")
                                ),
                                "energyBatteryChargeMonth": _safe_float(
                                    snapshot.get("eBatCharMonth") or snapshot.get("ebatCharMonth") or snapshot.get("bat1CharMonth")
                                ),
                                "energyBatteryChargeYear": _safe_float(
                                    snapshot.get("eBatCharYear") or snapshot.get("ebatCharYear") or snapshot.get("bat1CharYear")
                                ),
                                "energyBatteryChargeTotal": _safe_float(
                                    snapshot.get("eBatCharTotal") or snapshot.get("ebatCharTotal") or snapshot.get("bat1CharTotal")
                                ),
                                "energyBatteryDischargeToday": _safe_float(
                                    snapshot.get("eBatDisCharToday") or snapshot.get("ebatDischarToday") or snapshot.get("ebatDisCharToday") or snapshot.get("bat1DisCharToday")
                                ),
                                "energyBatteryDischargeMonth": _safe_float(
                                    snapshot.get("eBatDisCharMonth") or snapshot.get("ebatDischarMonth") or snapshot.get("ebatDisCharMonth") or snapshot.get("bat1DisCharMonth")
                                ),
                                "energyBatteryDischargeYear": _safe_float(
                                    snapshot.get("eBatDisCharYear") or snapshot.get("ebatDischarYear") or snapshot.get("ebatDisCharYear") or snapshot.get("bat1DisCharYear")
                                ),
                                "energyBatteryDischargeTotal": _safe_float(
                                    snapshot.get("eBatDisCharTotal") or snapshot.get("ebatDischarTotal") or snapshot.get("ebatDisCharTotal") or snapshot.get("bat1DisCharTotal")
                                ),
                                "totalEnergy": _safe_float(snapshot.get("totalEnergy")),
                                "smartLoadPower": _safe_float(snapshot.get("smartTotalPower") or snapshot.get("smartLoadPower")),
                                "smartLoadVoltage": _safe_float(snapshot.get("smartLoadVolt")),
                                "smartLoadCurrent": _safe_float(snapshot.get("smartLoadCurr")),
                                "smartLoadFrequency": _safe_float(snapshot.get("smartLoadFreq")),
                                "smartLoadEnergyToday": _safe_float(snapshot.get("smartLoadToday")),
                                "smartLoadEnergyTotal": _safe_float(snapshot.get("smartLoadTotal")),
                                "energyGenToday": _safe_float(snapshot.get("genToday")),
                                "energyGenTotal": _safe_float(snapshot.get("genTotal")),
                                "genPowerL2": _safe_float(snapshot.get("genPower2")),
                                "genPowerL3": _safe_float(snapshot.get("genPower3")),
                                "meterLinkStatus": str(snapshot.get("electricityMeterLinkStr")) if snapshot.get("electricityMeterLinkStr") else None,
                                "totalEmsCapacity": _safe_float(snapshot.get("totalEmsCapacity")),
                                "workModeStr": snapshot.get("workModeStr") or snapshot.get("operMStr"),
                                "ratedPower": raw_rated,
                                "workMode": WORK_MODE_MAP.get(
                                    _safe_int(snapshot.get("workMode") if snapshot.get("workMode") is not None else snapshot.get("workModel"), -1),
                                    "Unknown"
                                ),
                                "warnCount": warn_count,
                                "lastWarnMsg": last_warn_msg,
                            }
                        }

                    _LOGGER.debug("Data fetched successfully for %s (%s)", device_sn, device_type)

                except Exception as err:
                    _LOGGER.error("Failed to fetch snapshot for device %s: %s", device_sn, err)
                    continue

            _LOGGER.info(
                "Data update complete: %d device(s) with data out of %d",
                len(devices_data), len(serial_numbers)
            )
            return devices_data

        except Exception as err:
            _LOGGER.error("Update failed: %s", err)
            raise UpdateFailed(f"Error communicating with API: {err}")
