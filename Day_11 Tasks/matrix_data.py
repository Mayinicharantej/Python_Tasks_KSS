import numpy as np

# Convert 2D list of student marks (rows = students, columns = subjects) to a NumPy array
marks = np.array([[78, 85],  #[cite: 2]
                  [90, 88],  #[cite: 2]
                  [67, 72]]) #[cite: 2]

# Row index 1 is the second student; column index 1 is the second subject
print("Second student's second subject mark:", marks[1, 1])  #[cite: 2]