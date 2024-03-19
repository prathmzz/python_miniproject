from tkinter import *
from PIL import Image, ImageTk
from sidebar import create_sidebar

def open_volunteer_page():
    print("Opening Volunteer Page...")

root = Tk()
root.title("Volunteer Page")
root.geometry("800x600+100+100")

# Create the sidebar and get the buttons
sidebar, buttons = create_sidebar(root)

# Add the two additional buttons in the middle
add_campaign_button = Button(sidebar, text="Add Campaign", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
add_campaign_button.pack(anchor="w", fill=X)
view_campaign_button = Button(sidebar, text="View Campaign", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
view_campaign_button.pack(anchor="w", fill=X)

# Insert a space between the existing buttons and the new ones
Label(sidebar, text="").pack()

# Configure button commands
for button in buttons:
    if button["text"] == "Volunteer":
        button.config(command=open_volunteer_page)

root.mainloop()
