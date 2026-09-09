import logging
from homeassistant.components.switch import (
    SwitchEntity,
    SwitchEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .api import DeviceTypeEnum

_LOGGER = logging.getLogger(__name__)

SWITCH_DESCRIPTIONS: tuple[SwitchEntityDescription, ...] = (
    SwitchEntityDescription(
        key="gridChargeEnable",
        name="Grid Charge",
        icon="mdi:transmission-tower-export",
    ),
    SwitchEntityDescription(
        key="buzzerEnable",
        name="Buzzer",
        icon="mdi:volume-high",
    ),
    SwitchEntityDescription(
        key="lcdBacklightEnable",
        name="LCD Backlight",
        icon="mdi:television-ambient-light",
    ),
    SwitchEntityDescription(
        key="remoteOnOffEnable",
        name="Inverter Remote Standby",
        icon="mdi:power-standby",
    ),
    SwitchEntityDescription(
        key="remoteOutputOnOffControl",
        name="AC Output Relay",
        icon="mdi:power-socket-eu",
    ),
    SwitchEntityDescription(
        key="antiIslandingDetectionEnable",
        name="Anti-Islanding Protection",
        icon="mdi:shield-check",
    ),
    SwitchEntityDescription(
        key="gridPeakShavingEnable",
        name="Grid Peak Shaving",
        icon="mdi:chart-bell-curve",
    ),
    SwitchEntityDescription(
        key="timeOfUseEnable",
        name="Time of Use",
        icon="mdi:clock-outline",
    ),
    SwitchEntityDescription(
        key="genChargeEnable",
        name="Generator Charge",
        icon="mdi:generator-stationary",
    ),
    SwitchEntityDescription(
        key="overLoadProtectionResetEnable",
        name="Overload Auto-Reset",
        icon="mdi:restart",
    ),
)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the switch platform dynamically based on discovered devices."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []
    if coordinator.data:
        for device_sn, device_info in coordinator.data.items():
            device_type = device_info.get("type")
            settings = device_info.get("settings", {})
            if device_type == DeviceTypeEnum.HIGH_FREQUENCY_INVERTER:
                if not settings or coordinator.api.has_openapi_permissions is False:
                    _LOGGER.info(
                        "Skipping switch entities for inverter %s: remote control not permitted or settings unavailable",
                        device_sn,
                    )
                    continue
                for desc in SWITCH_DESCRIPTIONS:
                    entities.append(FelicityInverterSwitch(coordinator, device_sn, desc))
                _LOGGER.info(
                    "Created %d switch control entity/entities for inverter %s",
                    len(SWITCH_DESCRIPTIONS),
                    device_sn,
                )

    if entities:
        _LOGGER.info("Adding %d switch entities to Home Assistant", len(entities))
        async_add_entities(entities)


class FelicityInverterSwitch(CoordinatorEntity, SwitchEntity):
    """Switch entity for toggling inverter binary settings."""

    def __init__(self, coordinator, device_sn: str, description: SwitchEntityDescription):
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
    def is_on(self) -> bool | None:
        """Return True if the switch is on."""
        device_entry = self.coordinator.data.get(self.device_sn, {})
        settings = device_entry.get("settings", {})
        val = settings.get(self.entity_description.key)

        if val is None or val == "":
            return None

        try:
            return int(val) == 1
        except (ValueError, TypeError):
            return None

    async def async_turn_on(self, **kwargs) -> None:
        """Turn on the switch."""
        key = self.entity_description.key
        _LOGGER.info("Turning ON %s for device %s", key, self.device_sn)

        success = await self.coordinator.api.set_device_setting(self.device_sn, {key: 1})
        if success:
            device_entry = self.coordinator.data.get(self.device_sn)
            if device_entry and "settings" in device_entry:
                device_entry["settings"][key] = 1
            self.async_write_ha_state()
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.error("Failed to turn ON %s for device %s", key, self.device_sn)

    async def async_turn_off(self, **kwargs) -> None:
        """Turn off the switch."""
        key = self.entity_description.key
        _LOGGER.info("Turning OFF %s for device %s", key, self.device_sn)

        success = await self.coordinator.api.set_device_setting(self.device_sn, {key: 0})
        if success:
            device_entry = self.coordinator.data.get(self.device_sn)
            if device_entry and "settings" in device_entry:
                device_entry["settings"][key] = 0
            self.async_write_ha_state()
            await self.coordinator.async_request_refresh()
        else:
            _LOGGER.error("Failed to turn OFF %s for device %s", key, self.device_sn)
