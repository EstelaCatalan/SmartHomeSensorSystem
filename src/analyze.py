from pathlib import Path
import csv

# Ruta absoluta del archivo analyze.py
BASE_DIR = Path(__file__).parent

# readings.csv dentro de data/
FILE_PATH = BASE_DIR / "data" / "readings.csv"

if not FILE_PATH.exists():
    print(f"❌ readings.csv file does not exist yet at {FILE_PATH}")
    exit()

temperatures = []
humidities = []

with open(FILE_PATH, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            temperatures.append(float(row["temperature"]))
            humidities.append(float(row["humidity"]))
        except (ValueError, KeyError):
            continue

if len(temperatures) < 2:
    print("⚠️ Not enough data to analyze.")
else:
    avg_temp = sum(temperatures) / len(temperatures)
    avg_hum = sum(humidities) / len(humidities)
    print(f"Number of readings: {len(temperatures)}")
    print(f"Average temperature: {avg_temp:.1f}°C")
    print(f"Average humidity: {avg_hum:.1f}%")
