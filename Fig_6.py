import matplotlib.pyplot as plt
import numpy as np
import json
from scipy.optimize import curve_fit

# -----------Figure 6 a -----------
# List of JSON files and corresponding labels/colors
DATA_FOLDER = 'json_files'
files = [
    (f'{DATA_FOLDER}/10000_lvl1_a0.json', 'r', '.', r'$\rho$ = 1'),
    (f'{DATA_FOLDER}/10000_lvl2_a0.json', 'b', 'o',r'$\rho$  = 2'),
    (f'{DATA_FOLDER}/10000_lvl3_a0.json', 'g', 'D',r'$\rho$  = 3'),
    (f'{DATA_FOLDER}/10000_lvl5_a0.json', 'orange', 's', r'$\rho$  = 5'),
    (f'{DATA_FOLDER}/10000_lvl10_a0.json', 'purple', '^',r'$\rho$  = 10'),
    (f'{DATA_FOLDER}/10000_lvl15_a0.json', 'c', 'v',r'$\rho$  = 15'),
    (f'{DATA_FOLDER}/10000_lvl19_a0.json', 'm', 'x',r'$\rho$  = 19')
]

plt.figure(figsize=(8, 6))  # Set figure size

for file, color, marker, label in files:
    # Load JSON data
    with open(file, 'r') as f:
        data = json.load(f)

    # Extract the live counts
    all_live_counts = data['live_counts']
    all_depleted_counts = data['depleted_tiles_counts']

    num_runs = len(all_live_counts)
    max_timesteps = max(len(run) for run in all_live_counts)

    # Initialize arrays
    result = np.zeros(max_timesteps)
    depleted_result = np.zeros(max_timesteps)

    # Process each run
    for run, depleted_run in zip(all_live_counts, all_depleted_counts):
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=run[-1])
        padded_depleted = np.pad(depleted_run, (0, max_timesteps - len(depleted_run)), 'constant', constant_values=depleted_run[-1])

        result += padded_run
        depleted_result += padded_depleted

    # Compute averages
    average_live_counts = result / num_runs
    average_depleted_counts = depleted_result / num_runs

    # Compute carrying capacity (maximum average live count)
    carrying_capacity = np.max(average_live_counts)
    print(f"Carrying capacity for {label}: {carrying_capacity:.2f}")

    # Plot the averaged result
    plt.plot(average_live_counts, 
             color=color, 
             marker=marker, 
             label=label, 
             linestyle='-',
             markersize=4,
             markevery = 2)

# Label the plot
plt.xlabel('Time ($n$)')
plt.ylabel('Population ($S_n$)')
#plt.title('Surviving Organisms Over Time Based On Moore Radius r (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()



# -----------Figure 6 b -----------

# List of JSON files and corresponding labels/colors
files = [
    (f'{DATA_FOLDER}/10000_lvl19_a0.json', 'r', 'o', 'α = 0'),
    (f'{DATA_FOLDER}/10000_lvl19_a025.json', 'b', 'D', 'α = 0.25'),
    (f'{DATA_FOLDER}/10000_lvl19_a05.json', 'g', 'x', 'α = 0.5'),
    (f'{DATA_FOLDER}/10000_lvl19_a075.json', 'orange', 's', 'α = 0.75'),
    (f'{DATA_FOLDER}/10000_lvl19_a1.json', 'purple', 'v', 'α = 1')
]

plt.figure(figsize=(8, 6))  # Set figure size

for file, color, marker, label in files:
    # Load JSON data
    with open(file, 'r') as f:
        data = json.load(f)

    # Extract the live counts
    all_live_counts = data['live_counts']
    all_depleted_counts = data['depleted_tiles_counts']

    num_runs = len(all_live_counts)
    max_timesteps = max(len(run) for run in all_live_counts)

    # Initialize arrays
    result = np.zeros(max_timesteps)
    depleted_result = np.zeros(max_timesteps)

    # Process each run
    for run, depleted_run in zip(all_live_counts, all_depleted_counts):
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=run[-1])
        padded_depleted = np.pad(depleted_run, (0, max_timesteps - len(depleted_run)), 'constant', constant_values=depleted_run[-1])

        result += padded_run
        depleted_result += padded_depleted

    # Compute averages
    average_live_counts = result / num_runs
    average_depleted_counts = depleted_result / num_runs

    # Compute carrying capacity (maximum average live count)
    carrying_capacity = np.max(average_live_counts)
    print(f"Carrying capacity for {label}: {carrying_capacity:.2f}")


    
    # Plot the averaged result
    plt.plot(average_live_counts, 
             color=color, 
             marker=marker, 
             label=label, 
             linestyle='-',
             markersize=4,
             markevery = 2)


# Label the plot
plt.xlabel('Time ($n$)')
plt.ylabel('Population ($S_n$)')
#plt.title('Surviving Organisms Over Time Based On Alpha α (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()





# -----------Figure 6 c -----------

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