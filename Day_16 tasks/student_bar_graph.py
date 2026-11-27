import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df = pd.DataFrame({"Name": names, "Marks": marks})

# Plot vertical bar chart with student names on X-axis
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()