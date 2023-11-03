import turtle
ablak=turtle.Screen()
ablak.bgcolor('lightgreen')
eszti=turtle.Turtle()
eszti.shape('turtle')
eszti.color('blue')

eszti.stamp()
for i in range(12):
    eszti.penup()
    eszti.forward(200)
    eszti.pendown()
    eszti.forward(30)
    eszti.penup()
    eszti.forward(30)
    eszti.stamp()
    eszti.goto(0,0)
    eszti.right(30)
