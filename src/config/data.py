import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class ActiveUser:

    # Existing user
    FIRST_NAME = os.getenv("FIRST_NAME")
    LAST_NAME = os.getenv("LAST_NAME")
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    EMAIL = os.getenv("EMAIL")
    PHONE_NUMBER = os.getenv("PHONE_NUMBER")


@dataclass
class NewUser:
    first_name: str
    last_name: str
    address: str
    city: str
    state: str
    zip_code: str
    phone_number: str
    ssn: str
    username: str
    password: str
    email: str

