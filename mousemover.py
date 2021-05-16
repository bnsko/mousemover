import pyautogui as gui
import win32api
from time import sleep
savedpos = win32api.GetCursorPos()

def eksn():
    while True:
        gui.move(2, 2)
        sleep(0.2)
        gui.move(-2, -2)
        nomove()

def nomove():
    count = 0
    while True:
        savedpos = win32api.GetCursorPos()
        sleep(1)
        curpos = win32api.GetCursorPos()
        if savedpos == curpos:
            savedpos = curpos
            print("You did not move the cursor for" ,(count+1), " seconds.")
            count += 1
            if count >= 240: 
                print("You are AFK for 4 minutes, moving cursor for few pixels.")
                eksn()
                break
            else:
                pass
        else:
            print("Mouse is currently moving")
            count = 0

nomove()
