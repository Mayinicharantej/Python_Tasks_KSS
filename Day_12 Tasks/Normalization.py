import numpy as np

# Generate 8 random float values between 0 and 1
random_floats = np.random.rand(8)

# 1. Normalize by multiplying with 100
normalized = random_floats * 100

# 2. Filter values greater than 50
filtered = normalized[normalized > 50]

# 3. Sort the filtered values
sorted_filtered = np.sort(filtered)

print("Normalized values:", normalized)
print("Filtered (> 50) and sorted:", sorted_filtered)