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
        valid_task_types = ["habits", "dailys", "todos", "rewards", "completedTodos"]
        if task_type and task_type not in valid_task_types:
            return {
                "success": False,
                "error": f"Invalid task_type. Must be one of {valid_task_types}."
            }

        url = f"{self.base_url}/tasks/user"
        params = {"type": task_type} if task_type else {}
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            response_data = response.json()
            return {"success": True, "data": response_data["data"]}
        except requests.exceptions.RequestException as e:
            logging.error(f"List tasks failed: {e}")
            return {"success": False, "error": f"Request failed: {e}"}

    def update_task(self, task_id: str, task_data: dict) -> dict:
        """
        Update details of an existing task in Habitica.

        :param task_id: The ID or alias of the task to update.
            Example: "task-id-123"
        :param task_data: Dictionary containing fields to update.
            Optional fields include:
            - "text" (str): The text to display for the task.
            - "attribute" (str): User's attribute used; Allowed values: "str", "int", "per", "con".
            - "collapseChecklist" (bool): If checklist should be displayed collapsed.
            - "notes" (str): Extra notes for the task.
            - "date" (str): Due date for "todo" tasks.
            - "priority" (str or float): Task difficulty; Allowed values: 0.1 (Trivial), 1 (Easy), 1.5 (Medium), 2 (Hard).
            - "reminders" (list): Array of reminders; each object must have "id", "startDate", and "time".
            - "frequency" (str): Frequency type; Allowed values: "daily", "weekly", "monthly", "yearly" (only for type "daily").
            - "repeat" (dict): Days of the week to repeat for frequency "weekly".
            - "everyX" (int): Number of days until a daily task is available again.
            - "streak" (int): Consecutive days streak for type "daily".
            - "daysOfMonth" (list): List of integers, days to repeat for frequency "monthly".
            - "weeksOfMonth" (list): List of integers, weeks to repeat for frequency "monthly".
            - "startDate" (str): Date when a task first becomes available (only for type "daily").
            - "up" (bool): Enable "+" action for type "habit".
            - "down" (bool): Enable "-" action for type "habit".
            - "value" (int or float): Cost in gold, only valid for type "reward".
            Example:
            {
                "notes": "Updated notes for the task.",
                "priority": 1.5
            }

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": True,
                "data": {
                    "_id": "task-id-123",
                    "text": "Updated task text",
                    "notes": "New notes",
                    ...
                }
            }
            Example error response:
            {
                "success": False,
                "error": "Request failed: <error details>"
            }
        """
        # Input validation
        if not task_id or not isinstance(task_id, str):
            return {"success": False, "error": "task_id must be a non-empty string."}
        if not isinstance(task_data, dict) or not task_data:
            return {"success": False, "error": "task_data must be a non-empty dictionary with fields to update."}

        url = f"{self.base_url}/tasks/{task_id}"
        try:
            response = requests.put(url, headers=self.headers, json=task_data, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()["data"]}
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                logging.error(f"Task not found (404): {task_id}")
                return {"success": False, "error": "Task not found."}
            logging.error(f"Update task failed: {e} | Response: {response.text}")
            return {"success": False, "error": f"Request failed: {e}"}
        except requests.exceptions.RequestException as e:
            logging.error(f"Update task request exception: {e}")
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
        
    def update_checklist(self, task_id: str, item_id: str, checklist_data: dict) -> dict:
        """
        Update a checklist item within a Habitica task.

        :param task_id: The ID or alias of the task containing the checklist item.
            Example: "task-id-123"
        :param item_id: The UUID of the checklist item to update.
            Example: "04f44e56-3b93-4fd1-b7fd-3831da062c5c"
        :param checklist_data: Dictionary containing fields to update.
            Required fields:
            - "text" (str): The replacement text for the current checklist item.

            Optional fields:
            - "completed" (bool): Whether the checklist item is checked off. (Default is False)

            Example:
            {
                "text": "Finish reading Chapter 4",
                "completed": true
            }

        :return: Dictionary with success status and data or error message.
            Example success response:
            {
                "success": True,
                "data": {
                    "_id": "task-id-123",
                    "checklist": [
                        {
                            "id": "04f44e56-3b93-4fd1-b7fd-3831da062c5c",
                            "text": "Finish reading Chapter 4",
                            "completed": true
                        },
                        ...
                    ],
                    ...
                }
            }
            Example error response:
            {
                "success": False,
                "error": "Request failed: <error details>"
            }
        """
        # Input validation
        if not task_id or not isinstance(task_id, str):
            return {"success": False, "error": "task_id must be a non-empty string."}
        if not item_id or not isinstance(item_id, str):
            return {"success": False, "error": "item_id must be a non-empty string."}
        if not isinstance(checklist_data, dict) or "text" not in checklist_data or not checklist_data["text"]:
            return {"success": False, "error": "'text' is required in checklist_data and cannot be empty."}

        url = f"{self.base_url}/tasks/{task_id}/checklist/{item_id}"
        try:
            response = requests.put(url, headers=self.headers, json=checklist_data, timeout=10)
            response.raise_for_status()
            return {"success": True, "data": response.json()["data"]}
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                error_data = response.json()
                error_message = error_data.get("message", "")
                if "Checklist item not found" in error_message:
                    logging.error(f"Checklist item not found (404): Task ID {task_id}, Item ID {item_id}")
                    return {"success": False, "error": "Checklist item not found."}
                elif "Task not found" in error_message:
                    logging.error(f"Task not found (404): {task_id}")
                    return {"success": False, "error": "Task not found."}
                else:
                    logging.error(f"Resource not found (404): {error_message}")
                    return {"success": False, "error": "Requested resource not found."}
            logging.error(f"Update checklist item failed: {e} | Response: {response.text}")
            return {"success": False, "error": f"Request failed: {e}"}
        except requests.exceptions.RequestException as e:
            logging.error(f"Update checklist item request exception: {e}")
            return {"success": False, "error": f"Request failed: {e}"}