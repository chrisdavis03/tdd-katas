import os
from dotenv import load_dotenv

#Get the environment variables in the app directory.
load_dotenv()

class Config():
    def __init__(self):
        self.db_file = os.environ.get('DB_FILE')

