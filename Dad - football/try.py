import turtle
import tkinter as tk
from tkinter import messagebox
import random

# Define a dictionary to store player stats
players = {
    "Lionel Messi": {"pace": 80, "shooting": 84, "passing": 88, "dribbling": 92, "defending": 36, "physicality": 63},
    "Cristiano Ronaldo": {"pace": 76, "shooting": 88, "passing": 77, "dribbling": 80, "defending": 39, "physicality": 79},
    "Kylian Mbappé": {"pace": 97, "shooting": 88, "passing": 78, "dribbling": 90, "defending": 41, "physicality": 79},
    "Neymar Jr.": {"pace": 89, "shooting": 83, "passing": 86, "dribbling": 94, "defending": 37, "physicality": 58},
    # Add more players...
}

player_score = 0
computer_score = 0

# Game logic for football player card comparison
def get_stat_value(player, stat):
    return players[player][stat]

def compare_stats(player1, player2, stat):
    value1 = get_stat_value(player1, stat)
    value2 = get_stat_value(player2, stat)

    if value1 > value2:
        return player1
    elif value2 > value1:
        return player2
    else:
        return "Draw"

# Football card game starts when a level is clicked
def start_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    while True:
        # Randomly select players for comparison
        player1 = random.choice(list(players.keys()))
        player2 = random.choice(list(players.keys()))
        while player1 == player2:
            player2 = random.choice(list(players.keys()))

        print(f"\nPlayer 1: {player1}")
        print(f"Player 2: {player2}")

        # Display player 1's card
        print(f"\nPlayer 1: {player1}")
        print(f"Pace: {players[player1]['pace']}")
        print(f"Shooting: {players[player1]['shooting']}")
        print(f"Passing: {players[player1]['passing']}")
        print(f"Dribbling: {players[player1]['dribbling']}")
        print(f"Defending: {players[player1]['defending']}")
        print(f"Physicality: {players[player1]['physicality']}")

        # User selects the stat to compare
        chosen_stat = input("Choose a stat to compare (pace, shooting, passing, dribbling, defending, physicality): ").lower()
        if chosen_stat not in players[player1]:
            print("Invalid stat. Please choose a valid stat.")
            continue

        # Compare the chosen stat between player1 and player2
        winner = compare_stats(player1, player2, chosen_stat)
        if winner == player1:
            print(f"{player1} wins this round!")
            player_score += 1
        elif winner == player2:
            print(f"{player2} wins this round!")
            computer_score += 1
        else:
            print("It's a draw!")

        # Show the current score
        print(f"\nCurrent Score: Player {player_score} - Computer {computer_score}")

        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Final Score: Player {player_score} - Computer {computer_score}")
            break

# Start of graphical home screen using Turtle and Tkinter
# Initialize turtle window
screen = turtle.Screen()
screen.title("Football Home Screen")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")

# Create a turtle object for drawing the screen layout
drawer = turtle.Turtle()
drawer.hideturtle()

# Global points variable for level unlocking
points = 0

# Username (top-left)
drawer.penup()
drawer.goto(-350, 250)
a = input("Enter username:")
drawer.write(f"Username: {a}", align="left", font=("Arial", 14, "bold"))

# Points and Gems (top-middle)
drawer.goto(-50, 250)
drawer.write("Points: 0 | Gems: 0", align="center", font=("Arial", 14, "bold"))

# Leaderboard button (top-right)
def show_leaderboard():
    leaderboard_window = tk.Tk()
    leaderboard_window.title("Leaderboard")
    ranks = "Rank 1: Player1\nRank 2: Player2\nRank 3: Player3\n...\nRank 10: Player10"
    label = tk.Label(leaderboard_window, text=ranks, font=("Arial", 12))
    label.pack()
    leaderboard_window.mainloop()

drawer.goto(250, 250)
drawer.write("[Leaderboard]", align="right", font=("Arial", 14, "underline"))

# Bind leaderboard click
def leaderboard_click(x, y):
    if 200 < x < 350 and 230 < y < 270:
        show_leaderboard()

screen.onscreenclick(leaderboard_click)

# Game Shop button (left-middle)
def open_game_shop():
    messagebox.showinfo("Game Shop", "Welcome to the Game Shop!")

drawer.goto(-350, 100)
drawer.write("[Game Shop]", align="left", font=("Arial", 14, "bold"))

# Player Details button (center)
def show_player_details():
    messagebox.showinfo("Player Details", "Player details and stats for the account.")

drawer.goto(-50, 0)
drawer.write("[Player Details]", align="center", font=("Arial", 18, "bold"))

# Team view button (right-middle)
def show_team_view():
    messagebox.showinfo("Team View", "Team View with all players and team rating.")

drawer.goto(250, 100)
drawer.write("[Team: 85]", align="right", font=("Arial", 14, "bold"))

# Play button (below team view)
def open_levels():
    levels_window = tk.Tk()
    levels_window.title("Play Levels")
    
    # Create buttons for each level
    def create_level_button(text, command, color, row, column):
        button = tk.Button(levels_window, text=text, command=command, bg=color, font=("Arial", 12))
        button.grid(row=row, column=column, padx=20, pady=20)

    def level_unlocked(level, cost, reward):
        if messagebox.askyesno("Play Level", f"Play Level {level}?\nCost: {cost} points\nReward: {reward} points"):
            start_game()  # Launch the card game when a level is played

    create_level_button("Level 1", lambda: level_unlocked(1, 20, 50), "green", 0, 0)
    create_level_button("Level 2", lambda: level_unlocked(2, 200, 500), "green" if points >= 1000 else "grey", 0, 1)
    create_level_button("Level 3", lambda: level_unlocked(3, 2500, 4000), "green" if points >= 5000 else "grey", 1, 0)
    create_level_button("Level 4", lambda: level_unlocked(4, 5000, 7500), "green" if points >= 10000 else "grey", 1, 1)
    create_level_button("Level 5", lambda: level_unlocked(5, 10000, 15000), "green" if points >= 20000 else "grey", 2, 0)

    levels_window.mainloop()

drawer.goto(250, 50)
drawer.write("[Play]", align="right", font=("Arial", 14, "bold"))

# Market and Quests buttons (bottom)
def open_market():
    messagebox.showinfo("Market", "Welcome to the Market!")

def open_quests():
    messagebox.showinfo("Quests", "Here are your quests!")

drawer.goto(-200, -200)
drawer.write("[Market]", align="center", font=("Arial", 14, "bold"))

drawer.goto(200, -200)
drawer.write("[Quests]", align="center", font=("Arial", 14, "bold"))

# Handle button clicks for Market and Quests
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

