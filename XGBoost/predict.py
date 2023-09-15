from model_utils import *
from settings import *



def main():
    prediction = prediction_input(PREDICTION_INPUT)
    day_models = load_models(PATH_TO_MODELS)
    for i, model in enumerate(day_models):
      print(f"Day {i}")
      print(model.predict(prediction))
    
    

  

if __name__ == "__main__":
  main()