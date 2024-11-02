import turtle
x = turtle.Pen()
x.color("blue")
x.speed(0)
length = 1
heading = 0
while length < 250:
    x.setheading(heading)
    heading = heading + 93
    x.forward(length)
    length = length + 2
turtle.mainloop()