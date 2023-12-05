from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os




class Resize(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Open and identify the image
        self.image = Image.open("mcbg2.png")

        # Create a copy of the image and store it in a variable
        self.img_copy = self.image.copy()

        # Define the image using PhotoImage function
        self.background_image = ImageTk.PhotoImage(self.image)

        # Create a canvas and display the background image
        self.canvas = Canvas(self, width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=NW, image=self.background_image)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Bind the function resize_background to screen resize
        self.canvas.bind('<Configure>', self.resize_background)

        

    def resize_background(self, event):
    # Get the new width and height for the image
        new_width = event.width
        new_height = event.height

    # Destroy the old "Quit" button
        if hasattr(self, 'quit_button'):
            self.quit_button.destroy()
        if hasattr(self, 'felh_entry'):
            self.felh_entry.destroy()
        if hasattr(self, 'felh_text'):
            self.felh_text.destroy()
        if hasattr(self, 'vers'):
            self.vers.destroy()


    # Create a new "Quit" button with updated position
        self.quit_button = Button(self.canvas, text="Start", command=self.quit_application,width=20,height=4)
        self.quit_button_window = self.canvas.create_window(new_width-200, new_height/2, anchor=NW, window=self.quit_button)

        self.felh_entry = Entry()
        self.felh_entry_window = self.canvas.create_window(100, new_height/2 + 10, anchor=NW, window=self.felh_entry)
        
        self.felh_text = Label(text="Felhasználónév:",width=17)
        self.felh_text_window = self.canvas.create_window(100, new_height/2 - 10, anchor=NW, window=self.felh_text)

        self.ind_text = Label(text="Complex 5 Craft")
        self.ind_text_window = self.canvas.create_window(20, 20, anchor=NW, window=self.ind_text)

        self.options=["1.2.5","1.5.2","2.0"]

        self.clicked=StringVar()
        self.clicked.set(self.options[0])

        self.vers = OptionMenu(self,self.clicked,*self.options)
        self.vers_window = self.canvas.create_window(20,new_height/1.2, anchor=NW, window=self.vers)


        self.image = self.img_copy.resize((new_width, new_height))

    # Define the new image using PhotoImage function
        self.background_image = ImageTk.PhotoImage(self.image)

    # Change the image in the canvas
        self.canvas.config(width=new_width, height=new_height)
        self.canvas.itemconfig(1, image=self.background_image)




    def quit_application(self):
        # Replace "path/to/minecraft.zip" with the actual path to your minecraft.zip file
        file_path = "C:\\Users\\adamc\\Downloads\\ForgeOptiFine 1.2.5-20231201T165459Z-001\\ForgeOptiFine 1.2.5"

        try:
            # Open the file with the default associated program
            os.startfile(file_path)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")

        #root.destroy()


# Create the main application window
root = Tk()
root.title("Complex 5 Craft")
root.geometry("800x500")
root.iconbitmap("mcchicken.ico")

# Instantiate the Resize class and display it on the app
app = Resize(root)
app.pack(fill=BOTH, expand=YES)

# Start the main event loop
root.mainloop()
