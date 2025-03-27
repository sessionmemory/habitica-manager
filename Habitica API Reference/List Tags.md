---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-Tag-GetTags"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
get
```
https://habitica.com/api/v3/tags
```

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Array | An array of tags |

- [Example return:](https://habitica.com/apidoc/#success-examples-Tag-GetTags-0_0_0-0)

```
{
    "success": true,
    "data": [
        {
            "name": "Work",
            "id": "3d5d324d-a042-4d5f-872e-0553e228553e"
        },
        {
            "name": "apitester",
            "challenge": "true",
            "id": "f23c12f2-5830-4f15-9c36-e17fd729a812"
        },
        {
            "name": "practicetag",
            "id": "8bc0afbf-ab8e-49a4-982d-67a40557ed1a"
        }
    ],
    "notifications": []
}
```