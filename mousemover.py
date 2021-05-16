import pyautogui as gui
import win32api
from time import sleep
savedpos = win32api.GetCursorPos()

def actions():
    print(gui.size())
    while True:
        gui.move(0, 3)
        sleep(0.5)
        gui.move(4, 0)
        cond()


def cond():
    count = 0
    while True:
        savedpos = win32api.GetCursorPos()
        sleep(0.5)
        curpos = win32api.GetCursorPos()
        if savedpos == curpos:
            savedpos = curpos
            print("Cursor is on this position for" (count+1)/2, " seconds.")
            count += 1
            if count >= 20:  # if count is greater than 60 it means timeout will occur after mouse is steady for more than
                # 240 seconds i.e. 4 minutes. (approx.)
                print("You are AFK for 5 minutes, moving cursor for few pixels")
                actions()
                break
            else:
                pass
        else:
            print("Mouse is currently moving")
            count = 0

cond()
