import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 2, 3])

# Get sorted unique values and their respective counts
unique_vals, counts = np.unique(data, return_counts=True)

for val, count in zip(unique_vals, counts):
    print(f"{val}: {count}")