import matplotlib.pyplot as plt

# Data
r_values = [1, 2, 3, 5, 10, 15, 19]
carrying_capacities = [3.64, 74.44,103.35, 126.71, 137.21, 144.92, 146.05]
# Plot
plt.figure(figsize=(8, 6))
plt.plot(r_values, carrying_capacities, '-o')  # Line with markers
plt.xlabel('Moore radius ρ')
plt.ylabel('Carrying Capacity (K)')
#plt.title('Carrying Capacity vs Moore Radius r (Alpha = 0)')

plt.xticks(r_values)
plt.grid(True)
plt.show()
