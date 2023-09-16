# Gaussian Process

This is the XGBoost black-box. All the models are saved in the XGBoostModels directory as JSON files.

``` bash
python GaussianProcess/predict.py
```

after you have modified settings.py.

If you want to use models in a different script add this repository to python path:

```bash
nano ~\.bashrc
```

add this line to the end of the file

```bash
export PYTHONPATH=/path/to/uth-centaur-diploma-thesis:$PYTHONPATH
```

save file.

Then execute,

```bash
source ~/.bashrc
```

Now that the directory is in the PYTHONPATH you can add the following lines to include the models in your script.

```python
from XGBoost.model_utils import *
from XGBoost.model_utils import load_models as load_xgbmodels
```

Set the PATH_TO_MODELS_XGBOOST accordingly to where the models are saved.  
Example:

```python
from XGBoost.model_utils import *
from XGBoost.model_utils import load_models as load_xgbmodels

PATH_TO_MODELS_XGBOOST = "/path/to/uth-centaur-diploma-thesis/XGBoost/XGBoostModels/"
day_models = load_xgbmodels(PATH_TO_MODELS_XGBOOST)

TO_PREDICT = [[32, 15, 4,4]]

modified_to_predict = prediction_input(TO_PREDICT)

y_hat = np.array([model.predict(modified_to_predict) for model in day_models])
```

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
