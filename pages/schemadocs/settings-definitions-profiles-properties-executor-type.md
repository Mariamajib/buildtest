# Untitled string in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/profiles/properties/executor-type
```

Specify the `executor-type` field used by `--executor-type` option which determines if test will run by local or batch executor

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## executor-type Type

`string`

## executor-type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"local"` |             |
| `"batch"` |             |
