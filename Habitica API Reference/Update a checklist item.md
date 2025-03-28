---
title: "Update a checklist item"
url: "https://habitica.com/apidoc/#api-Task-UpdateChecklistItem"
created: 2025-03-27
description:
tags:
  - "web-clips"
---
put
```
https://habitica.com/api/v3/tasks/:taskId/checklist/:itemId
```

## Path Parameters

| Field | Type | Description |
| --- | --- | --- |
| taskId | String | The task \_id or alias |
| itemId | UUID | The checklist item \_id |

## Body Parameters

| Field | Type | Description |
| --- | --- | --- |
| text | String | The replacement text for the current checklist item. |
| completed optional | Boolean | Whether the checklist item is checked off.  Default value: `false` |

- [Example body:](https://habitica.com/apidoc/#parameter-examples-Task-UpdateChecklistItem-0_0_0-0)

```
{
    "text": "learn Czech",
    "completed": true
}
```

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Object | The updated task |

## 404

| Name | Type | Description |
| --- | --- | --- |
| TaskNotFound | NotFound | The specified task could not be found. |
| ChecklistNotFound | NotFound | The specified checklist item could not be found. |
| ChallengeNotFound | NotFound | The specified challenge could not be found. |