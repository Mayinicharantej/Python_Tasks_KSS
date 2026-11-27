import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

df = pd.DataFrame(data)

# Plot both store series on the same axes
plt.plot(df["Month"], df["Store_A"], marker="o", label="Store A")
plt.plot(df["Month"], df["Store_B"], marker="s", label="Store B")

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Store A vs Store B Sales")
plt.legend()
plt.show()