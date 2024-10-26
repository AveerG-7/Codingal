import turtle
import random
import sqlite3

# Database Setup
conn = sqlite3.connect('football_game.db')
cursor = conn.cursor()

# Create player table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT,
    speed INTEGER,
    passing INTEGER,
    shooting INTEGER,
    defending INTEGER,
    stamina INTEGER
)
''')

# Insert sample players (comment this out if the players are already in the database)
sample_players = [
    ("Player 1", 85, 75, 90, 70, 88),
    ("Player 2", 80, 80, 86, 72, 85),
    ("Player 3", 78, 82, 88, 80, 82),
    ("Player 4", 82, 79, 85, 76, 80),
    ("Player 5", 88, 83, 87, 78, 86),
    # Add more players as needed
]
cursor.executemany('INSERT OR IGNORE INTO players (name, speed, passing, shooting, defending, stamina) VALUES (?, ?, ?, ?, ?, ?)', sample_players)
conn.commit()

# Fetch all players
cursor.execute("SELECT * FROM players")
players_data = cursor.fetchall()

# Game Variables
user_points = 0
gems = 0
levels_unlocked = 1

# Turtle Screen Setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Football Card Game")
screen.bgcolor("green")

# Interface Display Elements
username = "Player1"  # You can customize this as needed

# Text Display Functions
def display_text(x, y, text, size=16, color="black"):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color(color)
    pen.goto(x, y)
    pen.write(text, align="center", font=("Arial", size, "normal"))

# Button Functions
def leaderboard():
    print("Leaderboard pressed")

def game_shop():
    print("Game Shop pressed")

def show_stats():
    print("Player Stats pressed")

def open_team():
    print("Team button pressed")

def start_game():
    global user_points
    global levels_unlocked
    
    if levels_unlocked > 0:
        user_points += play_game()  # Game logic adds points
        if user_points >= levels_unlocked * 10:
            levels_unlocked += 1
            print(f"Level {levels_unlocked} unlocked!")

# Draw Buttons
display_text(-250, 250, username, 18, "white")  # Username display
display_text(0, 250, f"Points: {user_points}", 18, "white")
display_text(250, 250, f"Gems: {gems}", 18, "white")

# Draw buttons and map actions
leaderboard_button = turtle.Turtle()
leaderboard_button.shape("square")
leaderboard_button.color("blue")
leaderboard_button.shapesize(stretch_wid=1, stretch_len=4)
leaderboard_button.penup()
leaderboard_button.goto(250, 200)
leaderboard_button.onclick(lambda x, y: leaderboard())

shop_button = turtle.Turtle()
shop_button.shape("square")
shop_button.color("blue")
shop_button.shapesize(stretch_wid=1, stretch_len=4)
shop_button.penup()
shop_button.goto(-250, 200)
shop_button.onclick(lambda x, y: game_shop())

stats_button = turtle.Turtle()
stats_button.shape("square")
stats_button.color("blue")
stats_button.shapesize(stretch_wid=1, stretch_len=4)
stats_button.penup()
stats_button.goto(0, 0)
stats_button.onclick(lambda x, y: show_stats())

team_button = turtle.Turtle()
team_button.shape("square")
team_button.color("blue")
team_button.shapesize(stretch_wid=1, stretch_len=4)
team_button.penup()
team_button.goto(250, 0)
team_button.onclick(lambda x, y: open_team())

play_button = turtle.Turtle()
play_button.shape("square")
play_button.color("red")
play_button.shapesize(stretch_wid=2, stretch_len=6)
play_button.penup()
play_button.goto(0, -100)
play_button.onclick(lambda x, y: start_game())

# Football Card Game Logic
def get_random_player():
    return random.choice(players_data)

def play_game():
    user_score, computer_score = 0, 0

    for _ in range(25):  # 25 rounds
        user_player = get_random_player()
        computer_player = get_random_player()

        print(f"Your player: {user_player[1]} (Speed: {user_player[2]}, Passing: {user_player[3]}, Shooting: {user_player[4]}, Defending: {user_player[5]}, Stamina: {user_player[6]})")
        print(f"Computer's player: {computer_player[1]}")

        stat_choice = input("Choose a stat (speed, passing, shooting, defending, stamina): ").strip().lower()
        
        # Compare stats
        user_stat = user_player[2 + ["speed", "passing", "shooting", "defending", "stamina"].index(stat_choice)]
        computer_stat = computer_player[2 + ["speed", "passing", "shooting", "defending", "stamina"].index(stat_choice)]
        
        if user_stat > computer_stat:
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    return user_score  # Return user's score for points calculation

# Main Loop
turtle.done()
