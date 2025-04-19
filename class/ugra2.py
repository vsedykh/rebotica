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

class Gamer2(Gamer):
    def __init__(self):
        super().__init__()
        self.id = calnmas.create_rectangle(780, 10, 790, 90, fill="red")
        self.sonik2y = 0
        self.speeeeeeeeed = 3
c1 = Gamer1
c2 = Gamer2
while True:
    jd.update()
    jd.update_idletasks()
    time.sleep(0.01)