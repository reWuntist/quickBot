import pyautogui
import pydirectinput
import time
import keyboard
import webbrowser
import pygetwindow as gw

directions = {
    'forward': 'w',
    'backward': 's',
    'left': 'a',
    'right': 'd'
}

def windowActivate(window, extra=None):
    try:
        win = gw.getWindowsWithTitle(window)[0]
        win.activate()
    except IndexError:
        print(f'{window} is not open on the device/account.')

    win.maximize()
def getActiveWindow():
    activeWindow = gw.getActiveWindow()
    if activeWindow:
        return activeWindow
    else:
        return None

class Main:
    def keyPress(keyToPress, delay, window='Roblox'):
        windowActivate('Roblox')
        pydirectinput.keyDown(keyToPress)
        time.sleep(delay)
        pydirectinput.keyUp(keyToPress)
    def write(text):
        windowActivate('Roblox')
        keyboard.write(f'{text}   ', 0.01)
    class Movement:
        def move(studs, walkspeed, direction):
            timetoWalk = studs/walkspeed
            if direction in directions:
                Main.keyPress(directions[direction], timetoWalk)
    class Character:
        def resetCharacter():
            Main.keyPress('esc', 0)
            Main.keyPress('r', 0)
            Main.keyPress('enter', 0)
        def cameraZoom(direction):
            if direction == 'in':
                Main.keyPress('i', 0)
            if direction == 'out':
                Main.keyPress('o', 0)
        def cameraMove(direction):
            if direction == 'left':
                Main.keyPress('.', 0)
            if direction == 'right':
                Main.keyPress(',', 0)
        def chat(message):
            Main.keyPress('/',0.1)
            Main.write(message)
            Main.keyPress('enter',0.1)
    class Game:
        def joinGame(id):
            webbrowser.open(f'roblox://placeId={id}')