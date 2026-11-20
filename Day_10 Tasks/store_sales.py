import numpy as np

# Daily sales arrays for both stores
store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])

# Element-wise daily difference (Store A - Store B)
daily_diff = store_a - store_b
print("Daily Sales Difference (Store A - Store B):", daily_diff)