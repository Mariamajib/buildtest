# Untitled object in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/file_regex_in_metrics
```

Specify a regular expressions on a filepath used for assigning value to metrics. The regular expression is matched using `re.search` python module.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## file\_regex\_in\_metrics Type

`object` ([Details](definitions-definitions-file_regex_in_metrics.md))

# file\_regex\_in\_metrics Properties

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                                                                      |
| :-------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [additionalProperties](#additionalproperties) | Not specified | Optional | cannot be null | [Untitled schema](undefined.md "undefined#undefined")                                                                                                                           |
| [file](#file)                                 | `string`      | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-file.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/file") |
| [exp](#exp)                                   | `string`      | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-exp.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/exp")   |
| [item](#item)                                 | `integer`     | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-item.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/item") |

## additionalProperties

no description

`additionalProperties`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Untitled schema](undefined.md "undefined#undefined")

### Untitled schema Type

unknown

## file

Specify a file name to match with regular expression

`file`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-file.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/file")

### file Type

`string`

## exp

Specify a regular expression to run on the selected file name

`exp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-exp.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/exp")

### exp Type

`string`

## item

Specify the item number used to index element in `match.group() <https://docs.python.org/3/library/re.html#match-objects>`\_

`item`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-item.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/item")

### item Type

`integer`

### item Constraints

**minimum**: the value of this number must greater than or equal to: `0`
