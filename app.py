

import pyautogui
import time

distance = 100

while distance > 0:
    time.sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('s')
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen('Capture.png'))
    time.sleep(1)
    pyautogui.typewrite("a")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(pyautogui.locateCenterOnScreen('save.png'))
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen('Capture2.png'))
    time.sleep(2)
    pyautogui.click(pyautogui.locateCenterOnScreen('file.png'))
    time.sleep(2)
    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down'])
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
