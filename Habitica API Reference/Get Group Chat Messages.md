---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Chat-GetChat"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
Fetches an array of messages from a group

get
```
https://habitica.com/api/v3/groups/:groupId/chat
```

## Path Parameters

| Field | Type | Description |
| --- | --- | --- |
| groupId | String | The group \_id ('party' for the user party and 'habitrpg' for tavern are accepted). |

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Array | An array of [chat messages](https://github.com/HabitRPG/habitica/blob/develop/website/server/models/group.js#L51) |

## 400

| Name | Type | Description |
| --- | --- | --- |
| groupIdRequired | badRequest | A group ID is required |

## 404

| Name | Type | Description |
| --- | --- | --- |
| GroupNotFound | NotFound | The specified group could not be found. |