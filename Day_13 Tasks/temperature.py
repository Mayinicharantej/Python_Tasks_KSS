import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

# Return indices where temperature is greater than 30
alert_indices = np.where(temps > 30)[0]

print(alert_indices)