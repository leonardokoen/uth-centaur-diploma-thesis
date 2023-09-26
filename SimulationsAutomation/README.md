# Simulation Automation

## Pyhton Files

- call_simulation.py
- settings.py
- sleep_simulation.py

## Folders

- test
- test/test_json

## Settings

- <span style="color:#7CB9E8">SCRIPT</span> : The script that you want to call many times.
- <span style="color:#7CB9E8">INPUT_FOLDER</span> : The directory where you have all your test json files.
- <span style="color:#7CB9E8">LOG_FILE</span> : A text file that keeps track of the simulations.
- <span style="color:#7CB9E8">TIME_LOG_FILE</span> : A text file that keeps track of the time of the simulations
- <span style="color:#7CB9E8">THRESHOLD</span> : The maximum simulations you want to perform
- <span style="color:#7CB9E8">RANGE_FROM_DEFAULT</span> : A boolean flag that enables the default behaviour, if True: 

        Read from the LOG_FILE and continue execution from the last failed simulation. 
    
    if False:
        
        The user is responsible to provide RANGE_FROM

- <span style="color:#7CB9E8">RANGE_FROM</span> : This setting is used only when the RANGE_FROM_DEFAULT == False. The user should specify from which test the script will continue the simulations.

## Sleep Simulation

A test simulation that performs sleep for 5 seconds. It has 0.8 chance to be successful and 0.2 chance to raise RuntimeError.

## Call Simulation

This is the main script of the automation it combines all the settings and perform simulations. The status of the simulation is updated in the LOG_FILE, if the simulation was successful or if the simulation failed.

If you call again the script after a failed simulation the execution will continue automatically starting from the failed simulation, except if RANGE_FROM_DEFAULT == False, where the script will start from the RANGE_FROM simulation.

The script stops if a simulation fails or if the last simulation is successful or if it reaches the THRESHOLD number of simulations.

If you want to wipe the LOG_FILE you can call

```bash
python call_simulation -w
```

If the LOG_FILE or TIME_LOG_FILE do not exist the script will ask you if you want to create them.

**WARNING**

Never change LOG_FILE by hand. Only through the script functionalities.

## Test Files

Test file names should have a name and a number. The numbering of the files should start from 0.

**Valid Example 1**:

    test_0.json
    test_1.json 
    test_2.json

**Valid Example 2**:

    test_0.json
    test_01.json
    test2.json
The way you write numbers does not effect the execution nor if they are seperated with underscore or not.

**Valid Example 3**:

    first_0.json
    second_1.json
    third_2.json

The names do not effect the execution if the numbering is valid.

**Invalid Example 1**:

    test_1.json
    test_2.json
    test_3.json

The numbering should start from 0.

**Invalid Example 2**:

    t2st_0.json
    test_1.json
    test_2.json

The interpeter will use the first number that it finds so the names should not have a number.

**Invalid Example 3**:

    test_0.json
    test_4.json
    test_10.json

Numbers should be consecutive.

## Change Command

You can change default command

```bash
python3 simulation_script simulation_input_folder/test.json keep_locally
```

from call_simulation.py build_path_input function.