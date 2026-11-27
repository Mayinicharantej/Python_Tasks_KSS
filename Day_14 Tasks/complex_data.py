import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

# Assign Pass/Fail based on threshold of 50
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Filter passing students and compute their average score
passed_df = df[df["Status"] == "Pass"]
avg_passed_marks = passed_df["Marks"].mean()

print(df)
print("\nPassed students:")
print(passed_df)
print("\nAverage marks of passed students:", avg_passed_marks)