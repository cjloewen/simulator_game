import sys
from io import StringIO
from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
from typing import Union, Dict


basicMovement: Dict["str", bool] = {
    "a" : False,
    "s" : False,
    "d" : False,
    "w" : False,
}

def setupInput():
    # Redirect sys.stdin to a dummy StringIO object
    sys.stdin = StringIO("")
    # ^ a cheap way of stopping user input from showing up on the cmdline
    listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
    listener.start()

def setTrue(key: Union[Key, KeyCode, None]):
    if isinstance(key, KeyCode):
        if key.char in basicMovement:
            basicMovement[key.char] = True
    print(basicMovement)

def setFalse(key: Union[Key, KeyCode, None]):
    if isinstance(key, KeyCode):
        if key.char in basicMovement:
            basicMovement[key.char] = False

def on_press(key: Union[Key, KeyCode, None]):
    try:
        setTrue(key)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key: Union[Key, KeyCode, None]):
    setFalse(key)
    if key == keyboard.Key.esc:
        return False




#keyboard.on_press_key("p", lambda _:print("You pressed p"))

