from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np 
from settings import *
from GaussianProcess.model_utils import *
from GaussianProcess.model_utils import load_models as load_gpmodels
from XGBoost.model_utils import *
from XGBoost.model_utils import load_models as load_xgbmodels
import os
import shutil
import pandas as pd

def main():

    param_values = saltelli.sample(PROBLEM, 1024)
    param_values[:,2] = param_values[:,2]*param_values[:,3]
    param_values = np.delete(param_values, 3, axis=1)
    while 1:
        model = input("Which model [gp/xgb] (XGBoost is faster)? -> ").lower()
        if model != "gp" and model != "xgb":
            print("Please type xgb or gp...")
            continue
        else:
            break
    if model == "gp":
        day_models = load_gpmodels(PATH_TO_MODELS_GP)
    elif model == "xgb":
        day_models = load_xgbmodels(PATH_TO_MODELS_XGBOOST)
    else:
        return
    print("Predicting...")
    y_hat = []
    for model in day_models:
        y_hat.append(model.predict(param_values))
    print("End of Prediction...")
    print("--------Initialize Sobol Analysis--------")
    temp_si = []
    mc_si = []
    co2_si = []
    o2_si = []
    dama_by_heat_si = []
    mould_si = []

    list_of_variables = [temp_si, mould_si, mc_si, co2_si, o2_si, dama_by_heat_si]

    for i, day in enumerate(DAYS):
        temp_si.append([])
        mc_si.append([])
        co2_si.append([])
        o2_si.append([])
        dama_by_heat_si.append([])
        mould_si.append([])
        for index in SOBOL_INDICES:
            temp_si[i].append(sobol.analyze(PROBLEM, y_hat[day-1][:,0])[index])
            mould_si[i].append(sobol.analyze(PROBLEM, y_hat[day-1][:,0])[index])
            mc_si[i].append(sobol.analyze(PROBLEM, y_hat[day-1][:,0])[index])
            co2_si[i].append(sobol.analyze(PROBLEM, y_hat[day-1][:,0])[index])
            o2_si[i].append(sobol.analyze(PROBLEM, y_hat[day-1][:,0])[index])
            dama_by_heat_si[i].append(sobol.analyze(PROBLEM, y_hat[day-1][:,0])[index])

    print("--------End of Sobol Analysis--------")

    print("--------Saving Analysis in CSV Format--------")

    list_of_input_names = ["Temperature", "Mould", "MoistureContent", "CO2", "O2", "DamagedByHeat"]
    list_of_output_names = ["Temperature", "Moisture Content", "Damaged", "Fermented"]
    if os.path.exists(SENSITIVITY_OUTPUT):
        shutil.rmtree(SENSITIVITY_OUTPUT)

    os.makedirs(SENSITIVITY_OUTPUT)
            
    for i, name in enumerate(list_of_input_names):
        day_path = os.path.join(SENSITIVITY_OUTPUT, name)
        os.makedirs(day_path)
        for j,index in enumerate(SOBOL_INDICES):
            index_path = os.path.join(day_path, index+ '.csv')
            temporary_array = np.array([list_of_variables[i][k][j] for k,day in enumerate(DAYS)])
            np.savetxt(index_path, temporary_array, delimiter=",")
            df = pd.read_csv(index_path, header=None)
            df.columns = list_of_output_names
            df["Days"] = DAYS
            df = df[["Days"] + [col for col in df if col != "Days"]]
            df.to_csv(index_path, index=False)


if __name__ == '__main__':
    main()
