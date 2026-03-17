import numpy as np
import matplotlib.pyplot as plt

speed = np.array([10, 20, 30, 40, 50])
braking_distance = np.array([5, 20, 45, 80, 125])

A = np.vstack([np.ones_like(speed), speed, speed**2]).T
b0, b1, b2 = np.linalg.lstsq(A, braking_distance, rcond=None)[0]
speed_smooth = np.linspace(5, 55, 100)
braking_smooth = b0 + b1 * speed_smooth + b2 * speed_smooth**2


plt.scatter(speed, braking_distance, color="blue", label="Data Points")
plt.plot(speed_smooth, braking_smooth, color="red", label="Polynomial Fit (Degree 2)")
plt.xlabel("Speed (km/h)")
plt.ylabel("Braking Distance (m)")
plt.title("Polynomial Regression: Speed vs Braking Distance")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Print the equation
print(f"Polynomial Equation: Braking Distance = {b0:.2f} + {b1:.2f}*Speed + {b2:.2f}*Speed^2")