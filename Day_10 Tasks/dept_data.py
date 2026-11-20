import numpy as np

# Employee counts across branches
branch_a = np.array([
    [10, 20],
    [30, 40]
])
branch_b = np.array([
    [5, 15],
    [25, 35]
])

# Combine matrices and compute total employees
combined_matrix = branch_a + branch_b
total_employees = np.sum(combined_matrix)

print("Combined Matrix:\n", combined_matrix)
print("Total Employees:", total_employees)