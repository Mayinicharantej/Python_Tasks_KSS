import pandas as pd

S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])

# Add matching indices across both Series
combined = S1 + S2

# Sum all values across all fruits
total_sales = combined.sum()

print(combined)
print("Total sales:", total_sales)