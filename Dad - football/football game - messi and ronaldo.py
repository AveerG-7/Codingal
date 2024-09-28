import random

# Define a dictionary to store player stats
players = {
    "Messi": {
        "pace": 80,
        "shooting": 84,
        "passing": 88,
        "dribbling": 92,
        "defending": 36,
        "physicality": 63
    },
    "Ronaldo": {
        "pace": 76,
        "shooting": 88,
        "passing": 77,
        "dribbling": 80,
        "defending": 39,
        "physicality": 79
    },
    "Aveer": {
        "pace": 99,
        "shooting": 99,
        "passing": 99,
        "dribbling": 99,
        "defending": 99,
        "physicality": 99
    },
    "Mbappe": {
        "pace": 97,
        "shooting": 88,
        "passing": 78,
        "dribbling": 90,
        "defending": 41,
        "physicality": 79
    },
    "Neymar": {
        "pace": 89,
        "shooting": 83,
        "passing": 86,
        "dribbling": 94,
        "defending": 37,
        "physicality": 58
    },
    "Lewandowski": {
        "pace": 75,
        "shooting": 91,
        "passing": 79,
        "dribbling": 85,
        "defending": 44,
        "physicality": 82
    },
    "De Bruyne": {
        "pace": 74,
        "shooting": 85,
        "passing": 93,
        "dribbling": 87,
        "defending": 64,
        "physicality": 78
    },
    "Salah": {
        "pace": 93,
        "shooting": 87,
        "passing": 82,
        "dribbling": 90,
        "defending": 45,
        "physicality": 75
    },
    "Kane": {
        "pace": 70,
        "shooting": 91,
        "passing": 83,
        "dribbling": 81,
        "defending": 47,
        "physicality": 82
    },
    "Erling Haaland": {
        "pace": 89,
        "shooting": 93,
        "passing": 65,
        "dribbling": 80,
        "defending": 45,
        "physicality": 88
    },
    "Benzema": {
        "pace": 79,
        "shooting": 90,
        "passing": 83,
        "dribbling": 87,
        "defending": 40,
        "physicality": 82
    },
    "Luka Modric": {
        "pace": 72,
        "shooting": 76,
        "passing": 89,
        "dribbling": 88,
        "defending": 69,
        "physicality": 67
    },
    "Joshua Kimmich": {
        "pace": 70,
        "shooting": 70,
        "passing": 86,
        "dribbling": 85,
        "defending": 82,
        "physicality": 78
    },
    "Jadon Sancho": {
        "pace": 83,
        "shooting": 74,
        "passing": 80,
        "dribbling": 88,
        "defending": 35,
        "physicality": 61
    },
    "Sergio Ramos": {
        "pace": 72,
        "shooting": 62,
        "passing": 71,
        "dribbling": 70,
        "defending": 89,
        "physicality": 84
    },
    "Manuel Neuer": {
        "pace": 60,
        "shooting": 28,
        "passing": 50,
        "dribbling": 50,
        "defending": 50,
        "physicality": 87
    },
    "Bruno Fernandes": {
        "pace": 76,
        "shooting": 84,
        "passing": 89,
        "dribbling": 83,
        "defending": 65,
        "physicality": 72
    },
    "Raheem Sterling": {
        "pace": 91,
        "shooting": 80,
        "passing": 77,
        "dribbling": 86,
        "defending": 45,
        "physicality": 69
    },
    "Phil Foden": {
        "pace": 84,
        "shooting": 79,
        "passing": 82,
        "dribbling": 89,
        "defending": 45,
        "physicality": 60
    },
    "Virgil van Dijk": {
        "pace": 79,
        "shooting": 60,
        "passing": 71,
        "dribbling": 70,
        "defending": 90,
        "physicality": 86
    },
    "João Cancelo": {
        "pace": 85,
        "shooting": 68,
        "passing": 83,
        "dribbling": 82,
        "defending": 79,
        "physicality": 71
    },
    "Pedri": {
        "pace": 80,
        "shooting": 72,
        "passing": 85,
        "dribbling": 89,
        "defending": 60,
        "physicality": 65
    },
    "Frenkie de Jong": {
        "pace": 81,
        "shooting": 70,
        "passing": 83,
        "dribbling": 86,
        "defending": 76,
        "physicality": 72
    },
    "Antonio Rudiger": {
        "pace": 82,
        "shooting": 45,
        "passing": 64,
        "dribbling": 66,
        "defending": 88,
        "physicality": 85
    },
    "Alphonso Davies": {
        "pace": 96,
        "shooting": 69,
        "passing": 75,
        "dribbling": 85,
        "defending": 75,
        "physicality": 77
    },
    # Additional 25 players
    "Gerard Moreno": {
        "pace": 78,
        "shooting": 82,
        "passing": 80,
        "dribbling": 87,
        "defending": 43,
        "physicality": 75
    },
    "Raúl Jiménez": {
        "pace": 75,
        "shooting": 80,
        "passing": 73,
        "dribbling": 77,
        "defending": 48,
        "physicality": 80
    },
    "Son Heung-min": {
        "pace": 89,
        "shooting": 86,
        "passing": 81,
        "dribbling": 90,
        "defending": 32,
        "physicality": 71
    },
    "Marcus Rashford": {
        "pace": 90,
        "shooting": 81,
        "passing": 77,
        "dribbling": 86,
        "defending": 38,
        "physicality": 70
    },
    "Gareth Bale": {
        "pace": 84,
        "shooting": 85,
        "passing": 80,
        "dribbling": 88,
        "defending": 36,
        "physicality": 78
    },
    "Thomas Müller": {
        "pace": 78,
        "shooting": 84,
        "passing": 87,
        "dribbling": 80,
        "defending": 30,
        "physicality": 72
    },
    "Angel Di María": {
        "pace": 83,
        "shooting": 79,
        "passing": 88,
        "dribbling": 87,
        "defending": 34,
        "physicality": 66
    },
    "Nicolas Pépé": {
        "pace": 90,
        "shooting": 78,
        "passing": 76,
        "dribbling": 88,
        "defending": 30,
        "physicality": 68
    },
    "Riyad Mahrez": {
        "pace": 83,
        "shooting": 82,
        "passing": 84,
        "dribbling": 89,
        "defending": 40,
        "physicality": 68
    },
    "Cesar Azpilicueta": {
        "pace": 72,
        "shooting": 60,
        "passing": 75,
        "dribbling": 70,
        "defending": 88,
        "physicality": 85
    },
    "Jack Grealish": {
        "pace": 77,
        "shooting": 78,
        "passing": 83,
        "dribbling": 86,
        "defending": 35,
        "physicality": 62
    },
    "Ederson": {
        "pace": 58,
        "shooting": 22,
        "passing": 66,
        "dribbling": 53,
        "defending": 45,
        "physicality": 82
    },
    "Jan Oblak": {
        "pace": 60,
        "shooting": 20,
        "passing": 55,
        "dribbling": 49,
        "defending": 50,
        "physicality": 87
    },
    "Kylian Mbappé": {
        "pace": 97,
        "shooting": 90,
        "passing": 80,
        "dribbling": 91,
        "defending": 44,
        "physicality": 76
    },
    "Lautaro Martínez": {
        "pace": 80,
        "shooting": 82,
        "passing": 74,
        "dribbling": 86,
        "defending": 42,
        "physicality": 70
    },
    "Gerard Piqué": {
        "pace": 64,
        "shooting": 65,
        "passing": 73,
        "dribbling": 61,
        "defending": 90,
        "physicality": 83
    },
    "Marco Verratti": {
        "pace": 70,
        "shooting": 69,
        "passing": 88,
        "dribbling": 85,
        "defending": 64,
        "physicality": 55
    },
    "Jules Koundé": {
        "pace": 80,
        "shooting": 55,
        "passing": 72,
        "dribbling": 71,
        "defending": 82,
        "physicality": 78
    },
    "Matthijs de Ligt": {
        "pace": 73,
        "shooting": 54,
        "passing": 70,
        "dribbling": 63,
        "defending": 88,
        "physicality": 82
    },
    "David Alaba": {
        "pace": 80,
        "shooting": 65,
        "passing": 78,
        "dribbling": 74,
        "defending": 86,
        "physicality": 74
    },
    "Ciro Immobile": {
        "pace": 77,
        "shooting": 86,
        "passing": 73,
        "dribbling": 80,
        "defending": 34,
        "physicality": 79
    }
}

