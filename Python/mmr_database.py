import json
import os

# File path for the JSON database
DATABASE_FILE = "mmr_data.json"

# Initialize or load the database
def initialize_database():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'w') as f:
            json.dump({}, f)  # Start with an empty dictionary

def load_database():
    with open(DATABASE_FILE, 'r') as f:
        return json.load(f)

def save_database(data):
    with open(DATABASE_FILE, 'w') as f:
        json.dump(data, f, indent=4)  # Pretty-print with indentations

# Initialize database on start
initialize_database()

# Functions to Manage Player Data
def get_player_data(player_id):
    database = load_database()
    player_id = str(player_id)
    return database.get(player_id, {"mmr": 1000, "wins": 0, "losses": 0})

def update_player_data(player_id, result):
    database = load_database()
    player_id = str(player_id)

    # Ensure the player exists in the database
    if player_id not in database:
        database[player_id] = {"mmr": 1000, "wins": 0, "losses": 0}

    # Update the player's MMR and stats based on the result
    if result == "win":
        database[player_id]["mmr"] += 25
        database[player_id]["wins"] += 1
    elif result == "loss":
        database[player_id]["mmr"] -= 25
        database[player_id]["losses"] += 1

    save_database(database)

def get_leaderboard(top_n=10):
    database = load_database()
    sorted_players = sorted(
        database.items(),
        key=lambda item: item[1]["mmr"],
        reverse=True
    )
    return sorted_players[:top_n]

# Example Usage
if __name__ == "__main__":
    player_id = 12345  # Replace with a valid Discord user ID
    print("Before Update:", get_player_data(player_id))
    update_player_data(player_id, "win")
    print("After Update:", get_player_data(player_id))

    print("\nLeaderboard:")
    leaderboard = get_leaderboard()
    for i, (player_id, stats) in enumerate(leaderboard, 1):
        print(f"{i}. Player ID: {player_id}, MMR: {stats['mmr']}, Wins: {stats['wins']}, Losses: {stats['losses']}")
