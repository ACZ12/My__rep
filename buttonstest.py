import tkinter as tk

# Create the main Tkinter window
root = tk.Tk()
root.title("Button Example")

# Function to perform some action when a button is clicked
def button_click(button_number):
    print(f"Button {button_number} clicked!")

# Create multiple buttons
button1 = tk.Button(root, text="Button 1", command=lambda: button_click(1))
button2 = tk.Button(root, text="Button 2", command=lambda: button_click(2))
button3 = tk.Button(root, text="Button 3", command=lambda: button_click(3))
button4 = tk.Button(root, text="Button 4", command=lambda: button_click(4))
button5 = tk.Button(root, text="Button 5", command=lambda: button_click(5))

# Pack the buttons (you can use grid or place for custom layouts)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

# Run the Tkinter main loop
root.mainloop()