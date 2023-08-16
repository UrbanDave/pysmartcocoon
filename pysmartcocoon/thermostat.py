"""Define a SmartCocoon Thermostat class."""
# pylint: disable=too-few-public-methods,too-many-instance-attributes

from typing import Any


class Thermostat:  # pylint: disable=too-many-instance-attributes
    """Define the thermostat."""

    def __init__(self, data: dict[str, Any]) -> None:
        """Initialize."""
        self._identifier: int = data["id"]
        self._name: str = data["name"]
        self._thermostat_id: id = data["thermostat_id"]
        self._token: str = data["token"]
        self._hvac_mode: str = data["hvac_mode"]
        self._hvac_state: str = data["hvac_state"]
        self._temperature: float = data["temperature"]
        self._target_temperature: float = data["target_temperature"]
        self._vendor: str = data["vendor"]

    @property
    def identifier(self) -> str:
        """Return Thermostat id.

        This is a numerical ID generated by SmartCocoon
        This value can change if the thermostat is re-added to
        an cloud account
        """
        return self._identifier

    @property
    def name(self) -> str:
        """Return thermostat name."""
        return self._name

    @property
    def thermostat_id(self) -> str:
        """Return thermostat id."""
        return self._thermostat_id

    @property
    def token(self) -> str:
        """Return token ."""
        return self._token

    @property
    def hvac_mode(self) -> str:
        """Return HVAC mode"""
        return self._hvac_mode

    @property
    def hvac_state(self) -> str:
        """Return HVAC state"""
        return self._hvac_state

    @property
    def temperature(self) -> str:
        """Return is temperature."""
        return self._temperature

    @property
    def target_temperature(self) -> str:
        """Return target temperature"""
        return self._target_temperature

    @property
    def vendor(self) -> str:
        """Return vendor"""
        return self._vendor
