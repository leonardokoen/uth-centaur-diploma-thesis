import os
import re
from settings import *

def create_output_path(test_number, path, output_path_template):
    parts = re.split(r'\d+', output_path_template, maxsplit=1)
    return path + parts[0] + str(test_number) + parts[1]

def create_folder_path(test_number, path):
    return path + "output_test_" + str(test_number) + "/"


def output_collection(from_range, cases_folder_path, csv_folder_path):

    list_of_names = ['CO2','DamageHeat', 'Mould', 'O2', 'T', 'Wg']
    

    number_of_files = len(next(os.walk(cases_folder_path))[1])

    for i in range(from_range, number_of_files):

        output_path = create_output_path(i, cases_folder_path, CASE_PATH_TEMPLATE)
        folder_path = create_folder_path(i, csv_folder_path)

        try:
            os.mkdir(folder_path)
        except:
            pass

        for name in list_of_names:

            with open(output_path + name, 'r') as f:

                lines = f.readlines()

            list_to_csv = []

            for i in range (26,len(lines)):
                list_to_csv.append(','.join(lines[i].split()))
            list_to_csv[0] = "Time" + list_to_csv[0][7:]
            list_to_csv.pop(1)

            with open(folder_path + "output_" + name + '.csv', 'w+') as f:
                for line in list_to_csv:
                    f.write(line + "\n")
    return