import time
import pyautogui

time.sleep(4)
def dig(seconds):
    print("Начинаем копать...")
    pyautogui.mouseDown("Button1")
    time.sleep(5)
    print("Копание завершено!")
    pyautogui.mouseUp("Button1")

def action():
    print("Выполняется дополнительное действие.")
    pyautogui.keyDown("w")
    time.sleep(5)
    pyautogui.keyUp("w")

while True:
    dig(0.1)
    action()