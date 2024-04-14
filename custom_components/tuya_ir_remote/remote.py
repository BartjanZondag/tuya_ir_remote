"""Support for Tuya IR Remote entity."""
from homeassistant.helpers.entity import Entity

class TuyaIrRemoteEntity(Entity):
    """Representation of a Tuya IR Remote entity."""

    def __init__(self, device_info):
        """Initialize the entity."""
        self._device_info = device_info
        self._name = device_info['data']['name']
        self._state = None
        self._last_pressed_function = None

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    @property
    def state(self):
        """Return the state of the entity."""
        return self._state

    @property
    def device_info(self):
        """Return device information."""
        return self._device_info

    @property
    def last_pressed_function(self):
        """Return the last pressed function."""
        return self._last_pressed_function

    def press_function(self, function_name):
        """Simulate pressing a function (button) on the device."""
        # Perform actions to send the function command to the device
        # Here, you can simulate the action by updating the last pressed function
        self._last_pressed_function = function_name

    def update(self):
        """Update the state of the entity."""
        # Update the state of the entity, for example by querying the device for its current state
        self._state = "On" if self._device_info['data']['online'] else "Off"
