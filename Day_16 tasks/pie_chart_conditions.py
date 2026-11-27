import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

scores = np.array([40, 60, 80, 30, 90])

# Categorize scores into Pass (>50) and Fail (<=50)
status = np.where(scores > 50, "Pass", "Fail")
counts = pd.Series(status).value_counts()

plt.pie(counts.values, labels=counts.index, autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()