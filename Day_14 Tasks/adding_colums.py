import pandas as pd

df = pd.DataFrame({
    "Price": [100, 200, 300]
})

# Calculate 10% discount and final price
df["Discount"] = df["Price"] * 0.10
df["Final Price"] = df["Price"] - df["Discount"]

print(df)