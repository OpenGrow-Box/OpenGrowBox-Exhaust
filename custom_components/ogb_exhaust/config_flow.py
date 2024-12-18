from homeassistant import config_entries
import voluptuous as vol
from custom_components.ogb_exhaust.const import DOMAIN

class PwmFansConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for PWM Fans."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)

        data_schema = vol.Schema({
            vol.Required("api_url", description="API URL for PWM Fan Controller"): str,
            vol.Required("name", description="Fan name (e.g., Flower)"): str,
        })

        return self.async_show_form(step_id="user", data_schema=data_schema)
