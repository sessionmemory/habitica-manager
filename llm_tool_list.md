### 1. `habitica_tasks`
This module contains methods for managing tasks within Habitica.
- **`create_task`**  
  Creates a new task in Habitica.
- **`get_task`**  
  Retrieves details of a specific task.
- **`list_tasks`**  
  Lists all tasks for the authenticated user, optionally filtered by type.
- **`add_checklist_item`**  
  Adds a checklist item to an existing task.

### 2. `habitica_manage`
This module contains methods for managing user-related interactions with Habitica.
- **`user_login`**  
  Authenticates a user with Habitica using username/email and password.
- **`get_user_profile`**  
  Retrieves the authenticated user's profile information.
- **`export_user_data_json`**  
  Exports the authenticated user's data in JSON format.

### 3. `habitica_tags_skills`
This module contains methods for managing tags and skills within Habitica.
- **`create_tag`**  
  Creates a new tag in Habitica.
- **`list_tags`**  
  Lists all tags for the authenticated user.
- **`cast_skill`**  
  Casts a skill in Habitica, optionally targeting a specific task or party member.