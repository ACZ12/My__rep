from tkinter import *
root=Tk()

def func():
    print (checkbool.get())
    checkbool.set(False)
radiostr=StringVar()
checkbool=BooleanVar()
check=Checkbutton(root,text="Checkbutton",variable=checkbool,command=lambda:print(radiostr.get()))
check.pack()
radio1=Radiobutton(root,text="Checkbutton",value="A",command=func,variable=radiostr)
radio2=Radiobutton(root,text="Checkbutton",value="B",command=func,variable=radiostr)
radio1.pack()
radio2.pack()
root.mainloop()