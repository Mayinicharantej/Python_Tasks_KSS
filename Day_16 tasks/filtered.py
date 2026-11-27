import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({"Name": names, "Marks": marks})

# Filter DataFrame to include only students with marks > 50
filtered_df = df[df["Marks"] > 50]

plt.bar(filtered_df["Name"], filtered_df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Students with Marks > 50")
plt.show()