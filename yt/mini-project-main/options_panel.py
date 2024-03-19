import tkinter as tk
from tkinter import messagebox

def open_option_panel(parent):
    option_panel = tk.Toplevel(parent)
    option_panel.title("Options Panel")

    # Add your option buttons and associated functions here
    btn_pet_adoption = tk.Button(option_panel, text="Pet Adoption", command=pet_adoption)
    btn_pet_adoption.pack(pady=10)

    btn_donation = tk.Button(option_panel, text="Donation", command=donation)
    btn_donation.pack(pady=10)

    btn_pet_info = tk.Button(option_panel, text="Pet Information", command=pet_info)
    btn_pet_info.pack(pady=10)

    btn_ngo = tk.Button(option_panel, text="NGO", command=ngo)
    btn_ngo.pack(pady=10)

def pet_adoption():
    # Add logic for pet adoption
    messagebox.showinfo("Pet Adoption", "Pet Adoption Option Selected")

def donation():
    # Add logic for donation
    messagebox.showinfo("Donation", "Donation Option Selected")

def pet_info():
    # Add logic for pet information
    messagebox.showinfo("Pet Information", "Pet Information Option Selected")

def ngo():
    # Add logic for NGO
    messagebox.showinfo("NGO", "NGO Option Selected")
