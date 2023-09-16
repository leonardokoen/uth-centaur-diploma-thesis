from SALib.analyze import morris
import SALib as sa
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import math
from settings import *
import seaborn as sns
import shutil


def plot_sensitivities(list, name):
    dict = {'Mu*': list[0], 'Sigma':list[1], 'Input':list[2], 'Day':list[3]}
    df = pd.DataFrame(dict)
    
    b = sns.scatterplot(data=df, x="Mu*", y="Sigma", hue = "Input", style = 'Day',size = 'Day',sizes=(20, 200), legend="full")
    b.axes.set_title(name,fontsize=20)
    plt.savefig(os.path.join(FIGURES_DIRECTORY, name + ".png"))
    plt.clf()
    
    return


def create_sensitivity_day(list_day, df_CO2, df_O2, df_T, df_Mould, df_Wg, df_DamageHeat, problem):
    day_array = np.array(list_day) + 3

    X_CO2 = df_CO2.iloc[:, :4].to_numpy()
    X_O2 = df_O2.iloc[:, :4].to_numpy()
    X_T = df_T.iloc[:, :4].to_numpy()
    X_Mould = df_Mould.iloc[:, :4].to_numpy()
    X_Wg = df_Wg.iloc[:, :4].to_numpy()
    X_DamageHeat = df_DamageHeat.iloc[:, :4].to_numpy()
    CO2 = [[],[],[],[]]
    O2 = [[],[],[],[]]
    T = [[],[],[],[]]
    Mould = [[],[],[],[]]
    Wg = [[],[],[],[]]
    DamageHeat = [[],[],[],[]]

    for day_new in day_array:
        Y_CO2=df_CO2.iloc[:, day_new].to_numpy()
        Si_CO2 = morris.analyze(problem, X_CO2, Y_CO2, conf_level=0.95,num_levels=LEVEL_OF_DESCRITIZATION)
        mu_CO2 = Si_CO2['mu_star']
        sigma_CO2 = Si_CO2['sigma']
        for i,mu in enumerate(mu_CO2):
            CO2[0].append(mu)
            CO2[1].append(sigma_CO2[i])
            CO2[2].append(problem['names'][i])
            CO2[3].append(day_new-3)

        Y_O2=df_O2.iloc[:, day_new].to_numpy()
        Si_O2 = morris.analyze(problem, X_O2, Y_O2, conf_level=0.95,num_levels=LEVEL_OF_DESCRITIZATION)
        mu_O2 = Si_O2['mu_star']
        sigma_O2 = Si_O2['sigma']
        for i,mu in enumerate(mu_O2):
            O2[0].append(mu)
            O2[1].append(sigma_O2[i])
            O2[2].append(problem['names'][i])
            O2[3].append(day_new-3)

        Y_T=df_T.iloc[:, day_new].to_numpy()
        Si_T = morris.analyze(problem, X_T, Y_T, conf_level=0.95,num_levels=LEVEL_OF_DESCRITIZATION)
        mu_T = Si_T['mu_star']
        sigma_T = Si_T['sigma']
        for i,mu in enumerate(mu_T):
            T[0].append(mu)
            T[1].append(sigma_T[i])
            T[2].append(problem['names'][i])
            T[3].append(day_new-3)
        

        Y_Mould=df_Mould.iloc[:, day_new].to_numpy()
        Si_Mould = morris.analyze(problem, X_Mould, Y_Mould, conf_level=0.95,num_levels=LEVEL_OF_DESCRITIZATION)
        mu_Mould = Si_Mould['mu_star']
        sigma_Mould = Si_Mould['sigma']
        for i,mu in enumerate(mu_Mould):
            Mould[0].append(mu)
            Mould[1].append(sigma_Mould[i])
            Mould[2].append(problem['names'][i])
            Mould[3].append(day_new-3)
        
        Y_Wg=df_Wg.iloc[:, day_new].to_numpy()
        Si_Wg = morris.analyze(problem, X_Wg, Y_Wg, conf_level=0.95,num_levels=LEVEL_OF_DESCRITIZATION)
        mu_Wg = Si_Wg['mu_star']
        sigma_Wg = Si_Wg['sigma']
        for i,mu in enumerate(mu_Wg):
            Wg[0].append(mu)
            Wg[1].append(sigma_Wg[i])
            Wg[2].append(problem['names'][i])
            Wg[3].append(day_new-3)

        Y_DamageHeat=df_DamageHeat.iloc[:, day_new].to_numpy()
        Si_DamageHeat = morris.analyze(problem, X_DamageHeat, Y_DamageHeat, conf_level=0.95,num_levels=LEVEL_OF_DESCRITIZATION)
        mu_DamageHeat = Si_DamageHeat['mu_star']
        sigma_DamageHeat = Si_DamageHeat['sigma']
        for i,mu in enumerate(mu_DamageHeat):
            DamageHeat[0].append(mu)
            DamageHeat[1].append(sigma_DamageHeat[i])
            DamageHeat[2].append(problem['names'][i])
            DamageHeat[3].append(day_new-3)

    
    plot_sensitivities(CO2, "CO2")
    plot_sensitivities(O2, "O2")
    plot_sensitivities(T, "T")
    plot_sensitivities(Mould, "Mould")
    plot_sensitivities(Wg, "Moisture Content")
    plot_sensitivities(DamageHeat, "DamageHeat")

    return



def main():
    df_CO2 = pd.read_csv(MORRIS_FINAL_CSV_FILE_CO2)
    df_O2 = pd.read_csv(MORRIS_FINAL_CSV_FILE_O2)
    df_T = pd.read_csv(MORRIS_FINAL_CSV_FILE_T)
    df_Mould = pd.read_csv(MORRIS_FINAL_CSV_FILE_MOULD)
    df_Wg = pd.read_csv(MORRIS_FINAL_CSV_FILE_MC)
    df_DamageHeat = pd.read_csv(MORRIS_FINAL_CSV_FILE_DAMHEAT)
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    if os.path.exists(FIGURES_DIRECTORY):
        shutil.rmtree(FIGURES_DIRECTORY)
        
    os.makedirs(FIGURES_DIRECTORY)
    create_sensitivity_day(LIST_OF_DAYS, df_CO2, df_O2, df_T, df_Mould, df_Wg, df_DamageHeat, PROBLEM)
    return



if __name__ == "__main__":
    main()