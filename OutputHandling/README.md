# Output Handling

This directory is responsible for retrieving information from the cases folder. The cases folder is the folder where all the CFD outputs from an organised plan from SimulationsAutomation are placed. The automation has 4 steps:

- Collect output values.
- Find and replace rows with the median(The median is the middle probe measurement) of the row.
- Reorganize files into a more helpful format and preparing the final csv files.
- Apply Hardlimits to the outliers.

To run the automation

```bash
python output_automated_pipeline.py
```

## Settings

These are the hardlimits for the output values.
- <span style="color:#7CB9E8">TEMP</span>

    <span style="color:#7CB9E8">MOULD</span>

    <span style="color:#7CB9E8">WG</span>

    <span style="color:#7CB9E8">DAM_HEAT</span>

    <span style="color:#7CB9E8">CO2</span>

    <span style="color:#7CB9E8">O2</span>

-  <span style="color:#7CB9E8">CASE_PATH_TEMPLATE</span> : This is an example of how the cases are named and where is the valuable information.

-  <span style="color:#7CB9E8">SENSITIVITY_CSV_PATH</span> : This is the csv file that it was produced by Simulation Automation

-  <span style="color:#7CB9E8">CASES_FOLDER_PATH</span> : This is the directory where all the cases are placed.

-  <span style="color:#7CB9E8">CSV_FOLDER_PATH</span> : This folder if it does not exist it will be created. It will contain csv files with the initial information of height.

-  <span style="color:#7CB9E8">CSV_MEDIAN_FOLDER_PATH</span> : This folder if it does not exist it will be created. It will contain csv files with the median of each row.

-  <span style="color:#7CB9E8">CSV_FINAL_PATH</span> : This folder if it does not exist it will be created. It will contain the final csv files.

Warning! In every directory path do not forget to place a backslash at the end.
