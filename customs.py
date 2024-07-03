import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import string
from datetime import datetime, timedelta

# Sample in-memory storage for orders and customs data
orders = {}
customs_data = {}

# Function to generate a tracking number
def generate_tracking_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

# Function to generate a random delivery date within a week
def generate_delivery_date():
    today = datetime.today()
    delivery_date = today + timedelta(days=random.randint(1, 7))
    return delivery_date.strftime("%Y-%m-%d")

# Function to place an order
def place_order():
    item_description = item_description_entry.get()
    pickup_location = pickup_location_entry.get()
    delivery_location = delivery_location_entry.get()

    if not item_description or not pickup_location or not delivery_location:
        messagebox.showerror("Error", "All fields are required!")
        return

    tracking_number = generate_tracking_number()
    delivery_date = generate_delivery_date()

    orders[tracking_number] = {
        'item_description': item_description,
        'pickup_location': pickup_location,
        'delivery_location': delivery_location,
        'delivery_date': delivery_date
    }
    customs_data[tracking_number] = {
        "status": "Processing",
        "details": "Your package is being processed for customs.",
        "estimated_delivery": delivery_date
    }

    messagebox.showinfo("Success", f"Order placed successfully! Tracking number: {tracking_number}")
    item_description_entry.delete(0, tk.END)
    pickup_location_entry.delete(0, tk.END)
    delivery_location_entry.delete(0, tk.END)

# Function to check customs status
def check_customs_status():
    tracking_number = tracking_number_entry.get()
    if tracking_number in customs_data:
        status = customs_data[tracking_number]["status"]
        details = customs_data[tracking_number]["details"]
        estimated_delivery = customs_data[tracking_number]["estimated_delivery"]

        result_text.set(f"Status: {status}\nDetails: {details}\nEstimated Delivery: {estimated_delivery}")
    else:
        messagebox.showerror("Error", "Tracking number not found.")

# Initialize the main window
root = tk.Tk()
root.title("Order Placement and Customs Status")

# Create a canvas and scrollbar
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Define styles (optional)
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Create and place the widgets for order placement
tk.Label(scrollable_frame, text="Order Placement", font=title_font).pack(pady=10)

tk.Label(scrollable_frame, text="Item Description:", font=label_font).pack(pady=5)
item_description_entry = tk.Entry(scrollable_frame, font=entry_font)
item_description_entry.pack(pady=5)

tk.Label(scrollable_frame, text="Pickup Location:", font=label_font).pack(pady=5)
pickup_location_entry = tk.Entry(scrollable_frame, font=entry_font)
pickup_location_entry.pack(pady=5)

tk.Label(scrollable_frame, text="Delivery Location:", font=label_font).pack(pady=5)
delivery_location_entry = tk.Entry(scrollable_frame, font=entry_font)
delivery_location_entry.pack(pady=5)

place_order_button = tk.Button(scrollable_frame, text="Place Order", font=button_font, command=place_order)
place_order_button.pack(pady=10)

# Create and place the widgets for checking customs status
tk.Label(scrollable_frame, text="Check Customs Status", font=title_font).pack(pady=10)

tk.Label(scrollable_frame, text="Enter Tracking Number:", font=label_font).pack(pady=5)
tracking_number_entry = tk.Entry(scrollable_frame, font=entry_font)
tracking_number_entry.pack(pady=5)

check_button = tk.Button(scrollable_frame, text="Check Status", font=button_font, command=check_customs_status)
check_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(scrollable_frame, textvariable=result_text, justify="left", font=label_font)
result_label.pack(pady=5)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the application
root.mainloop()
