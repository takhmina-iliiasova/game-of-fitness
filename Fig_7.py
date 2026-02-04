import json
import numpy as np
import matplotlib.pyplot as plt

DATA_FOLDER = 'json_files'

#uncomment the desired file for the heatmap:
with open(f'{DATA_FOLDER}/1010_10000_a0_l1_hm.json', 'r') as f:  #for Figure 7 a
#with open(f'{DATA_FOLDER}/1010_10000_a05_l1_hm.json', 'r') as f: #for Figure 7 b
#with open(f'{DATA_FOLDER}/1010_10000_a1_l1_hm.json', 'r') as f:  #for Figure 7 c

#with open(f'{DATA_FOLDER}/1010_10000_a0_l2_hm.json', 'r') as f:  #for Figure 7 d
#with open(f'{DATA_FOLDER}/1010_10000_a05_l2_hm.json', 'r') as f: #for Figure 7 e
#with open(f'{DATA_FOLDER}/1010_10000_a1_l2_hm.json', 'r') as f:  #for Figure 7 f

#with open(f'{DATA_FOLDER}/1010_10000_a0_l19_hm.json', 'r') as f:  #for Figure 7 g
#with open(f'{DATA_FOLDER}/a05_l19_hm.json', 'r') as f: #for Figure 7 h
#with open(f'{DATA_FOLDER}/1010_10000_a1_l19_hm.json', 'r') as f:  #for Figure 7 i
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
plt.colorbar(im, label='Mean occupancy density')
plt.title('Heatmap of Final Organism Positions Across Runs')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.tight_layout()
plt.show()
