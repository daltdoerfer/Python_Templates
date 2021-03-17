# in command prompt, type "pip install pynput" to install pynput.
# https://pynput.readthedocs.io/en/latest/keyboard.html

from pynput import keyboard
from pynput.keyboard import Key, Controller, Listener

keyboard = Controller()

key = "a"

keyboard.press(key)
keyboard.release(key)


