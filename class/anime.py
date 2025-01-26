import time
import random
from tkinter import *


jd = Tk()
jd.geometry("800x600")
jd.title("anime")
jd["bg"]="white"

calnmas = Canvas(jd, width=800, height=600, bg="white")
calnmas.pack()

DEDEDE = []

calnmas.create_rectangle(0, 180, 40, 200, fill="black")
calnmas.create_rectangle(0, 230, 40, 250, fill="black")


def shot():
    global DEDEDE
    vrach = calnmas.create_oval(5, 205, 25, 225, fill="cyan2")
    dfdjg = (vrach, 10, random.random())
    DEDEDE.append(dfdjg)
    jd.after(50, shot)

def draw():
    for sdf in DEDEDE:
        r = sdf[0]
        er = sdf[1]
        error = sdf[2]
        e,r,t,y = calnmas.coords(r)
        if t >=800:
            print("fgfjhx")
            calnmas.delete(r)
            DEDEDE.remove(sdf)
        calnmas.move(r,er, error)
shot()
while True:
    jd.update()
    jd.update_idletasks()
    draw()
    time.sleep(0.01)