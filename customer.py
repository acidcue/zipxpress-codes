import tkinter as tk
from tkinter import messagebox

# Sample data storage (in-memory dictionary)
users_data = {}

# Function to register user
def register_user():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()

    if not username or not email or not password or not phone:
        messagebox.showerror("Error", "All fields are required!")
        return

    if email in users_data:
        messagebox.showerror("Error", "Email already registered!")
        return

    # Save the user data
    users_data[email] = {
        "username": username,
        "password": password,
        "phone": phone
    }

    messagebox.showinfo("Success", "User registered successfully!")
    clear_entries()

# Function to load user profile
def load_profile():
    email = email_entry.get()

    if not email:
        messagebox.showerror("Error", "Email is required to load profile!")
        return

    if email not in users_data:
        messagebox.showerror("Error", "Email not found!")
        return

    user = users_data[email]
    username_entry.delete(0, tk.END)
    username_entry.insert(0, user["username"])
    password_entry.delete(0, tk.END)
    password_entry.insert(0, user["password"])
    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, user["phone"])

# Function to update user profile
def update_profile():
    email = email_entry.get()

    if not email:
        messagebox.showerror("Error", "Email is required to update profile!")
        return

    if email not in users_data:
        messagebox.showerror("Error", "Email not found!")
        return

    username = username_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()

    if not username or not password or not phone:
        messagebox.showerror("Error", "All fields are required!")
        return

    users_data[email] = {
        "username": username,
        "password": password,
        "phone": phone
    }

    messagebox.showinfo("Success", "Profile updated successfully!")
    clear_entries()

# Function to clear all entry fields
def clear_entries():
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("User Registration and Profile Management")

# Create and place the widgets for user registration and profile management
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

tk.Label(root, text="Phone Number:").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

register_button = tk.Button(root, text="Register", command=register_user)
register_button.pack(pady=10)

load_button = tk.Button(root, text="Load Profile", command=load_profile)
load_button.pack(pady=10)

update_button = tk.Button(root, text="Update Profile", command=update_profile)
update_button.pack(pady=10)

# Run the application
root.mainloop()
