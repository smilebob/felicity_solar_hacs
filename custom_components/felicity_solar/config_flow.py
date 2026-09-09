import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import DOMAIN, CONF_EMAIL, CONF_PASSWORD, CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL
from .api import FelicitySolarAPI, create_felicity_client_session

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_EMAIL): selector.TextSelector(
        selector.TextSelectorConfig(type=selector.TextSelectorType.EMAIL)
    ),
    vol.Required(CONF_PASSWORD): selector.TextSelector(
        selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)
    ),
})


class FelicitySolarConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Felicity Solar."""
    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: config_entries.ConfigEntry):
        """Get the options flow for this handler."""
        return FelicitySolarOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle the initial setup step."""
        errors = {}

        if user_input is not None:
            email = user_input[CONF_EMAIL]
            password = user_input[CONF_PASSWORD]

            try:
                # Create a session with custom SSL handling for Felicity Solar
                session = create_felicity_client_session(self.hass)

                # Initialize the API to test credentials
                api = FelicitySolarAPI(email, password, session)

                # If initialize() passes without throwing an error, credentials are valid!
                await api.initialize()

                return self.async_create_entry(
                    title=email,
                    data=user_input
                )
            except Exception as err:
                _LOGGER.error(
                    f"Failed to authenticate with Felicity Solar: {err}")
                errors["base"] = "invalid_auth"

        # Show the form (with red errors if authentication failed)
        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors
        )


class FelicitySolarOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Felicity Solar."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current_interval = self.config_entry.options.get(
            CONF_UPDATE_INTERVAL,
            self.config_entry.data.get(CONF_UPDATE_INTERVAL, DEFAULT_UPDATE_INTERVAL)
        )

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_UPDATE_INTERVAL, default=current_interval): selector.NumberSelector(
                    selector.NumberSelectorConfig(
                        min=10,
                        max=600,
                        step=5,
                        unit_of_measurement="s",
                        mode=selector.NumberSelectorMode.BOX,
                    )
                ),
            }),
        )
