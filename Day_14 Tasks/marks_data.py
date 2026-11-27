import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

# Create Total column
df["Total"] = df["Math"] + df["Science"]

# Locate the row with the maximum Total score
top_student = df.loc[df["Total"].idxmax()]

print(df)
print("\nHighest total marks:")
print(top_student)