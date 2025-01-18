import tkinter as tk
from tkinter import ttk, messagebox
class Rom:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Order Management System ")
        self.menuitems={"Sushi": 2400,"Dimsum": 2500,"Bao": 1200,"Takoyaki": 1000,"Nigiri": 1300,"Sashimi": 2200,"Japanese Pizza": 1400,"Salads": 1200,"Grill": 3000,"Starters": 1800,"Curry/Rice": 2000,"Stone bowl": 4000,"Wok": 2000,"Mochi ice cream": 1000,"Mochi platter": 2700,"Boba": 900,"Bubble tea": 700,"Fun bottles": 800,"Aerated drinks": 600}
        self.er=90
        self.setupbg(room)