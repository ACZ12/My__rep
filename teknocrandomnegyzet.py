import turtle
import random
ablak=turtle.Screen()
eszti=turtle.Turtle()
eszti.shape('arrow')

a=random.randrange(20,300)
b=random.randrange(20,300)

for i in range(4):
    eszti.forward(a)
    eszti.right(90)

eszti.left(random.randrange(0,270))
eszti.forward(random.randrange(20,300))

for i in range(4):
    eszti.forward(b)
    eszti.right(90)
