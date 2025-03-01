import time
import random
from tkinter import *
from tkinter.colorchooser import *

jd = Tk()
jd.geometry("1800x1600")
jd.title("anime")
jd["bg"]="white"
color = "cyan2"

calnmas = Canvas(jd, width=800, height=600, bg="white")
calnmas.grid(row= 0,column= 0,rowspan= 7)

DEDEDE = []

calnmas.create_rectangle(0, 180, 40, 200, fill="black")
calnmas.create_rectangle(0, 230, 40, 250, fill="black")


def shot():
    global DEDEDE
    vrach = calnmas.create_oval(5, 205, 25, 225, fill=color)
    dfdjg = (vrach, 10, random.random())
    DEDEDE.append(dfdjg)
    jd.after(50, shot)



def retyuioo(event):
    jd.bind_all("<c>", )
    global color
    fdhzgs = askcolor()
    color = fdhzgs[1]
    return
jd.bind_all("<c>", retyuioo)

def draw():
    for sdf in DEDEDE:
        r = sdf[0]
        er = sdf[1]
        error = sdf[2]
        e,i,t,y = calnmas.coords(r)
        if t >=800:
            calnmas.delete(r)
            DEDEDE.remove(sdf)
        calnmas.move(r,er, error)
def WTFakt():
    for i in range(4):
        shot()
btn = Button(jd, text="OGONY", font=(None, 20),command=shot)
btn.grid(row=1, column=1)
while True:
    jd.update()
    jd.update_idletasks()
    draw()
    time.sleep(0.01)