#---carrying capacity over alpha plot---#
import matplotlib.pyplot as plt
import numpy as np
# Alpha values 
alpha_values = [0, 0.25, 0.5, 0.75, 1]
carrying_capacities = [146.05, 166.74, 179.13, 187.71, 193.98]  


# Plot
plt.figure(figsize=(8, 5))
plt.plot(alpha_values, carrying_capacities, '-o') 

plt.xlabel('Alpha')
plt.ylabel('Carrying Capacity (K)')
plt.title('Carrying Capacity Over Alpha')
plt.grid(True)
plt.tight_layout()
plt.show()

