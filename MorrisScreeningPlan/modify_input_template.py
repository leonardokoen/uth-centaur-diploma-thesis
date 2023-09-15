import json
import os
import stat
import shutil
import numpy as np
from settings import *

def new_grain_initial_conditions_json(template_file, json_folder_path,new_values, name_of_test):
    
    with open(template_file) as f:
        data = json.load(f)
    i = 0 
    for key, value in data['inputs']["maritimeParams"]["grainInitialConditions"][0].items():
        data['inputs']["maritimeParams"]["grainInitialConditions"][0][key] = new_values[i]
        i = i + 1

    data['inputs']["maritimeParams"]["vessel"] = name_of_test
    data['inputs']["maritimeParams"]["processed_vessel_name"] = name_of_test

    for i in range(0, len(new_values)):
        new_values[i] = str(new_values[i])

    name_of_json = name_of_test

    with open(json_folder_path + "{}".format(name_of_test)+'.json', 'w') as f:
        json.dump(data, f, indent = 2)

    os.chmod(json_folder_path + "{}".format(name_of_test) + '.json', stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)


def screening_to_json(screening_plan, template_file, json_folder_path, wipe = False ):
     
    if not os.path.exists(json_folder_path):
        while 1:
            answer = input(f"[{json_folder_path}] directory does not exist! Do you want to create it ?[Y/n]\n")
            answer = answer.lower()
            if answer == "yes" or answer == 'y':
                break
            elif answer == "no" or "n":
                raise RuntimeError
            else:
                print("Not a valid answer please respond with [Y/n]")
    
        os.makedirs(json_folder_path)

    if wipe:
        folder = json_folder_path
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    num_of_inputs = screening_plan.shape[0]
    for i in range(0, num_of_inputs):
        name_of_test = "test" + '_' + str(i)
        new_values = screening_plan[:][i]
        new_grain_initial_conditions_json(template_file, json_folder_path,new_values, name_of_test)        

def screening_to_csv(screening_plan, csv_file):
    np.savetxt(csv_file, np.column_stack((np.arange(0, screening_plan.shape[0]),screening_plan)),delimiter = ',',header='ID,loadingOrder,quantity,temp,mc,broken,damage,fermented,testWeight')
    # os.chmod("./SmartVesselHold/sensitivity_values.csv", stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)


