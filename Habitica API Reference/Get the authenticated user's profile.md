---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-User-UserGet"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
The user profile contains data related to the authenticated user including (but not limited to): Achievements; Authentications (including types and timestamps); Challenges memberships (Challenge IDs); Flags (including armoire, tutorial, tour etc...); Guilds memberships (Guild IDs); History (including timestamps and values, only for Experience and summed To Do values); Inbox; Invitations (to parties/guilds); Items (character's full inventory); New Messages (flags for party/guilds that have new messages; also reported in Notifications); Notifications; Party (includes current quest information); Preferences (user selected prefs); Profile (name, photo url, blurb); Purchased (includes subscription data and some gem-purchased items); PushDevices (identifiers for mobile devices authorized); Stats (standard RPG stats, class, buffs, xp, etc..); Tags; TasksOrder (list of all IDs for Dailys, Habits, Rewards and To Do's).

get
```
https://habitica.com/api/v3/user
```
- [Example use:](https://habitica.com/apidoc/#examples-User-UserGet-0_0_0-0)

```
curl -i https://habitica.com/api/v3/user?userFields=achievements,items.mounts
```

## Query Parameters

| Field | Type | Description |
| --- | --- | --- |
| userFields optional | String | A list of comma-separated user fields to be returned instead of the entire document. Notifications are always returned. |

## Success 200

| Field | Type | Description |
| --- | --- | --- |
| data | Object | The user object |

- [Result:](https://habitica.com/apidoc/#success-examples-User-UserGet-0_0_0-0)

```
{
  "success": true,
  "data": {
  --  User data included here, for details of the user model see:
  --  https://github.com/HabitRPG/habitica/tree/develop/website/server/models/user
  }
}
```