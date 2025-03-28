# Habitica API Toolkit

This toolkit provides a collection of Python classes to interact with Habitica's API, organized into three main modules: `habitica_tasks.py`, `habitica_manage.py`, and `habitica_tags_skills.py`. Each module is designed to handle specific aspects of Habitica's functionality, such as task management, user management, and tag/skill management.

## Installation

To use this toolkit, ensure you have Python installed. You can install the required dependencies using pip:

```bash
pip install requests
```

Make sure to set the following environment variables for authentication:
- `HABITICA_USER_ID`
- `HABITICA_API_KEY`

## Modules and Functions

### 1. `habitica_tasks.py`

This module contains methods for managing tasks within Habitica.

- **`create_task(task_data: dict) -> dict`**  
  Creates a new task in Habitica.  
  - **Parameters:**  
    - `task_data`: A dictionary containing task details. Required fields include `"text"` and `"type"`.
  - **Returns:** A dictionary with success status and task details or an error message.

- **`get_task(task_id: str) -> dict`**  
  Retrieves details of a specific task.  
  - **Parameters:**  
    - `task_id`: The ID of the task to retrieve.
  - **Returns:** A dictionary with success status and task details or an error message.

- **`list_tasks(task_type: str = None) -> dict`**  
  Lists all tasks for the authenticated user, optionally filtered by task type.  
  - **Parameters:**  
    - `task_type`: Optional task type to filter by (e.g., `"habits"`, `"dailys"`, `"todos"`, `"rewards"`, `"completedTodos"`).
  - **Returns:** A dictionary with success status and a list of tasks or an error message.

- **`add_checklist_item(task_id: str, item_data: dict) -> dict`**  
  Adds a checklist item to an existing task.  
  - **Parameters:**  
    - `task_id`: The ID of the task to add the checklist item to.
    - `item_data`: A dictionary containing the checklist item details.
  - **Returns:** A dictionary with success status and updated task details or an error message.

### 2. `habitica_manage.py`

This module contains methods for managing user-related interactions with Habitica.

- **`user_login(username: str, password: str) -> dict`**  
  Authenticates a user with Habitica using username/email and password.  
  - **Parameters:**  
    - `username`: Username or email of the user.
    - `password`: The user's password.
  - **Returns:** A dictionary with success status and authentication details or an error message.

- **`get_user_profile(user_fields: str = None) -> dict`**  
  Retrieves the authenticated user's profile information.  
  - **Parameters:**  
    - `user_fields`: Optional comma-separated list of user fields to return.
  - **Returns:** A dictionary with success status and user profile data or an error message.

- **`export_user_data_json() -> dict`**  
  Exports the authenticated user's data in JSON format.  
  - **Returns:** A dictionary containing the user's data as a JSON string or an error message.

### 3. `habitica_tags_skills.py`

This module contains methods for managing tags and skills within Habitica.

- **`create_tag(name: str) -> dict`**  
  Creates a new tag in Habitica.  
  - **Parameters:**  
    - `name`: The name of the tag to be created.
  - **Returns:** A dictionary with success status and tag details or an error message.

- **`list_tags() -> dict`**  
  Lists all tags for the authenticated user.  
  - **Returns:** A dictionary with success status and a list of tags or an error message.

- **`cast_skill(spell_id: str, target_id: str = None) -> dict`**  
  Casts a skill in Habitica.  
  - **Parameters:**  
    - `spell_id`: The skill to cast. Must be one of the allowed skills.
    - `target_id`: Optional UUID of the target (task or party member).
  - **Returns:** A dictionary containing the result of the skill cast or an error message.

## Usage Examples

Here's a quick example of how to create a task using the `habitica_tasks.py` module:

```python
from habitica_tasks import Tools

tools = Tools()
task_data = {
    "text": "Read a book",
    "type": "todo",
    "priority": 1.5
}
response = tools.create_task(task_data)
print(response)
```

Similarly, you can use other modules and methods as needed.

## General Notes

- **Authentication:** Each module requires the `HABITICA_USER_ID` and `HABITICA_API_KEY` environment variables to be set for authentication.
- **Error Handling:** All functions return a consistent dictionary structure with `success` and `data` or `error` keys, making it easy to handle responses programmatically.
- **Timeouts:** All API requests include a timeout to prevent indefinite waiting.

This toolkit is designed to be robust and easy to integrate with applications that need to interact with Habitica's API.