import pyautogui
import time
from playsound import playsound

def screenshot(up,down,right,left):
    pyautogui.screenshot("screen4.png",region=(left,up,right,down))


def position():
    position = 1
    position2 = 2
    while position != position2 :
        position = pyautogui.position()
        time.sleep(0.5)
        position2 = pyautogui.position()
        if position == position2 :
            playsound("shot22.mp3")
            return position
        else:
            continue
position1 = position()
position2 = position()
shirina = position2[0] - position1[0]
visota = position2[1] - position1[1]
screenshot(position1[1],visota,shirina,position1[0])
