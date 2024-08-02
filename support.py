import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

class SupportPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Care - Support Page")
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
        self.title_label = ttk.Label(self.scrollable_frame, text="Customer Support", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        # Contact Information
        self.contact_info_frame = ttk.Labelframe(self.scrollable_frame, text="Contact Information", padding="10")
        self.contact_info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.contact_info_frame, text="Email: zipxpress234@outlook.com", font=("Helvetica", 12)).pack(anchor=tk.W, padx=5, pady=2)
        ttk.Label(self.contact_info_frame, text="Phone: +233257889765", font=("Helvetica", 12)).pack(anchor=tk.W, padx=5, pady=2)

        # Contact Form
        self.contact_frame = ttk.Labelframe(self.scrollable_frame, text="Contact Us", padding="10")
        self.contact_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.contact_frame, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.contact_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.contact_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.email_entry = ttk.Entry(self.contact_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.contact_frame, text="Message:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.message_entry = ScrolledText(self.contact_frame, height=5)
        self.message_entry.grid(row=2, column=1, padx=5, pady=5)

        self.submit_button = ttk.Button(self.contact_frame, text="Submit", command=self.submit_contact_form)
        self.submit_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

        # FAQ Section
        self.faq_frame = ttk.Labelframe(self.scrollable_frame, text="FAQs", padding="10")
        self.faq_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        faqs = {
            "What should I do if my package is delayed?": "Please contact our customer support team for assistance.",
            "How can I track my shipment?": "You can track your shipment in real-time using our mobile app. Just enter your tracking number.",
            "Do you provide international shipping?": "Yes, we offer international shipping services. Please check our app for available destinations.",
            "How can I change my delivery address?": "You can update your delivery address in the app settings or contact customer support for assistance.",
            "What payment methods do you accept?": "We accept major credit cards, PayPal, and other popular payment methods. You can view available options during checkout."
        }

        for question, answer in faqs.items():
            question_label = ttk.Label(self.faq_frame, text=question, font=("Helvetica", 12, "bold"))
            question_label.pack(anchor=tk.W, padx=5, pady=5)
            answer_label = ttk.Label(self.faq_frame, text=answer, wraplength=500)
            answer_label.pack(anchor=tk.W, padx=5, pady=5)

        # Feedback Section
        self.feedback_frame = ttk.Labelframe(self.scrollable_frame, text="Feedback", padding="10")
        self.feedback_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Label(self.feedback_frame, text="Please provide your feedback:").pack(anchor=tk.W, padx=5, pady=5)
        self.feedback_entry = ScrolledText(self.feedback_frame, height=5)
        self.feedback_entry.pack(fill=tk.BOTH, padx=5, pady=5)

        self.feedback_button = ttk.Button(self.feedback_frame, text="Submit Feedback", command=self.submit_feedback)
        self.feedback_button.pack(anchor=tk.E, padx=5, pady=5)

    def submit_contact_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        message = self.message_entry.get("1.0", tk.END).strip()

        if not name or not email or not message:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Simulate form submission
        messagebox.showinfo("Submitted", "Your message has been sent. We will contact you shortly.")
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.message_entry.delete("1.0", tk.END)

    def submit_feedback(self):
        feedback = self.feedback_entry.get("1.0", tk.END).strip()

        if not feedback:
            messagebox.showerror("Error", "Feedback cannot be empty!")
            return

        # Simulate feedback submission
        messagebox.showinfo("Submitted", "Thank you for your feedback!")
        self.feedback_entry.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = SupportPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
