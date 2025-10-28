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

turtle.tracer(1,0)

def fill():
    c = ["red","orange","yellow","green","blue","purple"]
    i.begin_fill()
    i.fillcolor(random.choice(c))
    size = 100
    for q in range(5):
        i.forward(size)
        i.right(144)
    i.end_fill()


while True:
    for e in range(52):
        i.forward(6)
        i.up()
        i.forward(6)
        i.down()
    fill()
    i.up()
    i.goto(random.randint(-500,500),-390)
    i.down()



turtle.mainloop()