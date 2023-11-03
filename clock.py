from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from time import *
import locale
import turtle

window = Tk()
canvas = Canvas(window, height=1000, width=1500)
canvas.pack()
t = turtle.RawTurtle(canvas)
t.penup()
t.speed(0)
t.hideturtle()




def open_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((canvas.winfo_width(), canvas.winfo_height()))
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(-750, -500, anchor=tk.NW, image=img_tk, tag="image")
    canvas.img = img_tk

current_image_index = 0

def update():
    locale.setlocale(locale.LC_TIME, 'sk_SK')
    time_string = strftime("%I:%M:%S %p", localtime())
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)
    day_string = strftime("%A")
    day_label.config(text=day_string)
    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    canvas.tag_raise("image")
    window.after(1000, update)

time_label = Label(window, font=("Italic", 50, "bold"))
time_label.place(x=0, y=900)
day_label = Label(window, font=("Italic", 30, "bold"))
day_label.place(x=0, y=850)
date_label = Label(window, font=("Italic", 30, "bold"))
date_label.place(x=0, y=800)

ysav = 585

#black
def centrumc():  
    global brod, brdo  
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo=Button(window,text='do Kolónia',command=centrum)
    brod=Button(window,text="do Centrum",command=centrumr)
    brdo.place(x=500,y=500)
    brod.place(x=1000,y=500)

 

    
def centrum():
    brdo.destroy()
    brod.destroy()
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 920:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    
    move_rectangle()  # Start the rectangle movement
    image_paths = ["HMD_Center.png", "HMD_Doh..png", "HMD_Kolonia.png"]
    open_image(image_paths[0])
    window.after(1000, lambda: open_next_image(image_paths[1], 1000))
    def open_next_image(image_path, delay):

        open_image(image_path)
        if image_path == image_paths[1]:
            window.after(delay, lambda: open_next_image(image_paths[2], 1000))
    current_image_index = 0
    t.goto(-50, -450)
    t.write("Hajnáčka Centrum -  Hajnáčka do Centrum  - 4 minúty\nHajnáčka Centrum - Hajnáčka Doh.  - 8 minút\nHajnáčka Centrum - Hajnáčka do Ostrá skala   - 15 minút\nHajnáčka Centrum - Hajnáčka do Doh.  - 16 minút\nHajnáčka Centrum - Hajnáčka do Kolónia  - 20 minúty\nHajnáčka Centrum - Hajnáčka Kolónia  - 23 minút\nHajnáčka Centrum - Hajnáčka Kolónia do Pose  - 27 minút", font=("Italic",20,"bold"))

def centrumr():
    brdo.destroy()
    brod.destroy()
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 920:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    
    move_rectangle()  # Start the rectangle movement
    image_paths = ["HMD_Kolonia.png","HMD_Doh..png","HMD_Center.png"]
    open_image(image_paths[0])
    window.after(1000, lambda: open_next_image(image_paths[1], 1000))
    def open_next_image(image_path, delay):
        open_image(image_path)
        if image_path == image_paths[1]:
            window.after(delay, lambda: open_next_image(image_paths[2], 1000))
    current_image_index = 0
    canvas.create_text(900, 835, text="Hajnáčka Kolónia do Pose -Hajnáčka Kolónia - 27 minút\nHajnáčka Kolónia - do Kolónia - 23 minút\nHajnáčka do Kolónia - Hajnáčka do Doh. - 20 minúty\nHajnáčka do Doh.  - do Ostrá skala - 16 minút\nHajnáčka do Ostrá skala - Hajnáčka Doh. - 15 minút\nHajnáčka Doh. - Hajnáčka do Centrum - 8 minúty\nHajnáčka do Centrum - Hajnáčka Centrum - 4 minúty", font="Italic 20 bold")
#blue
def gortvac():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Gortva',command=gortva)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=gortvar)
    brod.place(x=1000,y=500)
    
def gortva():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 800:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 770, text="Hajnáčka Centrum - Hajnáčka Sasbik  - 35 minút\nHajnáčka Sasbik - Hajnáčka Gortva – 10 minút\nHajnáčka Gortva - Hajnáčka Gortva do Zaboda - 5 minút",font="Italic 20 bold")
    
