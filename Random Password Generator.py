import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string
import json
import os
import hashlib

# Constants
USER_DATA_FILE = "users.json"

# Load user data from file or create a new one if it doesn't exist
def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        return {}
    with open(USER_DATA_FILE, "r") as file:
        return json.load(file)

# Save user data to file
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register a new user
def register():
    username = simpledialog.askstring("Register", "Enter a username:")
    if not username:
        return
    if username in user_data:
        messagebox.showerror("Error", "Username already exists!")
        return

    password = simpledialog.askstring("Register", "Enter a password:", show='*')
    if not password:
        return
    confirm_password = simpledialog.askstring("Register", "Confirm password:", show='*')
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    security_question = simpledialog.askstring("Register", "Enter a security question (for password recovery):")
    if not security_question:
        return
    security_answer = simpledialog.askstring("Register", "Enter the answer to your security question:")
    if not security_answer:
        return

    user_data[username] = {
        "password": hash_password(password),
        "security_question": security_question,
        "security_answer": security_answer,
        "data_file": f"{username}_data.json"
    }
    save_user_data(user_data)
    messagebox.showinfo("Success", "User registered successfully!")

# Login existing user
def login():
    global current_user
    username = username_entry.get()
    password = password_entry.get()

    if username in user_data and user_data[username]["password"] == hash_password(password):
        current_user = username
        login_window.destroy()
        show_password_manager()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Password recovery
def recover_password():
    username = simpledialog.askstring("Password Recovery", "Enter your username:")
    if not username or username not in user_data:
        messagebox.showerror("Error", "Username not found!")
        return

    security_question = user_data[username]["security_question"]
    answer = simpledialog.askstring("Password Recovery", f"{security_question}")
    if not answer or answer != user_data[username]["security_answer"]:
        messagebox.showerror("Error", "Incorrect answer!")
        return

    new_password = simpledialog.askstring("Password Recovery", "Enter a new password:", show='*')
    confirm_password = simpledialog.askstring("Password Recovery", "Confirm new password:", show='*')
    if new_password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    user_data[username]["password"] = hash_password(new_password)
    save_user_data(user_data)
    messagebox.showinfo("Success", "Password reset successfully!")

# Generate a random password
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

# Save the generated password to the user's file
def save_password():
    account_name = account_entry.get()
    password = password_entry.get()

    if not account_name or not password:
        messagebox.showerror("Missing Information", "Please enter both an account name and generate a password.")
        return

    user_data_file = user_data[current_user]["data_file"]
    if not os.path.exists(user_data_file):
        user_data_content = {}
    else:
        with open(user_data_file, "r") as file:
            user_data_content = json.load(file)

    user_data_content[account_name] = password

    with open(user_data_file, "w") as file:
        json.dump(user_data_content, file, indent=4)
    
    messagebox.showinfo("Saved", "Password saved successfully!")
    
    # Clear the input fields
    account_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Open the file containing the user's saved passwords
def open_password_file():
    user_data_file = user_data[current_user]["data_file"]
    if os.path.exists(user_data_file):
        os.startfile(user_data_file)
    else:
        messagebox.showerror("File Not Found", "No passwords have been saved yet.")

# Show the main password manager window
def show_password_manager():
    global length_entry, account_entry, password_entry

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

    root.mainloop()

# Load user data
user_data = load_user_data()
current_user = None

# Login window
login_window = tk.Tk()
login_window.title("Login")

# Username label and entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(login_window, show='*')
password_entry.pack(pady=5)

# Login button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

# Register button
register_button = tk.Button(login_window, text="Register", command=register)
register_button.pack(pady=10)

# Recover password button
recover_button = tk.Button(login_window, text="Forgot Password?", command=recover_password)
recover_button.pack(pady=10)

login_window.mainloop()
