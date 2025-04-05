import multiprocessing
import time

from interface.controller import Controller
from input_test import basicMovement
# need this to basically put keystrokes on a stack that is taken care of every refresh, also, need it to "clean the stack every so often"
# either that or find different functions, as me hitting a once caused it to print out many more times.
import input_test

# Function for the main loop
def ticker(refresh_rate: float, control: Controller):
    while True:
        # read keystrokes
        control.moveMainCharacter(basicMovement)
        # update game
        control.tick()
        # print the game
        control.printConsole()
        time.sleep(refresh_rate)  # Control the loop's refresh rate
        
def printer(refresh_rate: float, control: Controller):
    while True:
        print("No")
        time.sleep(refresh_rate)  # Control the loop's refresh rate
    
def main():
    control: Controller = Controller()
    # Define the refresh rate (in seconds)
    refresh_rate = 1
    input_test.setupInput()
    # Start the main loop in a separate process
    tickProcess = multiprocessing.Process(target=ticker, args=(refresh_rate, control))
    tickProcess.start()
    # Start the secondary process
    # printProcess = multiprocessing.Process(target=printer, args=(refresh_rate, control))
    # printProcess.daemon = True
    # printProcess.start()
    
    tickProcess.join()


if __name__ == "__main__":
    main()
    