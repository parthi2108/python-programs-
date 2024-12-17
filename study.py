entry_fees = {
    "america" : 14,
    "japan" : 13,
    "canada" : 16
}
entry_fees ["brazil"] = 12
del entry_fees["japan"]
entry_fees ["malaysia"] = 17

print(entry_fees)





import random

# Players database
players = []
fixtures = []
results = []
leaderboard = {}

# Entry fees based on country
entry_fees = {
    "United Kingdom": 10,
    "United States": 15,
    "Australia": 12
}

# Function to register a player
def register_player(name, country):
    if country not in entry_fees:
        return f"Invalid country. Registration failed."

    # Calculate entry fee
    fee = entry_fees[country]

    # Add player to database
    player = {
        "name": name,
        "country": country,
        "entry_fee": fee
    }
    players.append(player)
    leaderboard[name] = 0
    return f"Player {name} from {country} registered successfully! Entry fee: ${fee}"

# Function to display fixtures
def display_fixtures():
    if not fixtures:
        return "No fixtures scheduled yet."
    else:
        fixture_list = []
        for i, fixture in enumerate(fixtures, 1):
            fixture_list.append(f"{i}. {fixture['player1']} vs {fixture['player2']} on {fixture['date']} at {fixture['time']}")
        return "\n".join(fixture_list)

# Function to add a fixture
def add_fixture(date, time):
    if len(players) < 2:
        return "Not enough players to schedule a fixture."

    player1 = random.choice(players)["name"]
    player2 = random.choice(players)["name"]

    # Ensure players are not matched with themselves
    while player1 == player2:
        player2 = random.choice(players)["name"]

    fixture = {
        "player1": player1,
        "player2": player2,
        "date": date,
        "time": time
    }
    fixtures.append(fixture)
    return "Fixture added successfully!"

# Function to record results
def record_result(fixture_number, winner):
    if not fixtures:
        return "No fixtures to record results for."

    if 0 <= fixture_number < len(fixtures):
        fixture = fixtures.pop(fixture_number)

        if winner == fixture['player1'] or winner == fixture['player2']:
            results.append({"fixture": fixture, "winner": winner})
            leaderboard[winner] += 3
            return f"Result recorded successfully! {winner} won the match."
        else:
            return "Invalid winner name. Result not recorded."
    else:
        return "Invalid fixture number."

# Function to display the leaderboard
def display_leaderboard():
    if not leaderboard:
        return "No players registered yet."

    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    leaderboard_list = []
    for rank, (player, points) in enumerate(sorted_leaderboard, 1):
        leaderboard_list.append(f"{rank}. {player}: {points} points")
    return "\n".join(leaderboard_list)

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    print(register_player("Alice", "United Kingdom"))
    print(register_player("Bob", "United States"))
    print(register_player("Charlie", "Australia"))

    print(add_fixture("2024-12-15", "15:00"))
    print(add_fixture("2024-12-16", "16:00"))

    print(display_fixtures())

    print(record_result(0, "Alice"))
    print(record_result(1, "Bob"))

    print(display_leaderboard())
