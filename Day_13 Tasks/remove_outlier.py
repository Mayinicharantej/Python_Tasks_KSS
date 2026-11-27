import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)
std = np.std(values)

# Keep only values within 2 standard deviations of the mean
cleaned = values[np.abs(values - mean) <= 2 * std]

print("Mean:", mean)
print("Std:", std)
print("Cleaned values:", cleaned)