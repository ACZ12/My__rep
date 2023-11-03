import turtle
ablak=turtle.Screen()
t=turtle.Turtle()
t.speed(0)
t.penup()
t.setpos(-400,0)
t.pendown()
a=-400

for i in range(40):
    for i in range(36):
        t.fd(20)
        t.rt(10)
    t.rt(20)
    t.stamp()
    a=a+20
    t.penup()
    t.goto(a,0)
    t.pendown()
