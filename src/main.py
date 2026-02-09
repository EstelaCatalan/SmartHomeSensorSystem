from sensor import read_sensor
from storage import save_reading
import time
from rules import (
    is_valid_reading,
    check_temperature_rules,
    check_humidity_rules
)

while True:
#-----------Alerts---------------------------------------------------------------------
    
    temp, hum = read_sensor()
    if not is_valid_reading(temp, hum):
        print("Lectura inválida, ignorando")
        time.sleep(2)
        continue
    temp_alert = check_temperature_rules(temp)
    hum_alert = check_humidity_rules(hum)
    if temp_alert:
        print(f"⚠️ Alerta temperatura: {temp_alert}")

    if hum_alert:
        print(f"⚠️ Alerta humedad: {hum_alert}")

    time.sleep(2)
#------------Save Temperature------------------------------------------------------------
    if temp and hum:
        print(f"Temp: {temp}°C | Humidity: {hum}%")
        save_reading(temp, hum)
    time.sleep(2)
