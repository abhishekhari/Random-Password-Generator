import tkinter as tk
from tkinter import messagebox
import random
import string
import os

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    account_name = account_entry.get()
    password = password_entry.get()

    if not account_name or not password:
        messagebox.showerror("Missing Information", "Please enter both an account name and generate a password.")
        return
    
    with open("passwords.txt", "a") as file:
        file.write(f"{account_name}: {password}\n")
    
    messagebox.showinfo("Saved", "Password saved successfully!")
    
    # Clear the input fields
    account_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def open_password_file():
    if os.path.exists("passwords.txt"):
        os.startfile("passwords.txt")
    else:
        messagebox.showerror("File Not Found", "No passwords have been saved yet.")

# Create the main application window
root = tk.Tk()
root.title("Password Manager")

# Account label and entry
account_label = tk.Label(root, text="Account Name:")
account_label.pack(pady=5)

account_entry = tk.Entry(root)
account_entry.pack(pady=5)

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Password entry (read-only)
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Save button
save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.pack(pady=10)

# Open file button
open_file_button = tk.Button(root, text="Open Password File", command=open_password_file)
open_file_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
