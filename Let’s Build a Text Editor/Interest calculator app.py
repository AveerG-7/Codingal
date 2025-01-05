import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        simple_interest = (principal * rate * time) / 100
        label_result.config(text=f"Simple Interest: {simple_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for all fields.")

# Create the main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("300x250")

# Title label
title_label = tk.Label(root, text="Simple Interest Calculator", font=("Arial", 16))
title_label.pack(pady=10)

# Input fields
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

label_principal = tk.Label(frame_inputs, text="Principal (P):")
label_principal.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_principal = tk.Entry(frame_inputs)
entry_principal.grid(row=0, column=1, padx=5, pady=5)

label_rate = tk.Label(frame_inputs, text="Rate (%) (R):")
label_rate.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_rate = tk.Entry(frame_inputs)
entry_rate.grid(row=1, column=1, padx=5, pady=5)

label_time = tk.Label(frame_inputs, text="Time (T):")
label_time.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_time = tk.Entry(frame_inputs)
entry_time.grid(row=2, column=1, padx=5, pady=5)

# Calculate button
btn_calculate = tk.Button(root, text="Calculate", command=calculate_interest)
btn_calculate.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

# Run the application
root.mainloop()