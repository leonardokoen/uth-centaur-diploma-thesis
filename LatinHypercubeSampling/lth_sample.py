from settings import *
from scipy.stats import qmc
from modify_input_template import *

#Fix broken -> 5.2, quantity -> 2500, loadingOrder -> 1

#   The function is used to filter plans that have big frequency differences.
def main():
    sampler = qmc.LatinHypercube(d=INPUT_DIMENSIONALITY)
    sample = sampler.random(n=NUMBER_OF_SAMPLES)
    sample = np.array(sample)

    temp_array = np.column_stack((np.ones(sample.shape[0]),2500*np.ones(sample.shape[0])))
    sample = np.column_stack((temp_array, sample))
    sample = np.column_stack((sample, 68.9*np.ones(sample.shape[0])))
    sample = np.hstack((sample[:,:4], 5.2*np.ones(sample.shape[0]).reshape(sample.shape[0],1), sample[:,4:]))

    screening_to_json(sample, TEMPLATE_FILE, json_folder_path=JSON_FOLDER_PATH,wipe = WIPE)
    screening_to_csv(sample, csv_file=CSV_FILE)
if __name__ == "__main__":
    main()

