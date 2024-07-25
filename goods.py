import tkinter as tk
from tkinter import ttk
import random
import string
import re
from datetime import datetime, timedelta

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class GoodsTransportPage(ScrollableFrame):
    def __init__(self, container, switch_to_payment):
        super().__init__(container)
        self.switch_to_payment = switch_to_payment
        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = ttk.Label(self.scrollable_frame, text="Define Goods for Pickup and Transport", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Goods Details
        self.details_frame = ttk.Labelframe(self.scrollable_frame, text="Goods Details", padding="10")
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

        # Vehicle Type Dropdown
        ttk.Label(self.details_frame, text="Preferred Vehicle Type:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.vehicle_type_var = tk.StringVar()
        self.vehicle_type_dropdown = ttk.Combobox(self.details_frame, textvariable=self.vehicle_type_var)
        self.vehicle_type_dropdown['values'] = ("Van", "Truck", "Motorbike", "Bicycle")
        self.vehicle_type_dropdown.grid(row=3, column=1, padx=5, pady=5)

        # Make Payment Button
        self.payment_button = ttk.Button(self.scrollable_frame, text="Make Payment", command=self.switch_to_payment)
        self.payment_button.pack(pady=10)

class PaymentPage(ScrollableFrame):
    def __init__(self, container, switch_to_tracking):
        super().__init__(container)
        self.switch_to_tracking = switch_to_tracking
        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.main_frame = ttk.Frame(self.scrollable_frame, padding="20")
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

        # Payment Method Buttons
        self.card_button = ttk.Button(self.payment_frame, text="Pay with Card", command=self.select_card)
        self.card_button.grid(row=4, column=0, padx=5, pady=5)

        self.mobile_money_button = ttk.Button(self.payment_frame, text="Pay with Mobile Money", command=self.select_mobile_money)
        self.mobile_money_button.grid(row=4, column=1, padx=5, pady=5)

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
        self.service_provider_var = tk.StringVar()
        self.service_provider_dropdown = ttk.Combobox(self.mobile_money_frame, textvariable=self.service_provider_var)
        self.service_provider_dropdown['values'] = ("MTN", "TELECEL", "AT")
        self.service_provider_dropdown.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(self.payment_frame, text="Submit Payment", command=self.submit_payment)
        self.submit_button.grid(row=6, column=1, padx=5, pady=10, sticky=tk.E)

        self.status_label = ttk.Label(self.payment_frame, text="")
        self.status_label.grid(row=7, column=0, columnspan=2, pady=10)

    def select_card(self):
        self.card_frame.grid()
        self.mobile_money_frame.grid_remove()

    def select_mobile_money(self):
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
        # Simulate payment processing
        self.status_label.config(text="Payment successful!", foreground="green")
        
        # Generate a tracking number and switch to tracking page
        tracking_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.switch_to_tracking(tracking_number)

class TrackingPage(ScrollableFrame):
    def __init__(self, container, tracking_number):
        super().__init__(container)
        self.tracking_number = tracking_number
        self.create_widgets()

    def create_widgets(self):
        # Title
        self.title_label = ttk.Label(self.scrollable_frame, text="Tracking and Customs Information", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Tracking Details
        self.tracking_frame = ttk.Labelframe(self.scrollable_frame, text="Track Your Goods", padding="10")
        self.tracking_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.tracking_frame, text="Tracking Number:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.tracking_number_label = ttk.Label(self.tracking_frame, text=self.tracking_number)
        self.tracking_number_label.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.tracking_frame, text="Estimated Delivery Date:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.estimated_delivery_label = ttk.Label(self.tracking_frame, text=self.get_estimated_delivery_date())
        self.estimated_delivery_label.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.tracking_frame, text="Customs Status:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.customs_status_label = ttk.Label(self.tracking_frame, text=self.get_customs_status())
        self.customs_status_label.grid(row=2, column=1, padx=5, pady=5)

        # Track Button
        self.track_button = ttk.Button(self.tracking_frame, text="Check Delivery Progress", command=self.check_delivery)
        self.track_button.grid(row=3, column=1, padx=5, pady=10, sticky=tk.E)

    def get_estimated_delivery_date(self):
        # Simulate an estimated delivery date (e.g., 5 days from today)
        pickup_date = datetime.now()
        estimated_delivery_date = pickup_date + timedelta(days=5)
        return estimated_delivery_date.strftime("%Y-%m-%d")

    def get_customs_status(self):
        # Simulate customs status
        return "Cleared"

    def check_delivery(self):
        # Simulate tracking functionality
        progress = "In transit"
        self.estimated_delivery_label.config(text=f"Status: {progress}")

class TransportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Goods Transport Service")

        # Create a container frame for all pages
        self.container = ttk.Frame(root)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Initialize the pages but do not show them yet
        self.goods_transport_page = GoodsTransportPage(self.container, self.show_payment_page)
        self.payment_page = PaymentPage(self.container, self.show_tracking_page)
        self.tracking_page = None  # Tracking page is created dynamically

        # Show the first page
        self.show_goods_transport_page()

    def show_goods_transport_page(self):
        self.goods_transport_page.pack(fill=tk.BOTH, expand=True)
        self.payment_page.pack_forget()
        if self.tracking_page:
            self.tracking_page.pack_forget()

    def show_payment_page(self):
        self.goods_transport_page.pack_forget()
        self.payment_page.pack(fill=tk.BOTH, expand=True)
        if self.tracking_page:
            self.tracking_page.pack_forget()

    def show_tracking_page(self, tracking_number):
        if self.tracking_page is None:
            self.tracking_page = TrackingPage(self.container, tracking_number)
        else:
            self.tracking_page.tracking_number = tracking_number
        self.goods_transport_page.pack_forget()
        self.payment_page.pack_forget()
        self.tracking_page.pack(fill=tk.BOTH, expand=True)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = TransportApp(root)
    root.mainloop()
