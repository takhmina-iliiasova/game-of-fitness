import numpy as np
import json
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# -----------Figure 8 a -----------
WIDTH, HEIGHT = 800, 800
TILE_SIZE = 40 # 20 x 20 tiles = 400 tiles in total
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
NO_TILES = GRID_WIDTH * GRID_HEIGHT
DATA_FOLDER = 'json_files'

# Load the JSON data
with open(f'{DATA_FOLDER}/plots-data-a0-l19-fig5.json', 'r') as f:
    data = json.load(f)

# Extract the live counts from the JSON data
all_live_counts = data['live_counts']
all_depleted_counts = data['depleted_tiles_counts']

num_runs = len(all_live_counts)

# Determine the maximum number of time steps across all runs
max_timesteps = max(len(run) for run in all_live_counts)

# Initialize result to store the cumulative sum of live counts
result = np.zeros(max_timesteps)

# for the prob plot # 2
depleted_result = np.zeros(max_timesteps)

# Iterate over each run and add the counts to the cumulative result
for i, (run, depleted_run) in enumerate(zip(all_live_counts, all_depleted_counts)):
    # Pad the run with last value if it has fewer time steps
    if len(run) < max_timesteps:
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=run[-1])
        padded_depleted = np.pad(depleted_run, (0, max_timesteps - len(depleted_run)), 'constant', constant_values=depleted_run[-1])
    else:
        padded_run = np.array(run[:max_timesteps])
        padded_depleted = np.array(depleted_run[:max_timesteps])

    # Add to cumulative results
    result += padded_run
    depleted_result += padded_depleted
    # Plot individual runs in gray
    plt.plot(padded_run, linestyle='', marker='.', markersize=1, color='#777777')
  
# Compute the average live count by dividing by the number of runs
average_live_counts = result / num_runs
average_depleted_counts = depleted_result / num_runs

# Get the last value from the averaged results
last_timestep_value = average_live_counts[-1]

# Print the value to the console
print(f"The value of the plot at the last timestep is: {last_timestep_value}")

# Plot the averaged result in red
# plt.plot(average_live_counts, color='r', label='Average')
plt.plot(average_live_counts, color='r', label=f'Average $S_n$')


# Label the plotS
plt.xlabel('Time ($n$)')
plt.ylabel('Population ($S_n$)')
#plt.title('Surviving Organisms Over Time (Averaged Across Runs)')
plt.legend()
plt.grid(True)
plt.show()
# -----------Figure 8 b -----------

# Logistic function definition
def logistic(x, L, k, t_0):
    return L / (1 + np.exp(-k * (x - t_0)))

# Logistic function definition - normalised version
def logistic_norm(t, r, t_0):
    return 1 / (1 + np.exp(-r * (t - t_0)))

# Load the JSON data
with open(f'{DATA_FOLDER}/plots-data-a0-l19-fig5.json', 'r') as f:
    data = json.load(f)

# Extract the live counts from the JSON data
all_live_counts = data['live_counts']

num_runs = len(all_live_counts)

# Determine the maximum number of time steps across all runs
max_timesteps = max(len(run) for run in all_live_counts)

# Initialize result to store the cumulative sum of live counts
result = np.zeros(max_timesteps)

# Iterate over each run and add the counts to the cumulative result
for i, run in enumerate(all_live_counts):
    # Pad the run with zeros (or the last value) if it has fewer time steps
    if len(run) < max_timesteps:
        padded_run = np.pad(run, (0, max_timesteps - len(run)), 'constant', constant_values=run[-1])  # Padding with last value
    else:
        padded_run = np.array(run[:max_timesteps])  # Truncate to max_timesteps if it's longer

    # Add to the cumulative result
    result += padded_run

    # Plot individual runs in gray
    # plt.plot(padded_run, linestyle='', marker='.', markersize=1, color='#777777')

# Compute the average live count by dividing by the number of runs
average_live_counts = result / num_runs
norm_average_live_counts = average_live_counts / max(average_live_counts) # normalised version

# Initial guesses for the logistic fit parameters
K_guess = max(average_live_counts) * 1.2  # A bit larger than the maximum value in the data
r_guess = 0.1  # A small growth rate
t_0_guess = max_timesteps / 2  # Midpoint of time steps

# Perform logistic curve fitting with initial guesses
time = np.arange(max_timesteps)
# params, _ = curve_fit(logistic, time, average_live_counts, p0=[K_guess, r_guess, t_0_guess], maxfev=10000)
params, _ = curve_fit(logistic_norm, time, norm_average_live_counts, p0=[r_guess, t_0_guess], maxfev=10000) # normalised version

# Print fitted parameters and mean squared error
print("NON-LINEAR LEAST SQUARES FITTING: \n")
fitted_values = logistic_norm(time, *params)
mse = np.mean((norm_average_live_counts - fitted_values) ** 2)
print(f"Fitted parameters: r = {params[0]}, t0 = {params[1]}, MSE = {mse}")

# Plot the averaged result in red
# plt.plot(average_live_counts, color='r', label=f'Average')
plt.plot(norm_average_live_counts, color='r', label=f'Normalised average $S_n$')

# Plot the logistic fit in blue
plt.plot(time, logistic_norm(time, *params), 'b--', label=f'Logistic Fit')

# Label the plot
plt.xlabel('Time ($n$)')
plt.ylabel('Normalized population')
plt.legend()
plt.grid(True)
plt.show()



# -----------Figure 8 c -----------
# Load data from the JSON file
with open(f'{DATA_FOLDER}/plots-data-a0-l19-fig5.json', 'r') as f:
    data = json.load(f)

#-------------------------------------------------------------------------------------#
# Plot for Figure 5c: p(n) theoretical VS p(n) simulation

\

# Extract live counts
live_counts = data['live_counts']


# Determine the maximum number of time steps across all runs
max_time_steps = len(average_live_counts)

# Calculate empty cell ratio considering depleted tiles
average_empty_ratios = (NO_TILES - average_live_counts - average_depleted_counts) / (NO_TILES - average_depleted_counts)

# Initialize lists to store probability values for each time step
probability_values = [[] for _ in range(max_time_steps)]

# Calculate probability values
for t in range(len(average_live_counts) - 1):
    current_population = average_live_counts[t]
    next_population = average_live_counts[t + 1]

    if current_population > 0:  # Avoid division by zero
        ratio = next_population / current_population
        #eq 13 from Overleaf:
        probability = 0.5 + (0.5 * np.sqrt(ratio - 1))
        
        probability_values[t].append(probability)

cleaned_probability = [
    # float(x[0]) for x in probability_values if isinstance(x, list) and x and not np.isnan(x[0])
    float(x[0]) if isinstance(x, list) and x else np.nan
    for x in probability_values
]

print(cleaned_probability)

# print mean squared error by omitting nan values between cleaned_probability and average_empty_ratios
mse = np.nanmean((np.array(cleaned_probability) - np.array(average_empty_ratios)) ** 2)
print(f"Mean Squared Error between theoretical and simulation probabilities: {mse} \n")  

# Plot the results
#plt.figure(figsize=(12, 8))

# Plot average probabilities from the first valid p(n) <= 1
plt.plot(range(len(cleaned_probability)), cleaned_probability, label='$p_n$ (theoretical)', marker='o', linestyle='-', color='b')

plt.plot(range(len(average_empty_ratios)), average_empty_ratios, label='$p_n$ (simulation)', marker='x', linestyle='--', color='orange')

plt.xlabel('Time ($n$)')
plt.ylabel('Success probability ($p_n$)')

plt.legend()
plt.grid(True)
plt.show()





