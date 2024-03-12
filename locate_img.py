from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


while True:
    try:
        if pyautogui.locateOnScreen("ema.jpg", confidence=0.8) is not None:
            print("I can see")
        else:
            print("I cannot see")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen")

    time.sleep(0.5)