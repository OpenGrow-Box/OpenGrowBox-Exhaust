import aiohttp

class ApiFanController:
    """Controller for a fan using an external API."""

    def __init__(self, api_url: str):
        """Initialize the controller with the API URL."""
        self.api_url = api_url
        self.min_percentage = 10  # Minimum allowed percentage
        self.max_percentage = 95  # Maximum allowed percentage

    async def set_pwm(self, percentage: int):
        """Set the PWM duty cycle via API."""
        if percentage < self.min_percentage:
            percentage = self.min_percentage
        if percentage > self.max_percentage:
            percentage = self.max_percentage

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_url}/air/ctrl", json={"newDuty": percentage}) as response:
                if response.status != 200:
                    raise RuntimeError(f"Failed to set PWM: {response.status}")

    async def start_fan(self):
        """Start the fan via API."""
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_url}/air/start") as response:
                if response.status not in (200, 409):  # 409 if already running
                    raise RuntimeError(f"Failed to start fan: {response.status}")

    async def stop_fan(self):
        """Stop the fan via API."""
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_url}/air/stop") as response:
                if response.status not in (200, 409):  # 409 if already stopped
                    raise RuntimeError(f"Failed to stop fan: {response.status}")

    async def get_status(self):
        """Get the current status of the fan."""
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_url}/") as response:
                if response.status != 200:
                    raise RuntimeError(f"Failed to get status: {response.status}")
                result = await response.json()
                return result["data"]
