# Sobol On Models

This directory uses pretrained models XGBoost and Gaussian Process to estimate Sobol first order "S1" and total order "ST" Indices.

To run this sensitivity analysis from the parent directory uth-centaur-diploma-thesis run the following command.

```bash
python SobolOnModels/sobol_sample_analyze.py
```
And the script will ask you which model you want to use.

## Settings

- <span style="color:#7CB9E8">PATH_TO_MODELS_XGBOOST
PATH_TO_MODELS_GP</span> : These are the paths to the directories that contain the pretrained models. Do not forget the forward slash.

- <span style="color:#7CB9E8">PROBLEM</span> : That is the problem that you want to define.

- <span style="color:#7CB9E8">SENSITIVITY_OUTPUT</span> : This is the path where the output of the sensitivity analysis will be saved. Do not forget the forward slash.

- <span style="color:#7CB9E8">DAYS</span> : These is a list of the days that the script will perform sensitivity analysis.

- <span style="color:#7CB9E8">SOBOL_INDICES</span> : This is the list of the indices that we want. Only avalaible options till now, "S1": first order, "ST": total order.
