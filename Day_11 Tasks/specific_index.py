import numpy as np

# Store product defect codes in a NumPy array
defect_codes = np.array([2, 4, 1, 4, 3, 4, 5])

# Find indexes where element equals 4; np.where returns a tuple, so take [0]
indexes = np.where(defect_codes == 4)[0]

print("Indexes where value == 4:", indexes)