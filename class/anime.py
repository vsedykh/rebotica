import time
from tkinter import *


jd = Tk()
jd.geometry("800x600")
jd.title("anime")
jd["bg"]="white"

calnmas = Canvas(jd, width=800, height=600, bg="white")
calnmas.pack()

sonikx = 4
sonik2y = 5
sonik3x = 6
sonik4y = 3
sonik5x = 7
sonik6y = 2

calnmas.create_rectangle(0, 180, 40, 200, fill="black")
calnmas.create_rectangle(0, 250, 40, 270, fill="black")

def draw():
    global sonikx
    global sonik2y
    global sonik3x
    global sonik4y
    global sonik5x
    global sonik6y
    e,r,t,y = calnmas.coords(vrach)
    b, a, s1, s2 = calnmas.coords(vrach2)
    w,f,s,d = calnmas.coords(vrach3)

    if e <= -1:
        sonikx=-sonikx
    if t >= 800:
        sonikx=-sonikx
    if r <= -1:
        sonik2y=-sonik2y
    if y >= 800:
        sonik2y=-sonik2y
    if b <= -1:
        sonik3x=-sonik3x
    if s1 >= 800:
        sonik3x=-sonik3x
    if a <= -1:
        sonik4y=-sonik4y
    if s2 >= 800:
        sonik4y=-sonik4y
    if w <= -1:
        sonik5x=-sonik5x
    if s >= 800:
        sonik5x=-sonik5x
    if f <= -1:
        sonik6y=-sonik6y
    if d <= 800:
        sonik6y=-sonik6y
    calnmas.move(vrach, sonikx, sonik2y)
    calnmas.move(vrach2, sonik3x, sonik4y)
    calnmas.move(vrach3, sonik5x, sonik6y)


vrach = calnmas.create_oval(80, 80, 100, 100, fill="cyan2")
vrach2 = calnmas.create_oval(130, 80, 150, 100, fill="red")
vrach3 = calnmas.create_oval(123, 80, 100, 321, fill="orange")

while True:
    jd.update()
    jd.update_idletasks()
    draw()
    time.sleep(0.01)