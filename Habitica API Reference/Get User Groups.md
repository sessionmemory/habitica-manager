---
title: "Get User Groups"
url: "https://habitica.com/apidoc/#api-Group-GetGroups"
created: 2025-03-27
description:
tags:
  - "web-clips"
---
get
```
https://habitica.com/api/v3/groups
```

## Query Parameters

| Field | Type | Description |
| --- | --- | --- |
| type | String | The type of groups to retrieve. Must be a query string representing a list of values like 'tavern,party'. Possible values are party, guilds, privateGuilds, publicGuilds, tavern. |
| paginate optional | String | Public guilds support pagination. When true guilds are returned in groups of 30.  Allowed values: `"true"`, `"false"` |
| page optional | Number | When pagination is enabled for public guilds this parameter can be used to specify the page number (the initial page is number 0 and not required). |

- [Private Guilds, Tavern:](https://habitica.com/apidoc/#parameter-examples-Group-GetGroups-0_0_0-0)

```
{
    "type": "privateGuilds,tavern"
}
```

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Object\[\] | An array of the requested groups (See [/website/server/models/group.js](https://github.com/HabitRPG/habitica/blob/develop/website/server/models/group.js)) |

- [Private Guilds, Tavern:](https://habitica.com/apidoc/#success-examples-Group-GetGroups-0_0_0-0)

```
HTTP/1.1 200 OK
[
  {guilds}
]
```

## 400

| Name | Type | Description |
| --- | --- | --- |
| groupTypesRequired | BadRequest | Group types are required |
| guildsPaginateBooleanString | BadRequest | Paginate query parameter must be a boolean (true or false). |
| queryPageInteger | BadRequest | Page query parameter must be a positive integer |
| guildsOnlyPaginate | BadRequest | Only public guilds support pagination |