import turtle
ablak=turtle.Screen()
ablak.title("Pong játék")
ablak.bgcolor("black")
ablak.setup(width=800,height=600)
ablak.tracer(0)
    
#pontszám
ps_a=0    
ps_b=0

#ütő A
uto_a=turtle.Turtle()
uto_a.speed(0)
uto_a.shape("square")
uto_a.color("white")
uto_a.shapesize(stretch_wid=5,stretch_len=1)
uto_a.penup()
uto_a.goto(-350,0)

#ütő B
uto_b=turtle.Turtle()
uto_b.speed(0)
uto_b.shape("square")
uto_b.color("white")
uto_b.shapesize(stretch_wid=5,stretch_len=1)
uto_b.penup()
uto_b.goto(350,0)

#labda
labda=turtle.Turtle()
labda.speed(0)
labda.shape("square")
labda.color("white")
labda.penup()
labda.goto(0,0)
labda.dx=0.3
labda.dy=-0.3

#toll
toll=turtle.Turtle()
toll.speed(0)
toll.color("white")
toll.penup()
toll.hideturtle()
toll.goto(0,260)
toll.write("Játékos A: 0  Játékos B: 0",align="center",font=("Courier",24,"normal"))




#funkció
def uto_a_fel():
    y=uto_a.ycor()
    y+=20
    uto_a.sety(y)
    
def uto_a_le():
    y=uto_a.ycor()
    y-=20
    uto_a.sety(y)
    
def uto_b_fel():
    y=uto_b.ycor()
    y+=20
    uto_b.sety(y)
    
def uto_b_le():
    y=uto_b.ycor()
    y-=20
    uto_b.sety(y)
    
#billentyűzet kötés
ablak.listen()
ablak.onkeypress(uto_a_fel,"w")
ablak.onkeypress(uto_a_le,"s")
ablak.onkeypress(uto_b_fel,"Up")
ablak.onkeypress(uto_b_le,"Down  ")



#fő játékhurok
while True:
    ablak.update()
    
    #labdamozgatás
    labda.setx(labda.xcor()+labda.dx)
    labda.sety(labda.ycor()+labda.dy)
    
    #határérzéklés
    if labda.ycor()>290:
        labda.sety(290)
        labda.dy*=-1
        
    if labda.ycor()<-290:
        labda.sety(-290)
        labda.dy*=-1
        
    if labda.xcor()>390:
        labda.goto(0,0)
        labda.dx*=-1
        ps_a+=1  
        toll.clear()    
        toll.write("Játékos A: {}  Játékos B: {}".format(ps_a,ps_b),align="center",font=("Courier",24,"normal"))
    
    if labda.xcor()<-390:
        labda.goto(0,0)
        labda.dx*=-1  
        ps_b+=1  
        toll.clear()
        toll.write("Játékos A: {}  Játékos B: {}".format(ps_a,ps_b),align="center",font=("Courier",24,"normal"))
        
    #ütő és labda ütközése
    if (labda.xcor() > 340 and labda.xcor() < 350) and (labda.ycor() < uto_b.ycor()+40 and labda.ycor() > uto_b.ycor()-40):
        labda.setx(340)
        labda.dx*=-1     
        
    if (labda.xcor() < -340 and labda.xcor() > -350) and (labda.ycor() < uto_a.ycor()+40 and labda.ycor() > uto_a.ycor()-40):
        labda.setx(-340)
        labda.dx*=-1     
        