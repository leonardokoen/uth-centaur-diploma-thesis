import pandas as pd
import os 
import re


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)


def prepare_final_csv(input_path, X_path):

    filename = ["output_CO2.csv", "output_DamageHeat.csv", "output_Mould.csv", "output_O2.csv", "output_T.csv", "output_Wg.csv"]
    df_CO2 = df_DamageHeat = df_Mould = df_O2 = df_T = df_Wg = []
    dataframes = [[],[],[], [], [],[]]
    list_dir = sorted_alphanumeric(os.listdir(input_path))

    for dir in list_dir:
        dir_path = os.path.join(input_path, dir)
        for file in filename:
            file_path = os.path.join(dir_path, file)
            df = pd.read_csv(file_path, header = None)
            if file == filename[0]:
                dataframes[0].append(df.iloc[:,1])
            elif file == filename[1]:
                dataframes[1].append(df.iloc[:,1])
            elif file == filename[2]:
                dataframes[2].append(df.iloc[:,1])
            elif file == filename[3]:
                dataframes[3].append(df.iloc[:,1])
            elif file == filename[4]:
                dataframes[4].append(df.iloc[:,1])
            elif file == filename[5]:
                dataframes[5].append(df.iloc[:,1])

    df_CO2 = pd.concat(dataframes[0], axis=1)
    column_names = []
    for i in range(0, df_CO2.shape[1]):
        name = "test_" + str(i)
        column_names.append(name)
    df_CO2.columns = column_names
    df_DamageHeat = pd.concat(dataframes[1], axis=1)
    df_DamageHeat.columns = column_names
    df_Mould = pd.concat(dataframes[2], axis=1)
    df_Mould.columns = column_names
    df_O2 = pd.concat(dataframes[3], axis=1)
    df_O2.columns = column_names
    df_T = pd.concat(dataframes[4], axis=1)
    df_T.columns = column_names 
    df_Wg = pd.concat(dataframes[5], axis=1)
    df_Wg.columns = column_names


    df_X = pd.read_csv(X_path)
    # df_X = df_X.head(60)

    df_CO2X = pd.concat([df_X, df_CO2.T], axis=1).reindex(df_X.index)
    df_CO2X.iloc[:, 9:] = df_CO2.T.iloc[:, :]
    df_CO2X = df_CO2X.drop(columns = ['loadingOrder', 'quantity', 'broken', 'testWeight', '# ID'])

    df_DamageHeatX = pd.concat([df_X, df_DamageHeat.T], axis=1).reindex(df_X.index)
    df_DamageHeatX.iloc[:, 9:] = df_DamageHeat.T.iloc[:, :]
    df_DamageHeatX = df_DamageHeatX.drop(columns = ['loadingOrder', 'quantity', 'broken', 'testWeight',  '# ID'])

    df_MouldX = pd.concat([df_X, df_Mould.T], axis=1).reindex(df_X.index)
    df_MouldX.iloc[:, 9:] = df_Mould.T.iloc[:, :]
    df_MouldX = df_MouldX.drop(columns = ['loadingOrder', 'quantity', 'broken', 'testWeight', '# ID'])

    df_O2X = pd.concat([df_X, df_O2.T], axis=1).reindex(df_X.index)
    df_O2X.iloc[:, 9:] = df_O2.T.iloc[:, :]
    df_O2X = df_O2X.drop(columns = ['loadingOrder', 'quantity', 'broken', 'testWeight', '# ID'])

    df_TX = pd.concat([df_X, df_T.T], axis=1).reindex(df_X.index)
    df_TX.iloc[:, 9:] = df_T.T.iloc[:, :]
    df_TX = df_TX.drop(columns = ['loadingOrder', 'quantity', 'broken', 'testWeight', '# ID'])

    df_WgX = pd.concat([df_X, df_Wg.T], axis=1).reindex(df_X.index)
    df_WgX.iloc[:, 9:] = df_Wg.T.iloc[:, :]
    df_WgX = df_WgX.drop(columns = ['loadingOrder', 'quantity', 'broken', 'testWeight', '# ID'])

    return(df_CO2X, df_DamageHeatX, df_MouldX , df_O2X, df_TX, df_WgX)



def df_save(df1, df2, df3, df4, df5, df6, path):
    df1.to_csv(os.path.join(path, "final_CO2.csv"), index = False)
    df2.to_csv(os.path.join(path, "final_DamageHeat.csv"), index = False)
    df3.to_csv(os.path.join(path, "final_Mould.csv"), index = False)
    df4.to_csv(os.path.join(path, "final_O2.csv"), index = False)
    df5.to_csv(os.path.join(path, "final_T.csv"), index = False)
    df6.to_csv(os.path.join(path, "final_Wg.csv"), index = False)