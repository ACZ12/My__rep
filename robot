import tkinter
canvas=tkinter.Canvas()
canvas.pack()


class Robot:
    def intro(self):
        canvas.create_text(200,20,text="hello i'm %s, i'm %s and i'm %.2f kg." %(self.name,self.color,self.weight))
        canvas.create_text(200,40,text="who are you?")
        e=tkinter.Entry()
        e.pack()
        eg=e.get()
        def intro2():
            canvas.create_text(200,80,text=f"hello arnold, my name is {eg}")
        b=tkinter.Button(text="send",command=intro2)
        b.pack()
    
global eg
objec=Robot()
objec.name="Arnold"
objec.color="green"
objec.weight=32
objec.intro()

canvas.mainloop()