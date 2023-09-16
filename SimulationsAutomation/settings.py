#Simulation Script
SCRIPT = './SimulationsAutomation/sleep_simulation.py'

#The folder with all JSON files
# !!! DO NOT FORGET TO PUT FRONTSLASH AT THE END !!! 
INPUT_FOLDER = './SimulationsAutomation/test/test_json_full/'

#Simulation log file
LOG_FILE = './SimulationsAutomation/test/simulation_log'

#Simulation time log file
TIME_LOG_FILE = "./SimulationsAutomation/test/simulation_time_log"

#The maximum simulations that will be performed everytime you call the script.
THRESHOLD = 5

#True : keep the default behaviour and continue simulations accordind to the log file 
RANGE_FROM_DEFAULT = True

#If RANGE_FROM_DEFAULT = False you should indicate from which simulation you want to start.
RANGE_FROM = 15