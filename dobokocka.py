import tkinter as tk
from random import *
window = tk.Tk()
window.attributes('-fullscreen', True)
window.title("Kockapóker")
canvas=tk.Canvas(window,height=800,width=800)
canvas.pack()



l=[]
def negyzet(x,y):
    global l
    l=[]
    for i in range(5):
        szam=randrange(1,7)
        canvas.create_rectangle(x-10, y-10, x+10, y+10,fill="white",outline="white")
        canvas.create_rectangle(x-10, y-10, x+10, y+10)
        canvas.create_text(x, y, text=szam)
        x+=50
        l.append(szam)

    print(l)
    




def button2_klikk():
        negyzet(100,100)

        

button1 = tk.Button(text='Dobás', command=button2_klikk)
button1.pack()

x=80
y=367

canvas.create_text(140,500,text="Tetszoleges \nkombinacio\n\nPár\n\nDrill\n\nKét pár\n\nKis póker\n\nFull\n\nKis sor\n\nNagy sor\n\nNagy póker")
for i in range(6):
        for i in range(9):
                canvas.create_rectangle(x,y,x+120,y+30)
                y+=30
        x+=120
        y=367

def hozzaad():
       x=250
       for i in range(6):
        canvas.create_text(x,s[i],text=f"{l[i]}")
        x+=120

s=[]
for i in range(9):
        b1=tk.Button(text="Hozzáadás",command=hozzaad)
        b1.place(x=350,y=y)
        s.append(y)
        y+=30



window.mainloop()

