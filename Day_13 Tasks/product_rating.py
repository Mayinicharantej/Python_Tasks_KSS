import numpy as np

ratings = np.array([2, 3, 4, 5, 1])

# Min-max normalization scaling values into [0, 1]
normalized = (ratings - np.min(ratings)) / (np.max(ratings) - np.min(ratings))

print(normalized)