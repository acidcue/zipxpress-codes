import tkinter as tk
from tkinter import ttk, messagebox
import re

class PaymentPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Payment and Invoicing")
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
        self.title_label = ttk.Label(self.scrollable_frame, text="Payment and Invoicing", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Payment Form
        self.payment_frame = ttk.Labelframe(self.scrollable_frame, text="Make a Payment", padding="10")
        self.payment_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.payment_frame, text="Full Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.payment_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.payment_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.payment_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.payment_frame, text="Phone:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.phone_entry = ttk.Entry(self.payment_frame)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.payment_frame, text="Amount:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.payment_frame)
        self.amount_entry.grid(row=3, column=1, padx=5, pady=5)

        # Payment Method
        ttk.Label(self.payment_frame, text="Payment Method:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.payment_method = tk.StringVar()
        self.payment_method.set("Mobile Money")  # default value

        methods = ["Mobile Money", "Card"]
        self.payment_method_menu = ttk.OptionMenu(self.payment_frame, self.payment_method, *methods)
        self.payment_method_menu.grid(row=4, column=1, padx=5, pady=5)

        # Payment Details (for card)
        self.card_frame = ttk.Labelframe(self.payment_frame, text="Card Details", padding="10")
        self.card_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.card_frame.grid_remove()

        ttk.Label(self.card_frame, text="Card Number:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.card_number_entry = ttk.Entry(self.card_frame)
        self.card_number_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.card_frame, text="Expiry Date (MM/YY):").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.expiry_date_entry = ttk.Entry(self.card_frame)
        self.expiry_date_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.card_frame, text="CVV:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.cvv_entry = ttk.Entry(self.card_frame, show='*')
        self.cvv_entry.grid(row=2, column=1, padx=5, pady=5)

        # Payment Details (for mobile money)
        self.mobile_money_frame = ttk.Labelframe(self.payment_frame, text="Mobile Money Details", padding="10")
        self.mobile_money_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.mobile_money_frame.grid_remove()

        ttk.Label(self.mobile_money_frame, text="Mobile Money Number:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.mobile_money_number_entry = ttk.Entry(self.mobile_money_frame)
        self.mobile_money_number_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.mobile_money_frame, text="Service Provider:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.mobile_money_provider_entry = ttk.Entry(self.mobile_money_frame)
        self.mobile_money_provider_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(self.payment_frame, text="Submit Payment", command=self.submit_payment)
        self.submit_button.grid(row=6, column=1, padx=5, pady=10, sticky=tk.E)

        self.status_label = ttk.Label(self.payment_frame, text="")
        self.status_label.grid(row=7, column=0, columnspan=2, pady=10)

        self.payment_method.trace("w", self.update_payment_method)

    def update_payment_method(self, *args):
        if self.payment_method.get() == "Card":
            self.card_frame.grid()
            self.mobile_money_frame.grid_remove()
        elif self.payment_method.get() == "Mobile Money":
            self.mobile_money_frame.grid()
            self.card_frame.grid_remove()

    def validate_card_details(self, card_number, expiry_date, cvv):
        # Simple validation for card details
        card_number_pattern = re.compile(r"^\d{16}$")
        expiry_date_pattern = re.compile(r"^(0[1-9]|1[0-2])\/\d{2}$")
        cvv_pattern = re.compile(r"^\d{3}$")

        if not card_number_pattern.match(card_number):
            return False, "Invalid card number. Must be 16 digits."
        if not expiry_date_pattern.match(expiry_date):
            return False, "Invalid expiry date. Must be MM/YY."
        if not cvv_pattern.match(cvv):
            return False, "Invalid CVV. Must be 3 digits."

        return True, "Valid"

    def submit_payment(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        amount = self.amount_entry.get()
        payment_method = self.payment_method.get()

        if not name or not email or not phone or not amount:
            messagebox.showerror("Error", "All fields are required!")
            return

        if payment_method == "Card":
            card_number = self.card_number_entry.get()
            expiry_date = self.expiry_date_entry.get()
            cvv = self.cvv_entry.get()

            valid, message = self.validate_card_details(card_number, expiry_date, cvv)
            if not valid:
                messagebox.showerror("Payment Declined", message)
                return
        elif payment_method == "Mobile Money":
            mobile_money_number = self.mobile_money_number_entry.get()
            mobile_money_provider = self.mobile_money_provider_entry.get()
            if not mobile_money_number or not mobile_money_provider:
                messagebox.showerror("Error", "All mobile money details are required!")
                return

        # Simulate payment submission
        payment_info = f"Payment Details:\nName: {name}\nEmail: {email}\nPhone: {phone}\nAmount: {amount}\nMethod: {payment_method}"
        if payment_method == "Card":
            payment_info += f"\nCard Number: {card_number}\nExpiry Date: {expiry_date}"
        elif payment_method == "Mobile Money":
            payment_info += f"\nMobile Money Number: {mobile_money_number}\nService Provider: {mobile_money_provider}"

        messagebox.showinfo("Payment Successful", payment_info)

        self.status_label.config(text="Payment Successful!")

        # Clear fields
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.card_number_entry.delete(0, tk.END)
        self.expiry_date_entry.delete(0, tk.END)
        self.cvv_entry.delete(0, tk.END)
        self.mobile_money_number_entry.delete(0, tk.END)
        self.mobile_money_provider_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = PaymentPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
