import pyautogui as cursor
import win32api
from time import sleep
save_pos = win32api.GetCursorPos()

def eksn():
    while True:
        x, y = win32api.GetCursorPos()
        cursor.moveTo(1, 1)
        sleep(0.1)
        cursor.click()
        sleep(0.1)
        win32api.SetCursorPos((x, y))
        donotmove()

def donotmove():
    count = 0
    while True:
        save_pos = win32api.GetCursorPos()
        sleep(1)
        current_pos = win32api.GetCursorPos()
        if save_pos == current_pos:
            save_pos = current_pos
            print("You did not move the cursor for" ,(count+1), " seconds.")
            count += 1
            if count >= 5: 
                print("You are AFK for 4 minutes, moving cursor for few pixels.")
                eksn()
                break
            else:
                pass
        else:
            print("Mouse is currently moving")
            count = 0

donotmove()
