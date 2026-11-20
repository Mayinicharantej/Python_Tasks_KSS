import numpy as np

# Store dataset and split into 3 equal parts
data = np.array([5, 10, 15, 20, 25, 30])
parts = np.array_split(data, 3)

for idx, part in enumerate(parts, start=1):
    print(f"Processor {idx} Data:", part)