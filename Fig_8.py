# Figure 8a

import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

DATA_FOLDER = 'json_files'
# List of JSON files and corresponding labels/colors
files = [
    (f'{DATA_FOLDER}/plots-data-a0-l19-fig5.json', 'r', '-', r'Full Kelly'),
    (f'{DATA_FOLDER}/0_75Kelly.json', 'b',':',r'3/4 Kelly'),
    (f'{DATA_FOLDER}/0_75FixedFractionBet.json', 'orange','--',r'Fixed fraction (f = 3/4)'),
    (f'{DATA_FOLDER}/all-in-FixedFractionBet.json', 'g', '-.',r'Fixed fraction (f = 1)'),
]

plt.figure(figsize=(8, 6))  # Set figure size

for file, color, linestyle, label in files:
    # Load JSON data
    with open(file, 'r') as f:
        data = json.load(f)

    # Extract the live counts
    all_live_counts = data['live_counts']
    all_depleted_counts = data['depleted_tiles_counts']

    num_runs = len(all_live_counts)
    max_timesteps = 101 # timestep 0 to 100

    # Initialize arrays
    result = np.zeros(max_timesteps)
    depleted_result = np.zeros(max_timesteps)

    for run, depleted_run in zip(all_live_counts, all_depleted_counts):
        
        last_value = run[-1] if len(run) > 0 else 0

        # Pad the run if it's shorter than max_timesteps
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=last_value)
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
             
             label=label,
             linestyle=linestyle,
             linewidth = 2,
            
            )

# Label the plot
plt.xlabel('Time ($n$)')
plt.xlim(0,40)
plt.ylabel('Population ($S_n$)')
#plt.title('Surviving Organisms Over Time Based On Moore Radius r (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()



# Figure 8 b

import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# List of JSON files and corresponding labels/colors
files = [
    (f'{DATA_FOLDER}/fig10_kelly_l19_a1.json', 'r', '-', r'Full Kelly'),
    (f'{DATA_FOLDER}/fig10_3-4kelly_l19_a1.json', 'b',':',r'3/4 Kelly'),
    (f'{DATA_FOLDER}/fig10_3-4fixed_l19_a1.json', 'orange','--',r'Fixed fraction (f = 3/4)'),
    (f'{DATA_FOLDER}/fig10_1fixed_l19_a1.json', 'g', '-.',r'Fixed fraction (f = 1)'),
]

plt.figure(figsize=(8, 6))  # Set figure size

for file, color, linestyle, label in files:
    # Load JSON data
    with open(file, 'r') as f:
        data = json.load(f)

    # Extract the live counts
    all_live_counts = data['live_counts']
    all_depleted_counts = data['depleted_tiles_counts']

    num_runs = len(all_live_counts)
    max_timesteps = 101 # timestep 0 to 100

    # Initialize arrays
    result = np.zeros(max_timesteps)
    depleted_result = np.zeros(max_timesteps)

    for run, depleted_run in zip(all_live_counts, all_depleted_counts):
        
        last_value = run[-1] if len(run) > 0 else 0

        # Pad the run if it's shorter than max_timesteps
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=last_value)
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
             
             label=label,
             linestyle=linestyle,
             linewidth = 2,
            
            )

# Label the plot
plt.xlabel('Time ($n$)')
plt.xlim(0,40)
plt.ylabel('Population ($S_n$)')
#plt.title('Surviving Organisms Over Time Based On Moore Radius r (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()




# Figure 8 c
import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# List of JSON files and corresponding labels/colors
files = [
    (f'{DATA_FOLDER}/fig10_kelly_l1_a0.json', 'r', '-', r'Full Kelly'),
    (f'{DATA_FOLDER}/fig10_3-4kelly_l1_a0.json', 'b',':',r'3/4 Kelly'),
    (f'{DATA_FOLDER}/fig10_3-4fixed_l1_a0.json', 'orange','--',r'Fixed fraction (f = 3/4)'),
    (f'{DATA_FOLDER}/fig10_1fixed_l1_a0.json', 'g', '-.',r'Fixed fraction (f = 1)'),
]

plt.figure(figsize=(8, 6))  # Set figure size

for file, color, linestyle, label in files:
    # Load JSON data
    with open(file, 'r') as f:
        data = json.load(f)

    # Extract the live counts
    all_live_counts = data['live_counts']
    all_depleted_counts = data['depleted_tiles_counts']

    num_runs = len(all_live_counts)
    max_timesteps = 101 # timestep 0 to 100

    # Initialize arrays
    result = np.zeros(max_timesteps)
    depleted_result = np.zeros(max_timesteps)

    for run, depleted_run in zip(all_live_counts, all_depleted_counts):
        
        last_value = run[-1] if len(run) > 0 else 0

        # Pad the run if it's shorter than max_timesteps
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=last_value)
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
             
             label=label,
             linestyle=linestyle,
             linewidth = 2,
            
            )

# Label the plot
plt.xlabel('Time ($n$)')
#plt.xlim(0,40)
plt.ylabel('Population ($S_n$)')
#plt.title('Surviving Organisms Over Time Based On Moore Radius r (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()

