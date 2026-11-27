import random

# Generate 10 random integers in [1, 50]
numbers = [random.randint(1, 50) for _ in range(10)]

even_count = 0
odd_count = 0

# Count even and odd numbers using a loop and conditional check
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Convert list to a set to remove duplicate values
unique_numbers = set(numbers)

print("Numbers:", numbers)
print("Even count:", even_count)
print("Odd count:", odd_count)
print("Unique numbers:", unique_numbers)