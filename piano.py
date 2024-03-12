from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 1- 817, 590
# 2- 900, 590
# 3- 992, 590
# 4- 1075, 590
while keyboard.is_pressed("q") == False:

    if pyautogui.pixel(817, 590)[0] == 0:
        click(817, 590)

    if pyautogui.pixel(900, 590)[0] == 0:
        click(900, 590)

    if pyautogui.pixel(990, 590)[0] == 0:
        click(990, 590)

    if pyautogui.pixel(1075, 590)[0] == 0:
        click(1075, 590)
