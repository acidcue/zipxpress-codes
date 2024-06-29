import tkinter as tk
from tkinter import messagebox

# Function to register driver
def register_driver():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    license_number = license_entry.get()
    license_type = license_type_var.get()

    if not name or not email or not phone or not license_number or not license_type:
        messagebox.showerror("Error", "All fields are required!")
        return

    if not (license_number.startswith("DL") or license_number.startswith("AB")):
        messagebox.showerror("Error", "Invalid driver license number! Registration cancelled.")
        clear_entries()
        return

    # Simulate saving the data (In a real application, you would save this data to a database)
    print(f"Driver Registered:\nName: {name}\nEmail: {email}\nPhone Number: {phone}\nLicense Type: {license_type}\nLicense Number: {license_number}")

    messagebox.showinfo("Success", "Driver registered successfully!")
    clear_entries()

# Function to clear all entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    license_entry.delete(0, tk.END)
    license_type_var.set('')

# Initialize the main window
root = tk.Tk()
root.title("Driver License Verification")

# Create and place the widgets for driver registration
tk.Label(root, text="Driver Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Label(root, text="Phone Number:").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

tk.Label(root, text="Driver License Number:").pack(pady=5)
license_entry = tk.Entry(root)
license_entry.pack(pady=5)

tk.Label(root, text="License Type:").pack(pady=5)
license_type_var = tk.StringVar()
license_type_menu = tk.OptionMenu(root, license_type_var, "Commercial", "Non-Commercial")
license_type_menu.pack(pady=5)

register_button = tk.Button(root, text="Register Driver", command=register_driver)
register_button.pack(pady=10)

# Run the application
root.mainloop()
