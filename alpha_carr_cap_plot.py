#---carrying capacity over alpha plot---#
import matplotlib.pyplot as plt
import numpy as np
# Alpha values used in your simulations
alpha_values = [0, 0.25, 0.5, 0.75, 1]

# Corresponding carrying capacities (from previous plots)
# Replace these with your actual values
carrying_capacities = [146.05, 166.74, 179.13, 187.71, 193.98]  

# # Fit a 4nd-degree polynomial (quadratic)
# coeffs = np.polyfit(alpha_values, carrying_capacities, deg=4)
# poly = np.poly1d(coeffs)

# # Generate smooth curve
# x_smooth = np.linspace(0, 1, 300)
# y_smooth = poly(x_smooth)

# Plot
plt.figure(figsize=(8, 5))
#plt.plot(alpha_values, carrying_capacities, 'o', label='Data')
#plt.plot(x_smooth, y_smooth, '-', label='4th Degree Polynomial Fit')
plt.plot(alpha_values, carrying_capacities, '-o')  # -o means line + circle markers

plt.xlabel('Alpha')
plt.ylabel('Carrying Capacity (K)')
plt.title('Carrying Capacity Over Alpha')
#plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



# # 1. fit the logistic equation to extract the K carrying capacity value
# import numpy as np
# import json
# import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# # Logistic growth model
# def logistic(t, K, r, A):
#     return K / (1 + A * np.exp(-r * t))

# # List of JSON files and corresponding alpha values
# files = [
#     ('10000_lvl19_a0.json', 0.0),
#     ('10000_lvl19_a025.json', 0.25),
#     ('10000_lvl19_a05.json', 0.5),
#     ('10000_lvl19_a075.json', 0.75),
#     ('10000_lvl19_a1.json', 1.0)
# ]

# alpha_vals = []
# carrying_capacities = []

# for file, alpha in files:
#     # Load JSON data
#     with open(file, 'r') as f:
#         data = json.load(f)

#     # Extract the live counts
#     all_live_counts = data['live_counts']
#     num_runs = len(all_live_counts)
#     max_timesteps = max(len(run) for run in all_live_counts)

#     # Average the live counts over runs
#     result = np.zeros(max_timesteps)
#     for run in all_live_counts:
#         padded_run = np.pad(run, (0, max_timesteps - len(run)), 'edge')
#         result += padded_run
#     average_live_counts = result / num_runs

#     # Time axis
#     t = np.arange(len(average_live_counts))

#     # Initial guesses for K, r, A
#     K0 = max(average_live_counts)
#     r0 = 0.1
#     A0 = (K0 - average_live_counts[0]) / average_live_counts[0]
#     p0 = [K0, r0, A0]

#     try:
#         # Fit the logistic model
#         popt, _ = curve_fit(logistic, t, average_live_counts, p0=p0, maxfev=10000)
#         K_fit = popt[0]
#     except RuntimeError:
#         K_fit = np.nan  # If the fit fails

#     alpha_vals.append(alpha)
#     carrying_capacities.append(K_fit)

# # Sort by alpha
# sorted_pairs = sorted(zip(alpha_vals, carrying_capacities))
# alpha_vals, carrying_capacities = zip(*sorted_pairs)

# # Plot Carrying Capacity vs Alpha
# plt.figure(figsize=(8, 6))
# plt.plot(alpha_vals, carrying_capacities, marker='o', linestyle='-')
# plt.xlabel('Alpha (α)')
# plt.ylabel('Estimated Carrying Capacity (K)')
# plt.title('Carrying Capacity vs Alpha (based on logistic fit)')
# plt.grid(True)
# plt.show()


