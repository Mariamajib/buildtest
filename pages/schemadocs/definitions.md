# JSON Schema Definitions File.  Schema

```txt
definitions.schema.json
```

This file is used for declaring definitions that are referenced from other schemas

| Abstract               | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :--------------------- | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Cannot be instantiated | Yes        | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [definitions.schema.json](../out/definitions.schema.json "open original schema") |

## JSON Schema Definitions File.  Type

unknown ([JSON Schema Definitions File. ](definitions.md))

# JSON Schema Definitions File.  Definitions

## Definitions group list\_of\_strings

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/list_of_strings"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group string\_or\_list

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/string_or_list"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group list\_of\_ints

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/list_of_ints"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group list\_of\_positive\_integers

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/list_of_positive_integers"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group int\_or\_list

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/int_or_list"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group file\_regex

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/file_regex"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group file\_regex\_in\_metrics

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/file_regex_in_metrics"}
```

| Property                                      | Type          | Required | Nullable       | Defined by                                                                                                                                                                      |
| :-------------------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [additionalProperties](#additionalproperties) | Not specified | Optional | cannot be null | [Untitled schema](undefined.md "undefined#undefined")                                                                                                                           |
| [file](#file)                                 | `string`      | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-file.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/file") |
| [exp](#exp)                                   | `string`      | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-exp.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/exp")   |
| [item](#item)                                 | `integer`     | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-item.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/item") |

### additionalProperties

no description

`additionalProperties`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Untitled schema](undefined.md "undefined#undefined")

#### Untitled schema Type

unknown

### file

Specify a file name to match with regular expression

`file`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-file.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/file")

#### file Type

`string`

### exp

Specify a regular expression to run on the selected file name

`exp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-exp.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/exp")

#### exp Type

`string`

### item

Specify the item number used to index element in `match.group() <https://docs.python.org/3/library/re.html#match-objects>`\_

`item`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics-properties-item.md "definitions.schema.json#/definitions/file_regex_in_metrics/properties/item")

#### item Type

`integer`

#### item Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## Definitions group regex

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/regex"}
```

| Property          | Type      | Required | Nullable       | Defined by                                                                                                                                          |
| :---------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| [stream](#stream) | `string`  | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex-properties-stream.md "definitions.schema.json#/definitions/regex/properties/stream") |
| [exp](#exp-1)     | `string`  | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex-properties-exp.md "definitions.schema.json#/definitions/regex/properties/exp")       |
| [item](#item-1)   | `integer` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex-properties-item.md "definitions.schema.json#/definitions/regex/properties/item")     |

### stream

The stream field can be stdout or stderr. buildtest will read the output or error stream after completion of test and check if regex matches in stream

`stream`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex-properties-stream.md "definitions.schema.json#/definitions/regex/properties/stream")

#### stream Type

`string`

#### stream Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"stdout"` |             |
| `"stderr"` |             |

### exp

Specify a regular expression to run with input stream specified by `stream` field. buildtest uses re.search when performing regex

`exp`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex-properties-exp.md "definitions.schema.json#/definitions/regex/properties/exp")

#### exp Type

`string`

### item

Specify the item number used to index element in `match.group() <https://docs.python.org/3/library/re.html#match-objects>`\_

`item`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex-properties-item.md "definitions.schema.json#/definitions/regex/properties/item")

#### item Type

`integer`

#### item Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## Definitions group env

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/env"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group description

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/description"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group summary

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/summary"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group tags

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/tags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group skip

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/skip"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group executor

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/executor"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group needs

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/needs"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group metrics\_field

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/metrics_field"}
```

| Property                   | Type     | Required | Nullable       | Defined by                                                                                                                                                      |
| :------------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)              | `string` | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-metrics_field-properties-type.md "definitions.schema.json#/definitions/metrics_field/properties/type") |
| [regex](#regex)            | `object` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/metrics_field/properties/regex")                        |
| [file\_regex](#file_regex) | `object` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics.md "definitions.schema.json#/definitions/metrics_field/properties/file_regex")   |

### type

Specify python data-type (str, int, float) to convert metric.

`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-metrics_field-properties-type.md "definitions.schema.json#/definitions/metrics_field/properties/type")

#### type Type

`string`

#### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"str"`   |             |
| `"int"`   |             |
| `"float"` |             |

### regex

Perform regular expression search using `re.search` python module on stdout/stderr stream for reporting if test `PASS`.

`regex`

*   is optional

