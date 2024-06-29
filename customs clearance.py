import tkinter as tk
from tkinter import messagebox

# Sample data for customs status
customs_data = {
    "123": {
        "status": "Cleared",
        "details": "Your package has cleared customs.",
        "estimated_delivery": "2024-06-25"
    },
    "456": {
        "status": "Pending",
        "details": "Your package is currently being processed by customs.",
        "estimated_delivery": "2024-06-28"
    }
}

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
root.title("Customs Clearance")

# Create and place the widgets
tracking_number_label = tk.Label(root, text="Enter Tracking Number:")
tracking_number_label.pack(pady=5)

tracking_number_entry = tk.Entry(root)
tracking_number_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Status", command=check_customs_status)
check_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left")
result_label.pack(pady=5)

# Run the application
root.mainloop()
