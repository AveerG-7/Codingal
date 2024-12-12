from tkinter import *

# Initialize window
window = Tk()
window.title("Calculator")
window.geometry('300x400')

# Define widgets
lbl1 = Label(window, text="Enter the first number", fg='white', bg='blue', height=1, width=30)
number1_entry = Entry(window)

lbl2 = Label(window, text="Enter the second number", fg='white', bg='blue', height=1, width=30)
number2_entry = Entry(window)

result_label = Label(window, text="Result:", height=1, width=30)

def add():
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid Input")

def sub():
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        result = num1 - num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid Input")

def mul():
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        result = num1 * num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid Input")

def div():
    try:
        num1 = float(number1_entry.get())
        num2 = float(number2_entry.get())
        if num2 == 0:
            result_label.config(text="Error: Division by zero")
        else:
            result = num1 / num2
            result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid Input")

# Buttons
btn_add = Button(window, text="Add", height=1, bg="#1261A0", fg='white', command=add)
btn_sub = Button(window, text="Subtract", height=1, bg="#1261A0", fg='white', command=sub)
btn_mul = Button(window, text="Multiply", height=1, bg="#1261A0", fg='white', command=mul)
btn_div = Button(window, text="Divide", height=1, bg="#1261A0", fg='white', command=div)

# Layout
lbl1.pack(pady=5)
number1_entry.pack(pady=5)
lbl2.pack(pady=5)
number2_entry.pack(pady=5)
btn_add.pack(pady=5)
btn_sub.pack(pady=5)
btn_mul.pack(pady=5)
btn_div.pack(pady=5)
result_label.pack(pady=10)

# Run the application
window.mainloop()
