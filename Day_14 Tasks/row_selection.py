import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [5, 15, 25]
}, index=["x", "y", "z"])

# Select row "y" by label
row_y = df.loc["y"]

# Drop row "x" and return a new DataFrame
df_updated = df.drop("x")

print("Row y:")
print(row_y)
print("\nUpdated DataFrame:")
print(df_updated)