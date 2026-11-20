import numpy as np

# Create 2D array for Day 1 and Day 2 temperatures
temps = np.array([
    [30, 32, 31],
    [29, 33, 34]
])

print("Temperature Array:\n", temps)
print("Total Temperature Recorded:", np.sum(temps))