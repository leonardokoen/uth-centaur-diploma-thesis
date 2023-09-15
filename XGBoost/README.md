# Gaussian Process

This is the XGBoost black-box. All the models are saved in the XGBoostModels directory as JSON files. To read them and perform predictions use predict.py script.

## Settings

- <span style="color:#7CB9E8">PATH_TO_MODELS</span>: The file path to the models directory.

- <span style="color:#7CB9E8">PREDICTION_INPUT</span>: A list of lists. The elements of every inner list are temperature, moisture content, damaged and fermented with that order.

## Useful Model Methods

- predict(array):

  - Input: a $n \times 3$ dimensional numpy array. Where n the number of samples and 3 the three variables(Temperature, Moisture Content, Damaged * Fermented).

  - Output: a $n \times 6$ numpy array where n the number of samples and 6 the 6 output variables (Temperature, Mould, Mc, CO2, O2, Damaged by Heat) in that order.

## Notes

The models where made with hardlimits to output values :

- Temperature : 330
- Mould : 4
- Wg : 0.1834
- Damage By Heat : 1.2
- CO2 : 2.435405
- O2 : -2.205569

And Input Space :

- Temperature : [22.03326, 35]
- Moisture Content : [10.02020, 15.9734]
- Damaged * Fermented : [0.25, 144.0]

When your input is near to the high bound edges of the Input Space the model is more unstable.
