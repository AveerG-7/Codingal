from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry('300x400')
lbl1 = Label(text="Enter the first number",fg='white',bg='blue',height =1,wdith=300)
number1_entry = Entry.get
lbl2 = Label(text="Enter the second number",fg='white',bg='blue',height=1,width=300)
number2_entry=Entry.get
btn = Button(text="Add",height= 1, bg = "#1261A0",fg = 'white',command = add)
btn = Button(text="Subtract",height= 1, bg = "#1261A0",fg = 'white',command = sub)
btn = Button(text="Multiply",height= 1, bg = "#1261A0",fg = 'white',command = mul)
btn = Button(text="Divide",height= 1, bg = "#1261A0",fg = 'white',command = div)
def add():
    lbl1.get + lbl2.get
def sub():
    lbl1.get - lbl2.get
def mul():
    lbl1.get * lbl2.get
def div():
    lbl1.get * lbl2.get

def display():
    text_box.insert(END,add)
    text_box.insert(END,sub)
    text_box.insert(END,mul)
    text_box.insert(END,div)
add.pack
sub.pack
mul.pack
div.pack
lbl1.pack
lbl2.pack
btn.pack
text_box.pack
display.pack







