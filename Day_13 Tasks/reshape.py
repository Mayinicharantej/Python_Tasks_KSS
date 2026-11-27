import numpy as np

# Generate numbers 1 to 12 and reshape into 3 rows by 4 columns
data = np.arange(1, 13)
matrix = data.reshape(3, 4)

# Compute mean along each row (axis=1)
row_averages = np.mean(matrix, axis=1)

print(matrix)
print("Row averages:", row_averages)