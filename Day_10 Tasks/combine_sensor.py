import numpy as np

# Store sensor readings in separate arrays
sensor1 = np.array([10, 20, 30])
sensor2 = np.array([40, 50, 60])

# Concatenate along axis 0 (1D)
combined = np.concatenate((sensor1, sensor2))
print("Combined Readings:", combined)