import matplotlib.pyplot as plt

# Data
r_values = [1, 2, 3, 5, 10, 15, 19]
carrying_capacities = [33.36, 83.01, 106.58, 127.54, 137.63, 144.92, 146.05]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(r_values, carrying_capacities, '-o')  # Line with markers
plt.xlabel('Moore Radius r')
plt.ylabel('Carrying Capacity (K)')
plt.title('Carrying Capacity vs Moore Radius r (Alpha = 0)')
plt.grid(True)
plt.show()
