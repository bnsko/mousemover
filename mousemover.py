import pyautogui as gui
import win32api
from time import sleep
savedpos = win32api.GetCursorPos()

def actions():
    print(gui.size())
    while True:
        gui.move(0, 1)
        sleep(0.2)
        gui.move(2, 0)
        cond()


def cond():
    count = 0
    while True:
        savedpos = win32api.GetCursorPos()
        sleep(0.5)
        curpos = win32api.GetCursorPos()
        if savedpos == curpos:
            savedpos = curpos
            print("Cursor is on this position for" ,(count+1)/2, " seconds.")
            count += 1
            if count >= 240: 
                print("You are AFK for 4 minutes, moving cursor for few pixels")
                actions()
                break
            else:
                pass
        else:
            print("Mouse is currently moving")
            count = 0

cond()
