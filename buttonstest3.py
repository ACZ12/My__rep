from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

window = Tk()
canvas = Canvas(window, height=1000, width=800)
canvas.pack()

# Declare button variables as global
bus_buttons = []

# Declare the "Back" button as a global variable
back_button = None

selected_bus_image = None  # Track the currently selected bus image

def open_image(image_path):
    global selected_bus_image
    img = Image.open(image_path)
    img.thumbnail((canvas.winfo_width(), canvas.winfo_height()))
    selected_bus_image = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=selected_bus_image)

def destroy_buttons():
    global back_button
    if back_button:
        back_button.destroy()
    for button in bus_buttons:
        button.destroy()

def centrum():
    destroy_buttons()
    open_image("C:\\Users\\A\\Downloads\\h1.jpg")
    
    # Create a "Back" button to return to the busses page
    global back_button
    back_button = Button(window, text="Späť", command=busses)
    back_button.pack()

def zelst():
    destroy_buttons()
    open_image("C:\\Users\\A\\Downloads\\h2.jpg")

def stavica():
    destroy_buttons()
    open_image("C:\\Users\\A\\Downloads\\h3.jpg")

# Other page functions (tenkes, selecov, kolonia, doh, posa) follow the same pattern as centrum.

def create_bus_buttons():
    bus_names = ["Bus 1", "Bus 2", "Bus 3"]
    bus_commands = [centrum, zelst, stavica]
    for i in range(len(bus_names)):
        button = Button(window, text=bus_names[i], command=bus_commands[i])
        button.config(font=('Italic', 20, 'bold'))
        button.config(activebackground='#aab1ff')
        button.config(activeforeground='#393b55')
        bus_buttons.append(button)
        image = PhotoImage(file="h10.png")
        button.config(image=image)
        button.config(compound='top')
        button.config(width=200, height=250)

def exit_program():
    window.destroy()

def busses():
    destroy_buttons()
    create_bus_buttons()

# Initial button creation
create_bus_buttons()

exit_button = Button(window, text='Exit', command=exit_program)
exit_button.config(font=('Italic', 20, 'bold'))
exit_button.config(activebackground='#aab1ff')
exit_button.config(activeforeground='#393b55')
exit_button.config(width=200, height=50)
exit_button.pack()

window.mainloop()
