import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas()
canvas.pack()

e1=tk.Entry()
e1.pack()
e2=tk.Entry()
e2.pack()

def udvozles():
    canvas.delete("all")
    kn=e1.get()
    vn=e2.get()
    canvas.create_text(50,30,text="Hello "+kn+" "+vn+"!")

b1=tk.Button(text="OK",command=udvozles)
b1.pack()



x,y=50,50
e3=tk.Entry()
e3.pack()


def mozgatas():
    global x
    m=int(e3.get())
    x+=m
    canvas.create_oval(x-5,y-5,x+5,y+5,tags="labda")
    
    
    


b2=tk.Button(text="Mozgatás",command=mozgatas)
b2.pack()


root.mainloop()

