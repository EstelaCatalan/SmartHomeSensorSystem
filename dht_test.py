import adafruit_dht
import time
import board 

sensor= adafruit_dht.DHT22(board.D4)


while True:
	try:
		temperature= sensor.temperature
		humidity= sensor.humidity
		if humidity is not None and temperature is not None:
			print(f'Temp={temperature:0.1f}ºC humidity={humidity:0.1f}%')

		else:
			print('No reading, trying again..')
	except RuntimeError as error:
		print(f"puta mierda : {error}")
	time.sleep(2)

