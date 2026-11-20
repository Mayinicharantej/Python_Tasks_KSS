import numpy as np

# 1. Convert list to NumPy array
arr = np.array([12, 7, 25, 3, 18, 10])

# 2. Sort the array
sorted_arr = np.sort(arr)

# 3. Split into two equal parts
part1, part2 = np.array_split(sorted_arr, 2)

# 4. Calculate sum of each part
sum1 = np.sum(part1)
sum2 = np.sum(part2)

print("Sorted Array:", sorted_arr)
print("Part 1:", part1, "| Sum:", sum1)
print("Part 2:", part2, "| Sum:", sum2)