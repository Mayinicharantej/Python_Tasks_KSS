import pandas as pd

cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

# Reindex/create Series with requested index; Bangalore becomes NaN
s = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

# Extract index labels where value is missing (NaN)
missing_cities = s[s.isna()].index.tolist()

print(s)
print("Missing cities:", missing_cities)