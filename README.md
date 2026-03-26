# GlobalAmBC-DRL: SBRC 2026 Artifact

## Description

This repository contains the experimental artifacts of the paper:

"A New Centralized DRL-Based Control Module for Dense Batteryless IoT Networks with Ambient Backscatter"

The goal of this artifact is to reproduce the main results presented in the paper, particularly the temporal behavior of the network success rate under different control strategies.

---

## Repository Structure

* `data/` → datasets used in the experiments
* `scripts/` → scripts for execution and plotting
* `figures/` → generated outputs
* `docs/` → additional documentation

---

## Artifact Goals

This artifact reproduces the behavior presented in **Figure 3** of the paper, demonstrating:

* Instability in networks without control
* Stabilization using the GlobalAmBC-DRL module

---

## Target Badges

This artifact aims to obtain the following badges:

* Artifacts Available (SeloD)
* Artifacts Functional (SeloF)
* Results Reproduced (SeloR)

---

## Requirements

* Operating System: Windows, Linux, or macOS
* Python: 3.8+
* RAM: at least 2GB

---

## Dependencies

Install required libraries:

pip install pandas matplotlib numpy

---

## Quick Start (Minimum Test)

Run the full experiment with a single command:

cd scripts
python run_experiment.py

---

## Expected Output

After execution, the following file will be generated:

figures/figure3.png

The resulting plot should show:

* High variability without control
* Stable behavior with GlobalAmBC-DRL

---

## Documentation

For detailed reproduction steps, see:

docs/reproduction.md

---

## Notes

The dataset used in this artifact is synthetically generated to reproduce the statistical behavior observed in the original simulations described in the paper.

---

## License

MIT License
