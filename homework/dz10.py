from tkinter import *
import random
tkck = Tk()
tkck.geometry("600x400")
tkck.title("Alle")
tkck["bg"] = "red"
def game(input):
    r = random.randint(1,4)
    print(r)
    if r == input:
        text1 = Label(tkck,text="ты угадал :)",font=("Sand cherif",12,"bold"),fg="grey1",bg="darkgrey")
        text1.grid(row=1,column=0)
    else:
        text1 = Label(tkck,text="ты не угадал :(",font=("Sand cherif",12,"bold"),fg="grey1",bg="darkgrey")
        text1.grid(row=1,column=0)

btn = Button(tkck, text="1", font=(None, 20),command=lambda:game(1))
btn.grid(row=0,column=0)
btn = Button(tkck, text="2", font=(None, 20),command=lambda:game(2))
btn.grid(row=0,column=1)
btn = Button(tkck, text="3", font=(None, 20),command=lambda:game(3))
btn.grid(row=0,column=2)
btn = Button(tkck, text="4", font=(None, 20),command=lambda:game(4))
btn.grid(row=0,column=3)
tkck.mainloop()