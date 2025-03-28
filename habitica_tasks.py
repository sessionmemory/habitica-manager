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

class Tools:
    def __init__(self):
        if not HABITICA_USER_ID or not HABITICA_API_KEY:
            raise ValueError("Habitica credentials are not set in environment variables.")
        self.headers = {
            "x-api-user": HABITICA_USER_ID,
            "x-api-key": HABITICA_API_KEY,
            "Content-Type": "application/json",
        }

    def create_task(self, task_data: dict) -> dict:
        """
        Create a new task in Habitica.
        :param task_data: A dictionary containing the task details.
        :return: The created task data as a dictionary.
        """
        # Habitica API endpoint for creating a task
        url = "https://habitica.com/api/v3/tasks/user"
        try:
            # Make the POST request to the Habitica API
            response = requests.post(url, headers=self.headers, json=task_data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Create task failed: {e}")
            return {"error": f"Request failed: {e}"}

    def get_task(self, task_id: str) -> dict:
        """
        Retrieve details of a specific task.
        :param task_id: The ID of the task to retrieve.
        :return: The task data as a dictionary.
        """
        # Habitica API endpoint for getting a task
        url = f"https://habitica.com/api/v3/tasks/{task_id}"
        try:
            # Make the GET request to the Habitica API
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            # Handle potential errors (e.g., network issues, invalid task ID)
            logging.error(f"Get task failed: {e}")
            return {"error": f"Request failed: {e}"}

    def list_tasks(self, task_type: str = None) -> Union[dict, list]:
        """
        List all tasks for the authenticated user.
        :param task_type: Optional task type to filter by (e.g., "habits", "dailys", "todos", "rewards", "completedTodos").
        :return: A list of tasks.
        """
        # Habitica API endpoint for listing tasks
        url = "https://habitica.com/api/v3/tasks/user"
        # Add optional query parameter for task type
        params = {"type": task_type} if task_type else {}
        # Add your authentication headers here
        try:
            # Make the GET request to the Habitica API
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle potential errors (e.g., network issues, invalid task ID)
            logging.error(f"List tasks failed: {e}")
            return {"error": f"Request failed: {e}"}

    def add_checklist_item(self, task_id: str, text: str, completed: bool = False) -> dict:
        """
        Adds a checklist item to a task in Habitica.
        :param task_id: The ID of the task to add the checklist item to.
        :param text: The text of the checklist item.
        :param completed: Whether the checklist item is checked off. Defaults to False.
        :return: The updated task data as a dictionary.
        """
        # Habitica API endpoint for adding a checklist item
        url = f"https://habitica.com/api/v3/tasks/{task_id}/checklist"
        # Construct the payload with the checklist item data
        payload = {"text": text, "completed": completed}
        try:
            # Make the POST request to the Habitica API
            response = requests.post(url, headers=self.headers, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle potential errors (e.g., network issues, invalid task ID)
            logging.error(f"Add checklist item failed: {e}")
            return {"error": f"Request failed: {e}"}