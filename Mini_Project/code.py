import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Calculator with History")
root.geometry("400x500")

# History list
history = []

# Entry field
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2)
entry.pack(pady=10)
