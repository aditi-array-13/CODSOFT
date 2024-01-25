# CodSoft
# Task 3
# Password Generator

import tkinter as tk
from tkinter import ttk
import string
import random


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self.root, text="Password Generator", font=("Helvetica", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        length_label = ttk.Label(self.root, text="Password Length:")
        length_label.grid(row=1, column=0, pady=5, padx=5, sticky='e')

        self.length_entry = ttk.Entry(self.root)
        self.length_entry.grid(row=1, column=1, pady=5, padx=5, sticky='w')

        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_and_display_password)
        generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_and_display_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                self.result_label.config(text="Please enter a valid length.")
                return

            password = self.generate_password(length)
            self.result_label.config(text="Generated Password: " + password)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
