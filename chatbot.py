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

associate = {
    '/forward': 'forward',
    '/backward': 'backward',
    '/left': 'left',
    '/right': 'right',
    '/hi': 'hello',
    '/py': 'thon',
    '/help': 'Still working on this.'
}

AbsolutePathToTesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd=AbsolutePathToTesseract
config = '--oem 3 --psm %d' % 13

def split_text(input_text: str) -> list:
    # Use regex to extract components
    pattern = r"\[(.*?)\]:\s*(/\w+)\s*(\d+)"
    match = re.match(pattern, input_text)
    if match:
        return [match.group(1), match.group(2), match.group(3)]
    else:
        raise ValueError("Input text does not match the expected format")

roblox.Main.Character.resetCharacter()
roblox.Main.keyPress('/', 0.1, 'Roblox')

pathToTemplate = r'storage\Template.png'
pathToScreenshot = r'storage\screenshot.png'

coordinates = None
while coordinates is None:
    try: 
        coordinates = pyautogui.locateOnScreen(pathToTemplate) 
    except pyautogui.ImageNotFoundException:
        roblox.Main.Character.cameraZoom('out')

roblox.Main.Character.chat('!team me Bot')
roblox.Main.Character.chat('/clear')
camera = dxcam.create()

while keyboard.is_pressed('l') == False:
    frame = camera.grab((0,25,coordinates[0]+coordinates.height,coordinates[1]))
    try:
        cv2.imwrite(pathToScreenshot, cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
    except:
        roblox.Main.Character.chat('Unable to take photo.')
        continue
    result = pytesseract.image_to_string(pathToScreenshot, lang='eng')
    print(result)
    
    try:
        extractedList = split_text(str(result))
    except ValueError:
        print('Result is probably empty.')
        continue
    
    if extractedList[1] in associate:
        if extractedList[1] in roblox.directions:
            roblox.Main.Movement.move(int(extractedList[2])*2,16,associate[extractedList[1]])
            roblox.Main.Character.chat('/clear')
        else:
            roblox.Main.Character.chat(extractedList[1])