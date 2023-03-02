# Untitled string in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/file_count/items/properties/filetype
```

Specify file type when searching for files in directory. It can be 'file', 'dir' or 'symlink'

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## filetype Type

`string`

## filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"file"`    |             |
| `"dir"`     |             |
| `"symlink"` |             |
