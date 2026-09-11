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

    async def async_step_reauth(self, entry_data=None):
        """Perform reauth upon an authentication error."""
        self._reauth_entry = self.hass.config_entries.async_get_entry(self.context.get("entry_id"))
        return await self.async_step_reauth_confirm()

    async def async_step_reauth_confirm(self, user_input=None):
        """Dialog that informs the user that reauth is required."""
        errors = {}
        if not hasattr(self, "_reauth_entry") or self._reauth_entry is None:
            self._reauth_entry = self.hass.config_entries.async_get_entry(self.context.get("entry_id"))

        email = self._reauth_entry.data.get(CONF_EMAIL, "") if self._reauth_entry else ""

        if user_input is not None and self._reauth_entry:
            new_password = user_input[CONF_PASSWORD]
            try:
                session = create_felicity_client_session(self.hass)
                api = FelicitySolarAPI(email, new_password, session)
                await api.initialize()

                self.hass.config_entries.async_update_entry(
                    self._reauth_entry,
                    data={
                        **self._reauth_entry.data,
                        CONF_PASSWORD: new_password,
                    },
                )
                await self.hass.config_entries.async_reload(self._reauth_entry.entry_id)
                return self.async_abort(reason="reauth_successful")
            except Exception as err:
                _LOGGER.error("Re-authentication failed for %s: %s", email, err)
                errors["base"] = "invalid_auth"

        return self.async_show_form(
            step_id="reauth_confirm",
            data_schema=vol.Schema({
                vol.Required(CONF_PASSWORD): selector.TextSelector(
                    selector.TextSelectorConfig(type=selector.TextSelectorType.PASSWORD)
                ),
            }),
            description_placeholders={"email": email},
            errors=errors,
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
