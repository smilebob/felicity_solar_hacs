from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfElectricPotential,
    UnitOfElectricCurrent,
    UnitOfPower,
    UnitOfEnergy,
    UnitOfTemperature,
    PERCENTAGE,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity

# Define all the data points from your BatteryData type
BATTERY_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    SensorEntityDescription(
        key="voltage", name="Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="current", name="Current",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="soc", name="State of Charge",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="soh", name="State of Health",
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="power", name="Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        device_class=SensorDeviceClass.POWER,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="chargingState", name="Charging State",
    ),
    SensorEntityDescription(
        key="tempMax", name="Max Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="tempMin", name="Min Temperature",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="ratedEnergy", name="Rated Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY_STORAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery-heart-variant",
    ),
    SensorEntityDescription(
        key="remainingEnergy", name="Remaining Energy",
        native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY_STORAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery-charging-high",
    ),
    SensorEntityDescription(
        key="capacity", name="Capacity",
        native_unit_of_measurement="Ah",
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="maxCellVoltage", name="Max Cell Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.MILLIVOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="minCellVoltage", name="Min Cell Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.MILLIVOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="maxCellVoltageNum", name="Max Cell Voltage Number",
        icon="mdi:battery-arrow-up",
    ),
    SensorEntityDescription(
        key="minCellVoltageNum", name="Min Cell Voltage Number",
        icon="mdi:battery-arrow-down",
    ),
    SensorEntityDescription(
        key="dvCells", name="dV Cells",
        native_unit_of_measurement=UnitOfElectricPotential.MILLIVOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery-alert",
    ),
    # Individual Cell Voltages (1 to 16)
    *(
        SensorEntityDescription(
            key=f"cellVolt{i}",
            name=f"Cell {i} Voltage",
            native_unit_of_measurement=UnitOfElectricPotential.MILLIVOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
            icon="mdi:battery-outline",
        )
        for i in range(1, 17)
    ),
    SensorEntityDescription(
        key="emsSocAvg", name="EMS Average SOC",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="wifiSignal", name="WiFi Signal",
        native_unit_of_measurement="dBm",
        device_class=SensorDeviceClass.SIGNAL_STRENGTH,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="cellTemp1", name="Cell Temperature 1",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="cellTemp2", name="Cell Temperature 2",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="cellTemp3", name="Cell Temperature 3",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="cellTemp4", name="Cell Temperature 4",
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="chargeLimitVoltage", name="Charge Limit Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="dischargeLimitVoltage", name="Discharge Limit Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    ),
    SensorEntityDescription(
        key="chargeLimitCurrent", name="Charge Limit Current",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery-arrow-up",
    ),
    SensorEntityDescription(
        key="dischargeLimitCurrent", name="Discharge Limit Current",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        device_class=SensorDeviceClass.CURRENT,
        state_class=SensorStateClass.MEASUREMENT,
        icon="mdi:battery-arrow-down",
    ),
    SensorEntityDescription(
        key="cellCount", name="Cell Count",
        icon="mdi:battery-heart-variant",
    ),
    SensorEntityDescription(
        key="maxCellTempNum", name="Max Temp Probe Number",
        icon="mdi:thermometer-chevron-up",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="minCellTempNum", name="Min Temp Probe Number",
        icon="mdi:thermometer-chevron-down",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="batteryType", name="Battery Type",
        icon="mdi:information-outline",
    ),
    SensorEntityDescription(
        key="connectedInverterSn", name="Connected Inverter SN",
        icon="mdi:barcode",
        entity_registry_enabled_default=False,
    ),
    SensorEntityDescription(
        key="bmsCommunicationStatus", name="BMS Communication Status",
        icon="mdi:lan-connect",
    ),
    SensorEntityDescription(key="warnCount", name="Active Warning Count", icon="mdi:alert-circle-outline"),
    SensorEntityDescription(key="warnMsg", name="Last Warning Message", icon="mdi:alert-decagram"),
)


def create_battery_sensors(coordinator, device_sn):
    return [FelicityBatterySensor(coordinator, device_sn, desc) for desc in BATTERY_DESCRIPTIONS]


class FelicityBatterySensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, device_sn: str, description: SensorEntityDescription):
        super().__init__(coordinator)
        self.entity_description = description
        self.device_sn = device_sn
        self._attr_unique_id = f"{device_sn}_{description.key}"
        device_entry = coordinator.data.get(device_sn, {}) if coordinator and coordinator.data else {}
        firmware_version = device_entry.get("firmwareVersion")

        device_info = {
            "identifiers": {("felicity_solar", device_sn)},
            "name": f"Felicity Battery {device_sn}",
            "manufacturer": "Felicity Solar",
            "model": "Lithium Battery Pack",
        }
        if firmware_version:
            device_info["sw_version"] = str(firmware_version)

        self._attr_device_info = device_info

    @property
    def native_value(self):
        device_data = self.coordinator.data.get(
            self.device_sn, {}).get("data", {})
        return device_data.get(self.entity_description.key)

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        if not super().available:
            return False
        # For individual cell voltages: mark unavailable if the cell voltage is not reported
        # by the BMS/cloud API, avoiding 'unknown' clutter for unstreamed cells.
        if self.entity_description.key.startswith("cellVolt"):
            device_data = self.coordinator.data.get(self.device_sn, {}).get("data", {})
            if device_data.get(self.entity_description.key) is None:
                return False
        return True
