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
    UnitOfFrequency,
    PERCENTAGE,
    UnitOfTemperature,
    UnitOfApparentPower,
)
from homeassistant.helpers.update_coordinator import CoordinatorEntity

# Define all the data points from your HighFrequencyInverterData type
INVERTER_DESCRIPTIONS: tuple[SensorEntityDescription, ...] = (
    # Grid Measurements
    SensorEntityDescription(key="acInputVoltage", name="AC Input Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acInputFrequency", name="AC Input Frequency",
                            native_unit_of_measurement=UnitOfFrequency.HERTZ, device_class=SensorDeviceClass.FREQUENCY, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acInputPower", name="AC Input Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acGridCurrentL1", name="Grid L1 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acGridCurrentL2", name="Grid L2 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acGridCurrentL3", name="Grid L3 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acGridVoltageL2", name="Grid L2 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acGridVoltageL3", name="Grid L3 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acGridPowerL1", name="Grid L1 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acGridPowerL2", name="Grid L2 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acGridPowerL3", name="Grid L3 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acTotalGridPower", name="Total Grid Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),

    # Backup Load / AC Output (EPS)
    SensorEntityDescription(key="acOutputVoltage", name="AC Output Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acOutputCurrent", name="AC Output Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acOutputFrequency", name="AC Output Frequency",
                            native_unit_of_measurement=UnitOfFrequency.HERTZ, device_class=SensorDeviceClass.FREQUENCY, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acTotalOutputActivePower", name="AC Total Output Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acTotalBackupApparentPower", name="Backup Total Apparent Power",
                            native_unit_of_measurement=UnitOfApparentPower.VOLT_AMPERE, device_class=SensorDeviceClass.APPARENT_POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acBackupVoltageL2", name="Backup L2 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acBackupVoltageL3", name="Backup L3 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acBackupCurrentL1", name="Backup L1 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acBackupCurrentL2", name="Backup L2 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acBackupCurrentL3", name="Backup L3 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acBackupPowerL1", name="Backup L1 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="acBackupPowerL2", name="Backup L2 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="acBackupPowerL3", name="Backup L3 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="loadPercentage", name="Load Percentage",
                            native_unit_of_measurement=PERCENTAGE, state_class=SensorStateClass.MEASUREMENT),

    # Solar PV Tracking
    SensorEntityDescription(key="pvVoltage", name="PV Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="pvInputCurrent", name="PV Input Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="pvPower", name="PV Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="pvTotalPower", name="PV Total Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    # Dual MPPT / PV String 1
    SensorEntityDescription(key="pv1Voltage", name="PV1 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="pv1Current", name="PV1 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="pv1Power", name="PV1 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    # Dual MPPT / PV String 2
    SensorEntityDescription(key="pv2Voltage", name="PV2 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="pv2Current", name="PV2 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="pv2Power", name="PV2 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    # Quad MPPT / PV Strings 3 & 4 (disabled by default)
    SensorEntityDescription(key="pv3Voltage", name="PV3 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="pv3Current", name="PV3 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="pv3Power", name="PV3 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="pv4Voltage", name="PV4 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="pv4Current", name="PV4 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="pv4Power", name="PV4 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),

    # Home Load & CT Clamp
    SensorEntityDescription(key="ctPower", name="External CT Clamp Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="meterPower", name="Home Load Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="totalConsumptionPower", name="Total Consumption Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),

    # Generator (disabled by default)
    SensorEntityDescription(key="genPower", name="Generator Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="genVoltage", name="Generator Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="genCurrent", name="Generator Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="genFrequency", name="Generator Frequency",
                            native_unit_of_measurement=UnitOfFrequency.HERTZ, device_class=SensorDeviceClass.FREQUENCY, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),

    # Battery Telemetry (from Inverter)
    SensorEntityDescription(key="batteryVoltage", name="Battery Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="batteryCurrent", name="Battery Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="batteryPower", name="Battery Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="batteryChargingPower", name="Battery Charging Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, icon="mdi:battery-charging"),
    SensorEntityDescription(key="batteryDischargingPower", name="Battery Discharging Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, icon="mdi:battery-minus"),
    SensorEntityDescription(key="batterySoc", name="Battery SOC",
                            native_unit_of_measurement=PERCENTAGE, device_class=SensorDeviceClass.BATTERY, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="bmsCommunicationStatus", name="BMS Communication Status",
                            icon="mdi:battery-sync"),

    # Battery Port 2 (for dual battery models, disabled by default)
    SensorEntityDescription(key="battery2Voltage", name="Battery 2 Voltage",
                            native_unit_of_measurement=UnitOfElectricPotential.VOLT, device_class=SensorDeviceClass.VOLTAGE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="battery2Current", name="Battery 2 Current",
                            native_unit_of_measurement=UnitOfElectricCurrent.AMPERE, device_class=SensorDeviceClass.CURRENT, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="battery2Power", name="Battery 2 Power",
                            native_unit_of_measurement=UnitOfPower.WATT, device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="battery2Soc", name="Battery 2 SOC",
                            native_unit_of_measurement=PERCENTAGE, device_class=SensorDeviceClass.BATTERY, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),

    # Temperatures & Alarms & Diagnostics
    SensorEntityDescription(key="tempMax", name="Inverter Temp",
                            native_unit_of_measurement=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE, state_class=SensorStateClass.MEASUREMENT),
    SensorEntityDescription(key="devTempMax", name="Inverter Max Temp",
                            native_unit_of_measurement=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="devTempMin", name="Inverter Min Temp",
                            native_unit_of_measurement=UnitOfTemperature.CELSIUS, device_class=SensorDeviceClass.TEMPERATURE, state_class=SensorStateClass.MEASUREMENT, entity_registry_enabled_default=False),
    SensorEntityDescription(key="warnCount", name="Active Warning Count", icon="mdi:alert-circle-outline"),
    SensorEntityDescription(key="lastWarnMsg", name="Last Warning Message", icon="mdi:alert-decagram"),
    SensorEntityDescription(key="workMode", name="Work Mode", icon="mdi:cog-transfer"),
    SensorEntityDescription(key="ratedPower", name="Rated Power", native_unit_of_measurement=UnitOfPower.KILO_WATT,
                            device_class=SensorDeviceClass.POWER, state_class=SensorStateClass.MEASUREMENT),

    # Energy Meters (for HA Energy Dashboard)
    SensorEntityDescription(key="energyPvToday", name="Energy PV Today", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
    SensorEntityDescription(key="energyPvTotal", name="Energy PV Total", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
    SensorEntityDescription(key="totalEnergy", name="Total System Energy", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
    SensorEntityDescription(key="energyLoadToday", name="Energy Load Today", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
    SensorEntityDescription(key="energyLoadTotal", name="Energy Load Total", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
    SensorEntityDescription(key="energyBatteryChargeTotal", name="Total Battery Charged Energy", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
    SensorEntityDescription(key="energyBatteryDischargeTotal", name="Total Battery Discharged Energy", native_unit_of_measurement=UnitOfEnergy.KILO_WATT_HOUR,
                            device_class=SensorDeviceClass.ENERGY, state_class=SensorStateClass.TOTAL_INCREASING),
)


def create_inverter_sensors(coordinator, device_sn):
    return [FelicityInverterSensor(coordinator, device_sn, desc) for desc in INVERTER_DESCRIPTIONS]


class FelicityInverterSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, device_sn: str, description: SensorEntityDescription):
        super().__init__(coordinator)
        self.entity_description = description
        self.device_sn = device_sn
        self._attr_unique_id = f"{device_sn}_{description.key}"
        
        device_entry = coordinator.data.get(device_sn, {}) if coordinator and coordinator.data else {}
        model_name = device_entry.get("modelName") or "Solar Inverter"
        firmware_version = device_entry.get("firmwareVersion")

        device_info = {
            "identifiers": {("felicity_solar", device_sn)},
            "name": f"Felicity Inverter {device_sn}",
            "manufacturer": "Felicity Solar",
            "model": model_name,
        }
        if firmware_version:
            device_info["sw_version"] = str(firmware_version)

        self._attr_device_info = device_info

    @property
    def native_value(self):
        """Extract the exact key value from coordinator data."""
        device_data = self.coordinator.data.get(
            self.device_sn, {}).get("data", {})
        return device_data.get(self.entity_description.key)
