from tkinter import *

root = Tk()
root.geometry("600x4000")
root.title("Окошко")
root["bg"] = 'green'
def test():
   text1 = Text(width=25, height=5, bg='darkgreen', fg='white', wrap=WORD)
   text2 = Text(width=25, height=5, bg='darkgrey', fg='white', wrap=WORD)
   text3 = Text(width=25, height=5, bg='darkblue', fg='white', wrap=WORD)
   text1.grid(row=1, column=1)
   text2.grid(row=1, column=2)
   text3.grid(row=1, column=3)
   # text.destroy()


btn = Button(root, text="Press me!𓁈", font=("Algerian", 0), command=test)
btn.grid(row=2, column=2)


root.mainloop()