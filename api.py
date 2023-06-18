import valorant
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']

# Set our client's region to EU. Client uses NA by default.
client = valorant.Client(API_KEY, region="eu")

# Get the top 15 players on the Ranked Leaderboard.
lb = client.get_leaderboard(size=15)

print("Top Players in EU:\n")

# Print all players on the leaderboard.
for p in lb.players:
    print(f"#{p.leaderboardRank} - {p.gameName} ({p.numberOfWins} wins)")