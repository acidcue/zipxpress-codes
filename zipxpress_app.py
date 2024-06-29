import tkinter as tk
from tkinter import ttk

class FAQPage:
    def __init__(self, root):
        self.root = root
        self.root.title("FAQ Page")

        self.faq_data = {
            "What should I do if my package is delayed?": "Please contact our customer support team for assistance.",
            "How can I track my shipment?": "You can track your shipment in real-time using our mobile app. Just enter your tracking number.",
            "Do you provide international shipping?": "Yes, we offer international shipping services. Please check our app for available destinations.",
            "How can I change my delivery address?": "You can update your delivery address in the app settings or contact customer support for assistance.",
            "What payment methods do you accept?": "We accept major credit cards, PayPal, and other popular payment methods. You can view available options during checkout."
        }

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label_title = ttk.Label(self.frame, text="FAQs", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=(0, 20))

        self.questions = list(self.faq_data.keys())

        for question in self.questions:
            question_frame = ttk.Frame(self.frame, padding="10", relief=tk.SUNKEN)
            question_frame.pack(fill=tk.X, padx=20, pady=10)

            question_label = ttk.Label(question_frame, text=question, font=("Helvetica", 12, "bold"))
            question_label.pack(anchor=tk.W, padx=(10, 0), pady=(10, 0))

            answer_label = ttk.Label(question_frame, text=self.faq_data[question], wraplength=400)
            answer_label.pack(anchor=tk.W, padx=(10, 0), pady=(0, 10))

            # Bind click event to show/hide answer
            question_label.bind("<Button-1>", lambda event, label=answer_label: self.toggle_answer(label))

    def toggle_answer(self, label):
        current_state = label.cget("state")
        if current_state == tk.NORMAL:
            label.config(state=tk.HIDDEN)
        else:
            label.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    faq_page = FAQPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
