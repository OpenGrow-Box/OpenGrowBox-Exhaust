# OpenGrowBox-Exhaust - Home Assistant Integration

## Overview

Welcome to the **OpenGrowBox-Exhaust Home Assistant Integration** repository! This project is designed to integrate EC exhaust fans running on Raspberry Pi with the RuckEC Web API into your Home Assistant setup. Manage your grow environment's ventilation efficiently and ensure optimal airflow control.

---

## Features

- **Fan Control:** Seamless integration with EC exhaust fans.
- **Dynamic Adjustments:** Automate fan speeds based on environmental conditions.
- **RuckEC API Integration:** Direct control via the RuckEC Web API.
- **Custom Automation:** Configure advanced rules and automations in Home Assistant.

---

## Getting Started

### Prerequisites

- A working **Home Assistant** instance.
- OpenGrowBox hardware or a compatible Raspberry Pi setup.
- Basic knowledge of Home Assistant configurations.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/OpenGrow-Box/OpenGrowBox-Exhaust.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd OpenGrowBox-Exhaust
   ```
3. Copy the directory to your Home Assistant custom components folder:
   ```bash
   cp -r OpenGrowBox-Exhaust /usr/share/hassio/homeassistant/custom_components/
   ```
4. Restart Home Assistant to load the new component.

---

## Configuration

### Basic Setup

1. Add the OpenGrowBox-Exhaust integration to your Home Assistant and restart
2. Add the Integration.
3. Restart Home Assistant to apply the changes.

### Device Configuration

Use the Home Assistant dashboard to monitor and control your exhaust fans.

---

## Example Automations

### Automation 1: Increase Fan Speed When Temperature Exceeds Threshold

```yaml
alias: Increase Fan Speed
trigger:
  - platform: numeric_state
    entity_id: sensor.temperature_sensor
    above: 28
action:
  - service: fan.set_percentage
    target:
      entity_id: fan.exhaust_fan
    data:
      percentage: 80
```

### Automation 2: Turn Off Fan When Humidity is Low

```yaml
alias: Turn Off Fan When Humidity Low
trigger:
  - platform: numeric_state
    entity_id: sensor.humidity_sensor
    below: 40
action:
  - service: fan.turn_off
    target:
      entity_id: fan.exhaust_fan
```

---

## Roadmap

- Add support for multi-fan setups.
- Expand compatibility with other fan APIs.
- Develop a detailed dashboard for airflow visualization.

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request. Ensure your code adheres to the repository's coding standards.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Support

For issues and feature requests, please open an issue on [GitHub](https://github.com/OpenGrow-Box/OpenGrowBox-Exhaust/issues).
