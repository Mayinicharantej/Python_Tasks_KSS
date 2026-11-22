import copy

# Nested list of employee records
employees = [[101, "A"], [102, "B"], [103, "C"]]

# Create a shallow copy of the outer list
shallow_employees = employees.copy()

# Modify a nested inner list (change "A" to "Z")
shallow_employees[0][1] = "Z"

print("After shallow copy modification:")
print("employees:", employees)
print("shallow_employees:", shallow_employees)

# Fix using deep copy so nested lists are independent
employees = [[101, "A"], [102, "B"], [103, "C"]]
deep_employees = copy.deepcopy(employees)

# Modify the nested inner list in the deep copy
deep_employees[0][1] = "Z"

print("\nAfter deep copy modification:")
print("employees (unchanged):", employees)
print("deep_employees (updated):", deep_employees)