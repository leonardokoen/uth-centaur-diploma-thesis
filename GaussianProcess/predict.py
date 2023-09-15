from model_utils import *
from settings import *
import os

def main():
    prediction = prediction_input(PREDICTION_INPUT)
    day_models = load_models(PATH_TO_MODELS)
    for i, model in enumerate(day_models):
      print(f"Day {i}")
      lower, upper = model.predict_uncertainty(prediction)
      print(f"Lower Bound: {lower}")
      print(f"Mean Value: {model.predict(prediction)}")
      print(f"Upper Bound: {upper}")
    

if __name__ == "__main__":
  main()