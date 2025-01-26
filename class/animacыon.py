import time
from tkinter import *


jd = Tk()
jd.geometry("800x600")
jd.title("animacыon")
jd["bg"]="white"

calnmas = Canvas(jd, width=800, height=600, bg="white")
calnmas.pack()

sonikx = 4
sonik2y = 5
sonik3x = 6
sonik4y = 3


def draw():
    global  sonikx
    global  sonik2y
    global  sonik3x
    global  sonik4y
    e,r,t,y = calnmas.coords(vrach)
    b, a, s1, s2 = calnmas.coords(vrach2)
    if e <= -1:
        sonikx=-sonikx
    if t >= 800:
        sonikx=-sonikx
    if r <= -1:
        sonik2y=-sonik2y
    if y >= 600:
        sonik2y=-sonik2y
    if b <= -1:
        sonik3x=-sonik3x
    if s1 >= 800:
        sonik3x=-sonik3x
    if a <= -1:
        sonik4y=-sonik4y
    if s2 >= 600:
        sonik4y=-sonik4y
    calnmas.move(vrach, sonikx, sonik2y)
    calnmas.move(vrach2, sonik3x, sonik4y )



vrach = calnmas.create_oval(80, 80, 100, 100, fill="cyan2")
vrach2 = calnmas.create_oval(130, 80, 150, 100, fill="red")

while True:
    jd.update()
    jd.update_idletasks()
    draw()
    time.sleep(0.01)