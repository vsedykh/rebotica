from tkinter import *
import time

jd = Tk()
jd.geometry("800x600")
jd.title("PONG")

calnmas = Canvas(jd, width=800, height=600, bg="black")
calnmas.pack()

class Gamer:
    def __init__(self):
        self.id = None
        self.sonik2y = None
    def draw (self):
        _,r, _, y = calnmas.coords(self.id)
        if r <= 0 or y >= 600:
            self.sonik2y = 0
        else:
            calnmas.move(self.id, 0, self.sonik2y)
class Gamer1(Gamer):
    def __init__(self):
        super().__init__()
        self.id = calnmas.create_rectangle(10, 10 ,20 ,90,fill="red")
        self.sonik2y = 0
        self.speeeeeeeeed = 3
    def movi_drs(self,event):
        if event.keysym == "w":
            self.sonik2y = - self.speeeeeeeeed
        if event.keysym == "s":
            self.sonik2y = self.speeeeeeeeed
    def anti_movi_drs(self,event):
        if event.keysym in "ws":
            self.sonik2y = 0
class Gamer2(Gamer):
    def __init__(self):
        super().__init__()
        self.id = calnmas.create_rectangle(780, 10, 790, 90, fill="red")
        self.sonik2y = 0
        self.speeeeeeeeed = 3

    def movi_drs2(self,event):
        if event.keysym == "Up":
            self.sonik2y = - self.speeeeeeeeed
        if event.keysym == "Down":
            self.sonik2y = self.speeeeeeeeed
    def anti_movi_drs2(self,event):
        if event.keysym in ["Up","Down"]:
            self.sonik2y = 0
c1 = Gamer1()
c2 = Gamer2()
jd.bind_all("<w>")
jd.bind_all("<s>")
jd.bind_all("<Up>")
jd.bind_all("<Down>")


class Balllllllllllllllllllllllllllllllllll:
    def __init__(self):
        super().__init__()
        self.id2 = calnmas.create_oval(456,90,90,456,fill="red")
        self.sonik2y = None
        self.speeeeeeeeed = 3
c3 = Balllllllllllllllllllllllllllllllllll()
while True:
    jd.update()
    jd.update_idletasks()
    time.sleep(0.01)