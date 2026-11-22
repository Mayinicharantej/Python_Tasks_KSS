import numpy as np

# Create a NumPy array of student roll numbers
roll_numbers = np.array([101, 102, 103, 104, 105, 106])  #[cite: 1]

# Slice from index 2 up to index 4 (index 4 is excluded, giving indices 2 and 3)
middle_students = roll_numbers[2:4]  #[cite: 1, 2]

print("Middle students:", middle_students)  #[cite: 1, 2]