def gortvar():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 800:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 770, text="Hajnáčka Gortva do Zaboda - Hajnáčka Gortva - 5 minút\nHajnáčka Gortva - Hajnáčka Sasbik – 10 minút\nHajnáčka Sasbik - Hajnáčka Centrum  - 35 minút",font="Italic 20 bold")
#green
def depoc():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Depo',command=depo)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=depor)
    brod.place(x=1000,y=500)
def depo():
    global ysav
    ysav = 670
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 850:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(940, 785, text="Hajnáčka Centrum - Hajnáčka Sasbik\nHajnáčka Sasbik - Hajnáčka  Železničná Stanica\nHajnáčka  Železničná Stanica - Hajnáčka Ipeľná Teheľňa - 35 minút\nHajnáčka Ipeľná Teheľňa - Hajnáčka Časť Železničná Stanica - 35 minút\nHajnáčka Časť Železničná Stanica - Hajnáčka Depo - 43 minút",font="Italic 20 bold")
def depor():
    global ysav
    ysav = 670
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 850:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(940, 785, text="Hajnáčka Depo - Hajnáčka Časť Železničná Stanica - 43 minút\nHajnáčka Časť Železničná Stanica - Hajnáčka Ipeľná Teheľňa - 35 minút\nHajnáčka Ipeľná Teheľňa - Hajnáčka  Železničná Stanica - 35 minút\nHajnáčka  Železničná Stanica - Hajnáčka Sasbik - 40 minút\nHajnáčka Sasbik - Hajnáčka Centrum",font="Italic 20 bold")
#red
def tenkesc():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Zabovy',command=tenkes)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=tenkesr)
    brod.place(x=1000,y=500)
def tenkes():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 920:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 835, text="Hajnáčka Centrum - Hajnáčka Durenda - 10 minút\nHajnáčka Durenda - Hajnáčka Hrad - 15 minút\nHajnáčka Hrad - Hajnáčka Nové Cintorín - 20 minút\nHajnáčka Nové Cintorín - Hajnáčka Ragačou - 27 minút\nHajnáčka Ragačou - Hajnáčka ulica Nového - 40 minút\nHajnáčka ulica Nového - Hajnáčka ulica Selecov - 45 minút\nHajnáčka ulica Selecov - Hajnáčka ulica Zabovy - 50 minút",font="Italic 20 bold")
def tenkesr():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 920:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 835, text="Hajnáčka ulica Zabovy - Hajnáčka ulica Selecov - 50 minút\nHajnáčka ulica Selecov - Hajnáčka ulica Nového - 45 minút\nHajnáčka ulica Nového - Hajnáčka Ragačou - 40 minút\nHajnáčka Ragačou - Hajnáčka Nové Cintorín - 27 minút \nHajnáčka Nové Cintorín - Hajnáčka Hrad - 20 minút  \nHajnáčka Hrad - Hajnáčka Durenda - 15 minút\nHajnáčka Durenda - Hajnáčka Centrum - 10 minút",font="Italic 20 bold")
#yellow
def selecovc():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Ragácou',command=selecov)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=selecovr)
    brod.place(x=1000,y=500)
def selecov():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 880:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 805, text="Hajnáčka Centrum - Hajnáčka Lekáreň - 2  minúty\nHajnáčka Lekáreň - Hajnáčka Pekáreň  - 5 minút\nHajnáčka Pekáreň - Hajnáčka ulica do Hradu - 10 minút\nHajnáčka ulica do Hradu - Hajnáčka Nové Cintorín - 15 minút\nHajnáčka Nové Cintorín - Hajnáčka Ragácou - 22 minút",font="Italic 20 bold")
def selecovr():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 880:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 805, text="Hajnáčka Ragácou - Hajnáčka Nové Cintorín - 22 minút\nHajnáčka Nové Cintorín - Hajnáčka ulica do Hradu - 15 minút\nHajnáčka ulica do Hradu - Hajnáčka Pekáreň - 10 minút\nHajnáčka Pekáreň - Hajnáčka Lekáreň - 5 minút\nHajnáčka Lekáreň - Hajnáčka Centrum - 2 minúty",font="Italic 20 bold")
    
#orange
def koloniac():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Selecov',command=selecov)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=selecovr)
    brod.place(x=1000,y=500)
def kolonia():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 850:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 790, text="Hajnáčka Centrum - Hajnáčka ulica do Hradu - 10 minút\nHajnáčka ulica do Hradu - Hajnáčka ulica Nového - 14 minút\nHajnáčka ulica Nového - Hajnáčka ulica Selecov - 18 minút\nHajnáčka Selecov - Hajnáčka ulica Zabovy - 22 minút",font="Italic 20 bold")
    
