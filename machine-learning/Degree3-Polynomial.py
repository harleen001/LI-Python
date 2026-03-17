import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the dataset (Temperature vs Ice Cream Sales)
temperature = np.array([10, 15, 20, 25, 30, 35, 40])
sales = np.array([5, 20, 50, 80, 100, 90, 60])

# Step 2: Create the polynomial feature matrix (Degree 3)
A = np.vstack([np.ones_like(temperature), temperature, temperature**2, temperature**3]).T

# Step 3: Solve for coefficients b0, b1, b2, b3
b0, b1, b2, b3 = np.linalg.lstsq(A, sales, rcond=None)[0]

# Print the polynomial equation
print(f"Polynomial Equation: Sales = {b0:.2f} + {b1:.2f}*Temp + {b2:.2f}*Temp^2 + {b3:.2f}*Temp^3")

# Step 4: Generate smooth predictions for plotting
temp_smooth = np.linspace(10, 40, 100)
sales_smooth = b0 + b1 * temp_smooth + b2 * temp_smooth**2 + b3 * temp_smooth**3

# Step 5: Plot the actual data points and polynomial regression curve
plt.scatter(temperature, sales, color="blue", label="Actual Sales")
plt.plot(temp_smooth, sales_smooth, color="red", label="Polynomial Fit (Degree 3)")

# Step 6: Labels, title, and legend
plt.xlabel("Temperature (°C)")
plt.ylabel("Ice Cream Sales")
plt.title("Polynomial Regression (Degree 3): Temperature vs Ice Cream Sales")
plt.legend()
plt.grid(True)

# Step 7: Show the plot
plt.show()