from homeassistant.helpers.entity import Entity
from custom_components.ogb_exhaust.const import DOMAIN


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the duty cycle sensor."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.data["name"]
    unique_id = f"{name}_exhaust"

    # Add the sensor entity
    async_add_entities([
        DutyCycleSensor(
            coordinator=coordinator,
            unique_id=unique_id,
            name=f"{name} Duty Cycle"
        )
    ])


class DutyCycleSensor(Entity):
    """Representation of a sensor for the PWM duty cycle."""

    def __init__(self, coordinator, unique_id, name):
        """Initialize the duty cycle sensor."""
        self._coordinator = coordinator
        self._attr_name = name
        self._attr_unique_id = unique_id

    @property
    def state(self):
        """Return the current Duty Cycle percentage."""
        return self._coordinator.data.get("DutyCycle", 10)

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return "%"

    @property
    def device_info(self):
        """Return the device information to associate the sensor with the fan."""
        return {
            "identifiers": {(DOMAIN, self._attr_unique_id.split("_exhaust")[0])},
        }
