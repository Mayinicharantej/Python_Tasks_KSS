import numpy as np

# 2D array: rows represent 5 students, columns represent 3 subjects
marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [50, 65, 70],
    [90, 95, 85],
    [40, 55, 60]
])

# Sum marks across columns (axis=1) to get each student's total
totals = np.sum(marks, axis=1)

# Find indices of students whose total exceeds the class average
above_avg_indices = np.where(totals > np.mean(totals))[0]

print("Totals:", totals)
print("Above average student indices:", above_avg_indices)
print("Above average totals:", totals[above_avg_indices])