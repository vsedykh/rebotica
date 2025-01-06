from tkinter import *
from tkinter.colorchooser import *
tkck = Tk()
tkck.geometry("1800x800")
tkck.title("Alle")
tkck["bg"] = "red"
callllllllllvas = Canvas(tkck,width=1600,height=400,bg="white")
callllllllllvas.grid(row= 0,column= 0,rowspan= 7)
stateeeeeee = "c"
brush = 10
color = "red"
def chose(input):
    global stateeeeeee, brush
    if input=="+" and brush<1000000000000000:
        brush += 2
        label.configure(text=brush)
        return
    if input=="-" and brush>0:
        brush -= 2
        label.configure(text=brush)
        return
    stateeeeeee = input
def paint(event):
    if event.widget.__class__!=callllllllllvas.__class__:
        return
    if stateeeeeee=="s":
        callllllllllvas.create_rectangle(event.x - brush, event.y - brush, event.x + brush, event.y + brush, fill=color,outline=color)
    elif stateeeeeee=="c":
        callllllllllvas.create_oval(event.x - brush, event.y - brush, event.x + brush, event.y + brush, fill=color,outline=color)
    elif stateeeeeee=="l1":
        callllllllllvas.create_line(event.x - brush, event.y - brush, event.x + brush, event.y + brush, fill=color)
    elif stateeeeeee=="l2":
        callllllllllvas.create_line(event.x + brush, event.y - brush, event.x - brush, event.y + brush, fill=color)

def ask__color(event):
    tkck.bind_all("<c>", )
    global color
    fdhzgs= askcolor(title="выберите цвет")
    color =fdhzgs[1]
    return

def clear(event):
    tkck.bind_all("<BackSpace>", callllllllllvas.delete("all"))
    return

tkck.bind_all("<1>", paint)
tkck.bind_all("<B1-Motion>", paint)
tkck.bind_all("<BackSpace>", clear)
tkck.bind_all("<c>", ask__color)

def fg (event):
    callllllllllvas.create_oval(event.x - brush*2, event.y - brush*2, event.x + brush*2, event.y + brush*2, fill="white",outline="white")
    return
tkck.bind_all("<3>", fg)
tkck.bind_all("<B3-Motion>", fg)

btn1 = Button(tkck, text="🟥", font=(None, 20),command=lambda: chose("s"))
btn1.grid(row=0,column=1)
btn2 = Button(tkck, text="🔴", font=(None, 20),command=lambda: chose("c"))
btn2.grid(row=1,column=1)
btn3 = Button(tkck, text=" ↘ ", font=(None, 20),command=lambda: chose("l1"))
btn3.grid(row=2,column=1)
btn4 = Button(tkck, text=" ↙ ", font=(None, 20),command=lambda: chose("l2"))
btn4.grid(row=3,column=1)
btn5 = Button(tkck, text="➕", font=(None, 20),command=lambda: chose("+"))
btn5.grid(row=4,column=1)
btn6 = Button(tkck, text="➖", font=(None, 20),command=lambda: chose("-"))
btn6.grid(row=5,column=1)
label = Label(tkck,text=brush, fg=color, font=(None, 20))
label.grid(row=6, column=1)
tkck.mainloop()