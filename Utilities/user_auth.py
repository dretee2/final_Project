import os
import json
import requests
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv


BASE_PATH = Path(__file__).parent

# Load environment variables from test.env
load_dotenv(dotenv_path=BASE_PATH.parent / "test.env")

SAMPLE_USER = {
    "email": os.getenv("USER_EMAIL"),
    "password": os.getenv("USER_PASSWORD"),
}


def get_access_token_for_user() -> Optional[str]:
    """Util for authenticating a user"""
    response = requests.post(
        f"{os.getenv("BASE_API_URL")}/api/usermgmt/v2/account/login",
        json=SAMPLE_USER,
    )
    if response.status_code == 200:
        return response.json()["access_token"]
    if response.status_code >= 500:
        print("critical error occurred")
        print(response.text)
    raise ValueError("Failed to get token")


print(get_access_token_for_user())