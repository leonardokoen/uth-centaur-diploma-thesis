from time import sleep
import random


print("-----------------Initialising Simulation-----------------")

success = random.choices([True,False],weights=[40,10], k=1)
if success[0]:
    sleep(5)
    print("-----------------End Of Simulation-----------------")
else:
    raise RuntimeError("Simulation Failed")