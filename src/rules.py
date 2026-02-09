
# src/rules.py

from constants import (
    TEMP_COLD,
    TEMP_HOT,
    TEMP_HOT_EXTREME,
    HUMIDITY_HIGH,
    HUMIDITY_VERY_HIGH,
    TEMP_MIN_VALID,
    TEMP_MAX_VALID,
    HUMIDITY_MIN_VALID,
    HUMIDITY_MAX_VALID
)

def is_valid_reading(temperature, humidity):
    if temperature is None or humidity is None:
        return False

    if not (TEMP_MIN_VALID <= temperature <= TEMP_MAX_VALID):
        return False

    if not (HUMIDITY_MIN_VALID <= humidity <= HUMIDITY_MAX_VALID):
        return False

    return True


def check_temperature_rules(temperature):
    if temperature < TEMP_COLD:
        return "ALERT_COLD"

    if temperature > TEMP_HOT_EXTREME:
        return "ALERT_HOT_EXTREME"

    if temperature > TEMP_HOT:
        return "ALERT_HOT"

    return None


def check_humidity_rules(humidity):
    if humidity > HUMIDITY_VERY_HIGH:
        return "ALERT_HUMIDITY_VERY_HIGH"

    if humidity > HUMIDITY_HIGH:
        return "ALERT_HUMIDITY_HIGH"

    return None


