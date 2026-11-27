import numpy as np

# Generate 10 random integers between 1 (inclusive) and 100 (exclusive)
nums = np.random.randint(1, 100, 10)

# Filter multiples of 5 and sort in ascending order
div_by_5 = np.sort(nums[nums % 5 == 0])

print("Generated:", nums)
print("Divisible by 5 (sorted):", div_by_5)