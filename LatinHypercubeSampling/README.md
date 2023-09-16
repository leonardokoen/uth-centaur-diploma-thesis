# Morris Screening Plan

This directory contains all the files responsible for preparing a plan with Latin Hypercube Sampling.

To perform lhs run after you have modified settings.py:

```bash
python LatinHypercubeSampling/lhs_sample.py
```

## Settings

- <span style="color:#7CB9E8">INPUT_DIMENSIONALITY</span>: The dimensionality of input.

- <span style="color:#7CB9E8">LOWER_BOUNDS</span>: A list, every element is responsible for the lower bound of a variable, Temperature, Moisture Content, Damaged and Fermented with that order.

- <span style="color:#7CB9E8">UPPER_BOUNDS</span>: A list, every element is responsible for the upper bound of a variable, Temperature, Moisture Content, Damaged and Fermented with that order.

- <span style="color:#7CB9E8">NUMBER_OF_SAMPLES</span>:
The number of samples.

- <span style="color:#7CB9E8">TEMPLATE_FILE</span> : The file that the script will use as template to produce all the other samples.

- <span style="color:#7CB9E8">JSON_FOLDER_PATH</span> : This is the path to the folder where all the samples will be saved.

- <span style="color:#7CB9E8">WIPE</span> : A boolean value. If true, all files in JSON_FOLDER_PATH will be erased, and new files will be produced.

- <span style="color:#7CB9E8">CSV_FILE</span> : A file that keeps the screening plan in a csv format.
