# MORRIS SAMPLING

# Define the problem
PROBLEM = {
        'num_vars':4,
        'names':["temp", "mc", "damage", "fermented"],
        'bounds':[[27,35],
                  [11,15],
                  [4,12],
                  [4,12]]
    }

# Number of morrises trajectories
# Number of final samples (r)*(n + 1) where:
# r = number_of_trajectories
# n = number_of_input_variables
NUM_OF_TRAJECTORIES = 18

# Level of descritization
# Descritize the input space defined by bounds
LEVEL_OF_DESCRITIZATION = 6

# FILTERS
# Number of Iterations, to find a plan that passes custom filters
NUM_OF_ITERATIONS = 10000

# The maximum frequency distance for a variable
# Example: 
# if we discretize the range [0,5] with a level of discretization = 6 we
# obtain the values [0,1,2,3,4,5]. We do not want our plan to have 20 0 values and only 7 1 values
# it creates an imbalanced plan  so we set a threshold for the maximum difference of the frequencies.
FILTER_DISTANCE = 12


# FILES
# Which json file to use as template
TEMPLATE_FILE = './MorrisScreeningPlan/template.json'

# Which directory to use to save all screening plan json files
# DO NOT FORGET THE LAST FRONTSLASH
JSON_FOLDER_PATH = './MorrisScreeningPlan/test/'

# If wipe = True all the json files from JSON_FOLDER_PATH will be erased
WIPE = True

# A file to save screening plan as csv
CSV_FILE = './MorrisScreeningPlan/test.csv'

