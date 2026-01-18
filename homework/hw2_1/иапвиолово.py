import  pyautogui
import time


time.sleep(5)
def open_chest_1():
    pyautogui.moveTo(1000, 500)
    pyautogui.click(button='right')


def transfer_items():
    item_position = (1050, 550)
    destination_position = (1150, 600)

    pyautogui.moveTo(item_position[0], item_position[1])
    time.sleep(0.5)

    for a in range(1):
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()
    time.sleep(0.2)

    while True:
        open_chest_1()
        transfer_items()
