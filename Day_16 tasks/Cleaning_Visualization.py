import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Convert to Series and impute missing values with the mean
s = pd.Series(data)
cleaned_s = s.fillna(s.mean())

# Filter values strictly greater than the cleaned average
avg_val = cleaned_s.mean()
above_avg = cleaned_s[cleaned_s > avg_val]

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Line graph of cleaned data
axes[0].plot(cleaned_s.index, cleaned_s.values, marker="o")
axes[0].set_title("Cleaned Data Trend")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Value")

# Bar chart of values above average
axes[1].bar(above_avg.index.astype(str), above_avg.values)
axes[1].set_title("Values > Average")
axes[1].set_xlabel("Index")
axes[1].set_ylabel("Value")

plt.tight_layout()
plt.show()