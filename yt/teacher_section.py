from tkinter import *
from sidebar import create_sidebar  # Import the create_sidebar function

def open_volunteer_page():
    print("Opening Volunteer Page...")

root = Tk()
root.title("Volunteer Page")

root.title("Animal Connect")
root.geometry("800x600+100+100")

# Use the create_sidebar function to create the sidebar
sidebar, buttons = create_sidebar(root)

# Create a frame for the buttons in the white portion
button_frame = Frame(root, bg="white")
button_frame.pack(side=TOP, fill=X)

# Add the two additional buttons in the middle
# add_campaign_button = Button(button_frame, text="Add Campaign", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# add_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(50, 0))  # Adjust pady to add space
# view_campaign_button = Button(button_frame, text="View Campaign", fg="white", bg="#eb4163", bd=0, padx=20, pady=10)
# view_campaign_button.pack(side=TOP, fill=X, padx=20, pady=(10, 0))  # Adjust pady to add space

# Insert a space between the existing buttons and the new ones
Label(button_frame, text="").pack(side=TOP, pady=10)

# Configure button commands
for button in buttons:
    button.config(command=open_volunteer_page)

root.mainloop()
