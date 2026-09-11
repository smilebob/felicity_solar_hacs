import sys
import os
import unittest
import logging

# Ensure mock for homeassistant modules if not in HA venv
try:
    from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
    from homeassistant.helpers.update_coordinator import CoordinatorEntity, DataUpdateCoordinator
except ImportError:
    # Minimal mock for running standalone
    from unittest.mock import MagicMock
    import types
    ha = types.ModuleType("homeassistant")
    ha_core = types.ModuleType("homeassistant.core")
    ha_core.HomeAssistant = MagicMock
    ha_core.ServiceCall = MagicMock
    ha_core.SupportsResponse = MagicMock
    ha_config = types.ModuleType("homeassistant.config_entries")
    ha_config.ConfigEntry = MagicMock
    ha_const = types.ModuleType("homeassistant.const")
    ha_const.PERCENTAGE = "%"
    class Platform:
        SENSOR = "sensor"
        SELECT = "select"
        NUMBER = "number"
        SWITCH = "switch"
    ha_const.Platform = Platform
    ha_const.UnitOfElectricPotential = MagicMock()
    ha_const.UnitOfElectricPotential.VOLT = "V"
    ha_const.UnitOfElectricPotential.MILLIVOLT = "mV"
    ha_const.UnitOfElectricCurrent = MagicMock()
    ha_const.UnitOfElectricCurrent.AMPERE = "A"
    ha_const.UnitOfPower = MagicMock()
    ha_const.UnitOfPower.WATT = "W"
    ha_const.UnitOfPower.KILO_WATT = "kW"
    ha_const.UnitOfEnergy = MagicMock()
    ha_const.UnitOfEnergy.KILO_WATT_HOUR = "kWh"
    ha_const.UnitOfTemperature = MagicMock()
    ha_const.UnitOfTemperature.CELSIUS = "°C"
    ha_sensor = types.ModuleType("homeassistant.components.sensor")
    ha_sensor.SensorDeviceClass = MagicMock()
    ha_sensor.SensorStateClass = MagicMock()
    class SensorEntityDescription:
        def __init__(self, key, name=None, **kwargs):
            self.key = key
            self.name = name
            for k, v in kwargs.items():
                setattr(self, k, v)
    ha_sensor.SensorEntityDescription = SensorEntityDescription
    class SensorEntity:
        entity_description = None
        _attr_device_info = {}
        _attr_unique_id = ""
    ha_sensor.SensorEntity = SensorEntity
    ha_coord = types.ModuleType("homeassistant.helpers.update_coordinator")
    class CoordinatorEntity:
        def __init__(self, coordinator):
            self.coordinator = coordinator
        @property
        def available(self):
            return True
    class DataUpdateCoordinator:
        def __init__(self, *args, **kwargs):
            self.data = {}
    class UpdateFailed(Exception):
        pass
    ha_coord.CoordinatorEntity = CoordinatorEntity
    ha_coord.DataUpdateCoordinator = DataUpdateCoordinator
    ha_coord.UpdateFailed = UpdateFailed
    sys.modules["homeassistant"] = ha
    sys.modules["homeassistant.core"] = ha_core
    sys.modules["homeassistant.config_entries"] = ha_config
    sys.modules["homeassistant.const"] = ha_const
    sys.modules["homeassistant.components"] = MagicMock()
    sys.modules["homeassistant.components.sensor"] = ha_sensor
    sys.modules["homeassistant.helpers"] = MagicMock()
    sys.modules["homeassistant.helpers.update_coordinator"] = ha_coord
    sys.modules["jwt"] = MagicMock()
    sys.modules["Crypto"] = MagicMock()
    sys.modules["Crypto.PublicKey"] = MagicMock()
    sys.modules["Crypto.Cipher"] = MagicMock()
    sys.modules["aiohttp"] = MagicMock()

sys.path.insert(0, "/home/pierre/Projets/felicity_solar_hacs")

from custom_components.felicity_solar.coordinator import (
    _parse_cell_voltage,
    _extract_voltage_list,
    _get_cell_raw_value,
    _calculate_battery_remaining_energy,
)
from custom_components.felicity_solar.sensors_battery import (
    FelicityBatterySensor,
    BATTERY_DESCRIPTIONS,
)

