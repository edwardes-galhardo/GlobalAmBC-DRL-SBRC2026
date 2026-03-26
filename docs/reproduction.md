# Reproduction Guide – GlobalAmBC-DRL (SBRC 2026)

## 1. Overview

This document provides detailed instructions to reproduce the main experimental result presented in the paper:

"A New Centralized DRL-Based Control Module for Dense Batteryless IoT Networks with Ambient Backscatter"

The goal is to reproduce Figure 3, which illustrates the temporal behavior of the network success rate under two scenarios:

* Without control (baseline)
* With GlobalAmBC-DRL control

---

## 2. Artifact Structure

The repository is organized as follows:

GlobalAmBC-DRL-SBRC2026/
│
├── data/
├── scripts/
├── figures/
├── docs/

* data/ → input data for experiments
* scripts/ → execution scripts
* figures/ → generated outputs
* docs/ → documentation

---

## 3. Requirements

### 3.1 System Requirements

* Operating System: Windows, Linux, or macOS
* Python: version 3.8 or higher

### 3.2 Python Dependencies

Install the required libraries:

pip install pandas matplotlib numpy

---

## 4. Reproduction Steps

### Step 1 – Navigate to the scripts directory

cd scripts

### Step 2 – Execute the experiment

python run_experiment.py

---

## 5. Execution Workflow

The script run_experiment.py performs the following steps:

1. Generates synthetic data representing network behavior
2. Simulates two scenarios:

   * No control (high variability)
   * GlobalAmBC-DRL control (stabilized behavior)
3. Generates a plot comparing both scenarios
4. Saves the result as an image

---

## 6. Expected Output

After execution, the following file will be generated:

figures/figure3.png

---

## 7. Expected Results

The generated figure should reproduce the qualitative behavior presented in the paper:

Without Control:

* High variability
* Frequent oscillations
* Unstable performance

With GlobalAmBC-DRL:

* Lower variability
* More stable behavior
* Convergence to higher success rates

---

## 8. Execution Time

Expected runtime: less than 5 seconds

---

## 9. Notes on Data

The dataset used in this artifact is synthetically generated.

It was designed to reproduce the statistical behavior observed in the original OMNeT++ simulations, as described in the paper.

This design choice ensures:

* Fast execution
* Reproducibility
* Independence from simulation environments

---

## 10. Scope of Reproducibility

This artifact reproduces:

* The qualitative behavior of Figure 3
* The impact of centralized DRL control on network stability

This artifact does NOT require:

* OMNeT++ installation
* Full DRL training process

---

## 11. Troubleshooting

Missing dependencies:

pip install pandas matplotlib numpy

Script not running:

Ensure you are inside the scripts directory:

cd scripts
python run_experiment.py

---

## 12. Contact

Edwardes A. Galhardo
[edwardesamarogalhardo@inf.ufg.br](mailto:edwardesamarogalhardo@inf.ufg.br)
