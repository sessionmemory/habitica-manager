---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-User-UserLoginLocal"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
Login a user with email / username and password

post
```
https://habitica.com/api/v3/user/auth/local/login
```

## Body Parameters

| Field | Type | Description |
| --- | --- | --- |
| username | String | Username or email of the user |
| password | String | The user's password |

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| \_id | String | The user's unique identifier |
| apiToken | String | The user's api token that must be used to authenticate requests. |
| newUser | Boolean | Returns true if the user was just created (always false for local login). |