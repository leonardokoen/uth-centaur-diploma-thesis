import os
from output_collection import *
from output_to_median import *
from prepare_final_csv import *
from handling_outliers import *
from settings import *

def create_direcory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

def main():
    
    cases_folder_path = CASES_FOLDER_PATH
    sensitivity_csv_path = SENSITIVITY_CSV_PATH

    csv_folder_path = CSV_FOLDER_PATH
    create_direcory(csv_folder_path)

    csv_median_folder_path = CSV_MEDIAN_FOLDER_PATH
    create_direcory(csv_median_folder_path)

    csv_final_path = CSV_FINAL_PATH
    create_direcory(csv_final_path)
    

    print("Collecting probes output...")
    output_collection(0, cases_folder_path, csv_folder_path)
    print("Done\n")

    print("Finding the median of the height for each day...")
    csv_to_median(csv_folder_path, csv_median_folder_path)
    print("Done\n")
    
    print("Preparing final csv files...")
    df_1, df_2, df_3, df_4, df_5, df_6 = prepare_final_csv(csv_median_folder_path, sensitivity_csv_path)
    print("Done\n")

    df_save(df_1, df_2, df_3, df_4, df_5, df_6, csv_final_path)
    
    print("Replacing outliers with max values...")
    handle_outliers(csv_final_path)
    print("Done\n")

    
    return

if __name__ == "__main__":
    main()