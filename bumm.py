import tkinter,random
canvas=tkinter.Canvas(width=400)
canvas.pack()

def animacio():
    global x1, x2
    canvas.delete('all')
    x1=x1+random.randint(5,10)
    x2=x2-random.randint(5,10)
    canvas.create_oval(x1-5,200,x1+5,210,fill='blue')
    canvas.create_oval(x2-5,200,x2+5,210,fill='red')
    if x1+5>=x2-5:
        canvas.create_text(x1,190,text='BUMM')
    else:
        canvas.after(100,animacio)

x1=0
x2=400
animacio()
canvas.mainloop()