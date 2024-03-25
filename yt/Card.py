# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk

# def open_image(img_label):
#     # Open a file dialog to select an image
#     filepath = filedialog.askopenfilename()
#     if filepath:
#         # Load the selected image
#         image = Image.open(filepath)
#         # Display the image in a label
#         photo = ImageTk.PhotoImage(image)
#         img_label.config(image=photo)
#         img_label.image = photo  # Keep a reference to avoid garbage collection

# def generate_card(info_entry, img_label, cards_frame):
#     # Function to generate card with uploaded image and entered information
#     info = info_entry.get()
#     if img_label.image and info:
#         card_frame = tk.Frame(cards_frame, bd=1, relief=tk.RAISED)
#         card_frame.pack(side=tk.TOP, padx=5, pady=5)

#         image_label = tk.Label(card_frame, image=img_label.image)
#         image_label.pack(side=tk.LEFT, padx=5, pady=5)

#         info_label = tk.Label(card_frame, text=info)
#         info_label.pack(side=tk.RIGHT, padx=5, pady=5)

# # Create main window
# root = tk.Tk()
# root.title("Image Card Generator")

# # Create frame for image and info entry
# input_frame = tk.Frame(root)
# input_frame.pack(pady=10)

# # Button to upload image
# upload_button = tk.Button(input_frame, text="Upload Image", command=lambda: open_image(img_label))
# upload_button.pack(side=tk.LEFT, padx=5)

# # Entry for information
# info_entry = tk.Entry(input_frame, width=30)
# info_entry.pack(side=tk.LEFT, padx=5)

# # Frame to display cards
# cards_frame = tk.Frame(root)
# cards_frame.pack(pady=10)

# # Label to display uploaded image
# img_label = tk.Label(root)
# img_label.pack()

# # Button to generate card
# generate_button = tk.Button(root, text="Generate Card", command=lambda: generate_card(info_entry, img_label, cards_frame))
# generate_button.pack(pady=5)

# root.mainloop()
import tkinter as tk

def add_card():
    text = text_input.get()
    if text:
        new_window = tk.Toplevel(root)
        new_window.title("Card Details")
        
        card_frame = tk.Frame(new_window, bg="lightblue", padx=10, pady=5)
        card_frame.pack(pady=10, padx=10)
        
        card_label = tk.Label(card_frame, text=text, bg="lightblue")
        card_label.pack(fill="both", expand=True)
        
        text_input.delete(0, "end")

# Create the main application window
root = tk.Tk()
root.title("User Input Cards")

# Input field and Add button
text_input = tk.Entry(root, width=40)
text_input.pack(pady=10)
add_button = tk.Button(root, text="Add Card", command=add_card)
add_button.pack()

# Run the application
root.mainloop()

