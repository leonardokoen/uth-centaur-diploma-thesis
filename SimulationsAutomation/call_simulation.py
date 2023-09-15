import os
import re
import sys
import time
from settings import *


# Build the command that you would like.
#If python3 does not work return this command 
#"python " + simulation_script + " " + simulation_input_folder + new_name + " keep_locally"
def build_path_input(new_name, simulation_script, simulation_input_folder):
    
    return "python3 " + simulation_script + " " + simulation_input_folder + new_name + " keep_locally"
    # return "python ./scripts/run_marine_simulation.py ./SmartVesselHold/Latin_Hypercube/latin_hypercube_json/" + new_name + " keep_locally"

def lastWord(string):
    lis = list(string.split(" "))
    length = len(lis)
    return (lis[length-1])

def file_name(string):
    lis = list(string.split(" "))
    return(lis[2])

def wipe_log_file(simulation_log_file):
    print("Perform Wiping")
    f = open(simulation_log_file, 'r+')
    f.truncate(0)
    f.close()
    print("PRESS 0, If you want to start simulations from the beginning or from the specified RANGE_FROM")
    print("PRESS 1, If you want to end the script")
    simulation_after_wiping_flag = int(input())
    if simulation_after_wiping_flag == True:
        return(-1)
    else:
        return(0)


def simulation_log_intepreter(simulation_log_file):
    
    if os.path.getsize(simulation_log_file) != 0:
        with open(simulation_log_file, 'r') as file:
            for line in file:
                pass
            last_line = line

        if lastWord(last_line)=="FAILED":
            last_file_name = file_name(last_line)
            file_number = re.findall(r'\d+', last_file_name)
            return(int(file_number[0]))

        elif last_line == "END OF SIMULATIONS\n":
            print("WIPE or change the default behaviour of RANGE_FROM")
            return(-1)

        else:    
            print(last_line)
            print("Something is wrong with the simulation_log file" )
            return(-1) 
            
    else:
        return(0)

def perform_simulations(json_files, range_from, threshold,simulation_log_file, simulation_script, simulation_input_folder, time_log_file):

    if range_from == -1:
        return

    with open(simulation_log_file, 'a') as f:
            
        if range_from == 0:
            print("START SIMULATIONS")
        else:
            f.write('\n')
            print("CONTINUE SIMULATIONS FROM SIMULATION no.{}".format(range_from))

        counter = 0
        for i in range(range_from, len(json_files)):

            command = build_path_input(json_files[i], simulation_script, simulation_input_folder)
            print(command)
            #error = os.system("python ./SmartVesselHold/scripts/sleep_simulation.py")
            if counter < threshold:
                start = time.time()
                error = os.system(command)
                if error == 0:
                    end = time.time()
                    with open(time_log_file, "a") as file:
                        file.write(json_files[i]+ ' ' + str(end-start) + "\n")

                    f.write("SIMULATION WITH " + json_files[i] + " STATUS: SUCCESS\n")
                else :
                    f.write("SIMULATION WITH " + json_files[i] + " STATUS: FAILED")
                    break
            else: 
                print(f"Reached Maximum Simulations: Threshold = {threshold}")
                f.write("SIMULATION WITH " + json_files[i] + " STATUS: FAILED")
                break
            if i == len(json_files)-1:
                f.write('\nEND OF SIMULATIONS\n')
            counter += 1 



def main():
    
    simulation_script = SCRIPT
    simulation_input_folder = INPUT_FOLDER
    simulation_log_file = LOG_FILE
    time_log_file = TIME_LOG_FILE
    threshold = THRESHOLD

    #python call_simulation.py -w to wipe the log_file
    try:
        arg = sys.argv[1]

        while 1:
            if "-w" == arg.lower():
                wipe = 1
                print("Press ENTER to wipe LOG_FILE OR Ctrl + C ")
                input()
                break
            else:
                print(f"{arg} is not a valid argument.")
                while 1:
                    answer = input("Continue with the default behaviour? [Y/n]\n")
                    answer = answer.lower()
                    if answer == "yes" or answer == 'y':
                        wipe = 0
                        break
                    elif answer == "no" or "n":
                        arg = input("New argument(-w): ")
                        break
                    else:
                        print("Not a valid answer please respond with [Y/n]")
    except:
        wipe = 0

    

    #Check the existance of simulation_log_file
    if not os.path.exists(simulation_log_file):
        while 1:
            answer = input(f"[{simulation_log_file}] file does not exist! Do you want to create it ?[Y/n]\n")
            answer = answer.lower()
            if answer == "yes" or answer == 'y':
                break
            elif answer == "no" or "n":
                print("Provide the file that you would like and rerun the script")
                return
            else:
                print("Not a valid answer please respond with [Y/n]")
                
        permissions = 0o600
        file_descriptor = os.open(simulation_log_file, os.O_CREAT | os.O_WRONLY, permissions)
        os.close(file_descriptor)

    #Check the existance of time_log_file
    if not os.path.exists(time_log_file):
        while 1:
            answer = input(f"[{time_log_file}] file does not exist! Do you want to create it ?[Y/n]\n")
            answer = answer.lower()
            if answer == "yes" or answer == 'y':
                break
            elif answer == "no" or "n":
                print("Provide the file that you would like and rerun the script")
                return
            else:
                print("Not a valid answer please respond with [Y/n]")
                
        permissions = 0o600
        file_descriptor = os.open(time_log_file, os.O_CREAT | os.O_WRONLY, permissions)
        os.close(file_descriptor)

    # RANGE FROM
    # From which file in simulation_input_folder simulations will start
    # This line will read the log file and it will start from the last failed simulation

    if wipe :
        range_from = wipe_log_file(simulation_log_file)
        if range_from != -1 and not RANGE_FROM_DEFAULT:
            range_from = RANGE_FROM
    else:
        if not RANGE_FROM_DEFAULT :
            range_from = RANGE_FROM
        else:
            range_from = simulation_log_intepreter(simulation_log_file)

    #Uncomment this line to change manually the number of the file you want to start the simulations from. 
    # range_from = 0

    # THRESHOLD
    #How many simulations will be performed everytime you call the script
    

    # Read and sort the names of the files in simulation_input_folder
    json_files = os.listdir(simulation_input_folder)
    json_files = sorted(json_files, key=lambda s: int(re.search(r'\d+', s).group()))

    perform_simulations(json_files, range_from, threshold, simulation_log_file, simulation_script, simulation_input_folder, time_log_file)    

    return 


if __name__ == "__main__":
    main()
