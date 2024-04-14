"""Support for Tuya IR Remote sensors."""
from homeassistant.helpers.entity import Entity

class TuyaIrRemoteSensor(Entity):
    """Representation of a Tuya IR Remote sensor."""

    def __init__(self, device_info):
        """Initialize the sensor."""
        self._device_info = device_info
        self._name = device_info['data']['name']
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_info(self):
        """Return device information."""
        return self._device_info

    def update(self):
        """Update the sensor."""
        # You can implement sensor update logic here
        # For example, query the device for its current state
        self._state = "On" if self._device_info['data']['online'] else "Off"
