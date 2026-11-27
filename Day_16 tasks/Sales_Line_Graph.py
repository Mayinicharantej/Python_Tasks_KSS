import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Convert into DataFrame and plot line graph
df = pd.DataFrame({"Month": months, "Sales": sales})
plt.plot(df["Month"], df["Sales"], marker="o")

# Label axes and display plot
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()