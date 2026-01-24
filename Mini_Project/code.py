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


# ---------- Functions ----------
def click(value):
    entry.insert(tk.END, value)


def clear_entry():
    entry.delete(0, tk.END)


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        history.append(f"{expression} = {result}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        update_history()
    except:
        messagebox.showerror("Error", "Invalid Expression")


def update_history():
    history_box.delete(0, tk.END)
    for item in history:
        history_box.insert(tk.END, item)


def clear_history():
    history.clear()
    history_box.delete(0, tk.END)


# ---------- Buttons ----------
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(button_frame, text=button, width=10, height=2,
                        command=calculate)
    else:
        btn = tk.Button(button_frame, text=button, width=10, height=2,
                        command=lambda b=button: click(b))

    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear button
clear_btn = tk.Button(root, text="Clear", width=20, command=clear_entry)
clear_btn.pack(pady=5)

# ---------- History Section ----------
tk.Label(root, text="History", font=("Arial", 14)).pack()

history_box = tk.Listbox(root, width=45, height=8)
history_box.pack(pady=5)

clear_history_btn = tk.Button(root, text="Clear History", command=clear_history)
clear_history_btn.pack(pady=5)

# Run the application
root.mainloop()