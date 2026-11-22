import copy

# Multi-level nested list of classroom data
classes = [["Math", [30, 35]], ["Science", [25, 28]]]

# Create an independent deep copy
classes_backup = copy.deepcopy(classes)

# Modify student count inside the original nested structure
classes[0][1][0] = 45

print("Original classes:", classes)
print("Deep copy classes_backup (unchanged):", classes_backup)