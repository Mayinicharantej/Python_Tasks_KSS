import numpy as np

# Convert the list of customer transactions into a NumPy array
transactions = np.array([1200, 500, 800, 1500])  #[cite: 1]

# Print the Python object type
print("Type:", type(transactions))  #[cite: 1]

# Verify that the object is an instance of numpy.ndarray
print("Is NumPy ndarray:", isinstance(transactions, np.ndarray))  #[cite: 1]