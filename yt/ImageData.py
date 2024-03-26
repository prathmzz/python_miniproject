import sqlite3
from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageTk
import io 
root = Tk()

# File dialog to select files
def filedialogs():
    global get_image
    get_image = filedialog.askopenfilenames(title="SELECT IMAGE", filetypes=( ("png", "*.png"), ("jpg" , "*.jpg"), ("Allfile", "*.*")))

# Image need to be conver into binary before insert into database
def convert_image_into_binary(filename):
    with open(filename, 'rb') as file:
        photo_image = file.read()
    return photo_image

def insert_image():
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()
    
    for image in get_image:
       insert_photo   = convert_image_into_binary(image)
       data.execute("INSERT INTO Image Values(:image)", 
                 {'image': insert_photo })

    image_database.commit()
    image_database.close()

def view_image():
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()
    
    data.execute("SELECT * FROM Image")
    images = data.fetchall()

    for image in images:
        image_data = image[0]
        image = Image.open(io.BytesIO(image_data))
        image.show()

    image_database.close()

# Create database in current file and create table if not exist
def create_database():
    image_database = sqlite3.connect("Image_data.db")
    data = image_database.cursor()

    data.execute("CREATE TABLE IF NOT EXISTS Image(Image BLOB)")

    image_database.commit()
    image_database.close()

create_database()

select_image = Button(root, text="Select Image", command=filedialogs)
select_image.grid(row=0, column=0, pady=(100, 0), padx=100)

save_image = Button(root, text="Save", command=insert_image)
save_image.grid(row=1, column=0)

view_image = Button(root, text="View Image", command=view_image)
view_image.grid(row=2, column=0)

root.mainloop()
