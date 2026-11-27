import matplotlib.pyplot as plt
import pandas as pd

products = ["Pen", "Book", "Pencil"]
sales = [50, 80, 40]

df = pd.DataFrame({"Product": products, "Sales": sales})

plt.bar(df["Product"], df["Sales"])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()