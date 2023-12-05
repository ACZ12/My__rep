from tkinter import *
from random import *
root=Tk()
root.geometry("1500x500")
canvas=Canvas(root,width=500,height=500)
canvas2=Canvas(root,width=500,height=500)
canvas3=Canvas(root,width=500,height=500)
canvas.place(x=0,y=0)
canvas2.place(x=500,y=0)
canvas3.place(x=1000,y=0)


[canvas.create_line(i,0,i,randrange(20,70),width=3,fill="green") for i in range(0,500,3)]
[canvas.create_line(i,500,i,randrange(430,480),width=3,fill="green") for i in range(0,500,3)]
for i in range(randrange(20)):
    x=randrange(500)
    y=randrange(70,330)
    r=randrange(20,100)
    canvas.create_oval(x,y,x+r,y+r,fill="blue",outline="blue")
canvas.create_line(0,300,500,300,fill="brown",width=3)
canvas.create_line(0,350,500,350,fill="brown",width=3)
[canvas.create_line(i,300,i,350,fill="brown",width=3) for i in range(0,500,30)]

[canvas2.create_line(0,0,randrange(100),randrange(100),fill="yellow") for i in range(40)]
canvas2.create_line(0,500,500,500,fill="green",width=30)
[canvas2.create_line(i,450,i,500,fill="green",width=3) for i in range(0,500,10)]
canvas2.create_rectangle(100,350,130,450,fill="brown")
canvas2.create_arc(50, 300, 180, 400, start=0, extent=180, fill="red")
canvas2.create_oval(100,320,110,330,fill="white")
canvas2.create_oval(70,330,80,340,fill="white")
canvas2.create_oval(130,325,140,335,fill="white")
[canvas2.create_oval(350-i,150-i,350+i,150+i,outline="blue",width=3) for i in range(10,100,10)]
[[canvas2.create_rectangle(i,j,i+randrange(50),j+randrange(50)) for i in range(250,500,50)] for j in range(250,500,50)]

def virag(x,y):
    canvas3.create_line(x,y,x,y+50,width=3,fill="green")
    [canvas3.create_line(x,y+50,x+randrange(-20,20),y+50-randrange(40),width=3,fill="green") for i in range(20)]
    [canvas3.create_line(x,y,x+randrange(-40,40),y+randrange(-40,40),width=3,fill="yellow") for i in range(40)]

def fa(x,y):
    canvas3.create_line(x,y,x,y+150,width=5,fill="brown")
    [canvas3.create_line(x,y+50,x+randrange(-40,40),y+50-randrange(40),width=2,fill="brown") for i in range(10)]

[virag(randrange(500),randrange(500)) for i in range(20)]
[fa(randrange(500),randrange(500)) for i in range(20)]



root.mainloop()