import tkinter
root=tkinter.Tk()
canvas=tkinter.Canvas(root,width=1000)
import random
canvas.pack()

e='red','green','blue','yellow','brown'

def mozdony(x,y):
    canvas.create_rectangle(x,y,x+80,y+20,fill=random.choice(e),tags="vonat")
    canvas.create_rectangle(x,y+20,x+40,y-30,fill=random.choice(e),tags="vonat")
    canvas.create_rectangle(x+5,y-40,x+15,y-30,fill=random.choice(e),tags="vonat")
    canvas.create_oval(x,y+10,x+30,y+40,fill='black',tags="vonat")
    canvas.create_oval(x+30,y+10,x+60,y+40,fill='black',tags="vonat")
    canvas.create_oval(x+60,y+10,x+90,y+40,fill='black',tags="vonat")






def kocsi(x,y):
    canvas.create_rectangle(x,y,x+80,y+60,fill=random.choice(e),tags="vonat")
    canvas.create_rectangle(x+5,y+5,x+35,y+35,fill='lightblue',tags="vonat")
    canvas.create_rectangle(x+45,y+5,x+75,y+35,fill='lightblue',tags="vonat")
    canvas.create_oval(x+5,y+50,x+35,y+80,fill='black',tags="vonat")
    canvas.create_oval(x+45,y+50,x+75,y+80,fill='black',tags="vonat")
    canvas.create_line(x+80,y+40,x+90,y+40,width=5,tags="vonat")




def animacio():
    global x
    canvas.delete('all')
    x=x+10
    mozdony(x,y+40)
    for i in range(1,4):
        kocsi(x-i*90,y)
    canvas.after(100,animacio)
    if x>1300:
        x=0

x=10
y=90
animacio()
canvas.mainloop()