---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Task-GetUserTasks"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
get
```
https://habitica.com/api/v3/tasks/user
```

## Query Parameters

| Field | Type | Description |
| --- | --- | --- |
| type | String | Optional query parameter to return just a type of tasks. By default all types will be returned except completed todos that must be requested separately. The "completedTodos" type returns only the 30 most recently completed.  Allowed values: `"habits"`, `"dailys"`, `"todos"`, `"rewards"`, `"completedTodos"` |
| dueDate optional |  | type Optional date to use for computing the nextDue field for each returned task. |

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Array | An array of tasks |

- [Example return:](https://habitica.com/apidoc/#success-examples-Task-GetUserTasks-0_0_0-0)

```
{"success":true,"data":[{"_id":"8a9d461b-f5eb-4a16-97d3-c03380c422a3",
"userId":"b0413351-405f-416f-8787-947ec1c85199","text":"15 minute break",
"type":"reward","notes":"","tags":[],"value":10,"priority":1,"attribute":"str",
"challenge":{},"group":{"assignedUsers":[],"approval":{"required":false,"approved":false,
"requested":false}},"reminders":[],"createdAt":"2017-01-07T17:52:09.121Z",
"updatedAt":"2017-01-11T14:25:32.504Z","id":"8a9d461b-f5eb-4a16-97d3-c03380c422a3"},
,{"_id":"84c2e874-a8c9-4673-bd31-d97a1a42e9a3","userId":"b0413351-405f-416f-8787-947ec1c85199",
"alias":"prac31","text":"Practice Task 31","type":"daily","notes":"","tags":[],"value":1,
"priority":1,"attribute":"str","challenge":{},"group":{"assignedUsers":[],
"approval":{"required":false,"approved":false,"requested":false}},
"reminders":[{"time":"2017-01-13T16:21:00.074Z","startDate":"2017-01-13T16:20:00.074Z",
"id":"b8b549c4-8d56-4e49-9b38-b4dcde9763b9"}],"createdAt":"2017-01-13T16:34:06.632Z",
"updatedAt":"2017-01-13T16:49:35.762Z","checklist":[],"collapseChecklist":false,
"completed":true,"history":[],"streak":1,"repeat":{"su":false,"s":false,"f":true,
"th":true,"w":true,"t":true,"m":true},"startDate":"2017-01-13T00:00:00.000Z",
"everyX":1,"frequency":"weekly","id":"84c2e874-a8c9-4673-bd31-d97a1a42e9a3"}],"notifications":[]}
```

## 401

| Name | Type | Description |
| --- | --- | --- |
| NoAccount | NotAuthorized | There is no account that uses those credentials. |

| Name | Type | Description |
| --- | --- | --- |
| Invalid\_request\_parameters |  | Error returned if the type URL param was not correct. |