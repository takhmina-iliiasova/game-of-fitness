import json
import numpy as np
import matplotlib.pyplot as plt

# Load the data
#with open('simulation_data.json', 'r') as f:
with open('1010_10000_a0_l19_hm.json', 'r') as f:
    data = json.load(f)

# Extract the list of final grids
final_grids = data["final_grids"]  # List of 2D arrays

# Convert to numpy array
grids_array = np.array(final_grids)  # shape: (num_runs, height, width)

# Compute heatmap data
heatmap_data = np.mean(grids_array, axis=0)  # shape: (height, width)

# Plot the heatmap
plt.figure(figsize=(8, 6))
#im = plt.imshow(heatmap_data, cmap='hot', interpolation='nearest', vmin=0.3, vmax=0.4)
im = plt.imshow(heatmap_data, cmap='hot', interpolation='nearest')

# Set integer ticks
height, width = heatmap_data.shape
plt.xticks(np.arange(width))
plt.yticks(np.arange(height))

# Add colorbar and labels
plt.colorbar(im, label='Proportion of times tile was occupied')
plt.title('Heatmap of Final Organism Positions Across Runs')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.tight_layout()
plt.show()



# import json
# import numpy as np
# import matplotlib.pyplot as plt

# # Load the data
# with open('simulation_data.json', 'r') as f:
#     data = json.load(f)

# # Extract the list of final grids
# final_grids = data["final_grids"]  # This is a list of 2D arrays

# # Convert to numpy arrays for fast processing
# grids_array = np.array(final_grids)  # shape: (num_runs, height, width)

# # Average over runs to get proportion of organism presence per tile
# heatmap_data = np.mean(grids_array, axis=0)  # shape: (height, width)

# # Plot the heatmap
# plt.figure(figsize=(8, 6))
# plt.imshow(heatmap_data, cmap='hot', interpolation='nearest', vmin=0, vmax=1)
# plt.colorbar(label='Proportion of times tile was occupied')
# plt.title('Heatmap of Final Organism Positions Across Runs')
# plt.xlabel('X Coordinate')
# plt.ylabel('Y Coordinate')
# plt.tight_layout()
# plt.show()
