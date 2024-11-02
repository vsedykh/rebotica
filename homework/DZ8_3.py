import turtle
x = turtle.Pen()
x.color("red")
x.speed(0)
heading = 0
while heading < 360:
    x.setheading(heading)
    heading = heading + 10
    x.circle(100)
turtle.mainloop()