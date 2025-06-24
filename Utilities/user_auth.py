import os
import json
import time
import requests
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv




BASE_PATH = Path(__file__).parent

# Load environment variables from test.env
#load_dotenv(dotenv_path=BASE_PATH.parent / "test.env")

TOKEN_CACHE_FILE = BASE_PATH / "token_cache.json"

BASE_API_URL = os.getenv("BASE_API_URL")

#if not BASE_API_URL:
#    raise EnvironmentError("Missing required environment variable: BASE_API_URL")

SAMPLE_USER = {
    "email": os.getenv("USER_EMAIL"),
    "password": os.getenv("USER_PASSWORD"),
}
if not SAMPLE_USER["email"] or not SAMPLE_USER["password"]:
    raise EnvironmentError("Missing USER_EMAIL or USER_PASSWORD in environment variables.")


def _save_token(token: str, expires_in: int):
    data = {
        "access_token": token,
        "expiry": time.time() + expires_in - 60,  # 60s early expiry buffer
    }
    with open(TOKEN_CACHE_FILE, "w") as f:
        json.dump(data, f)


def _load_token() -> Optional[str]:
    if not TOKEN_CACHE_FILE.exists():
        return None
    with open(TOKEN_CACHE_FILE, "r") as f:
        data = json.load(f)
    if data.get("expiry", 0) > time.time():
        return data.get("access_token")
    return None


def get_access_token_for_user() -> Optional[str]:
    # Check cache first
    token = _load_token()
    if token:
        return token

    # No cached token or expired, request new one
    login_url = f"{BASE_API_URL}/api/usermgmt/v2/account/login"
    response = requests.post(login_url, json=SAMPLE_USER)

    if response.status_code == 200:
        json_data = response.json()
        token = json_data.get("access_token")
        expires_in = json_data.get("expires_in", 3600)  # default to 1 hour if not provided

        if token:
            _save_token(token, expires_in)
            return token

    if response.status_code >= 500:
        raise ValueError("Failed to get token: Invalid credentials or bad request.")
