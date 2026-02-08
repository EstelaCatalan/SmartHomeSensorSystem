from sensor import read_sensor
from storage import save_reading
import time

while True:
    temp, hum = read_sensor()
    if temp and hum:
        print(f"Temp: {temp}°C | Humidity: {hum}%")
        save_reading(temp, hum)
    time.sleep(60)
