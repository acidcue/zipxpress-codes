import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import datetime

class BookingPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Booking and Scheduling")
        self.root.geometry("600x600")

        self.create_widgets()

    def create_widgets(self):
        # Create the main frame with a scrollbar
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame)
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Title
        self.title_label = ttk.Label(self.scrollable_frame, text="Booking and Scheduling", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Booking Form
        self.booking_frame = ttk.Labelframe(self.scrollable_frame, text="Book an Appointment", padding="10")
        self.booking_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.booking_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.booking_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.booking_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.booking_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.booking_frame, text="Phone:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.booking_frame)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.booking_frame, text="Date:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.date_entry = DateEntry(self.booking_frame, date_pattern='y-mm-dd', mindate=datetime.date.today())
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.booking_frame, text="Time:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.time_entry = ttk.Combobox(self.booking_frame, values=[f"{h:02}:{m:02}" for h in range(24) for m in (0, 30)])
        self.time_entry.grid(row=4, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(self.booking_frame, text="Submit", command=self.submit_booking)
        self.submit_button.grid(row=5, column=1, padx=5, pady=10, sticky=tk.E)

        self.status_label = ttk.Label(self.booking_frame, text="")
        self.status_label.grid(row=6, column=0, columnspan=2, pady=10)

    def submit_booking(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        if not name or not email or not phone or not date or not time:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Simulate booking submission
        booking_info = f"Booking Details:\nName: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}"
        messagebox.showinfo("Booking Confirmed", booking_info)

        self.status_label.config(text="Booking Confirmed!")

        # Clear fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.date_entry.set_date(datetime.date.today())
        self.time_entry.set('')

def main():
    root = tk.Tk()
    app = BookingPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
