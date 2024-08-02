import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to handle user signup
def signup():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    # Simulate saving user to the database
    messagebox.showinfo("Success", "User registered successfully!")
    clear_entries()

# Function to simulate Google Sign-In (Placeholder)
def google_signin():
    messagebox.showinfo("Google Sign-In", "Google Sign-In feature is not implemented yet!")

# Function to clear all entry fields
def clear_entries():
    username_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    confirm_password_entry.delete(0, tk.END)

# Initialize the main window
root = tk.Tk()
root.title("User Signup")

# Create and place the widgets for user signup
signup_frame = ttk.Frame(root, padding="20")
signup_frame.pack(padx=10, pady=10)

ttk.Label(signup_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = ttk.Entry(signup_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(signup_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = ttk.Entry(signup_frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(signup_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
password_entry = ttk.Entry(signup_frame, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(signup_frame, text="Confirm Password:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
confirm_password_entry = ttk.Entry(signup_frame, show="*")
confirm_password_entry.grid(row=3, column=1, padx=5, pady=5)

signup_button = ttk.Button(signup_frame, text="Sign Up", command=signup)
signup_button.grid(row=4, column=0, columnspan=2, pady=10)

# Google Sign-In button (non-functional placeholder)
google_signin_button = ttk.Button(signup_frame, text="Sign Up with Google", command=google_signin)
google_signin_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()