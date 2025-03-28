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
            "x-client": f"{HABITICA_USER_ID}-SessionMemory"
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

    def get_user_groups(self, group_types: list, paginate: bool = False, page: int = 0) -> dict:
        """
        Retrieve user's groups from Habitica.

        :param group_types: List of group types to retrieve. Accepted values are:
            - "party": The user's current party.
            - "guilds": All guilds the user is a member of (both private and public guilds).
            - "privateGuilds": Private guilds the user is a member of.
            - "publicGuilds": Public guilds the user is a member of or has joined.
            - "tavern": The Tavern group (official social space in Habitica).

            Example: ["privateGuilds", "tavern"]

        :param paginate: (optional, default False) Whether to paginate results (Only applicable to public guilds).
        :param page: (optional, default 0) Page number to retrieve (used only if paginate=True).

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": True,
                "data": [
                    {
                        "_id": "group-id-123",
                        "name": "Example Guild",
                        "type": "guild",
                        ...
                    },
                    ...
                ]
            }
            Example error response:
            {
                "success": False,
                "error": "Request failed: <error details>"
            }
        """
        # Input validation
        valid_types = {"party", "guilds", "privateGuilds", "publicGuilds", "tavern"}
        if not group_types or not isinstance(group_types, list):
            return {"success": False, "error": "group_types must be a non-empty list."}
        if not set(group_types).issubset(valid_types):
            return {"success": False, "error": f"group_types can only include {', '.join(valid_types)}."}

        query_params = {
            "type": ",".join(group_types)
        }

        if paginate:
            if "publicGuilds" not in group_types:
                return {"success": False, "error": "Pagination is only supported for 'publicGuilds' group type."}
            query_params["paginate"] = "true"
            if not isinstance(page, int) or page < 0:
                return {"success": False, "error": "page must be a non-negative integer."}
            query_params["page"] = page
        else:
            query_params["paginate"] = "false"

        url = f"{self.base_url}/groups"
        try:
            response = requests.get(url, headers=self.headers, params=query_params, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()["data"]}
        except requests.exceptions.HTTPError as e:
            if response.status_code == 400:
                error_data = response.json()
                error_message = error_data.get("message", "Bad Request")
                logging.error(f"Get user groups failed (400): {error_message}")
                return {"success": False, "error": error_message}
            logging.error(f"Get user groups failed: {e} | Response: {response.text}")
            return {"success": False, "error": f"Request failed: {e}"}
        except requests.exceptions.RequestException as e:
            logging.error(f"Get user groups request exception: {e}")
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