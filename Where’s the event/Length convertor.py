import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        label_result.config(text=f"{cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for inches.")

def clear():
    entry_inches.delete(0, tk.END)
    label_result.config(text="")

# Create the main application window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Create and place widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label_prompt = tk.Label(frame, text="Enter length in inches:")
label_prompt.grid(row=0, column=0, pady=5)

entry_inches = tk.Entry(frame, width=10)
entry_inches.grid(row=0, column=1, pady=5)

button_convert = tk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=1, column=0, pady=5)

button_clear = tk.Button(frame, text="Clear", command=clear)
button_clear.grid(row=1, column=1, pady=5)

label_result = tk.Label(frame, text="", font=("Arial", 14))
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()