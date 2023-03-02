# Untitled object in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/file_count/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## items Type

`object` ([Details](definitions-definitions-status-properties-file_count-items.md))

# items Properties

| Property                                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                              |
| :-------------------------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [dir](#dir)                                   | `string`  | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-dir.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/dir")                                 |
| [count](#count)                               | `integer` | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-count.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/count")                             |
| [depth](#depth)                               | `integer` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-depth.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/depth")                             |
| [ext](#ext)                                   | Merged    | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-string_or_list.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/ext")                                                                    |
| [filepattern](#filepattern)                   | `string`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-filepattern.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/filepattern")                 |
| [filetype](#filetype)                         | `string`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-filetype.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/filetype")                       |
| [file\_traverse\_limit](#file_traverse_limit) | `integer` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-file_traverse_limit.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/file_traverse_limit") |

## dir

Directory path to check for file count

`dir`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-dir.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/dir")

### dir Type

`string`

## count

Number of files expected in directory

`count`

*   is required

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-count.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/count")

### count Type

`integer`

### count Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## depth

Depth of directory to search for files

`depth`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-depth.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/depth")

### depth Type

`integer`

### depth Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## ext

File extension to filter files in directory

`ext`

*   is optional

*   Type: merged type ([Details](definitions-definitions-string_or_list.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-string_or_list.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/ext")

### ext Type

merged type ([Details](definitions-definitions-string_or_list.md))

one (and only one) of

*   [Untitled string in JSON Schema Definitions File. ](definitions-definitions-string_or_list-oneof-0.md "check type definition")

*   [Untitled array in JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "check type definition")

## filepattern

Specify a regular expression when searching for files in directory

`filepattern`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-filepattern.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/filepattern")

### filepattern Type

`string`

## filetype

Specify file type when searching for files in directory. It can be 'file', 'dir' or 'symlink'

`filetype`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-filetype.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/filetype")

### filetype Type

`string`

### filetype Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"file"`    |             |
| `"dir"`     |             |
| `"symlink"` |             |

## file\_traverse\_limit

Limit the number of files to traverse when searching for files in directory

`file_traverse_limit`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count-items-properties-file_traverse_limit.md "definitions.schema.json#/definitions/status/properties/file_count/items/properties/file_traverse_limit")

### file\_traverse\_limit Type

`integer`

### file\_traverse\_limit Constraints

**maximum**: the value of this number must smaller than or equal to: `999999`

**minimum**: the value of this number must greater than or equal to: `1`

### file\_traverse\_limit Default Value

The default value is:

```json
10000
```
