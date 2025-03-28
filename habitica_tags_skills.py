# habitica_tags_skills.py
"""
A collection of methods to manage tags and skills within Habitica.
"""
import os
import requests
import logging
from typing import Union

logging.basicConfig(level=logging.INFO)

HABITICA_USER_ID = os.environ.get("HABITICA_USER_ID")
HABITICA_API_KEY = os.environ.get("HABITICA_API_KEY")
VALID_SKILLS = ["fireball", "mpheal", "earth", "frost", "smash", "defensiveStance",
                "valorousPresence", "intimidate", "pickPocket", "backStab",
                "toolsOfTrade", "stealth", "heal", "protectAura", "brightness",
                "healAll", "snowball", "spookySparkles", "seafoam", "shinySeed"]

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


    def create_tag(self, name: str) -> dict:
        """
        Create a new tag in Habitica.
        :param name: The name of the tag to be created.
        :return: The newly created tag data as a dictionary.
        """
        url = f"{self.base_url}/tags"
        payload = {"name": name}
        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Create tag failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def list_tags(self) -> dict:
        """
        List all tags for the authenticated user.
        :return: A dictionary containing an array of tags.
        """
        url = f"{self.base_url}/tags"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"List tags failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def cast_skill(self, spell_id: str, target_id: str = None) -> dict:
        """
        Cast a skill in Habitica.

        :param spell_id: The skill to cast. Must be one of the allowed skills.
            Allowed values: "fireball", "mpheal", "earth", "frost", "smash", "defensiveStance",
            "valorousPresence", "intimidate", "pickPocket", "backStab", "toolsOfTrade",
            "stealth", "heal", "protectAura", "brightness", "healAll", "snowball",
            "spookySparkles", "seafoam", "shinySeed"
        :param target_id: Optional UUID of the target (task or party member).

        :return: Dictionary containing the result of the skill cast.
        """
        if spell_id not in VALID_SKILLS:
            error_msg = f"Invalid skill '{spell_id}'. Must be one of: {', '.join(VALID_SKILLS)}"
            logging.error(error_msg)
            return {"success": False, "error": error_msg}

        url = f"{self.base_url}/user/class/cast/{spell_id}"
        params = {"targetId": target_id} if target_id else {}
        try:
            response = requests.post(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Cast skill failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}
