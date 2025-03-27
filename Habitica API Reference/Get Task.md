---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Task-GetTask"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
get
```
https://habitica.com/api/v3/tasks/:taskId
```
- [Example use:](https://habitica.com/apidoc/#examples-Task-GetTask-0_0_0-0)

```
curl -i https://habitica.com/api/v3/tasks/54a81d23-529c-4daa-a6f7-c5c6e7e84936
```

## Path Parameters

| Field | Type | Description |
| --- | --- | --- |
| taskId | String | The task \_id or alias |

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Object | The task object |

- [Example returned object:](https://habitica.com/apidoc/#success-examples-Task-GetTask-0_0_0-0)

```
{
    "success": true,
    "data": {
        "_id": "2b774d70-ec8b-41c1-8967-eb6b13d962ba",
        "userId": "b0413351-405f-416f-8787-947ec1c85199",
        "text": "API Trial",
        "alias": "apiTrial",
        "type": "habit",
        "notes": "",
        "tags": [],
        "value": 11.996661122825959,
        "priority": 1.5,
        "attribute": "str",
        "challenge": {
            "taskId": "5f12bfba-da30-4733-ad01-9c42f9817975",
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
        "createdAt": "2017-01-12T19:03:33.495Z",
        "updatedAt": "2017-01-13T20:52:02.927Z",
        "history": [
            {
                "value": 1,
                "date": 1484248053486
            },
            {
                "value": 1.9747,
                "date": 1484252965224
            },
            {
                "value": 2.9253562257358428,
                "date": 1484252966902
            },
            {
                "value": 6.415599723011605,
                "date": 1484329050485
            },
            {
                "value": 10.482627142836241,
                "date": 1484329089835
            },
            {
                "value": 11.24705848799571,
                "date": 1484329095500
            },
            {
                "value": 11.996661122825959,
                "date": 1484329552423
            }
        ],
        "down": false,
        "up": true,
        "id": "2b774d70-ec8b-41c1-8967-eb6b13d962ba"
    },
    "notifications": []
}
```

## 404

| Name | Type | Description |
| --- | --- | --- |
| TaskNotFound | NotFound | The specified task could not be found. |