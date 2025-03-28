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
        self.base_url = "https://habitica.com/api/v3"

    def user_login(self, username: str, password: str) -> dict:
        """
        Authenticate a user with Habitica using username/email and password.

        :param username: Username or email of the user.
            Example: "user@example.com" or "username123"

        :param password: The user's password.
            Example: "securePassword123"

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": true,
                "data": {
                    "_id": "user-id",
                    "apiToken": "user-api-token",
                    "newUser": false
                }
            }

            Example error response:
            {
                "success": false,
                "error": "Request failed: <error details>"
            }
        """
        if not isinstance(username, str) or not username:
            return {"success": False, "error": "username must be a non-empty string."}
        if not isinstance(password, str) or not password:
            return {"success": False, "error": "password must be a non-empty string."}

        url = f"{self.base_url}/user/auth/local/login"
        payload = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as e:
            logging.error(f"User login failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def get_user_profile(self, user_fields: str = None) -> dict:
        """
        Retrieve the authenticated user's profile information.

        :param user_fields: Optional comma-separated list of user fields to return.
            Example: "achievements,items.mounts"

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": true,
                "data": {
                    "profile": {
                        "name": "User Name",
                        "photo": "url-to-photo",
                        ...
                    },
                    ...
                }
            }

            Example error response:
            {
                "success": false,
                "error": "Request failed: <error details>"
            }
        """
        if user_fields and not isinstance(user_fields, str):
            return {"success": False, "error": "user_fields must be a string."}

        url = f"{self.base_url}/user"
        params = {"userFields": user_fields} if user_fields else {}
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as e:
            logging.error(f"Get user profile failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

def export_user_data_json(self) -> dict:
    """
    Export the authenticated user's data in JSON format.

    :return: Dictionary containing the user's data as a JSON string on success.
        Example success response:
        {
            "success": true,
            "data": "{...}"  # JSON string
        }

        Example error response:
        {
            "success": false,
            "error": "Request failed: <error details>"
        }
    """
    url = "https://habitica.com/export/userdata.json"
    try:
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()
        return {"success": True, "data": response.text}
    except requests.exceptions.RequestException as e:
        logging.error(f"Export user data failed: {e}")
        return {"error": f"Request failed: {e}"}