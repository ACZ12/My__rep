import tkinter

canvas = tkinter.Canvas()

canvas.pack()


def rajzold_le(koorinatak):

    x=koorinatak.x

    y=koorinatak.y

    canvas.create_rectangle(x-40,y-30,x+40,y)

    canvas.create_rectangle(x-5,y,x+5,y+60)

    telepules=(entry1.get())

    athuzas=(entry2.get())
    
    canvas.create_text(x,y-15,text=telepules)

    if athuzas=='v' :
    
     canvas.create_line(x-40,y-30,x+40,y,width=3)

    

def torles():

    canvas.delete('all')

    

button1=tkinter.Button(text='Törlés', command=torles)

button1.pack()

entry1=tkinter.Entry()

entry1.pack()

entry2=tkinter.Entry()

entry2.pack()




canvas.bind('<Button-1>',rajzold_le)

canvas.mainloop()