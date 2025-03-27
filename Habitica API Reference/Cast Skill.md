---
title: "Habitica"
url: "https://habitica.com/apidoc/#api-User-UserCast"
created: 2025-03-26
description:
tags:
  - "web-clips"
---
Skill Key to Name Mapping

Mage: fireball="Burst of Flames", mpheal="Ethereal Surge", earth="Earthquake", frost="Chilling Frost"

Warrior: smash="Brutal Smash", defensiveStance="Defensive Stance", valorousPresence="Valorous Presence", intimidate="Intimidating Gaze"

Rogue: pickPocket="Pickpocket", backStab="Backstab", toolsOfTrade="Tools of the Trade", stealth="Stealth"

Healer: heal="Healing Light", protectAura="Protective Aura", brightness="Searing Brightness", healAll="Blessing"

Transformation Items: snowball="Snowball", spookySparkles="Spooky Sparkles", seafoam="Seafoam", shinySeed="Shiny Seed"

post
```
https://habitica.com/api/v3/user/class/cast/:spellId
```

## Path Parameters

| Field | Type | Description |
| --- | --- | --- |
| spellId | String | The skill to cast.  Allowed values: `fireball`, `mpheal`, `earth`, `frost`, `smash`, `defensiveStance`, `valorousPresence`, `intimidate`, `pickPocket`, `backStab`, `toolsOfTrade`, `stealth`, `heal`, `protectAura`, `brightness`, `healAll`, `snowball`, `spookySparkles`, `seafoam`, `shinySeed` |

## Query Parameters

| Field | Type | Description |
| --- | --- | --- |
| targetId | UUID | Query parameter, necessary if the spell is cast on a party member or task. Not used if the spell is casted on the user or the user's current party. |

- [Query example:](https://habitica.com/apidoc/#parameter-examples-User-UserCast-0_0_0-0)

```
Cast "Pickpocket" on a task:
 https://habitica.com/api/v3/user/class/cast/pickPocket?targetId=fd427623...

Cast "Tools of the Trade" on the party:
 https://habitica.com/api/v3/user/class/cast/toolsOfTrade
```

## Success 200

| Field | Description |
| --- | --- |
| data | Will return the modified targets. For party members only the necessary fields will be populated. The user is always returned. |

## 400

| Name | Type | Description |
| --- | --- | --- |
| Not | NotAuthorized | enough mana. |

## 404

| Name | Type | Description |
| --- | --- | --- |
| TaskNotFound | NotFound | The specified task could not be found. |
| PartyNotFound | NotFound | The user's party could not be found. |
| UserNotFound | NotFound | The specified user could not be found. |