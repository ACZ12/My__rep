from tkinter import *
from ttkbootstrap import *

root = Window(themename="darkly")
root.geometry("500x300")

l = []

def create():
    entry = Entry(frame)
    entry.pack(side=BOTTOM)
    l.append(entry)

def szam():
    values = [entry.get() for entry in l]
    # Convert the input values to floats and handle non-numeric input
    try:
        values = [float(value) for value in values]
        average = sum(values) / len(values)
        lambdal= [abs(average-value) for value in values]
        lambdalavg=sum(lambdal) / len(lambdal)
        result=(lambdalavg/average)*100
        print("Relatív hiba: %.2f"%result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

frame = Frame(root)
button = Button(frame, text="Érték hozzáadása", command=create)
button.pack(side=BOTTOM)
frame.grid(row=0, column=0)

szamitas = Button(frame, text="Számítás", command=szam)
szamitas.pack(side=RIGHT)

root.mainloop()
