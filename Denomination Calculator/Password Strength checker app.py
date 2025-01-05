import tkinter as tk
from tkinter import messagebox
import re
def check_password_strength():
    password = entry_password.get()
    if len(password) < 8:
        label_result.config(text="Weak: Password must be at least 8 characters long.", fg="red")
    elif not re.search(r"[A-Z]", password):
        label_result.config(text="Weak: Password must contain at least one uppercase letter.", fg="red")
    elif not re.search(r"[a-z]", password):
        label_result.config(text="Weak: Password must contain at least one lowercase letter.", fg="red")
    elif not re.search(r"[0-9]", password):
        label_result.config(text="Weak: Password must contain at least one digit.", fg="red")
    elif not re.search(r"[@$!%*?&#]", password):
        label_result.config(text="Moderate: Adding a special character will make it stronger.", fg="orange")
    else:
        label_result.config(text="Strong: Great job!", fg="green")
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16))
title_label.pack(pady=10)
frame_input = tk.Frame(root)
frame_input.pack(pady=10)
label_password = tk.Label(frame_input, text="Enter Password:")
label_password.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_password = tk.Entry(frame_input, show="*", width=30)
entry_password.grid(row=0, column=1, padx=5, pady=5)
btn_check = tk.Button(root, text="Check Strength", command=check_password_strength)
btn_check.pack(pady=10)
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)
root.mainloop()