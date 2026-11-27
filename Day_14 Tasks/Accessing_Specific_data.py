import pandas as pd

S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])

# Use .loc with a list of labels to return a Series subset
subset = S.loc[["B", "D"]]

print(subset)