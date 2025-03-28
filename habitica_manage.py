# habitica_manage.py
"""
A collection of methods to manage user-related interactions with Habitica's API.
"""
import os
import requests
import logging
from typing import Union

logging.basicConfig(level=logging.INFO)

HABITICA_USER_ID = os.environ.get("HABITICA_USER_ID")
HABITICA_API_KEY = os.environ.get("HABITICA_API_KEY")

class Tools:
    def __init__(self):
        if not HABITICA_USER_ID or not HABITICA_API_KEY:
            raise ValueError("Habitica credentials are not set in environment variables.")
        self.headers = {
            "x-api-user": HABITICA_USER_ID,
            "x-api-key": HABITICA_API_KEY,
            "Content-Type": "application/json",
        }

    def user_login(self, username: str, password: str) -> dict:
        """
        Authenticate a user with Habitica using username/email and password.
        :param username: Username or email of the user.
        :param password: The user's password.
        :return: Authentication details including user ID and API token.
        """
        url = "https://habitica.com/api/v3/user/auth/local/login"
        payload = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"User login failed: {e}")
            return {"error": f"Request failed: {e}"}

    def get_user_profile(self, user_fields: str = None) -> dict:
        """
        Retrieve the authenticated user's profile information.
        :param user_fields: Optional comma-separated list of user fields to return.
        :return: The user's profile data as a dictionary.
        """
        url = "https://habitica.com/api/v3/user"
        params = {"userFields": user_fields} if user_fields else {}
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Get user profile failed: {e}")
            return {"error": f"Request failed: {e}"}

    def export_user_data_json(self) -> Union[dict, bytes]:
        """
        Export the authenticated user's data in JSON format.
        :return: The user's data as JSON bytes or an error dictionary.
        """
        url = "https://habitica.com/export/userdata.json"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.content  # returns raw JSON bytes
        except requests.exceptions.RequestException as e:
            logging.error(f"Export user data failed: {e}")
            return {"error": f"Request failed: {e}"}