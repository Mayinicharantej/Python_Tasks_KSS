import matplotlib.pyplot as plt
import numpy as np

expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# autopct formats percentage slices automatically
plt.pie(expenses, labels=labels, autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.show()