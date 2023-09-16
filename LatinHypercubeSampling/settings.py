# LATIN HYPERCUBE SAMPLING

INPUT_DIMENSIONALITY = 4

# Temperature, Moisture Content, Damaged, Fermented
LOWER_BOUNDS = [22, 13.5, 1, 1]
UPPER_BOUNDS = [35, 15, 10, 10]

NUMBER_OF_SAMPLES = 80



# FILES
# Which json file to use as template
TEMPLATE_FILE = './LatinHypercubeSampling/template.json'

# Which directory to use to save all screening plan json files
# DO NOT FORGET THE LAST FRONTSLASH
JSON_FOLDER_PATH = './LatinHypercubeSampling/test/'

# A file to save screening plan as csv
CSV_FILE = './LatinHypercubeSampling/test.csv'

WIPE = True

