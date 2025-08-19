#histogram
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# --- Load the data ---
with open("10000_lvl19_a0.json", "r") as f:
    data = json.load(f)

live_counts = data["live_counts"]  # list of 10,000 runs, each with 100 time steps
live_counts = np.array(live_counts)  # shape: (10000, 100)

# --- Time points of interest ---
time_points = [2, 10, 20]

# --- Plotting ---
for t in time_points:
    populations_at_t = live_counts[:, t]  # extract values at time t across all runs

    # Fit a normal distribution
    mu, std = norm.fit(populations_at_t)

    # Plot histogram
    plt.figure(figsize=(8, 6))
    count, bins, ignored = plt.hist(populations_at_t, bins=30, density=True, color='skyblue', edgecolor='black', label=f"Histogram (t={t})")

    # Plot PDF
    x = np.linspace(min(populations_at_t), max(populations_at_t), 1000)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'r--', linewidth=2, label=f'Gaussian Fit\nμ = {mu:.2f}, σ = {std:.2f}')

    # Labels and legend
    plt.title(f"Population Size Distribution at t={t}")
    plt.xlabel("Population Size")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
