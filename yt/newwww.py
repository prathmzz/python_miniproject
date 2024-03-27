import tkinter as tk
from tkinter import filedialog
import sqlite3
from PIL import Image, ImageTk
import io

# Database initialization
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, address TEXT, image BLOB)''')
conn.commit()

# Define label_image globally
label_image = None

# Function to handle image upload
def upload_image():
    global label_image  # Using global label_image
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.thumbnail((250, 250))  # Resizing image to fit in the frame
    img = ImageTk.PhotoImage(img)
    label_image = tk.Label(frame, image=img)
    label_image.image = img  # Keeping a reference to avoid garbage collection
    label_image.grid(row=4, column=0, columnspan=2, padx=10, pady=10)  # Adjust position as needed
    
    with open(file_path, 'rb') as f:
        image_data = f.read()

    # Inserting data into database
    c.execute("INSERT INTO users (name, phone, address, image) VALUES (?, ?, ?, ?)",
              (entry_name.get(), entry_phone.get(), entry_address.get("1.0", "end-1c"), image_data))
    conn.commit()

    # Displaying data as a card
    display_card(entry_name.get(), entry_phone.get(), entry_address.get("1.0", "end-1c"), image_data)

# Function to display user data as a card
def display_card(name, phone, address, image_data):
    card_frame = tk.Frame(frame, width=480, height=150, bg="white", relief="raised", bd=2)
    card_frame.pack(pady=10)
    
    # Displaying image
    img = Image.open(io.BytesIO(image_data))
    img = ImageTk.PhotoImage(img.resize((100, 100)))  # Resize image for display
    label_img = tk.Label(card_frame, image=img, bg="white")
    label_img.image = img
    label_img.grid(row=0, column=0, rowspan=2, padx=10, pady=10)
    
    # Displaying user information
    label_name = tk.Label(card_frame, text=f"Name: {name}", bg="white")
    label_name.grid(row=0, column=1, sticky="w", padx=10)
    
    label_phone = tk.Label(card_frame, text=f"Phone: {phone}", bg="white")
    label_phone.grid(row=1, column=1, sticky="w", padx=10)
    
    label_address = tk.Label(card_frame, text=f"Address: {address}", bg="white", wraplength=300, justify="left")
    label_address.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Tkinter setup
root = tk.Tk()
root.title("User Form")
root.geometry("500x500")

# Frame to display user information
frame = tk.Frame(root, width=500, height=500, bg="white")
frame.pack_propagate(False)
frame.pack()

# Form fields
label_name = tk.Label(frame, text="Name:", bg="white")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(frame, text="Phone:", bg="white")
label_phone.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_phone = tk.Entry(frame)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_address = tk.Label(frame, text="Address:", bg="white")
label_address.grid(row=2, column=0, padx=10, pady=5, sticky="nw")
entry_address = tk.Text(frame, height=4, width=30)
entry_address.grid(row=2, column=1, padx=10, pady=5)

# Button to upload image and save data
upload_button = tk.Button(frame, text="Upload Image", command=upload_image)
upload_button.grid(row=3, column=0, padx=10, pady=5, columnspan=2)

root.mainloop()
