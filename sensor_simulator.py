import requests
import random
import time
from datetime import datetime

API_URL = "http://localhost:5000/api/farm"

def send_sensor_data(zone_id, sensor_type, value, unit):
    data = {
        "zoneId": zone_id,
        "type": sensor_type,
        "value": value,
        "unit": unit
    }
    
    try:
        response = requests.post(f"{API_URL}/reading", json=data)
        if response.status_code == 200:
            print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] Zone {zone_id} - {sensor_type}: {value}{unit}")
        else:
            print(f"❌ Failed")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Starting Sensor Simulator...")
print("Press Ctrl+C to stop\n")

while True:
    try:
        # Zone 1 (Sectie A) - High humidity
        temp_a = random.uniform(17.5, 19.5)
        humidity_a = random.uniform(75, 92)
        
        # Zone 2 (Sectie B) - Normal
        temp_b = random.uniform(19.5, 21.5)
        humidity_b = random.uniform(55, 70)
        
        send_sensor_data(1, "temperature", round(temp_a, 1), "°C")
        time.sleep(1)
        send_sensor_data(1, "humidity", round(humidity_a, 1), "%")
        time.sleep(1)
        send_sensor_data(2, "temperature", round(temp_b, 1), "°C")
        time.sleep(1)
        send_sensor_data(2, "humidity", round(humidity_b, 1), "%")
        
        print(f"📊 Zone A: {temp_a:.1f}°C / {humidity_a:.0f}%")
        print(f"📊 Zone B: {temp_b:.1f}°C / {humidity_b:.0f}%\n")
        
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("\n👋 Stopping simulator...")
        break
