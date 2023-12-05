from tkinter import *
root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

def negyzet(x,y,a1,a2):
    A,B,C,D=x,y,x+a1,y+a1
    canvas.create_rectangle(A,B,C,D,fill="indianred")
    canvas.create_rectangle(A+(a1-a2)/2,B+(a1-a2)/2,A+a1-(a1-a2)/2,B+a1-(a1-a2)/2,fill="lightblue")
    canvas.create_text(A,B,text="A")
    canvas.create_text(C,B,text="B")
    canvas.create_text(A,D,text="C")
    canvas.create_text(C,D,text="D")
    canvas.create_text(C,D/2,text=a1)
    canvas.create_text(A+a1/2,B+a1-(a1-a2)/2,text=a2)
negyzet(140,20,200,190)

root.mainloop()