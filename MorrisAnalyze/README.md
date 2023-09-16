# Morris Analyze

This directory is responsible for printing the output of Morris's Method after we have collected and reorganised the output using OutputHandling.

To perform analysis run after you have modified settings.py:

```bash
python MorrisAnalyze/morris_analyze.py
```

## Settings

-  <span style="color:#7CB9E8">PROBLEM</span>: A dictonary with 3 keys,

    **'num_vars'** : Dimensionality of the input space.

    **'names'** : A list of strings with names for each variable

    **'bounds'** : A list of lists, every inner list contains 2 elements, the lower and the higher bounds of the variable that you want.

    example:

    ```python
    PROBLEM = {
            'num_vars':4,
            'names':["temp", "mc", "damage", "fermented"],
            'bounds':[[27,35],
                    [11,15],
                    [4,12],
                    [4,12]]
        }
    ```

    This should be the same as the one you defined in MorrisScreeningPlan settings.py

-  <span style="color:#7CB9E8">LEVEL_OF_DESCRITIZATION</span> : This is the level that we will descritize our input variable bounds.

    This should be the same as the one you defined in MorrisScreeningPlan settings.py.

- <span style="color:#7CB9E8">MORRIS_FINAL_CSV_FILE_T
MORRIS_FINAL_CSV_FILE_MC
MORRIS_FINAL_CSV_FILE_O2
MORRIS_FINAL_CSV_FILE_CO2
MORRIS_FINAL_CSV_FILE_MOULD
MORRIS_FINAL_CSV_FILE_DAMHEAT</span>

    These are filepaths to the final csv files produced from OutputHandling.

- <span style="color:#7CB9E8">LIST_OF_DAYS</span> : This is a list of the days of the simulation, that we want Morris to Analyze, 3-5 entries are good for analysis and get a first intuition for your output variables.

- <span style="color:#7CB9E8">FIGURES_DIRECTORY</span> : The path where the figures will be saved.