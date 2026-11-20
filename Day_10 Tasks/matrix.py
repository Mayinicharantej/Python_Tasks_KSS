import numpy as np

# Create pixel intensity matrix and compute its transpose
matrix = np.array([
    [1, 2],
    [3, 4]
])
transposed = matrix.T

print("Original Matrix:\n", matrix)
print("Transposed Matrix:\n", transposed)