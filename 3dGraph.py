# X-axis: Alpha
# Y-axis: Rho
# Z-axis: K (Carrying Capacity)

import matplotlib.pyplot as plt
import numpy as np

alpha_values = [0, 0.25, 0.5, 0.75, 1]
r_values = [1, 2, 3, 5, 10, 15, 19]

ALPHA, R = np.meshgrid(alpha_values, r_values)

CARRYING_CAPACITY = np.array([
    # alpha=0,  0.25,     0.5,      0.75,        1
    [3.64,     35.37,    70.19,    97.54,    117.97],  # r = 1
    [74.44,    104.86,   130.15,   150,      164.67],  # r = 2
    [103.35,   134.22,   156.91,   173.04,   184.59],  # r = 3
    [126.71,   154.21,   171.38,   183.13,   191.52],  # r = 5
    [137.21,   162.64,   177.13,   186.65,   193.47],  # r = 10
    [144.92,   166.17,   178.84,   187.54,   193.93],  # r = 15
    [146.05,   166.74,   179.13,   187.71,   193.98]   # r = 19
])

fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot
surf = ax.plot_surface(ALPHA, R, CARRYING_CAPACITY, cmap='viridis', edgecolor='none')

#labels 
ax.set_xlabel('Information parameter α', labelpad=10)
ax.set_ylabel('Moore radius ρ', labelpad=10)
ax.set_zlabel('Carrying capacity (K)', labelpad=10)
#ax.set_title('Carrying Capacity as a function of Alpha and r')

ax.set_xticks(alpha_values)
ax.set_yticks(r_values)

# color bar which maps values to colors
fig.colorbar(surf, shrink=0.53, aspect=10, pad=0.1)

plt.show()