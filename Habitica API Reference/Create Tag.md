---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Tag-CreateTag"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
post
```
https://habitica.com/api/v3/tags
```

## Body Parameters

| Field | Type | Description |
| --- | --- | --- |
| name | string | The name of the tag to be added. |

- [Example body:](https://habitica.com/apidoc/#parameter-examples-Tag-CreateTag-0_0_0-0)

```
{
    "name": "practicetag"
}
```

## 201

| Field | Type | Description |
| --- | --- | --- |
| data | Object | The newly created tag |

- [Example return:](https://habitica.com/apidoc/#success-examples-Tag-CreateTag-0_0_0-0)

```
{
    "success": true,
    "data": {
        "name": "practicetag",
        "id": "8bc0afbf-ab8e-49a4-982d-67a40557ed1a"
    },
    "notifications": []
}
```