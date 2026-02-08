import adafruit_dht
import board

dht = adafruit_dht.DHT22(board.D4)

def read_sensor():
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        return temperature, humidity
    except Exception as e:
        return None, None
