import math
import numpy as np
import pandas as pd

# Generate random marks and store in a DataFrame
marks_arr = np.random.randint(30, 100, size=6)
df = pd.DataFrame({
    "Student": ["S1", "S2", "S3", "S4", "S5", "S6"],
    "Marks": marks_arr
})

# Filter passing students (marks >= 50)
passed_df = df[df["Marks"] >= 50]

# Compute mean using math.fsum
mean_marks = math.fsum(df["Marks"]) / len(df["Marks"])

for _, row in passed_df.iterrows():
    print(f"Passed: {row['Student']} with {row['Marks']}")

print("Mean marks:", mean_marks)