from homeassistant.components.fan import FanEntity, FanEntityFeature
from .const import DOMAIN


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up PWM fan entities from a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    controller = hass.data[DOMAIN][config_entry.entry_id]["controller"]
    name = config_entry.data["name"]

    # Create the fan entity
    async_add_entities([
        PwmFanEntity(
            coordinator=coordinator,
            controller=controller,
            unique_id=f"{name}_exhaust",
            name=f"{name} Exhaust"
        )
    ])


class PwmFanEntity(FanEntity):
    """Representation of an API-controlled fan."""

    _attr_supported_features = FanEntityFeature.SET_SPEED | FanEntityFeature.TURN_ON | FanEntityFeature.TURN_OFF

    def __init__(self, coordinator, controller, unique_id, name):
        """Initialize the fan entity."""
        self._coordinator = coordinator
        self._controller = controller
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._is_on = False
        self._speed_percentage = 10  # Default to 10%

    @property
    def is_on(self):
        """Return true if the fan is on."""
        return self._coordinator.data.get("isRunning", False)

    @property
    def percentage(self):
        """Return the current speed percentage."""
        return self._coordinator.data.get("DutyCycle", 10)

    @property
    def device_info(self):
        """Return device information to link this entity to a device."""
        return {
            "identifiers": {(DOMAIN, self._attr_unique_id)},
            "name": self._attr_name,
            "model": "Exhaust Device",
            "manufacturer": "OpenGrowBox",
        }

    async def async_turn_on(self, percentage=None, **kwargs):
        """Turn on the fan."""
        if percentage is None:
            percentage = self.percentage  # Default to current percentage if not set
        self._is_on = True
        await self._controller.start_fan()
        await self._controller.set_pwm(percentage)

    async def async_turn_off(self, **kwargs):
        """Turn off the fan."""
        self._is_on = False
        await self._controller.stop_fan()

    async def async_set_percentage(self, percentage: int):
        """Set the fan's speed percentage."""
        percentage = max(10, min(percentage, 95))  # Enforce min/max
        await self._controller.set_pwm(percentage)
        self._speed_percentage = percentage

    async def async_update(self):
        """Fetch updates from the coordinator."""
        await self._coordinator.async_request_refresh()
