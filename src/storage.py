import csv
from datetime import datetime

def save_reading(temp, hum):
    with open("data/readings.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), temp, hum])
