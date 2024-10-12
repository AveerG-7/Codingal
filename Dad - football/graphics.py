import turtle
from tkinter import messagebox
import tkinter as tk

# Initialize turtle window
screen = turtle.Screen()
screen.title("Football Home Screen")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create a turtle object for drawing the screen layout
drawer = turtle.Turtle()
drawer.hideturtle()

# Global points variable for level unlocking
points = 20

# Username (top-left)
def write_username():
    global a
    a = screen.textinput("Username", "Enter username:")
    if a:
        drawer.penup()
        drawer.goto(-350, 250)
        drawer.write(f"Username: {a}", align="left", font=("Arial", 14, "bold"))
        
write_username()

# Points and Gems (top-middle)
def update_points_and_gems():
    drawer.penup()
    drawer.goto(-50, 250)
    drawer.clear()  # Clear previous points display before updating
    drawer.write(f"Points: {points} | Gems: 0", align="center", font=("Arial", 14, "bold"))

update_points_and_gems()

# Leaderboard button (top-right)
def show_leaderboard():
    leaderboard_window = tk.Tk()
    leaderboard_window.title("Leaderboard")
    ranks = "Rank 1: Player1\nRank 2: Player2\nRank 3: Player3\n...\nRank 10: Player10"
    label = tk.Label(leaderboard_window, text=ranks, font=("Arial", 12))
    label.pack()
    leaderboard_window.mainloop()

drawer.penup()
drawer.goto(250, 250)
drawer.write("[Leaderboard]", align="right", font=("Arial", 14, "underline"))

# Game Shop button (left-middle)
def open_game_shop():
    messagebox.showinfo("Game Shop", "Welcome to the Game Shop!")

drawer.penup()
drawer.goto(-350, 100)
drawer.write("[Game Shop]", align="left", font=("Arial", 14, "bold"))

# Player Details button (center)
def show_player_details():
    messagebox.showinfo("Player Details", "Player details and stats for the account.")

drawer.penup()
drawer.goto(-50, 0)
drawer.write("[Player Details]", align="center", font=("Arial", 18, "bold"))

# Team view button (right-middle)
def show_team_view():
    messagebox.showinfo("Team View", "Team View with all players and team rating.")

drawer.penup()
drawer.goto(250, 100)
drawer.write("[Team: 85]", align="right", font=("Arial", 14, "bold"))

# Play button (below team view)
def open_levels():
    levels_window = tk.Tk()
    levels_window.title("Play Levels")
    
    def level_unlocked(level, cost, reward):
        global points
        if points >= cost:
            points -= cost
            messagebox.showinfo("Level", f"Played Level {level}! You earned {reward} points.")
            points += reward
            update_points_and_gems()
        else:
            messagebox.showwarning("Insufficient Points", f"You need {cost} points to play Level {level}.")

    def create_level_button(text, command, color, row, column):
        button = tk.Button(levels_window, text=text, command=command, bg=color, font=("Arial", 12))
        button.grid(row=row, column=column, padx=20, pady=20)

    create_level_button("Level 1", lambda: level_unlocked(1, 20, 50), "green", 0, 0)
    create_level_button("Level 2", lambda: level_unlocked(2, 200, 500), "green" if points >= 200 else "grey", 0, 1)
    create_level_button("Level 3", lambda: level_unlocked(3, 2500, 4000), "green" if points >= 2500 else "grey", 1, 0)
    create_level_button("Level 4", lambda: level_unlocked(4, 5000, 7500), "green" if points >= 5000 else "grey", 1, 1)
    create_level_button("Level 5", lambda: level_unlocked(5, 10000, 15000), "green" if points >= 10000 else "grey", 2, 0)

    levels_window.mainloop()

drawer.penup()
drawer.goto(250, 50)
drawer.write("[Play]", align="right", font=("Arial", 14, "bold"))

# Market and Quests buttons (bottom)
def open_market():
    messagebox.showinfo("Market", "Welcome to the Market!")

def open_quests():
    messagebox.showinfo("Quests", "Here are your quests!")

drawer.penup()
drawer.goto(-200, -200)
drawer.write("[Market]", align="center", font=("Arial", 14, "bold"))

drawer.penup()
drawer.goto(200, -200)
drawer.write("[Quests]", align="center", font=("Arial", 14, "bold"))

# Handle button clicks
def button_click(x, y):
    if -250 < x < -150 and -220 < y < -180:
        open_market()
    elif 150 < x < 250 and -220 < y < -180:
        open_quests()
    elif 200 < x < 350 and 50 < y < 100:
        open_levels()
    elif 200 < x < 350 and 100 < y < 140:
        show_team_view()
    elif -100 < x < 100 and -30 < y < 30:
        show_player_details()
    elif -350 < x < -250 and 80 < y < 120:
        open_game_shop()

# Bind the screen to detect clicks on buttons
screen.onscreenclick(button_click)

# Keep the screen open
try:
    turtle.mainloop()
except turtle.Terminator:
    pass
