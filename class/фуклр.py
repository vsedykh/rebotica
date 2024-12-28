from tkinter import *
tkck = Tk()
tkck.geometry("600x400")
tkck.title("Alle")
tkck["bg"] = "red"
callllllllllvas = Canvas(tkck,width=540,height=400,bg="white")
callllllllllvas.grid(row= 0,column= 0,rowspan= 7)
stateeeeeee = "circle"
def chose(input):
    global stateeeeeee
    stateeeeeee = input

btn = Button(tkck, text="🟥", font=(None, 20),command=lambda:chose("square"))
btn.grid(row=0,column=1)
btn = Button(tkck, text="🟥", font=(None, 20),command=lambda:chose("square"))
btn.grid(row=1,column=1)
btn = Button(tkck, text="🟥", font=(None, 20))
btn.grid(row=2,column=1)
btn = Button(tkck, text="🟥", font=(None, 20))
btn.grid(row=3,column=1)
tkck.mainloop()