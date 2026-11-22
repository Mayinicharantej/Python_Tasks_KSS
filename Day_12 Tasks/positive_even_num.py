import numpy as np

# Convert dataset into a NumPy array
arr = np.array([-5, 10, 15, 2, 20, 25, 30])

# Filter values that are both positive (> 0) and even (% 2 == 0)
positive_even = arr[(arr > 0) & (arr % 2 == 0)]

print("Positive even numbers:", positive_even)