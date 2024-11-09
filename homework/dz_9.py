import turtle
x = turtle.Pen()
rgiuhler = turtle.Screen()
x.color("white")
rgiuhler.setup(1000,800)
rgiuhler.title("Ракушка")
x.speed(0)
rgiuhler.bgcolor("black")
length = 100
heading = 0
while length > 0:
    x.setheading(heading)
    heading = heading - 5
    x.circle(length)
    length = length - 2
turtle.mainloop()