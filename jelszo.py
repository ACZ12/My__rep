import tkinter
canvas=tkinter.Canvas()
canvas.pack()

e=tkinter.Entry()
e.pack()

def check():
    eg=e.get()
    #import re
    password="bombokla"
    #regex="^[A-Z]{1}\w+\s[A-Z]{1}\w+$"
    #for attempt in passwords:
    #match=re.search(regex,attempt)
    if eg=="bombokla":
        print(f"Acess garnted. {eg}")
    else:
        print("Access denied.")

b=tkinter.Button(command=check)
b.pack()
canvas.mainloop()