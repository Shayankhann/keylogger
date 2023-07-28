#from pynput.mouse import Controller
from pynput.keyboard import Controller
#(left to right, top to bottom)
#(from top left of screen)

def controlMouse():
    mouse = Controller()
    mouse.position = (10,20)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("Hello again")


controlKeyboard()