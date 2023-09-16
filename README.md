# uth-centaur-diploma-thesis

This repository has all the code I 've developed during my diploma thesis:

    "Sensitivity analysis and surrogate model design on a computational fluid dynamics model to predict grain conditions in cargo ship holds"

This thesis was also the product of my internship with [Centaur Analytics Inc.](https://centaur.ag/).

## Contents

### Sampling

**MorrisScreeningPlan** : This directory contains code that produces a uniform Morris Screening Plan ready for the CFD simulation.

**LatinHypercubeSampling** : This directory contains code that produces a Latin Hapercube Sample ready for the CFD simulation.

### Automation

**SimulationAutomation** : This directory contains code that automates the CFD simulation execution.

**OutputHandling** : This directory contains code that automates the information retrieval from CFD simulation output.

### CFD Surrogate Models

**GaussianProcess** : This directory contains the pretrained Gaussian Process model.

**XGBoost** : This directory contains the pretrained XGBoost model.

### Sensitivity Analysis

**MorrisAnalyze** : After the creation of a Morris Sample, Simulation Automation and Output Handling you can use this directory to perform sensitivity analysis.

**SobolOnModels** : This directory contains code that performs Sobol Sensitivity Analysis by utilizing surrogate models.

## Installation

Initialy clone the repository:

```bash
git clone https://github.com/leonardokoen/uth-centaur-diploma-thesis.git
```

Then add the repository to your $PYTHONPATH:

```bash
nano ~/.bashrc
```
add this line at the end of the file

```bash
export PYTHONPATH=/path/to/uth-centaur-diploma-thesis:$PYTHONPATH
```
save file.

Then execute,

```bash
source ~/.bashrc
```

All the scripts are made to be run from uth-centaur-diploma-thesis directory. If you want to alter that behaviour change the paths in settings.py in the directory that you want to work with.