# Function to play the game
def play_game():
    available_players = list(players.keys())
    random.shuffle(available_players)  # Shuffle players

    player_points = 0
    computer_points = 0
    total_players = len(available_players)
    rounds = 0

    # Player chooses the initial stat
    stat_options = list(players[available_players[0]].keys())
    chosen_stat = input(f"Choose a stat to start with {stat_options}: ")

    while rounds < total_players // 2:
        rounds += 1
        print("\nRound", rounds)

        # Select players for this round
        user_player = available_players.pop(0)  # User's player
        computer_player = available_players.pop(0)  # Computer's player
        
        print(f"You selected: {user_player} (Stat: {players[user_player][chosen_stat]})")
        print(f"Computer selected: {computer_player} (Stat: {players[computer_player][chosen_stat]})")
        
        user_stat = players[user_player][chosen_stat]
        computer_stat = players[computer_player][chosen_stat]

        # Determine the winner
        if user_stat > computer_stat:
            print("You win this round!")
            player_points += 1
            winner = "You"
        elif user_stat < computer_stat:
            print("Computer wins this round!")
            computer_points += 1
            winner = "Computer"
        else:
            print("It's a tie!")
            winner = "None"

        # Show points
        print(f"Score - You: {player_points}, Computer: {computer_points}")

        # Winner chooses the next stat
        if winner != "None":
            chosen_stat = input(f"{winner}, choose the next stat from {stat_options}: ")

    # Final results
    print("\nGame over!")
    print(f"Final Score - You: {player_points}, Computer: {computer_points}")
    if player_points > computer_points:
        print("You win the game!")
    elif player_points < computer_points:
        print("Computer wins the game!")
    else:
        print("It's a tie overall!")

# Start the game
play_game()
