import multiprocessing
import time
import keyboard
# need this to basically put keystrokes on a stack that is taken care of every refresh, also, need it to "clean the stack every so often"
# either that or find different functions, as me hitting a once caused it to print out many more times.
def listen_for_keystrokes():
    while True:
        try:
            if keyboard.is_pressed('q'):  # Check if 'q' is pressed
                print("You pressed 'q'. Exiting listener...")
                break  # Exit on 'q' key press
            elif keyboard.is_pressed('a'):  # Check if 'a' is pressed
                print("You pressed 'a'")
        except Exception as e:
            print(f"Error: {e}")
            break

# Function for the main loop
def ticker(refresh_rate: float):
    while True:
        print("No")
        time.sleep(refresh_rate)  # Control the loop's refresh rate
        

def main():
    # Define the refresh rate (in seconds)
    refresh_rate = 1

    # Start the main loop in a separate process
    main_process = multiprocessing.Process(target=ticker, args=(refresh_rate,))
    main_process.start()

    # Start the secondary process
    secondary = multiprocessing.Process(target=listen_for_keystrokes)
    #secondary.daemon = True
    secondary.start()
    
    main_process.join()


if __name__ == "__main__":
    main()
    