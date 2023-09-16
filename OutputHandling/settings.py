# HARDLIMITS
TEMP = 330
MOULD = 4
WG = 0.1834
DAM_HEAT = 1.2
CO2 = 2.435405
O2 = -2.205569

# This is an example of how the cases are named and where is the valuable information.
# DO NOT FORGET THE BACKSLASH AT THE END
CASE_PATH_TEMPLATE = "test_0_hold5_18616ba1073/postProcessing/probes/0/"

#This is the csv file that it was produced by either Latin Hypercube Sampling or Morris Screening
SENSITIVITY_CSV_PATH = "/mnt/e/DiplomaThesis/Code/SmartVesselHold/enhance_model/enhance_model.csv"

#This is the path where all the cases are placed.
# DO NOT FORGET THE BACKSLASH AT THE END
CASES_FOLDER_PATH = '/mnt/e/CFD-Simulations/enhance_cases/'

# Automation Output Paths

# This folder if it does not exist it will be created 
# it will contain csv files with the initial information of height.
# DO NOT FORGET THE BACKSLASH AT THE END
CSV_FOLDER_PATH = "./OutputHandling/InitialOutputCSV/"

# This folder if it does not exist it will be created 
# it will contain csv files with the median of each row.
# DO NOT FORGET THE BACKSLASH AT THE END
CSV_MEDIAN_FOLDER_PATH = "./OutputHandling/MedianOutputCSV/"

# This folder if it does not exist it will be created 
# it will contain the final csv files.
# DO NOT FORGET THE BACKSLASH AT THE END
CSV_FINAL_PATH = "./OutputHandling/FinalOutputCSV/"


