import os
from pull_dataset import pull
import pandas as pd 

#reads the .env file and sets each line of the code as environment variable
#I need this bc I would be putting secrets (my username and key) which should stay hidden
#.env file is not commited to your repository
from dotenv import load_dotenv
load_dotenv()

pull(os.environ['KAGGLE_USERNAME'], os.environ['KAGGLE_APIKEY'], os.environ['KAGGLE_DATASET_PATH'])

# player_stats = pd.read_csv('data/Players.csv')
# team_stats = pd.read_csv('data/Teams.csv')
# print(team_stats)

player_stats = pd.read_csv('data/val_stats.csv')

#print(player_stats)

agent_stats = player_stats[['agent_1', 'win_percent']].copy()
agent_median = agent_stats.groupby('agent_1').median()

print(agent_median)