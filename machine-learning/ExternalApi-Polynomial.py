import numpy as np
import matplotlib.pyplot as plt
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 31.32,
    "longitude": 75.57,
    "hourly": "temperature_2m",
    "timezone": "auto",
    "forecast_days": 1
}

response = requests.get(url, params=params)
data = response.json()

raw_temps = np.array(data['hourly']['temperature_2m'])
hours = np.arange(len(raw_temps))

A = np.vstack([np.ones_like(hours), hours, hours**2, hours**3]).T

b0, b1, b2, b3 = np.linalg.lstsq(A, raw_temps, rcond=None)[0]

hours_smooth = np.linspace(0, 23, 100)
temp_smooth = b0 + b1 * hours_smooth + b2 * hours_smooth**2 + b3 * hours_smooth**3

plt.figure(figsize=(10, 6))
plt.scatter(hours, raw_temps, color="darkorange", label="API Data")
plt.plot(hours_smooth, temp_smooth, color="teal", linewidth=2, label="Degree 3 Fit")

plt.xlabel("Hour of Day (0-23)")
plt.ylabel("Temperature (°C)")
plt.title("Jalandhar Temperature Trend (Live API)")
plt.xticks(np.arange(0, 24, 2))
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

print(f"Equation: y = {b0:.2f} + {b1:.2f}x + {b2:.2f}x^2 + {b3:.2f}x^3")