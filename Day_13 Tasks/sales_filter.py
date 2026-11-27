import numpy as np

# Define monthly sales array
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])

# Calculate average sales and filter values strictly greater than the average
filtered_sales = sales[sales > np.mean(sales)]

print(filtered_sales)