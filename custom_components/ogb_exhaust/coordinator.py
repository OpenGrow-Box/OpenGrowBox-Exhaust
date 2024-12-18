from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import logging
import aiohttp
from datetime import timedelta


_LOGGER = logging.getLogger(__name__)

class PwmFansCoordinator(DataUpdateCoordinator):
    """Coordinator to manage data updates for PWM fans."""

    def __init__(self, hass, entry):
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="PWM Fans",
            update_interval=timedelta(seconds=10),
        )
        self.api_url = entry.data["api_url"]

    async def _async_update_data(self):
        """Fetch and update fan state."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/") as response:
                if response.status != 200:
                    raise RuntimeError(f"Failed to fetch data: {response.status}")
                data = await response.json()
                return {
                    "isRunning": data["data"].get("isRunning", False),
                    "DutyCycle": data["data"].get("DutyCycle", 10),
                }
