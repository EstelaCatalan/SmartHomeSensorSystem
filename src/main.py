from sensor import read_sensor
from storage import save_reading
import time
import logger
import logging
from rules import (
    is_valid_reading,
    check_temperature_rules,
    check_humidity_rules
)

while True:

    temp, hum = read_sensor()
    print("DEBUG:", temp, hum)

    if not is_valid_reading(temp, hum):
        logging.warning("Lectura inválida, ignorando")
        time.sleep(2)
        print("DEBUG: lectura inválida")

        continue

    logging.info(
        "Lectura válida: temp=%.1f°C hum=%.1f%%",
        temp,
        hum
    )

    temp_alert = check_temperature_rules(temp)
    hum_alert = check_humidity_rules(hum)

    if temp_alert:
        logging.warning("Alerta temperatura: %s", temp_alert)

    if hum_alert:
        logging.warning("Alerta humedad: %s", hum_alert)

    save_reading(temp, hum)

    time.sleep(2)

