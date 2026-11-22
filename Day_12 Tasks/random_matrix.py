import numpy as np

# Generate a 3x3 matrix of random integers from 0 to 50 (inclusive)
matrix = np.random.randint(0, 51, size=(3, 3))

# Filter elements strictly greater than 25
filtered_values = matrix[matrix > 25]

print("3x3 Matrix:\n", matrix)
print("Values > 25:", filtered_values)