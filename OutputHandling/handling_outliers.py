import os
import pandas as pd
from settings import *



def handle_outliers(folder_path):
    filenames = ['final_CO2.csv','final_O2.csv','final_T.csv','final_Mould.csv','final_Wg.csv','final_DamageHeat.csv']
    max_CO2 = CO2
    min_O2 = O2
    max_T = TEMP
    max_Mould = MOULD
    max_Wg = WG
    max_DamageHeat = DAM_HEAT
    for file in filenames:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        len_rows = df.shape[0]
        len_cols = df.shape[1]

        if file == filenames[0]:
            for i in range(0,len_rows):
                for j in range(4, len_cols):
                    if df.iloc[i,j] > max_CO2 or pd.isna(df.iloc[i,j]):
                        df.iloc[i,j] = max_CO2
        
        elif file == filenames[1]:
            for i in range(0,len_rows):
                for j in range(4, len_cols):
                    if df.iloc[i,j] < min_O2 or pd.isna(df.iloc[i,j]):
                        df.iloc[i,j] = min_O2
        elif file == filenames[2]:
            for i in range(0,len_rows):
                for j in range(4, len_cols):
                    if df.iloc[i,j] > max_T or pd.isna(df.iloc[i,j]):
                        df.iloc[i,j] = max_T
        elif file == filenames[3]:
            for i in range(0,len_rows):
                for j in range(4, len_cols):
                    if df.iloc[i,j] > max_Mould or pd.isna(df.iloc[i,j]):
                        df.iloc[i,j] = max_Mould

        elif file == filenames[4]:
            for i in range(0,len_rows):
                for j in range(4, len_cols):
                    if df.iloc[i,j] > max_Wg or pd.isna(df.iloc[i,j]):
                        df.iloc[i,j] = max_Wg
        elif file == filenames[5]:
            for i in range(0,len_rows):
                for j in range(4, len_cols):
                    if df.iloc[i,j] > max_DamageHeat or pd.isna(df.iloc[i,j]):
                        df.iloc[i,j] = max_DamageHeat

        df.to_csv(file_path, index=False)
    return
