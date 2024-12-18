from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from custom_components.ogb_exhaust.coordinator import PwmFansCoordinator
from custom_components.ogb_exhaust.controller import ApiFanController


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up PWM Fans from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    coordinator = PwmFansCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    controller = ApiFanController(entry.data["api_url"])

    hass.data[DOMAIN][entry.entry_id] = {
        "coordinator": coordinator,
        "controller": controller,
    }

    await hass.config_entries.async_forward_entry_setups(entry, ["fan", "sensor"])

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle unloading of a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, ["fan", "sensor"])

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
