import numpy as np 
import xgboost as xgb
import os

def load_models(path):
  day_models = []
  num_of_models = len(os.listdir(path))
  for i in range(num_of_models):
    name = path + "model" + str(i).zfill(2) + ".json"
    model = xgb.XGBRegressor()
    model.load_model(name)
    day_models.append(model)
  return day_models


def prediction_input(input_arguments):
  for i, element in  enumerate(input_arguments):
    element[2] = element[2] * element[3]
    element.pop()
  return np.array(input_arguments)