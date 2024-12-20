# chatbot.py
import lib.roblox as roblox
import cv2
import pyautogui
import keyboard
import time
import dxcam
import pytesseract
import re
from configparser import ConfigParser

def splitAccordingly(text: str) -> list:
    pattern = r'\[([A-Za-z0-9_]+)\]: (/\w+)'
    return re.findall(pattern=pattern, string=text)

associate = {
    '/forward': 'forward',
    '/backward': 'backward',
    '/left': 'left',
    '/right': 'right',
    '/hi': 'hello',
    '/py': 'thon',
    '/help': 'Still Working on this.',
    '/test': '1, 2, 3... Testing'
}

AbsolutePathToTesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd=AbsolutePathToTesseract

roblox.Main.Character.resetCharacter()
roblox.Main.keyPress('/', 0.1, 'Roblox')
roblox.Main.keyPress('enter', 0.1, 'Roblox')

pathToTemplate = r'storage\Template.png'
pathToScreenshot = r'storage\screenshot.png'

coordinates = None
while coordinates is None:
    try: 
        coordinates = pyautogui.locateOnScreen(pathToTemplate) 
    except pyautogui.ImageNotFoundException:
        roblox.Main.Character.cameraZoom('out')

roblox.Main.Character.chat('!team set me Bot')
roblox.Main.Character.chat('/clear')
camera = dxcam.create()

while keyboard.is_pressed('l') == False:
    frame = camera.grab((0,25,coordinates[0]+coordinates.height,coordinates[1]))
    try:
        cv2.imwrite(pathToScreenshot, cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
    except:
        roblox.Main.Character.chat('Unable to take photo.')
        roblox.Main.Character.chat('/clear')
        continue
    result = pytesseract.image_to_string(pathToScreenshot, lang='eng')
    
    extracted = splitAccordingly(result)
    
    for username, command in extracted:
        for item in associate:
            if item == command:
                if associate[command] in roblox.directions:
                    roblox.Main.Movement.move(16,16,associate[item])
                    roblox.Main.Character.chat('/clear')
                else:
                    roblox.Main.Character.chat(associate[item])
                    roblox.Main.Character.chat('/clear')
            else:
                pass