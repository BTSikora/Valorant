import os
from pull_dataset import pull

#reads the .env file and sets each line of the code as environment variable
#I need this bc I would be putting secrets (my username and key) which should stay hidden
#.env file is not commited to your repository
from dotenv import load_dotenv
load_dotenv()

pull(os.environ['KAGGLE_USERNAME'], os.environ['KAGGLE_APIKEY'])

