import tkinter

import random

canvas = tkinter.Canvas()

canvas.pack()

canvas.create_rectangle random.randint(0,500),random.randint(0,500)
