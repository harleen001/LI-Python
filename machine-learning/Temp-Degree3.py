import numpy as np
import matplotlib.pyplot as plt

hours = np.array([6, 9, 12, 15, 18, 21, 24])  # x and y are variables, where temperature depends on hour
temp = np.array([15, 22, 28, 32, 27, 20, 14])
A = np.vstack([np.ones_like(hours), hours, hours**2, hours**3]).T    #making matrix and transform


b0, b1, b2, b3 = np.linalg.lstsq(A, temp, rcond=None)[0]    # ax=b formula

hours_smooth = np.linspace(6, 24, 100)   #plotting normal points
temp_smooth = b0 + b1 * hours_smooth + b2 * hours_smooth**2 + b3 * hours_smooth**3     #temperature values for line

plt.scatter(hours, temp, color="darkorange", label="Observed Temp")
plt.plot(hours_smooth, temp_smooth, color="teal", label="Degree 3 Trendline")
plt.xlabel("Hour of Day (24h Format)")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Cycle: Polynomial Regression")
plt.xticks(np.arange(6, 25, 3))
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()