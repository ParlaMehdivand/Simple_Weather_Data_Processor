import numpy as np

# Creates a NumPy array of daily temperatures (in Celsius)
temperatures = np.array([22.5, 23.0, 19.8, 21.4, 24.1, 20.0, 22.0])

# Converts to Fahrenheit (°F = °C × 9/5 + 32)
fahrenheit = temperatures * 9.5 + 32
print('Temperatures in Fahrenheit:', fahrenheit)

# Calculate average, min, and max temperature
average_temp = np.mean(temperatures)
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)

print(f"Average Celsius: {average_temp:.2f}")
print(f"Min Celsius: {min_temp:.2f}")
print(f"Max Celsius: {max_temp:.2f}")
