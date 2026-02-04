# Game of Fitness

Simulation code and data analysis for the paper:
**"Game of Fitness: Kelly betting in a limited environment leads to logistic growth"**

🌐 **Live Demo:** [www.gameoffitness.net](https://www.gameoffitness.net/)

---

## 📂 Structure

* **`game.py`**: Main simulation engine using the **Optimal Kelly** strategy.
* **`KellyandfixedFractionGame.py`**: Extended simulation for testing alternate strategies (Fixed Fraction, All-in, Fractional Kelly).
* **`Fig_XX.py`**: Scripts to generate figures and heatmaps using data from `json_files/`.
* **`json_files/`**: Pre-computed simulation data used by the plotting scripts.

## 🚀 Usage

### 1. Install Dependencies
```bash
pip install pygame numpy matplotlib scipy
```
### 2. Run Simulations
Open **`game.py`** and adjust the Configuration Region at the top to change
* **level**  Moore neighborhood radius ($\rho$)
* **tile_selection_bias**: Information parameter ($\alpha$)
* **NUM_RUNS**: Iterations for averaging

Run the script:
```bash
python game.py
```
### 3. Generate Figures
Ensure the required .json files are in the json_files/ folder, then run the specific figure script:

```bash
python Fig_6.py
```
