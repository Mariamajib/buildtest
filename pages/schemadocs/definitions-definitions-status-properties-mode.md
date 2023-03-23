# Untitled string in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/mode
```

Determine how the status check is resolved, for instance it can be logical AND or OR

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## mode Type

`string`

## mode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"any"` |             |
| `"all"` |             |
