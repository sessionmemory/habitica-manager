---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Task-CreateUserTasks"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
Can be passed an object to create a single task or an array of objects to create multiple tasks.

post
```
https://habitica.com/api/v3/tasks/user
```

## Body Parameters

| Field | Type | Description |
| --- | --- | --- |
| text | String | The text to be displayed for the task |
| type | String | Task type, options are: "habit", "daily", "todo", "reward".  Allowed values: `"habit"`, `"daily"`, `"todo"`, `"reward"` |
| tags optional | String\[\] | Array of UUIDs of tags |
| alias optional | String | Alias to assign to task |
| attribute optional | String | User's attribute to use, options are: "str", "int", "per", "con"  Allowed values: `"str"`, `"int"`, `"per"`, `"con"` |
| checklist optional | Array | An array of checklist items. For example, \[{"text":"buy tools", "completed":true}, {"text":"build shed", "completed":false}\] |
| collapseChecklist optional | Boolean | Determines if a checklist will be displayed  Default value: `false` |
| notes optional | String | Extra notes |
| date optional | Date | Due date to be shown in task list. Only valid for type "todo." |
| priority optional | Number | Difficulty, options are 0.1, 1, 1.5, 2; equivalent of Trivial, Easy, Medium, Hard.  Default value: `1`  Allowed values: `"0.1"`, `"1"`, `"1.5"`, `"2"` |
| reminders optional | String\[\] | Array of reminders, each an object that must include: a UUID, startDate and time. For example {"id":"ed427623-9a69-4aac-9852-13deb9c190c3", "startDate":"1/16/17","time":"1/16/17" } |
| frequency optional | String | Values "weekly" and "monthly" enable use of the "repeat" field. All frequency values enable use of the "everyX" field. Value "monthly" enables use of the "weeksOfMonth" and "daysOfMonth" fields. Frequency is only valid for type "daily".  Default value: `weekly`  Allowed values: `"daily"`, `"weekly"`, `"monthly"`, `"yearly"` |
| repeat optional | String | List of objects for days of the week, Days that are true will be repeated upon. Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s. Value of frequency must be "weekly". For example, to skip repeats on Mon and Fri: "repeat":{"f":false,"m":false}  Default value: `true` |
| everyX optional | Number | Value of frequency must be "daily", the number of days until this daily task is available again.  Default value: `1` |
| streak optional | Number | Number of days that the task has consecutively been checked off. Only valid for type "daily"  Default value: `0` |
| daysOfMonth | Integer\[\] | Array of integers. Only valid for type "daily" |
| weeksOfMonth | Integer\[\] | Array of integers. Only valid for type "daily" |
| startDate optional | Date | Date when the task will first become available. Only valid for type "daily" |
| up optional | Boolean | Only valid for type "habit" If true, enables the "+" under "Directions/Action" for "Good habits"-  Default value: `true` |
| down optional | Boolean | Only valid for type "habit" If true, enables the "-" under "Directions/Action" for "Bad habits"  Default value: `true` |
| value optional | Number | Only valid for type "reward." The cost in gold of the reward. Should be greater then or equal to 0.  Default value: `0` |

- [Request-Example:](https://habitica.com/apidoc/#parameter-examples-Task-CreateUserTasks-0_0_0-0)

```
{
    "text": "Update Habitica API Documentation - Tasks",
    "type": "todo",
    "alias": "hab-api-tasks",
    "notes": "Update the tasks api on GitHub",
    "tags": [
        "ed427623-9a69-4aac-9852-13deb9c190c3"
    ],
    "checklist": [
        {
            "text": "read wiki",
            "completed": true
        },
        {
            "text": "write code"
        }
    ],
    "priority": 2
}
```

## 201

| Field | Description |
| --- | --- |
| data | An object if a single task was created, otherwise an array of tasks |

- [Success-Response:](https://habitica.com/apidoc/#success-examples-Task-CreateUserTasks-0_0_0-0)

```
{
    "success": true,
    "data": {
        "userId": "b0413351-405f-416f-8787-947ec1c85199",
        "alias": "hab-api-tasks",
        "text": "Update Habitica API Documentation - Tasks",
        "type": "todo",
        "notes": "Update the tasks api on GitHub",
        "tags": [
            "ed427623-9a69-4aac-9852-13deb9c190c3"
        ],
        "value": 0,
        "priority": 2,
        "attribute": "str",
        "challenge": {},
        "group": {
            "assignedUsers": [],
            "approval": {
                "required": false,
                "approved": false,
                "requested": false
            }
        },
        "reminders": [],
        "_id": "829d435b-edc4-498c-a30e-e52361a0f35a",
        "createdAt": "2017-01-12T02:11:02.876Z",
        "updatedAt": "2017-01-12T02:11:02.876Z",
        "checklist": [
            {
                "completed": true,
                "text": "read wiki",
                "id": "91edadda-fb62-4e6e-b110-aff26f936678"
            },
            {
                "completed": false,
                "text": "write code",
                "id": "d1ddad50-ab22-49c4-8261-9996ae337b6a"
            }
        ],
        "collapseChecklist": false,
        "completed": false,
        "id": "829d435b-edc4-498c-a30e-e52361a0f35a"
    },
    "notifications": []
}
```

## 400

| Name | Type | Description |
| --- | --- | --- |
| MustBeType | BadRequest | Task type must be one of "habit", "daily", "todo", "reward". |
| Text-ValidationFailed | BadRequest | Path 'text' is required. |
| Alias-ValidationFailed | BadRequest | Task short names can only contain alphanumeric characters, underscores and dashes. |
| Value-ValidationFailed | BadRequest | `x` is not a valid enum value for path `(body param)`. |

## 401

| Name | Type | Description |
| --- | --- | --- |
| NoAccount | NotAuthorized | There is no account that uses those credentials. |

## 404

| Name | Type | Description |
| --- | --- | --- |
| ChecklistNotFound | NotFound | The specified checklist item could not be found. |

- [Error-Response:](https://habitica.com/apidoc/#error-examples-Task-CreateUserTasks-0_0_0-0)

```
{
    "success": false,
    "error": "BadRequest",
    "message": "todo validation failed",
    "errors": [
        {
            "message": "Path \`text\` is required.",
            "path": "text"
        }
    ]
}
```