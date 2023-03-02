# Untitled integer in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/file_count/items/properties/file_traverse_limit
```

Limit the number of files to traverse when searching for files in directory

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## file\_traverse\_limit Type

`integer`

## file\_traverse\_limit Constraints

**maximum**: the value of this number must smaller than or equal to: `999999`

**minimum**: the value of this number must greater than or equal to: `1`

## file\_traverse\_limit Default Value

The default value is:

```json
10000
```
