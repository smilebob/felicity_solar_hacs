import logging
from dataclasses import dataclass
from homeassistant.components.number import (
    NumberEntity,
    NumberEntityDescription,
    NumberMode,
)
from homeassistant.const import (
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfPower,
    PERCENTAGE,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .api import DeviceTypeEnum

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class FelicityNumberDescription(NumberEntityDescription):
    """Description for Felicity Solar number entity."""
    min_value: float = 0.0
    max_value: float = 100.0
    step: float = 1.0


NUMBER_DESCRIPTIONS: tuple[FelicityNumberDescription, ...] = (
    FelicityNumberDescription(
        key="batteryMaxChargedCurrent",
        name="Battery Max Charge Current",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        min_value=1.0,
        max_value=200.0,
        step=1.0,
        icon="mdi:battery-arrow-up",
    ),
    FelicityNumberDescription(
        key="batteryMaxDischargeCurrent",
        name="Battery Max Discharge Current",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        min_value=5.0,
        max_value=200.0,
        step=1.0,
        icon="mdi:battery-arrow-down",
    ),
    FelicityNumberDescription(
        key="batteryOnGridDischargeDepthSoc",
        name="Battery On-Grid Discharge Depth SOC",
        native_unit_of_measurement=PERCENTAGE,
        min_value=10.0,
        max_value=100.0,
        step=1.0,
        icon="mdi:battery-low",
    ),
    FelicityNumberDescription(
        key="batteryOffGridDischargeDepthSoc",
        name="Battery Off-Grid Discharge Depth SOC",
        native_unit_of_measurement=PERCENTAGE,
        min_value=0.0,
        max_value=100.0,
        step=1.0,
        icon="mdi:battery-off",
    ),
    FelicityNumberDescription(
        key="batteryChargedVoltage",
        name="Battery Charged Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        min_value=48.0,
        max_value=60.0,
        step=0.1,
        icon="mdi:lightning-bolt",
    ),
    FelicityNumberDescription(
        key="batteryFloatingChargedVoltage",
        name="Battery Float Voltage",
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        min_value=48.0,
        max_value=60.0,
        step=0.1,
        icon="mdi:lightning-bolt-outline",
    ),
    FelicityNumberDescription(
        key="gridChargeCurrent",
        name="Grid Charge Current Limit",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        min_value=0.0,
        max_value=200.0,
        step=1.0,
        icon="mdi:transmission-tower-export",
    ),
    FelicityNumberDescription(
        key="genChargeCurrent",
        name="Generator Charge Current Limit",
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        min_value=0.0,
        max_value=100.0,
        step=1.0,
        icon="mdi:generator-stationary",
    ),
    FelicityNumberDescription(
        key="genAutoStartChargeSoc",
        name="Generator Auto Start SOC",
        native_unit_of_measurement=PERCENTAGE,
        min_value=0.0,
        max_value=100.0,
        step=1.0,
        icon="mdi:battery-clock",
    ),
    FelicityNumberDescription(
        key="genAutoExitChargeSoc",
        name="Generator Auto Exit SOC",
        native_unit_of_measurement=PERCENTAGE,
        min_value=5.0,
        max_value=100.0,
        step=1.0,
        icon="mdi:battery-check",
    ),
    FelicityNumberDescription(
        key="zeroExportAdjustmentPower",
        name="Zero Export Adjustment Power",
        native_unit_of_measurement=UnitOfPower.WATT,
        min_value=-5000.0,
        max_value=5000.0,
        step=10.0,
        icon="mdi:scale-balance",
    ),
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the number platform dynamically based on discovered devices."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    if coordinator.data:
        for device_sn, device_info in coordinator.data.items():
            device_type = device_info.get("type")
            if device_type == DeviceTypeEnum.HIGH_FREQUENCY_INVERTER:
                for desc in NUMBER_DESCRIPTIONS:
                    entities.append(FelicityInverterNumber(coordinator, device_sn, desc))
                _LOGGER.info(
                    "Created %d number control entity/entities for inverter %s",
                    len(NUMBER_DESCRIPTIONS),
                    device_sn,
                )

    if entities:
        _LOGGER.info("Adding %d number entities to Home Assistant", len(entities))
        async_add_entities(entities)


class FelicityInverterNumber(CoordinatorEntity, NumberEntity):
    """Number entity for setting inverter parameters."""

    entity_description: FelicityNumberDescription

    def __init__(self, coordinator, device_sn: str, description: FelicityNumberDescription):
        super().__init__(coordinator)
        self.entity_description = description
        self.device_sn = device_sn
        self._attr_unique_id = f"{device_sn}_{description.key}"
        self._attr_mode = NumberMode.BOX
        self._attr_native_min_value = description.min_value
        self._attr_native_max_value = description.max_value
        self._attr_native_step = description.step

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
    def native_value(self) -> float | None:
        """Return the current setting value from coordinator data."""
        device_entry = self.coordinator.data.get(self.device_sn, {})
        settings = device_entry.get("settings", {})
        val = settings.get(self.entity_description.key)

        if val is None or val == "":
            return None

        try:
            return float(val)
        except (ValueError, TypeError):
            return None

    async def async_set_native_value(self, value: float) -> None:
        """Apply parameter value to inverter."""
        target_value = round(value, 1) if self.entity_description.step < 1.0 else int(round(value))
        key = self.entity_description.key
        _LOGGER.info("Setting %s to %s for device %s", key, target_value, self.device_sn)

        success = await self.coordinator.api.set_device_setting(self.device_sn, {key: target_value})
        if success:
            device_entry = self.coordinator.data.get(self.device_sn)
            if device_entry and "settings" in device_entry:
                device_entry["settings"][key] = target_value
            self.async_write_ha_state()
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.error("Failed to set %s to %s on device %s", key, target_value, self.device_sn)
