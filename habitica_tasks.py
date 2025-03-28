# habitica_tasks.py
"""
A collection of methods to interact with Habitica's API for task management.
"""
import os
import requests
import logging
from typing import Union

logging.basicConfig(level=logging.INFO)

HABITICA_USER_ID = os.environ.get("HABITICA_USER_ID")
HABITICA_API_KEY = os.environ.get("HABITICA_API_KEY")
HABITICA_GPT_TAG_ID = "30cfedfe-4510-43a2-a8db-d87042c0c33a"

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

    def create_task(self, task_data: dict) -> dict:
        """
        Create a new task in Habitica.

        valid_types = ["habit", "daily", "todo", "reward"]

        :param task_data: Dictionary containing task details.
            Required fields:
            - "text" (str): The title or description of the task.
            - "type" (str): The type of task. Must be one of the following:
                - "habit": Actions to encourage or discourage without a fixed schedule.
                Example: "Take a stretching break" (positive) or "Chew nails" (negative).
                - "daily": Tasks to be completed on a regular schedule (e.g., daily, weekly).
                Example: "Go to bed on time" or "Do laundry every Saturday".
                - "todo": One-time or infrequent tasks.
                Example: "Send dad a birthday card" or "Pick up package at post office".
                - "reward": Treats or indulgences purchasable with in-game gold.
                Example: "Buy a new book" or "Enjoy a special treat".

        :return: Dictionary with success status and task details or error message.
            Example success response:
            {
                "success": true,
                "data": {
                    "_id": "task-id",
                    "text": "Read a book",
                    "type": "todo",
                    ...
                }
            }

            Example error response:
            {
                "success": false,
                "error": "Request failed: <error details>"
            }
        """
        # Input validation
        required_fields = ["text", "type"]
        for field in required_fields:
            if field not in task_data or not task_data[field]:
                return {"success": False, "error": f"'{field}' is required and cannot be empty."}

        valid_types = ["habit", "daily", "todo", "reward"]
        if task_data["type"] not in valid_types:
            return {"success": False, "error": f"Invalid task type. Must be one of {valid_types}."}

        # Ensure the task is tagged with the specified tag ID
        if "tags" in task_data:
            if HABITICA_GPT_TAG_ID not in task_data["tags"]:
                task_data["tags"].append(HABITICA_GPT_TAG_ID)
        else:
            task_data["tags"] = [HABITICA_GPT_TAG_ID]

        url = f"{self.base_url}/tasks/user"
        try:
            response = requests.post(url, headers=self.headers, json=task_data, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as e:
            logging.error(f"Create task failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def get_task(self, task_id: str) -> dict:
        """
        Retrieve details of a specific task.

        :param task_id: The ID of the task to retrieve.
            Example: "task-id-123"

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": true,
                "data": {
                    "_id": "task-id",
                    "text": "Read a book",
                    "type": "todo",
                    ...
                }
            }

            Example error response:
            {
                "success": false,
                "error": "Request failed: <error details>"
            }
        """
        if not isinstance(task_id, str) or not task_id:
            return {"success": False, "error": "task_id must be a non-empty string."}

        url = f"{self.base_url}/tasks/{task_id}"
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as e:
            logging.error(f"Get task failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def list_tasks(self, task_type: str = None) -> dict:
        """
        List all tasks for the authenticated user.

        :param task_type: Optional task type to filter by (e.g., "habits", "dailys", "todos", "rewards", "completedTodos").
            Example: "todos"

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": true,
                "data": [
                    {
                        "_id": "task-id",
                        "text": "Read a book",
                        "type": "todo",
                        ...
                    },
                    ...
                ]
            }

            Example error response:
            {
                "success": false,
                "error": "Request failed: <error details>"
            }
        """
        if task_type and not isinstance(task_type, str):
            return {"success": False, "error": "task_type must be a string."}

        url = f"{self.base_url}/tasks/user"
        params = {"type": task_type} if task_type else {}
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as e:
            logging.error(f"List tasks failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def add_checklist_item(self, task_id: str, item_data: dict) -> dict:
        """
        Add a checklist item to an existing task.

        :param task_id: The ID of the task to add the checklist item to.
            Example: "task-id-123"

        :param item_data: A dictionary containing the checklist item details.
            Example:
            {
                "text": "Buy groceries",
                "completed": false
            }

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": true,
                "data": {
                    "checklist": [
                        {
                            "id": "checklist-item-id",
                            "text": "Buy groceries",
                            "completed": false
                        },
                        ...
                    ]
                }
            }

            Example error response:
            {
                "success": false,
                "error": "Request failed: <error details>"
            }
        """
        if not isinstance(task_id, str) or not task_id:
            return {"success": False, "error": "task_id must be a non-empty string."}
        if not isinstance(item_data, dict) or not item_data:
            return {"success": False, "error": "item_data must be a non-empty dictionary."}

        url = f"{self.base_url}/tasks/{task_id}/checklist"
        try:
            response = requests.post(url, headers=self.headers, json=item_data, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()}
        except requests.exceptions.RequestException as e:
            logging.error(f"Add checklist item failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}