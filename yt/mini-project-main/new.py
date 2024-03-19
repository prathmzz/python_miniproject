from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess

def open_lecture_page():
    print("Opening Lecture Page...")
    subprocess.run(["python", "lecture_page.py"])

def open_Volunteer_page():
    print("Opening Volunteer Page...")
    subprocess.run(["python", "Volunteer_page.py"])

def open_teacher_section():
    print("Opening Teacher Section Page...")
    subprocess.run(["python", "teacher_section.py"])

def open_Rescue():
    print("Opening Rescue Page...")
    subprocess.run(["python", "Rescue.py"])


# Define functions for different pages
def lecture_page():
    print("Navigating to lecture page...")
    print("Lecture Page opened")
    # Remove any existing content
    for widget in content_frame.winfo_children():
        widget.destroy()
    # Add content for lecture page
    content_label = Label(content_frame, text="Lecture Page Content", font=("Arial", 16), bg="white", fg="black")
    content_label.pack(padx=10, pady=10)

def Volunteer_page():
    print("Navigating to Volunteer page...")
    print("Volunteer Page opened")
    # Remove any existing content
    for widget in content_frame.winfo_children():
        widget.destroy()
    # Add content for volunteer page
    content_label = Label(content_frame, text="Volunteer Page Content", font=("Arial", 16), bg="white", fg="black")
    content_label.pack(padx=10, pady=10)

def teacher_section():
    print("Navigating to teacher_section page...")
    print("Teacher Section Page opened")
    # Remove any existing content
    for widget in content_frame.winfo_children():
        widget.destroy()
    # Add content for teacher section page
    content_label = Label(content_frame, text="Teacher Section Page Content", font=("Arial", 16), bg="white", fg="black")
    content_label.pack(padx=10, pady=10)

def Rescue():
    print("Navigating to Rescue page...")
    print("Rescue Page opened")
    # Remove any existing content
    for widget in content_frame.winfo_children():
        widget.destroy()
    # Add content for rescue page
    content_label = Label(content_frame, text="Rescue Page Content", font=("Arial", 16), bg="white", fg="black")
    content_label.pack(padx=10, pady=10)

# Create the main window
root = Tk()
root.title("Animal Connect")
root.geometry("800x600+100+100")

# Create the top bar
topbar = Frame(root, bg="#ed5876", width=600, height=50)
topbar.pack(side=TOP, fill=X)

title = Label(topbar, text="Donation", font=("Arial", 20, "bold"), bg="#ed5876", fg="#ffffff")
title.pack(side=LEFT, padx=20, pady=10)

user_icon_image = PhotoImage(file="Images/settings_icon.png").subsample(2)
user_icon = Label(topbar, image=user_icon_image, bg="#ed5876")
user_icon.pack(side=RIGHT, padx=10, pady=10)

user_name = Label(topbar, text="Animal Connect", font=("Arial", 16), bg="#ed5876", fg="#ffffff")
user_name.pack(side=RIGHT, pady=10)

# Create the sidebar
sidebar = Frame(root, width=200, height=600, bg="#eb4163")
sidebar.pack(side=LEFT, fill=Y)

menu_items = [
    ("Volunteer", "home_icon.png"),
    ("Donation", "lecture_icon.png"),
    ("Adoption", "user_icon.png"),
    ("Rescue", "teacher_icon.png"),
]

buttons = []


for item in menu_items:
    image = Image.open("Images/" + item[1])
    photo_image = ImageTk.PhotoImage(image)
    button = Button(sidebar, text=item[0], image=photo_image, compound=LEFT, fg="white", bg="#eb4163", bd=0, padx=20,
                    pady=10, anchor="w")
    button.image = photo_image
    button.pack(anchor="w", fill=X)
    buttons.append(button)

    # Modify button commands
    if item[0] == "Donation":
        button.config(command=open_lecture_page)
    elif item[0] == "Adoption":
        button.config(command=open_teacher_section)
    elif item[0] == "Volunteer":
        button.config(command=open_Volunteer_page)
    elif item[0] == "Rescue":
        button.config(command=open_Rescue)

# Create a frame for the content
content_frame = Frame(root, bg="white", width=600, height=550)
content_frame.pack(side=RIGHT, fill=BOTH, expand=True)

root.mainloop()
