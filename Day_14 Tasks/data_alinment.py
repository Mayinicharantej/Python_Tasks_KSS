import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

# Standard addition produces NaN where index labels do not overlap ("a" and "d")
aligned_sum = S1 + S2

# Use .add() with fill_value=0 so missing counterparts default to 0
final_result = S1.add(S2, fill_value=0)

print("With NaN:")
print(aligned_sum)
print("\nAfter replacing NaN with 0:")
print(final_result)