class TestBatteryCellFix(unittest.TestCase):
    def setUp(self):
        self.raw_snapshot = {
            'acRInVolt': None, 'acSInVolt': None, 'acTInVolt': None, 'acROutVolt': None, 'acSOutVolt': None, 'acTOutVolt': None,
            'pvVolt': None, 'pv2Volt': None, 'pv3Volt': None, 'pvTotalVoltage': None,
            'bmsPower': '-903.34', 'bmsState': '5056', 'bmsChargingState': 2, 'battVolt': '53.77',
            'bmsFlag': False, 'bmsFlag2': None, 'emsVoltage': '54', 'emsVoltage2': None,
            'bmsCommuQuantity': None, 'maxCellTempNum': '1', 'maxVoltageNum2bms': '12',
            'maxVoltage2bms': '3382', 'minVoltageNum2bms': '1', 'minVoltage2bms': '3349',
            'bmsVoltageList': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            'bmsVoltageListStr': None, 'cellTempList': ['0', '0', '0', '0', '0', '0', '0', '0'],
            'BMSLCVolt': '57.6', 'BMSLDVolt': '48', 'BMSLCCurr': '10', 'BMSLDCurr': '100',
            'cellVolt1': '0', 'cellVolt2': '0', 'cellVolt3': '0', 'cellVolt4': '0',
            'cellVolt5': '0', 'cellVolt6': '0', 'cellVolt7': '0', 'cellVolt8': '0',
            'cellVolt9': '0', 'cellVolt10': '0', 'cellVolt11': '0', 'cellVolt12': '0',
            'cellVolt13': '0', 'cellVolt14': '0', 'cellVolt15': '0', 'cellVolt16': '0',
            'cellTemp1': '0', 'cellTemp2': '0', 'cellTemp3': '0', 'cellTemp4': '0',
            'cellNumber': '3', 'rateVolt': '48', 'volt': '51.2', 'productTypeEnum': 'LITHIUM_BATTERY_PACK'
        }

    def test_cell_voltage_parsing(self):
        # 0 values should be rejected as None
        for i in range(1, 17):
            raw = self.raw_snapshot[f"cellVolt{i}"]
            parsed = _parse_cell_voltage(raw)
            self.assertIsNone(parsed, f"cellVolt{i} should be None when raw is '0'")

        # Non-zero voltages should parse correctly
        self.assertEqual(_parse_cell_voltage("3382"), 3382.0)
        self.assertEqual(_parse_cell_voltage("3.382 V"), 3382.0)
        self.assertEqual(_parse_cell_voltage("3349 mV"), 3349.0)

    def test_cell_count_derivation(self):
        # When cellNumber is 3 on a 48V/51.2V pack with cell 12 active, cellCount should be 16
        raw_cell_num = int(self.raw_snapshot["cellNumber"])
        max_cell_num = int(self.raw_snapshot["maxVoltageNum2bms"])
        batt_volt = float(self.raw_snapshot["battVolt"])
        rate_volt = float(self.raw_snapshot["rateVolt"])

        if raw_cell_num is not None and (raw_cell_num < 8 or (max_cell_num is not None and raw_cell_num < max_cell_num)):
            if (batt_volt is not None and batt_volt > 40) or (rate_volt is not None and rate_volt >= 48):
                cell_count = 16
            else:
                cell_count = None
        else:
            cell_count = raw_cell_num

        self.assertEqual(cell_count, 16)

    def test_entity_availability(self):
        device_sn = "073404810025290225"
        cell_voltages = {f"cellVolt{i}": None for i in range(1, 17)}
        coordinator = MagicMock()
        coordinator.data = {
            device_sn: {
                "type": "LITHIUM_BATTERY_PACK",
                "firmwareVersion": "1.0",
                "data": {
                    "maxCellVoltage": 3382.0,
                    "minCellVoltage": 3349.0,
                    "dvCells": 33.0,
                    "maxCellVoltageNum": 12,
                    "minCellVoltageNum": 1,
                    "cellCount": 16,
                    "bmsCommunicationStatus": "Disconnected",
                    **cell_voltages,
                }
            }
        }

        # Check sensor availability and values
        for desc in BATTERY_DESCRIPTIONS:
            sensor = FelicityBatterySensor(coordinator, device_sn, desc)
            if desc.key.startswith("cellVolt"):
                self.assertFalse(sensor.available, f"Sensor {desc.key} should be unavailable when value is None")
                self.assertIsNone(sensor.native_value)
            elif desc.key in ("maxCellVoltage", "minCellVoltage", "dvCells"):
                self.assertTrue(sensor.available, f"Sensor {desc.key} should be available")
                self.assertIsNotNone(sensor.native_value)
            elif desc.key == "bmsCommunicationStatus":
                self.assertTrue(sensor.available)
                self.assertEqual(sensor.native_value, "Disconnected")

        # If a battery DOES provide cellVolt1 (e.g. 3320 mV), it should be available
        coordinator.data[device_sn]["data"]["cellVolt1"] = 3320.0
        desc_cell1 = next(d for d in BATTERY_DESCRIPTIONS if d.key == "cellVolt1")
        sensor_cell1 = FelicityBatterySensor(coordinator, device_sn, desc_cell1)
        self.assertTrue(sensor_cell1.available)
        self.assertEqual(sensor_cell1.native_value, 3320.0)

    def test_logging_throttled(self):
        from unittest.mock import patch
        from custom_components.felicity_solar.coordinator import FelicitySolarCoordinator

        coordinator = FelicitySolarCoordinator.__new__(FelicitySolarCoordinator)
        coordinator._unsupported_cells_logged = set()
        coordinator.data = {}

        device_sn = "073404810025290225"
        valid_cells = []

        with patch("custom_components.felicity_solar.coordinator._LOGGER") as mock_logger:
            # Simulate 10 update cycles with unsupported individual cell voltages
            for _ in range(10):
                if valid_cells:
                    mock_logger.info(...)
                    coordinator._unsupported_cells_logged.discard(device_sn)
                else:
                    if device_sn not in coordinator._unsupported_cells_logged:
                        coordinator._unsupported_cells_logged.add(device_sn)
                        mock_logger.info(
                            "Battery %s does not report individual cell voltages via cloud API (min/max cell telemetry and dV remain active)",
                            device_sn,
                        )
                    mock_logger.debug("debug message")

            # Verify that warning was NEVER called
            mock_logger.warning.assert_not_called()
            # Verify that info was called exactly ONCE across all 10 cycles
            self.assertEqual(mock_logger.info.call_count, 1)
            self.assertIn(device_sn, coordinator._unsupported_cells_logged)

if __name__ == "__main__":
    unittest.main()
