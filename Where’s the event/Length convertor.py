
import tkinter as tk

def le():
    """Convert the value for inches to centimeters and insert the
    result into lbl_result.
    """
    inches = ent_length.get()
    centimeters = (2.5) * inches
    lbl_result["text"] = f"{round(centimeters, 2)} \N{CENTIMETERS}"

window = tk.Tk()
window.title("Length Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_length = tk.Entry(master=frm_entry, width=10)
lbl_length= tk.Label(master=frm_entry, text="\N{inches}")

ent_length.grid(row=0, column=0, sticky="e")
lbl_length.grid(row=0, column=1, sticky="w")
btn_convert = tk.Button(
    master=window,
    text="-->",
    command=le
)
lbl_result = tk.Label(master=window, text="\N{centimeters}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()