import turtle
i = turtle.Pen()
rtyyyyy = turtle.Screen()
rtyyyyy.setup(1000,800)
i.speed(0)
rtyyyyy.bgcolor("black")
rtyyyyy.title("спераль")
qrweqrwrweqrw = ["white"]
for rtyu in range(10000000000):
    i.pencolor(qrweqrwrweqrw[rtyu%1])
    i.circle(100)
    i.penup()
    i.forward(rtyu*1)
    i.pendown()
    i.left(34)
turtle.mainloop()