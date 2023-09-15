# Path to pretrained models
PATH_TO_MODELS_XGBOOST = "./XGBoost/XGBoostModels/"
PATH_TO_MODELS_GP = "./GaussianProcess/GPModels/"

#Define Problem
PROBLEM = {
    'num_vars': 4,
    'names': ['Temperature', 'Moisture Content', 'Damage', 'Fermented'],
    'bounds': [[23, 35],
               [11, 15.5],
               [0.5, 10],
               [0.5, 10]]
}


#Where do you want to save the output ?
SENSITIVITY_OUTPUT = './SobolOnModels/SensitivityOutput/'

#Which Days ?
DAYS = [10,20,25,30,35,44]

# Use only "S1" , "ST"
SOBOL_INDICES = ["S1","ST"]