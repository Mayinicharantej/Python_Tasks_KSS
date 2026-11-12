import random
import math

numbers = []
for i in range(20):
    numbers.append(random.randint(1, 200))

max_val = max(numbers)
min_val = min(numbers)

print("List:", numbers)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
print("Square root of maximum:", math.sqrt(max_val))
print("Logarithm of minimum:", math.log(min_val))