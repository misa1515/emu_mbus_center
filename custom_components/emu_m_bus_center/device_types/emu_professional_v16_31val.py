from custom_components.emu_m_bus_center.device_types.readable_device import (
    Readable_device,
)

from custom_components.emu_m_bus_center.const import (
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
    FREQUENCY,
    CURRENT_TRANSFORMER_FACTOR,
    ERROR_FLAGS,
    ACTIVE_ENERGY_IMPORT_TARIFF_1,
    ACTIVE_ENERGY_IMPORT_TARIFF_2,
    ACTIVE_ENERGY_EXPORT_TARIFF_1,
    ACTIVE_ENERGY_EXPORT_TARIFF_2,
    REACTIVE_ENERGY_INDUCTIVE_TARIFF_1,
    REACTIVE_ENERGY_INDUCTIVE_TARIFF_2,
    REACTIVE_ENERGY_CAPACITIVE_TARIFF_1,
    REACTIVE_ENERGY_CAPACITIVE_TARIFF_2,
    REACTIVE_POWER_PHASE_1,
    REACTIVE_POWER_PHASE_2,
    REACTIVE_POWER_PHASE_3,
    REACTIVE_POWER_ALL_PHASES,
    APPARENT_POWER_ALL_PHASES,
    FORM_FACTOR_PHASE_1,
    FORM_FACTOR_PHASE_2,
    FORM_FACTOR_PHASE_3,
    POWER_FAILURES,
)

from custom_components.emu_m_bus_center.sensor import (
    EmuActiveEnergySensor,
    EmuActivePowerSensor,
    EmuVoltageSensor,
    EmuCurrentSensor,
    EmuFrequencySensor,
    EmuTransformerFactorSensor,
    EmuErrorSensor,
    EmuReactiveEnergySensor,
    EmuReactivePowerSensor,
    EmuApparentPowerSensor,
    EmuFormFactorSensor,
    EmuPowerFailureSensor,
)


