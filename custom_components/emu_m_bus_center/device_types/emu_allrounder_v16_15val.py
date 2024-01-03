import logging

from homeassistant.core import HomeAssistant

from custom_components.emu_m_bus_center.const import (
    ACTIVE_ENERGY_TARIFF_1,
    ACTIVE_ENERGY_TARIFF_2,
    ACTIVE_POWER_PHASE_1,
    ACTIVE_POWER_PHASE_2,
    ACTIVE_POWER_PHASE_3,
    ACTIVE_POWER_ALL_PHASES,
    VOLTAGE_PHASE_1,
    VOLTAGE_PHASE_2,
    VOLTAGE_PHASE_3,
    CURRENT_PHASE_1,
    CURRENT_PHASE_2,
    CURRENT_PHASE_3,
    CURRENT_ALL_PHASES,
    ERROR_FLAGS,
    POWER_FAILURES,
)
from custom_components.emu_m_bus_center.sensor import (
    EmuActiveEnergySensor,
    EmuActivePowerSensor,
    EmuVoltageSensor,
    EmuCurrentSensor,
    EmuErrorSensor,
    EmuCoordinator,
    EmuPowerFailureSensor,
)


class EmuAllrounderV16_15val(EmuCoordinator):
    def __init__(
        self,
        hass: HomeAssistant,
        config_entry_id: str,
        logger: logging.Logger,
        sensor_id: int,
        serial_no: str,
        center_name: str,
        sensor_given_name: str,
    ) -> None:
        self._config_entry_id = config_entry_id
        self._hass = hass
        self._name = (
            sensor_given_name if sensor_given_name else f"{sensor_id}/{serial_no}"
        )
        self._sensor_id = sensor_id
        self._logger = logger
        self._serial_no = serial_no
        self._center_name = center_name
        self._config = dict(
            self._hass.config_entries.async_get_entry(self._config_entry_id).data
        )

        super().__init__(
            hass=hass,
            config_entry_id=config_entry_id,
            logger=logger,
            sensor_id=sensor_id,
            serial_no=serial_no,
            center_name=center_name,
            sensor_given_name=sensor_given_name,
        )

    @property
    def version_number(self) -> int:
        return 16

    @property
    def sensor_count(self) -> int:
        return 17

    @property
    def model_name(self) -> str:
        return "Allrounder 3/75"

    @property
    def manufacturer_name(self) -> str:
        return "EMU"

    def sensors(self) -> list[str]:
        return [
            EmuActiveEnergySensor(self, ACTIVE_ENERGY_TARIFF_1),
            EmuActiveEnergySensor(self, ACTIVE_ENERGY_TARIFF_2),
            EmuActivePowerSensor(self, ACTIVE_POWER_PHASE_1),
            EmuActivePowerSensor(self, ACTIVE_POWER_PHASE_2),
            EmuActivePowerSensor(self, ACTIVE_POWER_PHASE_3),
            EmuActivePowerSensor(self, ACTIVE_POWER_ALL_PHASES),
            EmuVoltageSensor(self, VOLTAGE_PHASE_1),
            EmuVoltageSensor(self, VOLTAGE_PHASE_2),
            EmuVoltageSensor(self, VOLTAGE_PHASE_3),
            EmuCurrentSensor(self, CURRENT_PHASE_1),
            EmuCurrentSensor(self, CURRENT_PHASE_2),
            EmuCurrentSensor(self, CURRENT_PHASE_3),
            EmuCurrentSensor(self, CURRENT_ALL_PHASES),
            EmuPowerFailureSensor(self, POWER_FAILURES),
            EmuErrorSensor(self, ERROR_FLAGS),
        ]

    def parse(self, data: str) -> dict[str, float]:
        active_energy_tariff_1 = next(item for item in data if item["Position"] == 0)
        # test if we found the right entry for active_energy_tariff_1
        if not (
            active_energy_tariff_1["UnitStr"] == "Wh"
            and active_energy_tariff_1["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for active_energy_tariff_1 in the JSON response from the "
                "M-Bus Center"
            )

        active_energy_tariff_2 = next(item for item in data if item["Position"] == 1)
        # test if we found the right entry for active_energy_tariff_2
        if not (
            active_energy_tariff_2["UnitStr"] == "Wh"
            and active_energy_tariff_2["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for active_energy_tariff_2 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_phase_1 = next(item for item in data if item["Position"] == 2)
        # test if we found the right entry for active_power_phase_1
        if not (
            active_power_phase_1["UnitStr"] == "W"
            and active_power_phase_1["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_phase_2 = next(item for item in data if item["Position"] == 3)
        # test if we found the right entry for active_power_phase_2
        if not (
            active_power_phase_2["UnitStr"] == "W"
            and active_power_phase_2["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_phase_3 = next(item for item in data if item["Position"] == 4)
        # test if we found the right entry for power_phase_3
        if not (
            active_power_phase_3["UnitStr"] == "W"
            and active_power_phase_3["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        power_all_phases = next(item for item in data if item["Position"] == 5)
        # test if we found the right entry for power_phase_3
        if not (
            power_all_phases["UnitStr"] == "W"
            and power_all_phases["DescriptionStr"] == "Power"
        ):
            raise ValueError(
                "Did not find the required Fields for power_all_phases in the JSON response from the "
                "M-Bus Center"
            )

        voltage_phase_1 = next(item for item in data if item["Position"] == 6)
        # test if we found the right entry voltage_phase_1
        if not (
            voltage_phase_1["UnitStr"] == "V"
            and voltage_phase_1["DescriptionStr"] == "Volts (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for voltage_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        voltage_phase_2 = next(item for item in data if item["Position"] == 7)
        # test if we found the right entry voltage_phase_2
        if not (
            voltage_phase_2["UnitStr"] == "V"
            and voltage_phase_2["DescriptionStr"] == "Volts (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for voltage_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        voltage_phase_3 = next(item for item in data if item["Position"] == 8)
        # test if we found the right entry voltage_phase_3
        if not (
            voltage_phase_3["UnitStr"] == "V"
            and voltage_phase_3["DescriptionStr"] == "Volts (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for voltage_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        current_phase_1 = next(item for item in data if item["Position"] == 9)
        # test if we found the right entry current_phase_1
        if not (
            current_phase_1["UnitStr"] == "A"
            and current_phase_1["DescriptionStr"] == "Ampere (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for current_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        current_phase_2 = next(item for item in data if item["Position"] == 10)
        # test if we found the right entry current_phase_2
        if not (
            current_phase_2["UnitStr"] == "A"
            and current_phase_2["DescriptionStr"] == "Ampere (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for current_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        current_phase_3 = next(item for item in data if item["Position"] == 11)
        # test if we found the right entry current_phase_3
        if not (
            current_phase_3["UnitStr"] == "A"
            and current_phase_3["DescriptionStr"] == "Ampere (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for current_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        current_all_phases = next(item for item in data if item["Position"] == 12)
        # test if we found the right entry current_all_phases
        if not (
            current_all_phases["UnitStr"] == "A"
            and current_all_phases["DescriptionStr"] == "Ampere"
        ):
            raise ValueError(
                "Did not find the required Fields for current_all_phases in the JSON response from the "
                "M-Bus Center"
            )

        power_failures = next(item for item in data if item["Position"] == 13)
        # test if we found the right entry power_failures
        if not (
            power_failures["UnitStr"] == "None"
            and power_failures["DescriptionStr"] == "Reset counter"
        ):
            raise ValueError(
                "Did not find the required Fields for resets in the JSON response from the "
                "M-Bus Center"
            )

        error_flags = next(item for item in data if item["Position"] == 14)
        # test if we found the right entry error_flags
        if not (
            error_flags["UnitStr"] == "Bin"
            and error_flags["DescriptionStr"] == "Error flags (Device type specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for error_flags in the JSON response from the "
                "M-Bus Center"
            )

        return {
            ACTIVE_ENERGY_TARIFF_1: int(active_energy_tariff_1["LoggerLastValue"])
            / 1000,
            ACTIVE_ENERGY_TARIFF_2: int(active_energy_tariff_2["LoggerLastValue"])
            / 1000,
            ACTIVE_POWER_PHASE_1: int(active_power_phase_1["LoggerLastValue"]) / 1000,
            ACTIVE_POWER_PHASE_2: int(active_power_phase_2["LoggerLastValue"]) / 1000,
            ACTIVE_POWER_PHASE_3: int(active_power_phase_3["LoggerLastValue"]) / 1000,
            ACTIVE_POWER_ALL_PHASES: int(power_all_phases["LoggerLastValue"]) / 1000,
            VOLTAGE_PHASE_1: int(voltage_phase_1["LoggerLastValue"]),
            VOLTAGE_PHASE_2: int(voltage_phase_2["LoggerLastValue"]),
            VOLTAGE_PHASE_3: int(voltage_phase_3["LoggerLastValue"]),
            CURRENT_PHASE_1: int(current_phase_1["LoggerLastValue"]),
            CURRENT_PHASE_2: int(current_phase_2["LoggerLastValue"]),
            CURRENT_PHASE_3: int(current_phase_3["LoggerLastValue"]),
            CURRENT_ALL_PHASES: int(current_all_phases["LoggerLastValue"]),
            POWER_FAILURES: int(power_failures["LoggerLastValue"]),
            ERROR_FLAGS: int(error_flags["LoggerLastValue"]),
        }
