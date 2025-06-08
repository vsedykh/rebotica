import turtle
import random

i = turtle.Pen()
o = turtle.Screen()
o.setup(1000,800)
i.shape("arrow")

o.title("Фейерверки")
o.bgcolor("darkblue")
i.speed(0)
i.up()
i.goto(random.randint(-500,500),-390)
i.down()
i.left(90)

size = 100

c = ["red","orange","yellow","green","blue","purple"]

for e in range(52):
    i.forward(6)
    i.up()
    i.forward(6)
    i.down()
    random.choice(c)

for q in range(5):
    i.forward(size)
    i.right(144)
    i.begin_fill()
    i.fillcolor()
    i.end_fill()

turtle.mainloop()