class EmuProfessionalV16_31val(Readable_device):
    @property
    def version_number(self):
        return 16

    @property
    def sensor_count(self):
        return 31

    @property
    def model_name(self) -> str:
        return "Professional II 3/100"

    @property
    def manufacturer_name(self) -> str:
        return "EMU"

    def sensors(self, coordinator) -> list[str]:
        return [
            EmuActiveEnergySensor(coordinator, ACTIVE_ENERGY_IMPORT_TARIFF_1),
            EmuActiveEnergySensor(coordinator, ACTIVE_ENERGY_IMPORT_TARIFF_2),
            EmuActiveEnergySensor(coordinator, ACTIVE_ENERGY_EXPORT_TARIFF_1),
            EmuActiveEnergySensor(coordinator, ACTIVE_ENERGY_EXPORT_TARIFF_2),
            EmuReactiveEnergySensor(coordinator, REACTIVE_ENERGY_INDUCTIVE_TARIFF_1),
            EmuReactiveEnergySensor(coordinator, REACTIVE_ENERGY_INDUCTIVE_TARIFF_2),
            EmuReactiveEnergySensor(coordinator, REACTIVE_ENERGY_CAPACITIVE_TARIFF_1),
            EmuReactiveEnergySensor(coordinator, REACTIVE_ENERGY_CAPACITIVE_TARIFF_2),
            EmuActivePowerSensor(coordinator, ACTIVE_POWER_PHASE_1),
            EmuActivePowerSensor(coordinator, ACTIVE_POWER_PHASE_2),
            EmuActivePowerSensor(coordinator, ACTIVE_POWER_PHASE_3),
            EmuActivePowerSensor(coordinator, ACTIVE_POWER_ALL_PHASES),
            EmuReactivePowerSensor(coordinator, REACTIVE_POWER_PHASE_1),
            EmuReactivePowerSensor(coordinator, REACTIVE_POWER_PHASE_2),
            EmuReactivePowerSensor(coordinator, REACTIVE_POWER_PHASE_3),
            EmuReactivePowerSensor(coordinator, REACTIVE_POWER_ALL_PHASES),
            EmuApparentPowerSensor(coordinator, APPARENT_POWER_ALL_PHASES),
            EmuVoltageSensor(coordinator, VOLTAGE_PHASE_1),
            EmuVoltageSensor(coordinator, VOLTAGE_PHASE_2),
            EmuVoltageSensor(coordinator, VOLTAGE_PHASE_3),
            EmuCurrentSensor(coordinator, CURRENT_PHASE_1),
            EmuCurrentSensor(coordinator, CURRENT_PHASE_2),
            EmuCurrentSensor(coordinator, CURRENT_PHASE_3),
            EmuCurrentSensor(coordinator, CURRENT_ALL_PHASES),
            EmuFormFactorSensor(coordinator, FORM_FACTOR_PHASE_1),
            EmuFormFactorSensor(coordinator, FORM_FACTOR_PHASE_2),
            EmuFormFactorSensor(coordinator, FORM_FACTOR_PHASE_3),
            EmuFrequencySensor(coordinator, FREQUENCY),
            EmuPowerFailureSensor(coordinator, POWER_FAILURES),
            EmuTransformerFactorSensor(coordinator, CURRENT_TRANSFORMER_FACTOR),
            EmuErrorSensor(coordinator, ERROR_FLAGS),
        ]

    def parse(self, data: str) -> dict[str, float]:
        active_energy_import_tariff_1 = next(
            item for item in data if item["Position"] == 0
        )
        # test if we found the right entry for active_energy_import_tariff_1
        if not (
            active_energy_import_tariff_1["UnitStr"] == "Wh"
            and active_energy_import_tariff_1["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for active_energy_import_tariff_1 in the JSON response from the "
                "M-Bus Center"
            )

        active_energy_import_tariff_2 = next(
            item for item in data if item["Position"] == 1
        )
        # test if we found the right entry for active_energy_import_tariff_2
        if not (
            active_energy_import_tariff_2["UnitStr"] == "Wh"
            and active_energy_import_tariff_2["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for active_energy_import_tariff_2 in the JSON response from the "
                "M-Bus Center"
            )

        active_energy_export_tariff_1 = next(
            item for item in data if item["Position"] == 2
        )
        # test if we found the right entry for active_energy_export_tariff_1
        if not (
            active_energy_export_tariff_1["UnitStr"] == "Wh"
            and active_energy_export_tariff_1["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for active_energy_export_tariff_1 in the JSON response from the "
                "M-Bus Center"
            )

        active_energy_export_tariff_2 = next(
            item for item in data if item["Position"] == 3
        )
        # test if we found the right entry for active_energy_export_tariff_2
        if not (
            active_energy_export_tariff_2["UnitStr"] == "Wh"
            and active_energy_export_tariff_2["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for active_energy_export_tariff_2 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_energy_inductive_tariff_1 = next(
            item for item in data if item["Position"] == 4
        )
        # test if we found the right entry for reactive_energy_inductive_tariff_1
        if not (
            reactive_energy_inductive_tariff_1["UnitStr"] == "Wh"
            and reactive_energy_inductive_tariff_1["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_energy_inductive_tariff_1 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_energy_inductive_tariff_2 = next(
            item for item in data if item["Position"] == 5
        )
        # test if we found the right entry for reactive_energy_inductive_tariff_2
        if not (
            reactive_energy_inductive_tariff_2["UnitStr"] == "Wh"
            and reactive_energy_inductive_tariff_2["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_energy_inductive_tariff_2 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_energy_capacitive_tariff_1 = next(
            item for item in data if item["Position"] == 6
        )
        # test if we found the right entry for reactive_energy_capacitive_tariff_1
        if not (
            reactive_energy_capacitive_tariff_1["UnitStr"] == "Wh"
            and reactive_energy_capacitive_tariff_1["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_energy_capacitive_tariff_1 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_energy_capacitive_tariff_2 = next(
            item for item in data if item["Position"] == 7
        )
        # test if we found the right entry for reactive_energy_capacitive_tariff_2
        if not (
            reactive_energy_capacitive_tariff_2["UnitStr"] == "Wh"
            and reactive_energy_capacitive_tariff_2["DescriptionStr"] == "Energy"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_energy_capacitive_tariff_2 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_phase_1 = next(item for item in data if item["Position"] == 8)
        # test if we found the right entry for active_power_phase_1
        if not (
            active_power_phase_1["UnitStr"] == "W"
            and active_power_phase_1["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_phase_2 = next(item for item in data if item["Position"] == 9)
        # test if we found the right entry for active_power_phase_2
        if not (
            active_power_phase_2["UnitStr"] == "W"
            and active_power_phase_2["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_phase_3 = next(item for item in data if item["Position"] == 10)
        # test if we found the right entry for active_power_phase_3
        if not (
            active_power_phase_3["UnitStr"] == "W"
            and active_power_phase_3["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        active_power_all_phases = next(item for item in data if item["Position"] == 11)
        # test if we found the right entry for active_power_all_phases
        if not (
            active_power_all_phases["UnitStr"] == "W"
            and active_power_all_phases["DescriptionStr"] == "Power"
        ):
            raise ValueError(
                "Did not find the required Fields for active_power_all_phases in the JSON response from the "
                "M-Bus Center"
            )

        reactive_power_phase_1 = next(item for item in data if item["Position"] == 12)
        # test if we found the right entry for reactive_power_phase_1
        if not (
            reactive_power_phase_1["UnitStr"] == "W"
            and reactive_power_phase_1["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_power_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_power_phase_2 = next(item for item in data if item["Position"] == 13)
        # test if we found the right entry for reactive_power_phase_2
        if not (
            reactive_power_phase_2["UnitStr"] == "W"
            and reactive_power_phase_2["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_power_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_power_phase_3 = next(item for item in data if item["Position"] == 14)
        # test if we found the right entry for reactive_power_phase_3
        if not (
            reactive_power_phase_3["UnitStr"] == "W"
            and reactive_power_phase_3["DescriptionStr"] == "Power (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_power_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        reactive_power_all_phases = next(
            item for item in data if item["Position"] == 15
        )
        # test if we found the right entry for reactive_power_all_phases
        if not (
            reactive_power_all_phases["UnitStr"] == "W"
            and reactive_power_all_phases["DescriptionStr"] == "Power"
        ):
            raise ValueError(
                "Did not find the required Fields for reactive_power_all_phases in the JSON response from the "
                "M-Bus Center"
            )

        apparent_power_all_phases = next(
            item for item in data if item["Position"] == 16
        )
        # test if we found the right entry for apparent_power_all_phases
        if not (
            apparent_power_all_phases["UnitStr"] == "W"
            and apparent_power_all_phases["DescriptionStr"] == "Power"
        ):
            raise ValueError(
                "Did not find the required Fields for apparent_power_all_phases in the JSON response from the "
                "M-Bus Center"
            )

        voltage_phase_1 = next(item for item in data if item["Position"] == 17)
        # test if we found the right entry voltage_phase_1
        if not (
            voltage_phase_1["UnitStr"] == "V"
            and voltage_phase_1["DescriptionStr"] == "Volts (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for voltage_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        voltage_phase_2 = next(item for item in data if item["Position"] == 18)
        # test if we found the right entry voltage_phase_2
        if not (
            voltage_phase_2["UnitStr"] == "V"
            and voltage_phase_2["DescriptionStr"] == "Volts (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for voltage_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        voltage_phase_3 = next(item for item in data if item["Position"] == 19)
        # test if we found the right entry voltage_phase_3
        if not (
            voltage_phase_3["UnitStr"] == "V"
            and voltage_phase_3["DescriptionStr"] == "Volts (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for voltage_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        current_phase_1 = next(item for item in data if item["Position"] == 20)
        # test if we found the right entry current_phase_1
        if not (
            current_phase_1["UnitStr"] == "A"
            and current_phase_1["DescriptionStr"] == "Ampere (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for current_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        current_phase_2 = next(item for item in data if item["Position"] == 21)
        # test if we found the right entry current_phase_2
        if not (
            current_phase_2["UnitStr"] == "A"
            and current_phase_2["DescriptionStr"] == "Ampere (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for current_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        current_phase_3 = next(item for item in data if item["Position"] == 22)
        # test if we found the right entry current_phase_3
        if not (
            current_phase_3["UnitStr"] == "A"
            and current_phase_3["DescriptionStr"] == "Ampere (vendor specific)"
        ):
            raise ValueError(
                "Did not find the required Fields for current_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        current_all_phases = next(item for item in data if item["Position"] == 23)
        # test if we found the right entry current_all_phases
        if not (
            current_all_phases["UnitStr"] == "A"
            and current_all_phases["DescriptionStr"] == "Ampere"
        ):
            raise ValueError(
                "Did not find the required Fields for current_all_phases in the JSON response from the "
                "M-Bus Center"
            )

        form_factor_phase_1 = next(item for item in data if item["Position"] == 24)
        # test if we found the right entry for form_factor_phase_1
        if not (
            form_factor_phase_1["UnitStr"] == "None"
            and form_factor_phase_1["DescriptionStr"] == "Special supplier information"
        ):
            raise ValueError(
                "Did not find the required Fields for form_factor_phase_1 in the JSON response from the "
                "M-Bus Center"
            )

        form_factor_phase_2 = next(item for item in data if item["Position"] == 25)
        # test if we found the right entry for form_factor_phase_2
        if not (
            form_factor_phase_2["UnitStr"] == "None"
            and form_factor_phase_2["DescriptionStr"] == "Special supplier information"
        ):
            raise ValueError(
                "Did not find the required Fields for form_factor_phase_2 in the JSON response from the "
                "M-Bus Center"
            )

        form_factor_phase_3 = next(item for item in data if item["Position"] == 26)
        # test if we found the right entry for form_factor_phase_3
        if not (
            form_factor_phase_3["UnitStr"] == "None"
            and form_factor_phase_3["DescriptionStr"] == "Special supplier information"
        ):
            raise ValueError(
                "Did not find the required Fields for form_factor_phase_3 in the JSON response from the "
                "M-Bus Center"
            )

        frequency = next(item for item in data if item["Position"] == 27)
        # test if we found the right entry frequency
        if not (
            (frequency["UnitStr"] == "None" or frequency["UnitStr"] == "Hz")
            and frequency["DescriptionStr"] == "Special supplier information"
        ):
            raise ValueError(
                "Did not find the required Fields for frequency in the JSON response from the "
                "M-Bus Center"
            )

        power_failures = next(item for item in data if item["Position"] == 28)
        # test if we found the right entry power_failures
        if not (
            power_failures["UnitStr"] == "None"
            and power_failures["DescriptionStr"] == "Reset counter"
        ):
            raise ValueError(
                "Did not find the required Fields for resets in the JSON response from the "
                "M-Bus Center"
            )

        current_transformer_factor = next(
            item for item in data if item["Position"] == 29
        )
        # test if we found the right entry current_transformer_factor
        if not (
            current_transformer_factor["UnitStr"] == "None"
            and current_transformer_factor["DescriptionStr"]
            == "Special supplier information"
        ):
            raise ValueError(
                "Did not find the required Fields for current_transformer_factor in the JSON response from the "
                "M-Bus Center"
            )

        error_flags = next(item for item in data if item["Position"] == 30)
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
            ACTIVE_ENERGY_IMPORT_TARIFF_1: int(
                active_energy_import_tariff_1["LoggerLastValue"]
            )
            / 1000,
            ACTIVE_ENERGY_IMPORT_TARIFF_2: int(
                active_energy_import_tariff_2["LoggerLastValue"]
            )
            / 1000,
            ACTIVE_ENERGY_EXPORT_TARIFF_1: int(
                active_energy_export_tariff_1["LoggerLastValue"]
            )
            / -1000,
            ACTIVE_ENERGY_EXPORT_TARIFF_2: int(
                active_energy_export_tariff_2["LoggerLastValue"]
            )
            / -1000,
            REACTIVE_ENERGY_INDUCTIVE_TARIFF_1: int(
                reactive_energy_inductive_tariff_1["LoggerLastValue"]
            )
            / 1000,
            REACTIVE_ENERGY_INDUCTIVE_TARIFF_2: int(
                reactive_energy_inductive_tariff_2["LoggerLastValue"]
            )
            / 1000,
            REACTIVE_ENERGY_CAPACITIVE_TARIFF_1: int(
                reactive_energy_capacitive_tariff_1["LoggerLastValue"]
            )
            / -1000,
            REACTIVE_ENERGY_CAPACITIVE_TARIFF_2: int(
                reactive_energy_capacitive_tariff_2["LoggerLastValue"]
            )
            / -1000,
            ACTIVE_POWER_PHASE_1: int(active_power_phase_1["LoggerLastValue"]) / 1000,
            ACTIVE_POWER_PHASE_2: int(active_power_phase_2["LoggerLastValue"]) / 1000,
            ACTIVE_POWER_PHASE_3: int(active_power_phase_3["LoggerLastValue"]) / 1000,
            ACTIVE_POWER_ALL_PHASES: int(active_power_all_phases["LoggerLastValue"])
            / 1000,
            REACTIVE_POWER_PHASE_1: int(reactive_power_phase_1["LoggerLastValue"]),
            REACTIVE_POWER_PHASE_2: int(reactive_power_phase_2["LoggerLastValue"]),
            REACTIVE_POWER_PHASE_3: int(reactive_power_phase_3["LoggerLastValue"]),
            REACTIVE_POWER_ALL_PHASES: int(reactive_power_all_phases["LoggerLastValue"])
            / 1000,
            APPARENT_POWER_ALL_PHASES: int(
                apparent_power_all_phases["LoggerLastValue"]
            ),
            VOLTAGE_PHASE_1: int(voltage_phase_1["LoggerLastValue"]),
            VOLTAGE_PHASE_2: int(voltage_phase_2["LoggerLastValue"]),
            VOLTAGE_PHASE_3: int(voltage_phase_3["LoggerLastValue"]),
            CURRENT_PHASE_1: int(current_phase_1["LoggerLastValue"]),
            CURRENT_PHASE_2: int(current_phase_2["LoggerLastValue"]),
            CURRENT_PHASE_3: int(current_phase_3["LoggerLastValue"]),
            CURRENT_ALL_PHASES: int(current_all_phases["LoggerLastValue"]),
            FORM_FACTOR_PHASE_1: int(form_factor_phase_1["LoggerLastValue"]) / 100,
            FORM_FACTOR_PHASE_2: int(form_factor_phase_2["LoggerLastValue"]) / 100,
            FORM_FACTOR_PHASE_3: int(form_factor_phase_3["LoggerLastValue"]) / 100,
            FREQUENCY: int(frequency["LoggerLastValue"]) / 10,
            POWER_FAILURES: int(power_failures["LoggerLastValue"]),
            CURRENT_TRANSFORMER_FACTOR: int(
                current_transformer_factor["LoggerLastValue"]
            ),
            ERROR_FLAGS: int(error_flags["LoggerLastValue"]),
        }
