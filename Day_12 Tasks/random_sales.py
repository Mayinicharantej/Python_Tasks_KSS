import numpy as np

# Generate 10 random integer sales values in the range 100 to 500 (inclusive)
sales = np.random.randint(100, 501, size=10)

# Print the simulated sales array and its average
print("10-day sales:", sales)
print("Average sales:", np.mean(sales))