import numpy as np

# Create a 1D array of 12 monthly sales values
monthly_sales = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])

# Reshape into 4 rows (months) by 3 columns (products)
reshaped_sales = monthly_sales.reshape(4, 3)

print(reshaped_sales)