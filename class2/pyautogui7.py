import pyautogui
import time

def screen_search():
    time.sleep(2)
    screen1 = pyautogui.locateOnScreen("screen1.png")
    if screen1 is not None:
        x, y = pyautogui.center(screen1)
        pyautogui.click(x,y)
time.sleep(1)

screen_search()