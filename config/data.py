import os
from dotenv import load_dotenv

load_dotenv()

class Data:

    LOGIN = os.getenv("LOGIN_PASSANGER")
    PASSWORD = os.getenv("PASSWORD_PASSANGER")