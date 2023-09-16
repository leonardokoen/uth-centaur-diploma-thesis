# Morris Screening Plan

This directory contains all the files responsible for preparing a screening plan.

After you modified settings.py run

```bash
python MorrisScreeningPlan/screening_smaple.py
```

## Python Files

- modify_input_template.py

- screening_sample.py

- settings.py

## Settings 

- <span style="color:#7CB9E8">PROBLEM</span> :  A dictonary with 3 keys,

    'num_vars' : Dimensionality of the input space.

    'names' : A list of strings with names for each variable

    'bounds' : A list of lists, every inner list contains 2 elements, the lower and the higher bounds of the variable that you want.

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

- <span style="color:#7CB9E8">NUM_OF_TRAJECTORIES</span> : The number of trajectories. This number defines how many samples the final screening plan will have. The formula is : $r \times (n+1)$, where $r$ the number of trajectories and $n$ the dimensionality of input.

    example :

    If we have 4 input variables and we choose to have 17 trajectories, we will have $17 \times (4 +1) = 85$ samples in the screening plan. 

-  <span style="color:#7CB9E8">LEVEL_OF_DESCRITIZATION</span> : This is the level that we will descritize our input variable bounds.

- <span style="color:#7CB9E8">NUM_OF_ITERATIONS</span> : This number defines how many different plans we will try until we satisfy the filters that we have created for the plan to be uniform.

- <span style="color:#7CB9E8">FILTER_DISTANCE</span> :  The maximum frequency distance between 2 variables.

    example : 

    If we discretize the range [0,5] with level of discretization = 6 we
    obtain the values [0,1,2,3,4,5]. We do not want our plan to have 20 0 values and only 7 1 values it creates an imbalanced plan  so we set a threshold for the maximum difference of the frequencies.

- <span style="color:#7CB9E8">TEMPLATE_FILE</span> : The file that the script will use as template to produce all the other samples.

- <span style="color:#7CB9E8">JSON_FOLDER_PATH</span> : This is the path to the folder where all the samples will be saved.

- <span style="color:#7CB9E8">WIPE</span> : A boolean value. If true, all files in JSON_FOLDER_PATH will be erased, and new files will be produced.

- <span style="color:#7CB9E8">CSV_FILE</span> : A file that keeps the screening plan in a csv format.

## Screening Sample

The screening_sample.py finds a uniform screening plan and then using screening_to_json and screening_to_csv functions from modify_input_template.py saves the plan.
 