def koloniar():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 850:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 790, text="Hajnáčka Centrum - Hajnáčka ulica do Hradu - 10 minút\nHajnáčka ulica do Hradu - Hajnáčka ulica Nového - 14 minút\nHajnáčka ulica Nového - Hajnáčka ulica Selecov - 18 minút\nHajnáčka Selecov - Hajnáčka ulica Zabovy - 22 minút",font="Italic 20 bold")
    
#cyan
def dohc():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Posa',command=doh)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=dohr)
    brod.place(x=1000,y=500)
def doh():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 780:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 755, text="Hajnáčka Centrum - Hajnáčka Posa - 4 minúty\nHajnáčka Posa - Hajnáčka Posa do Tilíc - 6 minút",font="Italic 20 bold")
def dohr():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 780:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 755, text="Hajnáčka Posa do Tilíc - Hajnáčka Posa - 6 minút\nHajnáčka Posa - Hajnáčka Centrum - 4 minúty",font="Italic 20 bold")
    
#dark green
def posac():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do Pesov',command=posa)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=posar)
    brod.place(x=1000,y=500)
def posa():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 800:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 770, text="Hajnáčka Centrum - Hajnáčka Lekáreň - 2 minúty\nHajnáčka Lekáreň - Hajnáčka Futbal - 4 minúty\nHajnáčka Futbal - Hajnáčka ulica Pesov - 7 minút",font="Italic 20 bold")
def posar():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 800:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 770, text="Hajnáčka ulica Pesov - Hajnáčka Futbal - 7 minút\nHajnáčka Futbal - Hajnáčka Lekáreň - 4 minúty\nHajnáčka Lekáreň - Hajnáčka Centrum - 2 minúty",font="Italic 20 bold")
    
#pink
def sjrdc():
    button.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    button10.destroy()
    brdo = Button(window,text='do S.J.R.D.',command=sjrd)
    brdo.place(x=500,y=500)
    brod=Button(window,text="do Centrum",command=sjrdr)
    brod.place(x=1000,y=500)
def sjrd():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 850:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 805, text="Hajnáčka Centrum - Hajnáčka do Tenkeš - 4 minúty\nHajnáčka do Tenkeš - Hajnáčka Tenkeš - 7 minút\nHajnáčka Tenkeš - Hajnáčka S.J.R.D. - 12 minút\nHajnáčka S.J.R.D. - Hajnáčka Sťavica - 15 minút\n",font="Italic 20 bold")
def sjrdr():
    global ysav
    ysav = 690
    canvas.create_rectangle(400, ysav, 1490, ysav + 35, fill="red", outline="black", tag="sav")
    def move_rectangle():
        global ysav
        canvas.move("sav", 0, 32)
        ysav += 32
        if ysav >= 850:
            canvas.delete("sav")
        window.after(1000, move_rectangle)
    move_rectangle()  # Start the rectangle movement
    gif_filename = "kolonia.gif"
    gif_image = Image.open(gif_filename)
    tk_image = ImageTk.PhotoImage(gif_image)
    
    # Create a label to display the GIF
    gif_label = Label(window, image=tk_image,width=1500)
    gif_label.image = tk_image  # Keep a reference to avoid garbage collection
    gif_label.place(x=0, y=0)
    canvas.create_text(900, 805, text="Hajnáčka Sťavica - Hajnáčka S.J.R.D. - 15 minút\nHajnáčka S.J.R.D. - Hajnáčka Tenkeš - 12 minút\nHajnáčka Tenkeš - Hajnáčka do Tenkeš - 7 minút\nHajnáčka do Tenkeš - Hajnáčka Centrum - 4 minúty",font="Italic 20 bold")
    
def exit():
    window.destroy()

button = Button(window,text='Bus 1')
button.config(command=centrumc) #performs call back of function
button.config(font=('Italic',20,'bold'))
button.config(activebackground='#aab1ff')
button.config(activeforeground='#393b55')
image = PhotoImage(file='centrum.png')
button.config(image=image)
button.config(compound='top')
button.config(width=200,height=250)

button2 = Button(window,text='Bus 2')
button2.config(command=gortvac) #performs call back of function
button2.config(font=('Italic',20,'bold'))
button2.config(activebackground='#aab1ff')
button2.config(activeforeground='#393b55')
image2 = PhotoImage(file='zelst.png')
button2.config(image=image2)
button2.config(compound='top')
button2.config(width=200,height=250)

