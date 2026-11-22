# Original list of student marks
marks = [50, 60, 70, 80]

# Assignment creates another reference pointing to the same list object in memory
backup = marks

# Modify the first element in marks
marks[0] = 95

# Print both lists to observe the change
print("marks:", marks)
print("backup:", backup)