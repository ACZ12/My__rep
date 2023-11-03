import tkinter
canvas=tkinter.Canvas()
canvas.pack()



e=tkinter.Entry()
e.insert(1,"neved")
e.pack()
e2=tkinter.Entry()
e2.insert(1,"korod")
e2.pack()

def n():
    r=e.get()
    canvas.delete("all")
    canvas.create_text(50,10,text="csa %s" %str(r))
    
def k():
    t=e2.get()
    canvas.delete("all")    
    canvas.create_text(50,10,text="korod: %d" %int(r))
    
    
b=tkinter.Button(text="tovább",command=n)
b.pack()


canvas.mainloop()