---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Task-AddChecklistItem"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
post
```
https://habitica.com/api/v3/tasks/:taskId/checklist
```

## Path Parameters

| Field | Type | Description |
| --- | --- | --- |
| taskId | String | The task \_id or alias |

## Body Parameters

| Field | Type | Description |
| --- | --- | --- |
| text | String | The text of the checklist item |
| completed optional | Boolean | Whether the checklist item is checked off.  Default value: `false` |

- [Example body data:](https://habitica.com/apidoc/#parameter-examples-Task-AddChecklistItem-0_0_0-0)

```
{
    "text": "Do this subtask"
}
```

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Object | The updated task |

- [Example return:](https://habitica.com/apidoc/#success-examples-Task-AddChecklistItem-0_0_0-0)

```
{
    "success": true,
    "data": {
        "_id": "84f02d6a-7b43-4818-a35c-d3336cec4880",
        "userId": "b0413351-405f-416f-8787-947ec1c85199",
        "text": "Test API Params",
        "alias": "test-api-params",
        "type": "todo",
        "notes": "",
        "tags": [],
        "value": 0,
        "priority": 2,
        "attribute": "int",
        "challenge": {
            "taskId": "4a29874c-0308-417b-a909-2a7d262b49f6",
            "id": "f23c12f2-5830-4f15-9c36-e17fd729a812"
        },
        "group": {
            "assignedUsers": [],
            "approval": {
                "required": false,
                "approved": false,
                "requested": false
            }
        },
        "reminders": [],
        "createdAt": "2017-01-13T21:23:05.949Z",
        "updatedAt": "2017-01-14T03:38:07.406Z",
        "checklist": [
            {
                "id": "afe4079d-dff1-47d9-9b06-5d76c69ddb12",
                "text": "Do this subtask",
                "completed": false
            }
        ],
        "collapseChecklist": false,
        "completed": false,
        "id": "84f02d6a-7b43-4818-a35c-d3336cec4880"
    },
    "notifications": []
}
```

## 404

| Name | Type | Description |
| --- | --- | --- |
| TaskNotFound | NotFound | The specified task could not be found. |