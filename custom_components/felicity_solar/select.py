import logging
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity, SelectEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .api import DeviceTypeEnum

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True, kw_only=True)
class FelicitySelectDescription(SelectEntityDescription):
    """Description for Felicity Solar select entity."""
    options_map: dict[str, int]


SELECT_DESCRIPTIONS: tuple[FelicitySelectDescription, ...] = (
    FelicitySelectDescription(
        key="operatedMode",
        name="Work Mode",
        icon="mdi:solar-power",
        options=["General Mode", "Backup Mode", "Eco Mode", "Gen Mode"],
        options_map={
            "General Mode": 0,
            "Backup Mode": 1,
            "Eco Mode": 2,
            "Gen Mode": 3,
        },
    ),
    FelicitySelectDescription(
        key="energyPriority",
        name="Energy Priority",
        icon="mdi:priority-high",
        options=["Battery First", "Load First"],
        options_map={
            "Battery First": 0,
            "Load First": 1,
        },
    ),
    FelicitySelectDescription(
        key="zeroExportFunction",
        name="Zero Export Mode",
        icon="mdi:transmission-tower",
        options=["To Load", "To CT"],
        options_map={
            "To Load": 1,
            "To CT": 2,
        },
    ),
    FelicitySelectDescription(
        key="acOutputRatedFrequency",
        name="AC Output Frequency",
        icon="mdi:sine-wave",
        options=["50 Hz", "60 Hz"],
        options_map={
            "50 Hz": 0,
            "60 Hz": 1,
        },
    ),
    FelicitySelectDescription(
        key="batteryModel",
        name="Battery Model Type",
        icon="mdi:battery",
        options=["User Defined", "Lithium Battery", "FelicitySolar LPBF", "FelicitySolar LPBA"],
        options_map={
            "User Defined": 0,
            "Lithium Battery": 1,
            "FelicitySolar LPBF": 2,
            "FelicitySolar LPBA": 3,
        },
    ),
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the select platform dynamically based on discovered devices."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    if coordinator.data:
        for device_sn, device_info in coordinator.data.items():
            device_type = device_info.get("type")
            if device_type == DeviceTypeEnum.HIGH_FREQUENCY_INVERTER:
                for desc in SELECT_DESCRIPTIONS:
                    entities.append(FelicityInverterSelect(coordinator, device_sn, desc))
                _LOGGER.info(
                    "Created %d select entities for inverter %s",
                    len(SELECT_DESCRIPTIONS),
                    device_sn,
                )

    if entities:
        _LOGGER.info("Adding %d select entity/entities to Home Assistant", len(entities))
        async_add_entities(entities)


class FelicityInverterSelect(CoordinatorEntity, SelectEntity):
    """Select entity for controlling inverter operating modes and choices."""

    entity_description: FelicitySelectDescription

    def __init__(self, coordinator, device_sn: str, description: FelicitySelectDescription):
        super().__init__(coordinator)
        self.entity_description = description
        self.device_sn = device_sn
        self._attr_unique_id = f"{device_sn}_{description.key}"
        self._attr_options = description.options
        self._int_to_mode = {v: k for k, v in description.options_map.items()}

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
    def current_option(self) -> str | None:
        """Return the current selected option."""
        device_entry = self.coordinator.data.get(self.device_sn, {})
        settings = device_entry.get("settings", {})
        raw_val = settings.get(self.entity_description.key)

        if raw_val is None:
            # For operatedMode, fall back to telemetry workMode if settings not yet populated
            if self.entity_description.key == "operatedMode":
                telemetry_mode = device_entry.get("data", {}).get("workMode")
                for opt in self.entity_description.options:
                    if opt.lower() in str(telemetry_mode).lower():
                        return opt
            return None

        try:
            return self._int_to_mode.get(int(raw_val))
        except (ValueError, TypeError):
            return None

    async def async_select_option(self, option: str) -> None:
        """Apply option change to inverter."""
        if option not in self.entity_description.options_map:
            _LOGGER.error("Invalid option '%s' for %s", option, self.entity_description.key)
            return

        target_int = self.entity_description.options_map[option]
        key = self.entity_description.key
        _LOGGER.info("Setting %s to '%s' (%d) for device %s", key, option, target_int, self.device_sn)

        success = await self.coordinator.api.set_device_setting(self.device_sn, {key: target_int})
        if success:
            device_entry = self.coordinator.data.get(self.device_sn)
            if device_entry and "settings" in device_entry:
                device_entry["settings"][key] = target_int
            self.async_write_ha_state()
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.error("Failed to set %s to '%s' on device %s", key, option, self.device_sn)