*   Type: `object` ([Details](definitions-definitions-regex.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/metrics_field/properties/regex")

#### regex Type

`object` ([Details](definitions-definitions-regex.md))

### file\_regex

Specify a regular expressions on a filepath used for assigning value to metrics. The regular expression is matched using `re.search` python module.

`file_regex`

*   is optional

*   Type: `object` ([Details](definitions-definitions-file_regex_in_metrics.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex_in_metrics.md "definitions.schema.json#/definitions/metrics_field/properties/file_regex")

#### file\_regex Type

`object` ([Details](definitions-definitions-file_regex_in_metrics.md))

## Definitions group metrics

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/metrics"}
```

| Property              | Type   | Required | Nullable       | Defined by                                                                                                                                     |
| :-------------------- | :----- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | Merged | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-metrics_field.md "definitions.schema.json#/definitions/metrics/additionalProperties") |

### Additional Properties

Additional properties are allowed, as long as they follow this schema:



*   is optional

*   Type: `object` ([Details](definitions-definitions-metrics_field.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-metrics_field.md "definitions.schema.json#/definitions/metrics/additionalProperties")

#### additionalProperties Type

`object` ([Details](definitions-definitions-metrics_field.md))

one (and only one) of

*   [Untitled undefined type in JSON Schema Definitions File. ](definitions-definitions-metrics_field-oneof-0.md "check type definition")

*   [Untitled undefined type in JSON Schema Definitions File. ](definitions-definitions-metrics_field-oneof-1.md "check type definition")

## Definitions group state

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/state"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group returncode

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/returncode"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group status

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/status"}
```

| Property                              | Type          | Required | Nullable       | Defined by                                                                                                                                                              |
| :------------------------------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [slurm\_job\_state](#slurm_job_state) | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-slurm_job_state.md "definitions.schema.json#/definitions/status/properties/slurm_job_state") |
| [pbs\_job\_state](#pbs_job_state)     | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-pbs_job_state.md "definitions.schema.json#/definitions/status/properties/pbs_job_state")     |
| [lsf\_job\_state](#lsf_job_state)     | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-lsf_job_state.md "definitions.schema.json#/definitions/status/properties/lsf_job_state")     |
| [returncode](#returncode)             | Merged        | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-int_or_list.md "definitions.schema.json#/definitions/status/properties/returncode")                            |
| [regex](#regex-1)                     | `object`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/status/properties/regex")                                       |
| [file\_regex](#file_regex-1)          | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex.md "definitions.schema.json#/definitions/status/properties/file_regex")                             |
| [runtime](#runtime)                   | `object`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-runtime.md "definitions.schema.json#/definitions/status/properties/runtime")                 |
| [assert\_ge](#assert_ge)              | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ge.md "definitions.schema.json#/definitions/status/properties/assert_ge")             |
| [assert\_le](#assert_le)              | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_le.md "definitions.schema.json#/definitions/status/properties/assert_le")             |
| [assert\_gt](#assert_gt)              | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_gt.md "definitions.schema.json#/definitions/status/properties/assert_gt")             |
| [assert\_lt](#assert_lt)              | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_lt.md "definitions.schema.json#/definitions/status/properties/assert_lt")             |
| [assert\_eq](#assert_eq)              | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_eq.md "definitions.schema.json#/definitions/status/properties/assert_eq")             |
| [assert\_ne](#assert_ne)              | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne.md "definitions.schema.json#/definitions/status/properties/assert_ne")             |
| [assert\_range](#assert_range)        | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range.md "definitions.schema.json#/definitions/status/properties/assert_range")       |
| [contains](#contains)                 | Not specified | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-contains.md "definitions.schema.json#/definitions/status/properties/contains")               |
| [not\_contains](#not_contains)        | Not specified | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-not_contains.md "definitions.schema.json#/definitions/status/properties/not_contains")       |
| [is\_symlink](#is_symlink)            | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_symlink")                        |
| [exists](#exists)                     | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/exists")                            |
| [is\_dir](#is_dir)                    | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_dir")                            |
| [is\_file](#is_file)                  | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_file")                           |
| [file\_count](#file_count)            | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count.md "definitions.schema.json#/definitions/status/properties/file_count")           |
| [state](#state)                       | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-state.md "definitions.schema.json#/definitions/status/properties/state")                     |
| [mode](#mode)                         | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-mode.md "definitions.schema.json#/definitions/status/properties/mode")                       |

### slurm\_job\_state

This field can be used to pass test based on Slurm Job State, if there is a match buildtest will report as `PASS`

`slurm_job_state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-slurm_job_state.md "definitions.schema.json#/definitions/status/properties/slurm_job_state")

#### slurm\_job\_state Type

`string`

#### slurm\_job\_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"COMPLETED"`     |             |
| `"FAILED"`        |             |
| `"OUT_OF_MEMORY"` |             |
| `"TIMEOUT"`       |             |

### pbs\_job\_state

This field can be used to pass test based on PBS Job State, if there is a match buildtest will report as `PASS`

`pbs_job_state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-pbs_job_state.md "definitions.schema.json#/definitions/status/properties/pbs_job_state")

#### pbs\_job\_state Type

`string`

#### pbs\_job\_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `"H"` |             |
| `"S"` |             |
| `"F"` |             |

### lsf\_job\_state

This field can be used to pass test based on LSF Job State, if there is a match buildtest will report as `PASS`

`lsf_job_state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-lsf_job_state.md "definitions.schema.json#/definitions/status/properties/lsf_job_state")

#### lsf\_job\_state Type

`string`

#### lsf\_job\_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"DONE"` |             |
| `"EXIT"` |             |

### returncode

Specify a list of returncodes to match with script's exit code. buildtest will PASS test if script's exit code is found in list of returncodes. You must specify unique numbers as list and a minimum of 1 item in array

`returncode`

*   is optional

*   Type: merged type ([Details](definitions-definitions-int_or_list.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-int_or_list.md "definitions.schema.json#/definitions/status/properties/returncode")

#### returncode Type

merged type ([Details](definitions-definitions-int_or_list.md))

one (and only one) of

*   [Untitled integer in JSON Schema Definitions File. ](definitions-definitions-int_or_list-oneof-0.md "check type definition")

*   [Untitled array in JSON Schema Definitions File. ](definitions-definitions-list_of_ints.md "check type definition")

### regex

Perform regular expression search using `re.search` python module on stdout/stderr stream for reporting if test `PASS`.

`regex`

*   is optional

*   Type: `object` ([Details](definitions-definitions-regex.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/status/properties/regex")

#### regex Type

`object` ([Details](definitions-definitions-regex.md))

### file\_regex

Specify a list of regular expressions to match files in the current working directory. The regular expression is matched using `re.search` python module.

`file_regex`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-file_regex-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex.md "definitions.schema.json#/definitions/status/properties/file_regex")

#### file\_regex Type

`object[]` ([Details](definitions-definitions-file_regex-items.md))

### runtime

The runtime section will pass test based on min and max values and compare with actual runtime.

`runtime`

*   is optional

*   Type: `object` ([Details](definitions-definitions-status-properties-runtime.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-runtime.md "definitions.schema.json#/definitions/status/properties/runtime")

#### runtime Type

`object` ([Details](definitions-definitions-status-properties-runtime.md))

### assert\_ge

Perform assertion of greater and equal (>=) with reference value

`assert_ge`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_ge-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ge.md "definitions.schema.json#/definitions/status/properties/assert_ge")

#### assert\_ge Type

`object[]` ([Details](definitions-definitions-status-properties-assert_ge-items.md))

### assert\_le

Perform assertion of less than and equal (<=) with reference value

`assert_le`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_le-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_le.md "definitions.schema.json#/definitions/status/properties/assert_le")

#### assert\_le Type

`object[]` ([Details](definitions-definitions-status-properties-assert_le-items.md))

### assert\_gt

Perform assertion of greater than (>) with reference value

`assert_gt`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_gt-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_gt.md "definitions.schema.json#/definitions/status/properties/assert_gt")

#### assert\_gt Type

`object[]` ([Details](definitions-definitions-status-properties-assert_gt-items.md))

### assert\_lt

Perform assertion of less than (<) with reference value

`assert_lt`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_lt-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_lt.md "definitions.schema.json#/definitions/status/properties/assert_lt")

#### assert\_lt Type

`object[]` ([Details](definitions-definitions-status-properties-assert_lt-items.md))

### assert\_eq

Perform assertion of equality (=) with reference value

`assert_eq`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_eq-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_eq.md "definitions.schema.json#/definitions/status/properties/assert_eq")

#### assert\_eq Type

`object[]` ([Details](definitions-definitions-status-properties-assert_eq-items.md))

### assert\_ne

Perform assertion of not equal with reference value

`assert_ne`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_ne-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne.md "definitions.schema.json#/definitions/status/properties/assert_ne")

#### assert\_ne Type

`object[]` ([Details](definitions-definitions-status-properties-assert_ne-items.md))

### assert\_range

Perform assertion based on lower and upper bound

`assert_range`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_range-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range.md "definitions.schema.json#/definitions/status/properties/assert_range")

#### assert\_range Type

`object[]` ([Details](definitions-definitions-status-properties-assert_range-items.md))

### contains

Check if metric value is in a list of reference values

`contains`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-contains.md "definitions.schema.json#/definitions/status/properties/contains")

#### contains Type

unknown

### not\_contains

Check if metric value not in a list of reference values

`not_contains`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-not_contains.md "definitions.schema.json#/definitions/status/properties/not_contains")

#### not\_contains Type

unknown

### is\_symlink

Check for list of files or directory paths that are symbolic links

`is_symlink`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_symlink")

#### is\_symlink Type

`string[]`

#### is\_symlink Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### exists

Check for list of file or directory path for existences using os.path.exists

`exists`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/exists")

#### exists Type

`string[]`

#### exists Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### is\_dir

Check for list of filepaths are directories

`is_dir`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_dir")

#### is\_dir Type

`string[]`

#### is\_dir Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### is\_file

Check for list of filepaths are files

`is_file`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_file")

#### is\_file Type

`string[]`

#### is\_file Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### file\_count

Perform assertion check by comparing file count in a directory

`file_count`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-file_count-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count.md "definitions.schema.json#/definitions/status/properties/file_count")

#### file\_count Type

`object[]` ([Details](definitions-definitions-status-properties-file_count-items.md))

### state

explicitly mark state of test regardless of status calculation

`state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-state.md "definitions.schema.json#/definitions/status/properties/state")

#### state Type

`string`

#### state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"PASS"` |             |
| `"FAIL"` |             |

### mode

Determine how the status check is resolved, for instance it can be logical AND or OR

`mode`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-mode.md "definitions.schema.json#/definitions/status/properties/mode")

#### mode Type

`string`

#### mode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"any"` |             |
| `"all"` |             |

## Definitions group BB

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/BB"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group DW

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/DW"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group sbatch

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/sbatch"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group bsub

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/bsub"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cobalt

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/cobalt"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group pbs

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/pbs"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group executors

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/executors"}
```

| Property      | Type          | Required | Nullable       | Defined by                                                                                                                                                        |
| :------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description` | Not specified | Optional | cannot be null | [Untitled schema](undefined.md "undefined#undefined")                                                                                                             |
| `^.*$`        | Not specified | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-executors-patternproperties-.md "definitions.schema.json#/definitions/executors/patternProperties/^.*$") |

### Pattern: `description`

no description

`description`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [Untitled schema](undefined.md "undefined#undefined")

#### Untitled schema Type

unknown

### Pattern: `^.*$`



`^.*$`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-executors-patternproperties-.md "definitions.schema.json#/definitions/executors/patternProperties/^.*$")

#### ^.\*$ Type

unknown

## Definitions group cc

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/cc"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fc

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/fc"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cxx

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/cxx"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cflags

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/cflags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fflags

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/fflags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cxxflags

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/cxxflags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group ldflags

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/ldflags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cppflags

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/cppflags"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group run

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/run"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group module

Reference this group by using

```json
{"$ref":"definitions.schema.json#/definitions/module"}
```

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                                              |
| :------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [purge](#purge)     | `boolean` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-module-properties-purge.md "definitions.schema.json#/definitions/module/properties/purge")     |
| [load](#load)       | `array`   | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/module/properties/load")              |
| [restore](#restore) | `string`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-module-properties-restore.md "definitions.schema.json#/definitions/module/properties/restore") |
| [swap](#swap)       | `array`   | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-module-properties-swap.md "definitions.schema.json#/definitions/module/properties/swap")       |

### purge

Run `module purge` if purge is set

`purge`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-module-properties-purge.md "definitions.schema.json#/definitions/module/properties/purge")

#### purge Type

`boolean`

### load

Load one or more modules via `module load`

`load`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/module/properties/load")

#### load Type

`string[]`

#### load Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### restore

Load a collection name via `module restore`

`restore`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-module-properties-restore.md "definitions.schema.json#/definitions/module/properties/restore")

#### restore Type

`string`

### swap

Swap modules using `module swap`. The swap property expects 2 unique modules.

`swap`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-module-properties-swap.md "definitions.schema.json#/definitions/module/properties/swap")

#### swap Type

`string[]`

#### swap Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
