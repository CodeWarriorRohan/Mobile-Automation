import os
from dotenv import load_dotenv

load_dotenv()

VALID_USER = {
    "username": os.getenv("VALID_USERNAME"),
    "password": os.getenv("VALID_PASSWORD"),
}

INVALID_USER = {
    "username": os.getenv("INVALID_USERNAME"),
    "password": os.getenv("INVALID_PASSWORD"),
}
