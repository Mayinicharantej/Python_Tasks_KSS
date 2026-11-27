import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df = pd.DataFrame({"Product": products, "Sales": sales})

# Create 1 row with 3 side-by-side subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Line graph (trend)
axes[0].plot(df["Product"], df["Sales"], marker="o")
axes[0].set_title("Sales Trend")
axes[0].set_xlabel("Product")
axes[0].set_ylabel("Sales")

# Bar chart (comparison)
axes[1].bar(df["Product"], df["Sales"])
axes[1].set_title("Sales Comparison")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Sales")

# Pie chart (distribution)
axes[2].pie(df["Sales"], labels=df["Product"], autopct="%1.1f%%")
axes[2].set_title("Sales Distribution")

plt.tight_layout()
plt.show()