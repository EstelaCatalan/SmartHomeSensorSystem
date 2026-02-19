import csv
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
CSV_FILE = DATA_DIR / "readings.csv"

# Crear CSV con cabeceras si no existe
if not CSV_FILE.exists():
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidity"])

def save_reading(temp, hum):
    if temp is None or hum is None:
        return
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), temp, hum])
    print("💾 Reading saved")

