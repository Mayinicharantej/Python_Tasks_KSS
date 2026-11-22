import numpy as np

# Create NumPy array from dataset
arr = np.array([5, 12, 18, 7, 25, 30])

# Replace all elements greater than 15 with 0
arr[arr > 15] = 0

print("Updated array:", arr)