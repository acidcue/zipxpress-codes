import tkinter as tk
from tkinter import ttk
import random
import string

class GoodsTransportPage:
    def __init__(self, root, switch_to_payment):
        self.root = root
        self.switch_to_payment = switch_to_payment
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = ttk.Label(self.frame, text="Define Goods for Pickup and Transport", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Goods Details
        self.details_frame = ttk.Labelframe(self.frame, text="Goods Details", padding="10")
        self.details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.details_frame, text="Dimensions (L x W x H in cm):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.dimensions_entry = ttk.Entry(self.details_frame)
        self.dimensions_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.details_frame, text="Texture:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.texture_entry = ttk.Entry(self.details_frame)
        self.texture_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.details_frame, text="Size:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.size_entry = ttk.Entry(self.details_frame)
        self.size_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.details_frame, text="Preferred Vehicle Type:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.vehicle_type_entry = ttk.Entry(self.details_frame)
        self.vehicle_type_entry.grid(row=3, column=1, padx=5, pady=5)

        # Generate Tracking Number
        self.generate_button = ttk.Button(self.frame, text="Generate Tracking Number", command=self.generate_tracking_number)
        self.generate_button.pack(pady=10)

        # Result
        self.result_label = ttk.Label(self.frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def generate_tracking_number(self):
        dimensions = self.dimensions_entry.get()
        texture = self.texture_entry.get()
        size = self.size_entry.get()
        vehicle_type = self.vehicle_type_entry.get()

        if not dimensions or not texture or not size or not vehicle_type:
            self.result_label.config(text="Please fill in all fields!", foreground="red")
            return

        tracking_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        
        result_text = (f"Goods Details:\n"
                       f"Dimensions: {dimensions}\n"
                       f"Texture: {texture}\n"
                       f"Size: {size}\n"
                       f"Preferred Vehicle Type: {vehicle_type}\n\n"
                       f"Tracking Number: {tracking_number}")

        self.result_label.config(text=result_text, foreground="black")

        # Switch to Payment Page
        self.switch_to_payment()

class PaymentPage:
    def __init__(self, root):
        self.root = root
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        # Create the main frame with a scrollbar
        self.main_frame = ttk.Frame(self.frame, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        self.title_label = ttk.Label(self.main_frame, text="Payment and Invoicing", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Payment Form
        self.payment_frame = ttk.Labelframe(self.main_frame, text="Make a Payment", padding="10")
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
        card_number_pattern = re.compile(r"^\d{16}$")
        expiry_date_pattern = re.compile(r"^(0[1-9]|1[0-2])\/\d{2}$")
        cvv_pattern = re.compile(r"^\d{3}$")

        return (card_number_pattern.match(card_number) and
                expiry_date_pattern.match(expiry_date) and
                cvv_pattern.match(cvv))

    def submit_payment(self):
        payment_method = self.payment_method.get()
        if payment_method == "Card":
            card_number = self.card_number_entry.get()
            expiry_date = self.expiry_date_entry.get()
            cvv = self.cvv_entry.get()

            if not self.validate_card_details(card_number, expiry_date, cvv):
                self.status_label.config(text="Invalid card details!", foreground="red")
                return

            # Simulate card payment processing
            self.status_label.config(text="Payment successful!", foreground="green")
        elif payment_method == "Mobile Money":
            mobile_money_number = self.mobile_money_number_entry.get()
            service_provider = self.mobile_money_provider_entry.get()

            if not mobile_money_number or not service_provider:
                self.status_label.config(text="Please fill in all mobile money details!", foreground="red")
                return

            # Simulate mobile money payment processing
            self.status_label.config(text="Payment successful!", foreground="green")

def switch_to_payment():
    # Clear the current frame and switch to Payment Page
    for widget in root.winfo_children():
        widget.destroy()
    PaymentPage(root)

def main():
    global root
    root = tk.Tk()
    root.geometry("800x600")

    GoodsTransportPage(root, switch_to_payment)
    root.mainloop()

if __name__ == "__main__":
    main()
