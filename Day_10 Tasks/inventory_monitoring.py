import numpy as np

# Warehouse inventory matrix
inventory = np.array([
    [10, 15],
    [20, 25]
])

# Increase every item count by 2
updated_inventory = inventory + 2
print("Updated Inventory:\n", updated_inventory)