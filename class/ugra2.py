from tkinter import *
import time
from playsound import playsound


jd = Tk()
jd.geometry("1080x800")
jd.title("PONG")

calnmas = Canvas(jd, width=1080, height=800, bg="black")
calnmas.pack()

records = open("records.ini","r+")
data = records.readline()
if data == '':
    h = 0
    records.write(f'{h}')
    records.close()
else:
    h = int(data)
score = 0
score2 = calnmas.create_text(390,20,text=f'wscore {score}',fill="brown",font=("pixel",45))
calnmas.create_text(390,56,text=f'world record {h}',fill="brown",font=("pixel",45))
class Gamer:
    def __init__(self):
        self.id = None
        self.sonik2y = None
    def draw (self):
        _,r, _, y = calnmas.coords(self.id)
        if r <= 0 or y >= 1800:
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
            self.sonik2y = 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
c1 = Gamer1()
c2 = Gamer2()
jd.bind_all("<KeyPress>",c1.movi_drs)
jd.bind_all("<KeyPress>",c2.movi_drs2,add="+")
jd.bind_all("<KeyRelease>",c1.anti_movi_drs)
jd.bind_all("<KeyRelease>",c2.anti_movi_drs2,add="+")


class Balllllllllllllllllllllllllllllllllll:
    def __init__(self):
        super().__init__()
        self.id2 = calnmas.create_oval(40,20,70,50,fill="red")
        self.sonik2y = 1
        self.speeeeeeeeed = 1
    def draw(self):
        global score
        calnmas.move(self.id2, self.speeeeeeeeed, self.sonik2y)
        e, r, t, y = calnmas.coords(self.id2)
        if r <= 0 or y >= 800:
            self.sonik2y = - self.sonik2y
        if e <= 0 or t >= 1080:
            return True
        q, w ,u ,j = calnmas.coords(c1.id)
        m, i, o, p = calnmas.coords(c2.id)
        if r > w and y < j and e <= u:
            self.speeeeeeeeed -= 2.20
            playsound("pong.mp3", block=False)
            self.speeeeeeeeed = - self.speeeeeeeeed
            score += 1
            calnmas.itemconfig(score2, text=f'score {score}')

        if r > i and y < p and t >= m:
            self.speeeeeeeeed += 2.20
            playsound("pong.mp3", block=False)
            self.speeeeeeeeed = - self.speeeeeeeeed
            score += 1
            calnmas.itemconfig(score2,text=f'score {score}')

c3 = Balllllllllllllllllllllllllllllllllll()


while True:
    jd.update()
    jd.update_idletasks()
    c1.draw()
    c2.draw()
    lives = c3.draw()
    if lives:
        break
    time.sleep(0.01)

records = open("records.ini","r+")
data = records.readline()
if int(data) < score:
    records.truncate(0)
    records.seek(0)
    records.write(f'{score}')
records.close()