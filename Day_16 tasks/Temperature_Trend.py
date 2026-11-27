import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

temps = np.array([28, 30, 32, 31, 29])

# Convert array into a Pandas Series
s = pd.Series(temps, index=["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])

plt.plot(s.index, s.values, marker="o")
plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()