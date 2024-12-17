# chatbot.py
import lib.roblox as roblox
import cv2
import pyautogui
import keyboard
import time
import dxcam
import pytesseract
import re

AbsolutePathToTesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd=AbsolutePathToTesseract

def split_text(input_text):
    # Use regex to extract components
    pattern = r"\[(.*?)\]:\s*(/\w+)\s*(\d+)"
    match = re.match(pattern, input_text)
    if match:
        return [match.group(1), match.group(2), match.group(3)]
    else:
        raise ValueError("Input text does not match the expected format")

roblox.Main.Character.resetCharacter()
roblox.Main.keyPress('/', 0.1, 'Roblox')

AbsolutePathToTemplate = r'storage\Template.png'
AbsolutePathToScreenshot = r'storage\screenshot.png'

coordinates = None
while coordinates is None:
    try: 
        coordinates = pyautogui.locateOnScreen(AbsolutePathToTemplate) 
    except pyautogui.ImageNotFoundException:
        roblox.Main.Character.cameraZoom('out')

roblox.Main.write('/clear')
roblox.Main.write('!team me Bot')
roblox.Main.write('/clear')
camera = dxcam.create()

while keyboard.is_pressed('l') == False:
    frame = camera.grab((0,25,coordinates[0]+coordinates.height,coordinates[1]))
    try:
        cv2.imwrite(AbsolutePathToScreenshot, cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
    except:
        roblox.Main.Character.chat('Unable to take photo.')
        continue
    result = pytesseract.image_to_string(AbsolutePathToScreenshot, lang='eng')
    
    if '/forward' in result:
        roblox.Main.Movement.move(16,16,'forward')
        roblox.Main.Character.chat('/clear')
    elif '/backward' in result:
        roblox.Main.Movement.move(16,16,'backward')
        roblox.Main.Character.chat('/clear')
    elif '/left' in result:
        roblox.Main.Movement.move(16,16,'left')
        roblox.Main.Character.chat('/clear')
    elif '/right' in result:
        roblox.Main.Movement.move(16,16,'right')
        roblox.Main.Character.chat('/clear')
