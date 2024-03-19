from PIL import Image, ImageTk
import tkinter as tk
import subprocess
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Define the event handling functions
def open_volunteering(event):
    print("Opening Animal Volunteering Section")

def open_adoption(event):
    print("Opening Pet Adoption Section")

def open_donation(event):
    print("Opening Donation Section")

def open_rescue(event):
    print("Opening Rescue Section")

# Create the main window
root = tk.Tk()
root.title("Animal Welfare Homepage")

# Set background color
root.configure(bg='#E5E5E5')

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to be slightly less than full screen
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)
root.geometry(f"{window_width}x{window_height}")

# Load background image
image = Image.open("img.jpg")
background_image = ImageTk.PhotoImage(image)

# Create the navigation bar frame
navbar = tk.Frame(root, bg='#4CAF50', width=500, height=window_height, padx=10, pady=10, bd=0)
navbar.pack(side=tk.LEFT, fill=tk.Y)

# Create labels for each section in the navigation bar
volunteering_label = tk.Label(navbar, text="Volunteer", bg='#4CAF50', fg='white', font=('Helvetica', 12))
adoption_label = tk.Label(navbar, text="Animal Adoption", bg='#4CAF50', fg='white', font=('Helvetica', 12))
donation_label = tk.Label(navbar, text="Donation", bg='#4CAF50', fg='white', font=('Helvetica', 12))
rescue_label = tk.Label(navbar, text="Rescue", bg='#4CAF50', fg='white', font=('Helvetica', 12))

volunteering_label.pack(side=tk.TOP, pady=10)
adoption_label.pack(side=tk.TOP, pady=10)
donation_label.pack(side=tk.TOP, pady=10)
rescue_label.pack(side=tk.TOP, pady=10)

# Bind click events to labels
volunteering_label.bind("<Button-1>", open_volunteering)
adoption_label.bind("<Button-1>", open_adoption)
donation_label.bind("<Button-1>", open_donation)
rescue_label.bind("<Button-1>", open_rescue)

# Create a label with background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=500, y=0, relwidth=1, relheight=1)  # Start after the sidebar, covering the entire window

# Creating the left sidebar
sidebar = Frame(root, width=200, height=600, bg="#4a148c")
sidebar.pack(side=LEFT, fill=Y)

# Create a list of menu items for the sidebar
menu_items = [
    ("Volunteer", 2),
    ("Donation", 2),
    ("Adoption", 2),
    ("Rescue", 2),
    ("LATEST ACTIVITY", 2)
]

# Run the GUI
root.mainloop()
