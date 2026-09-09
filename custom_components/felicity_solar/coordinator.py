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
        return float(value) if value is not None else default
    except (ValueError, TypeError):
        return default


def _safe_int(value, default=0):
    """Convert value to int, returning default if value is None or invalid."""
    try:
        return int(value) if value is not None else default
    except (ValueError, TypeError):
        return default


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

            _LOGGER.info("Fetching snapshots for %d device(s)", len(serial_numbers))

            for device_sn in serial_numbers:
                try:
                    snapshot = await self.api.get_device_snapshot(device_sn)
                    device_type = snapshot.get("productTypeEnum")

                    _LOGGER.info("Snapshot received for device %s with productTypeEnum='%s'", device_sn, device_type)

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

                        devices_data[device_sn] = {
                            "type": DeviceTypeEnum.LITHIUM_BATTERY_PACK,
                            "serialNumber": device_sn,
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
                                "maxCellVoltage": _safe_float(snapshot.get("maxVoltage2bms")),
                                "minCellVoltage": _safe_float(snapshot.get("minVoltage2bms")),
                                "emsSocAvg": _safe_int(snapshot.get("emsSocAvg")),
                                "wifiSignal": _safe_int(snapshot.get("wifiSignal")),
                                "cellTemp1": _safe_float(snapshot.get("cellTemp1")),
                                "cellTemp2": _safe_float(snapshot.get("cellTemp2")),
                                "cellTemp3": _safe_float(snapshot.get("cellTemp3")),
                                "cellTemp4": _safe_float(snapshot.get("cellTemp4")),
                                "chargeLimitVoltage": _safe_float(snapshot.get("BMSLCVolt")),
                                "dischargeLimitVoltage": _safe_float(snapshot.get("BMSLDVolt")),
                            }
                        }
                    else:
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

                        devices_data[device_sn] = {
                            "type": DeviceTypeEnum.HIGH_FREQUENCY_INVERTER,
                            "productTypeEnum": device_type,
                            "modelName": model_display,
                            "serialNumber": device_sn,
                            "data": {
                                "acInputVoltage": _safe_float(snapshot.get("acRInVolt")),
                                "acInputFrequency": _safe_float(snapshot.get("acRInFreq")),
                                "acInputPower": _safe_float(snapshot.get("acRInPower")),
                                "acOutputVoltage": _safe_float(snapshot.get("acROutVolt")),
                                "acOutputCurrent": _safe_float(snapshot.get("acROutCurr")),
                                "acOutputFrequency": _safe_float(snapshot.get("acROutFreq")),
                                "acTotalOutputActivePower": _safe_float(snapshot.get("acTotalOutActPower")),
                                "loadPercentage": _safe_float(snapshot.get("loadPercent")),
                                "pvVoltage": _safe_float(snapshot.get("pvVolt")),
                                "pvInputCurrent": _safe_float(snapshot.get("pvInCurr")),
                                "pvPower": _safe_float(snapshot.get("pvPower")),
                                "pvTotalPower": _safe_float(snapshot.get("pvTotalPower")),
                                "pv1Voltage": _safe_float(snapshot.get("pv1Volt") or snapshot.get("pvVolt1") or snapshot.get("pvVolt")),
                                "pv1Current": _safe_float(snapshot.get("pv1InCurr") or snapshot.get("pvInCurr1") or snapshot.get("pvInCurr")),
                                "pv1Power": _safe_float(snapshot.get("pv1Power") or snapshot.get("pvPower1") or snapshot.get("pvPower")),
                                "pv2Voltage": _safe_float(snapshot.get("pv2Volt") or snapshot.get("pvVolt2")),
                                "pv2Current": _safe_float(snapshot.get("pv2InCurr") or snapshot.get("pvInCurr2")),
                                "pv2Power": _safe_float(snapshot.get("pv2Power") or snapshot.get("pvPower2")),
                                "batteryVoltage": _safe_float(snapshot.get("emsVoltage") or snapshot.get("battVolt")),
                                "batteryCurrent": _safe_float(snapshot.get("emsCurrent") or snapshot.get("battCurr")),
                                "batteryPower": _safe_float(snapshot.get("emsPower")),
                                "batterySoc": _safe_int(snapshot.get("emsSoc") or snapshot.get("battSoc")),
                                "tempMax": _safe_float(snapshot.get("tempMax")),
                                "devTempMax": _safe_float(snapshot.get("devTempMax")),
                                "energyPvToday": _safe_float(snapshot.get("ePvToday")),
                                "energyPvTotal": _safe_float(snapshot.get("ePvTotal")),
                                "energyLoadToday": _safe_float(snapshot.get("eLoadToday")),
                                "energyLoadTotal": _safe_float(snapshot.get("eLoadTotal")),
                                "totalEnergy": _safe_float(snapshot.get("totalEnergy")),
                                "ratedPower": raw_rated,
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