button3 = Button(window,text='Bus 3')
button3.config(command=depoc) #performs call back of function
button3.config(font=('Italic',20,'bold'))
button3.config(activebackground='#aab1ff')
button3.config(activeforeground='#393b55')
image3 = PhotoImage(file='stav.png')
button3.config(image=image3)
button3.config(compound='top')
button3.config(width=200,height=250)

button4 = Button(window,text='Bus 4')
button4.config(command=tenkesc) #performs call back of function
button4.config(font=('Italic',20,'bold'))
button4.config(activebackground='#aab1ff')
button4.config(activeforeground='#393b55')
image4 = PhotoImage(file='tenkes.png')
button4.config(image=image4)
button4.config(compound='top')
button4.config(width=200,height=250)

button5 = Button(window,text='Bus 5')
button5.config(command=selecovc) #performs call back of function
button5.config(font=('Italic',20,'bold'))
button5.config(activebackground='#aab1ff')
button5.config(activeforeground='#393b55')
image5 = PhotoImage(file='ragacou.png')
button5.config(image=image5)
button5.config(compound='top')
button5.config(width=200,height=250)

button6 = Button(window,text='Bus 6')
button6.config(command=koloniac) #performs call back of function
button6.config(font=('Italic',20,'bold'))
button6.config(activebackground='#aab1ff')
button6.config(activeforeground='#393b55')
image6 = PhotoImage(file='kol.png')
button6.config(image=image6)
button6.config(compound='top')
button6.config(width=200,height=250)

button7 = Button(window,text='Bus 7')
button7.config(command=dohc) #performs call back of function
button7.config(font=('Italic',20,'bold'))
button7.config(activebackground='#aab1ff')
button7.config(activeforeground='#393b55')
image7 = PhotoImage(file='doh.png')
button7.config(image=image7)
button7.config(compound='top')
button7.config(width=200,height=250)

button8 = Button(window,text='Bus 8')
button8.config(command=posac) #performs call back of function
button8.config(font=('Italic',20,'bold'))
button8.config(activebackground='#aab1ff')
button8.config(activeforeground='#393b55')
image8 = PhotoImage(file='posa.png')
button8.config(image=image8)
button8.config(compound='top')
button8.config(width=200,height=250)

button9 = Button(window,text='Bus 9')
button9.config(command=sjrdc) #performs call back of function
button9.config(font=('Italic',20,'bold'))
button9.config(activebackground='#aab1ff')
button9.config(activeforeground='#393b55')
image9 = PhotoImage(file='sjrd.png')
button9.config(image=image9)
button9.config(compound='top')
button9.config(width=200,height=250)

button10 = Button(window,text='Exit')
button10.config(command=exit) #performs call back of function
button10.config(font=('Italic',20,'bold'))
button10.config(activebackground='#aab1ff')
button10.config(activeforeground='#393b55')
image10 = PhotoImage(file='exit.png')
button10.config(image=image10)
button10.config(compound='top')
button10.config(width=200,height=250)

def busses():
    button.place(x=0,y=0)
    button2.place(x=250,y=0)
    button3.place(x=500,y=0)
    button4.place(x=750,y=0)
    button5.place(x=1000,y=0)
    button6.place(x=0,y=250)
    button7.place(x=250,y=250)
    button8.place(x=500,y=250)
    button9.place(x=750,y=250)
    button10.place(x=1000,y=250)

# Define custom colors
primary_color = "#3498db"  # Blue
secondary_color = "#e74c3c"  # Red
background_color = "#ecf0f1"  # Light Gray
text_color = "#333333"  # Dark Gray
button_color = "#2ecc71"  # Green

# Use the custom colors in your UI elements
window.configure(bg=background_color)
time_label.config(bg=background_color, fg=text_color)
day_label.config(bg=background_color, fg=text_color)
date_label.config(bg=background_color, fg=text_color)

buttons=[button,button2,button3,button4,button5,button6,button7,button8,button9,button10]

# Use the button_color for buttons
for b in buttons:
    b.config(bg=button_color)

# ... (repeat for other buttons)

# Use secondary_color for error messages or important alerts
error_message_label = Label(window, text="An error occurred.", bg=background_color, fg=secondary_color)




update()
busses()
window.mainloop()