---
title: "Update a task"
url: "https://habitica.com/apidoc/#api-Task-UpdateTask"
created: 2025-03-27
description:
tags:
  - "web-clips"
---
put
```
https://habitica.com/api/v3/tasks/:taskId
```

## Path Parameters

| Field | Type | Description |
| --- | --- | --- |
| taskId | String | The task \_id or alias |

## Body Parameters

| Field | Type | Description |
| --- | --- | --- |
| text optional | String | The text to be displayed for the task |
| attribute optional | String | User's attribute to use, options are: "str", "int", "per", "con".  Allowed values: `"str"`, `"int"`, `"per"`, `"con"` |
| collapseChecklist optional | Boolean | Determines if a checklist will be displayed  Default value: `false` |
| notes optional | String | Extra notes |
| date optional | Date | Due date to be shown in task list. Only valid for type "todo." |
| priority optional | Number | Difficulty, options are 0.1, 1, 1.5, 2; equivalent of Trivial, Easy, Medium, Hard.  Default value: `1`  Allowed values: `"0.1"`, `"1"`, `"1.5"`, `"2"` |
| reminders optional | String\[\] | Array of reminders, each an object that must include: a UUID, startDate and time. |
| frequency optional | String | Values "weekly" and "monthly" enable use of the "repeat" field. All frequency values enable use of the "everyX" field. Value "monthly" enables use of the "weeksOfMonth" and "daysOfMonth" fields. Frequency is only valid for type "daily".  Default value: `weekly`  Allowed values: `"daily"`, `"weekly"`, `"monthly"`, `"yearly"` |
| repeat optional | String | List of objects for days of the week, Days that are true will be repeated upon. Only valid for type "daily". Any days not specified will be marked as true. Days are: su, m, t, w, th, f, s. Value of frequency must be "weekly". For example, to skip repeats on Mon and Fri: "repeat":{"f":false,"m":false}  Default value: `true` |
| everyX optional | Number | Value of frequency must be "daily", the number of days until this daily task is available again.  Default value: `1` |
| streak optional | Number | Number of days that the task has consecutively been checked off. Only valid for type "daily",  Default value: `0` |
| daysOfMonth | Integer\[\] | Array of integers. Only valid for type "daily" |
| weeksOfMonth | Integer\[\] | Array of integers. Only valid for type "daily" |
| startDate optional | Date | Date when the task will first become available. Only valid for type "daily". |
| up optional | Boolean | Only valid for type "habit" If true, enables the "+" under "Directions/Action" for "Good habits".  Default value: `true` |
| down optional | Boolean | Only valid for type "habit" If true, enables the "-" under "Directions/Action" for "Bad habits".  Default value: `true` |
| value optional | Number | Only valid for type "reward." The cost in gold of the reward  Default value: `0` |

- [Request-Example:](https://habitica.com/apidoc/#parameter-examples-Task-UpdateTask-0_0_0-0)

```
{
    "notes": "This will be replace the notes, anything not specified will remain the same"
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