from tkinter import *

window = Tk()
canvas = Canvas(window,bg="lightgray")
canvas.pack()

class Email:
    y = 20

    def __init__(self, email, passw):
        self.email = email
        self.passw = passw
        self.display_button = Button(window, text=f"Display email {Email.y // 30}", command=self.printpass)
        self.display_button.place(x=10, y=Email.y)
        Email.y += 30

    def printpass(self):
        canvas.create_text(140, 20, text="Email = ",font="Ariel 10 bold")
        canvas.create_text(270, 20, text=self.email)
        canvas.create_text(140, 40, text=f"Password = ",font="Ariel 10 bold")
        canvas.create_text(270, 40, text=self.passw)

email_entries = []
passw_entries = []

def save_data():
    with open("email_password.txt", "w") as file:
        for email, passw in zip(email_entries, passw_entries):
            file.write(f"{email},{passw}\n")

def load_data():
    try:
        with open("email_password.txt", "r") as file:
            for line in file:
                email, passw = line.strip().split(",")
                e1 = Email(email, passw)
                email_entries.append(email)
                passw_entries.append(passw)
    except FileNotFoundError:
        # File doesn't exist, ignore and continue
        pass

# Load saved data when the program starts
load_data()

# Function to update the Email instance
def printemail():
    email_entry = email.get()
    passw_entry = passw.get()
    e1 = Email(email_entry, passw_entry)
    email_entries.append(email_entry)
    passw_entries.append(passw_entry)
    save_data()

email = Entry(window)
email.pack()
passw = Entry(window)
passw.pack()

# Create a "Submit" button that calls printemail when clicked
submit_button = Button(window, text="Submit new email", command=printemail)
submit_button.pack()

# Bind the Enter key to the printemail function
window.bind("<Return>", lambda event=None: printemail())

window.mainloop()
