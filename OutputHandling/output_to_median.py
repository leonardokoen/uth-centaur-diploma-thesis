import os
import pandas as pd
import stat
import csv

def csv_to_median(input_path, output_path):
    for root, dirs, files in os.walk(input_path):
        components_of_root = root.split('/')
        last_folder = components_of_root[-1]
        create_output_path = output_path + "/" + last_folder
        if not os.path.exists(create_output_path):
            os.makedirs(create_output_path)
            os.chmod(create_output_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        
        for file in files:
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(create_output_path, file)
            if not os.path.exists(output_file_path):
                with open(output_file_path, 'w+') as f:
                    pass
            df = pd.read_csv(input_file_path)
            days_median = []
            for index, row in df.iterrows():
                row_median = df.iloc[index, 1:21].median()
                days_median.append([index + 1,row_median])

            with open(output_file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(days_median)
            
    return