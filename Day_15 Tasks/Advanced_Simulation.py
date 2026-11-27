import math
import random
import numpy as np
import pandas as pd


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 75:
            return "B"
        elif self.score >= 50:
            return "C"
        else:
            return "F"


try:
    names = ["A", "B", "C", "D", "E", "F"]
    raw_scores = [random.randint(35, 100) for _ in names]
    arr = np.array(raw_scores)

    # Instantiate Student objects and build DataFrame rows
    students = [Student(n, s) for n, s in zip(names, arr)]
    rows = []
    for st in students:
        rows.append({"Name": st.name, "Score": st.score, "Grade": st.grade})

    df = pd.DataFrame(rows)

    # Calculate mean and standard deviation using math module
    mean_score = math.fsum(arr) / len(arr)
    variance = math.fsum((x - mean_score) ** 2 for x in arr) / len(arr)
    std_dev = math.sqrt(variance)

    # Write formatted report to file
    with open("exam_report.txt", "w") as f:
        f.write(df.to_string(index=False))
        f.write(f"\n\nMean Score: {mean_score:.2f}\n")
        f.write(f"Std Dev: {std_dev:.2f}\n")

    print(df)
    print(f"Mean: {mean_score:.2f}, Std Dev: {std_dev:.2f}")
except Exception as e:
    print("Simulation error:", e)