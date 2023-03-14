# Untitled object in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/metrics/additionalProperties
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## additionalProperties Type

`object` ([Details](definitions-definitions-metrics_field.md))

one (and only one) of

*   [Untitled undefined type in JSON Schema Definitions File. ](definitions-definitions-metrics_field-oneof-0.md "check type definition")

*   [Untitled undefined type in JSON Schema Definitions File. ](definitions-definitions-metrics_field-oneof-1.md "check type definition")

# additionalProperties Properties

| Property                   | Type     | Required | Nullable       | Defined by                                                                                                                                                      |
| :------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)              | `string` | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-metrics_field-properties-type.md "definitions.schema.json#/definitions/metrics_field/properties/type") |
| [regex](#regex)            | `object` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/metrics_field/properties/regex")                        |
| [file\_regex](#file_regex) | `object` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics.md "definitions.schema.json#/definitions/metrics_field/properties/file_regex")   |

## type

Specify python data-type (str, int, float) to convert metric.

`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-metrics_field-properties-type.md "definitions.schema.json#/definitions/metrics_field/properties/type")

### type Type

`string`

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"str"`   |             |
| `"int"`   |             |
| `"float"` |             |

## regex

Perform regular expression search using `re.search` python module on stdout/stderr stream for reporting if test `PASS`.

`regex`

*   is optional

*   Type: `object` ([Details](definitions-definitions-regex.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/metrics_field/properties/regex")

### regex Type

`object` ([Details](definitions-definitions-regex.md))

## file\_regex

Specify a regular expressions on a filepath used for assigning value to metrics. The regular expression is matched using `re.search` python module.

`file_regex`

*   is optional

*   Type: `object` ([Details](definitions-definitions-file_regex_in_metrics.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics.md "definitions.schema.json#/definitions/metrics_field/properties/file_regex")

### file\_regex Type

`object` ([Details](definitions-definitions-file_regex_in_metrics.md))
