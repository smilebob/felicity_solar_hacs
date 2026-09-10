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

    - If value is in Volts (e.g. 3.325 < 100), convert to mV (3325.0).
    - If value is already in mV (e.g. 3325 >= 100), keep as mV (3325.0).
    - If value is None, 0, or invalid, return None (avoids displaying false 0 mV).
    """
    v = _safe_float(value, default=None)
    if v is None or v <= 0:
        return None
    if v < 100:
        return round(v * 1000.0, 1)
    return round(v, 1)


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

                        # Parse individual cell voltages (1 to 16)
                        bms_voltage_list = snapshot.get("bmsVoltageList") or []
                        cell_voltages = {}
                        for i in range(1, 17):
                            raw_v = snapshot.get(f"cellVolt{i}")
                            if (raw_v is None or raw_v == "" or raw_v == 0 or raw_v == "0") and isinstance(bms_voltage_list, list) and len(bms_voltage_list) >= i:
                                raw_v = bms_voltage_list[i - 1]
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

                        devices_data[device_sn] = {
                            "type": DeviceTypeEnum.LITHIUM_BATTERY_PACK,
                            "serialNumber": device_sn,
                            "firmwareVersion": firmware_version,
                            "collectorSn": basic_info.get("collectorSn"),
                            "data": {
                                "voltage": _safe_float(snapshot.get("battVolt")),
                                "current": _safe_float(snapshot.get("battCurr")),
                                "soc": _safe_int(snapshot.get("battSoc")),
                                "soh": _safe_int(snapshot.get("battSoh")),
                                "ratedEnergy": _safe_float(snapshot.get("ratedEnergy")),
                                "energyUnit": str(snapshot.get("energyUnit", "")),
                                "nameplateRatedPower": str(snapshot.get("nameplateRatedPower", "")),
                                "power": _safe_float(snapshot.get("bmsPower")),
                                "chargingState": charging_state,
                                "tempMax": _safe_float(snapshot.get("tempMax")),
                                "tempMin": _safe_float(snapshot.get("tempMin")),
                                "remainingEnergy": _safe_float(snapshot.get("remainingBatteryEnergy1")),
                                "capacity": _safe_float(snapshot.get("battCapacity")),
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
                                "cellCount": _safe_int(snapshot.get("cellNumber"), default=None),
                                "maxCellTempNum": _safe_int(snapshot.get("maxCellTempNum"), default=None),
                                "minCellTempNum": _safe_int(snapshot.get("minBattTempNum"), default=None),
                                "batteryType": str(snapshot.get("batTyStr")) if snapshot.get("batTyStr") else None,
                                "connectedInverterSn": str(snapshot.get("invSn")) if snapshot.get("invSn") else None,
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
