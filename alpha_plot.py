#------------------average live organisms over time for different moore radius---------#


import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from sim import NO_TILES


# List of JSON files and corresponding labels/colors
files = [
    ('10000_lvl19_a0.json', 'r', 'α = 0'),
    ('10000_lvl19_a025.json', 'b', 'α = 0.25'),
    ('10000_lvl19_a05.json', 'g', 'α = 0.5'),
    ('10000_lvl19_a075.json', 'orange', 'α = 0.75'),
    ('10000_lvl19_a1.json', 'purple', 'α = 1')
]

plt.figure(figsize=(8, 6))  # Set figure size

for file, color, label in files:
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
    plt.plot(average_live_counts, color=color, label=label)

# Label the plot
plt.xlabel('Time (iterations)')
plt.ylabel('Number of surviving organisms')
plt.title('Surviving Organisms Over Time Based On Alpha α (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()

