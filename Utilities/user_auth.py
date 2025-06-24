
import os
import json
import pytest
import requests
from pathlib import Path
from typing import Optional
from Utilities.URL_Environment import BASE_API_URL


BASE_PATH = Path(__file__).parent

SAMPLE_USER = {
    "email": os.getenv("USER_EMAIL"),
    "password": os.getenv("USER_PASSWORD"),
}


def get_access_token_for_user() -> Optional[str]:
    """Util for authenticating a user

     Args:
         user_email (str): Target user email
         password (str): Target user password

     Returns:
         Optional[str]: Access token
     """

    user_email = "preciousanthony1997@gmail.com"
    password = "Adinlewa150497"

    """email = os.getenv("API_EMAIL")
        password = os.getenv("API_PASSWORD")"""


    response = requests.post(
            f"{BASE_API_URL}/api/usermgmt/v2/account/login",
            json={"email": user_email, "password": password},
        )
    if response.status_code == 200:
            return response.json()["access_token"]
    if response.status_code >= 500:
            print("critical error occured")
            print(response.text)
    raise ValueError("Failed to get token")

