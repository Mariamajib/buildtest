# Untitled object in spack schema version Schema

```txt
spack.schema.json#/properties/status
```

The status section describes how buildtest detects PASS/FAIL on test. By default returncode 0 is a PASS and anything else is a FAIL, however buildtest can support other types of PASS/FAIL conditions.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [spack.schema.json\*](../out/spack.schema.json "open original schema") |

## status Type

`object` ([Details](definitions-definitions-status.md))

# status Properties

| Property                              | Type          | Required | Nullable       | Defined by                                                                                                                                                              |
| :------------------------------------ | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [slurm\_job\_state](#slurm_job_state) | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-slurm_job_state.md "definitions.schema.json#/definitions/status/properties/slurm_job_state") |
| [pbs\_job\_state](#pbs_job_state)     | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-pbs_job_state.md "definitions.schema.json#/definitions/status/properties/pbs_job_state")     |
| [lsf\_job\_state](#lsf_job_state)     | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-lsf_job_state.md "definitions.schema.json#/definitions/status/properties/lsf_job_state")     |
| [returncode](#returncode)             | Merged        | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-int_or_list.md "definitions.schema.json#/definitions/status/properties/returncode")                            |
| [regex](#regex)                       | `object`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/status/properties/regex")                                       |
| [file\_regex](#file_regex)            | `array`       | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-file_regex.md "definitions.schema.json#/definitions/status/properties/file_regex")                             |
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
| [state](#state)                       | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-state.md "definitions.schema.json#/definitions/status/properties/state")                                       |
| [mode](#mode)                         | `string`      | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-mode.md "definitions.schema.json#/definitions/status/properties/mode")                       |

## slurm\_job\_state

This field can be used to pass test based on Slurm Job State, if there is a match buildtest will report as `PASS`

`slurm_job_state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-slurm_job_state.md "definitions.schema.json#/definitions/status/properties/slurm_job_state")

### slurm\_job\_state Type

`string`

### slurm\_job\_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value             | Explanation |
| :---------------- | :---------- |
| `"COMPLETED"`     |             |
| `"FAILED"`        |             |
| `"OUT_OF_MEMORY"` |             |
| `"TIMEOUT"`       |             |

## pbs\_job\_state

This field can be used to pass test based on PBS Job State, if there is a match buildtest will report as `PASS`

`pbs_job_state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-pbs_job_state.md "definitions.schema.json#/definitions/status/properties/pbs_job_state")

### pbs\_job\_state Type

`string`

### pbs\_job\_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value | Explanation |
| :---- | :---------- |
| `"H"` |             |
| `"S"` |             |
| `"F"` |             |

## lsf\_job\_state

This field can be used to pass test based on LSF Job State, if there is a match buildtest will report as `PASS`

`lsf_job_state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-lsf_job_state.md "definitions.schema.json#/definitions/status/properties/lsf_job_state")

### lsf\_job\_state Type

`string`

### lsf\_job\_state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"DONE"` |             |
| `"EXIT"` |             |

## returncode

Specify a list of returncodes to match with script's exit code. buildtest will PASS test if script's exit code is found in list of returncodes. You must specify unique numbers as list and a minimum of 1 item in array

`returncode`

*   is optional

*   Type: merged type ([Details](definitions-definitions-int_or_list.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-int_or_list.md "definitions.schema.json#/definitions/status/properties/returncode")

### returncode Type

merged type ([Details](definitions-definitions-int_or_list.md))

one (and only one) of

*   [Untitled integer in JSON Schema Definitions File. ](definitions-definitions-int_or_list-oneof-0.md "check type definition")

*   [Untitled array in JSON Schema Definitions File. ](definitions-definitions-list_of_ints.md "check type definition")

## regex

Perform regular expression search using `re.search` python module on stdout/stderr stream for reporting if test `PASS`.

`regex`

*   is optional

*   Type: `object` ([Details](definitions-definitions-regex.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/status/properties/regex")

### regex Type

`object` ([Details](definitions-definitions-regex.md))

## file\_regex

Specify a list of regular expressions to match files in the current working directory. The regular expression is matched using `re.search` python module.

`file_regex`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-file_regex-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-file_regex.md "definitions.schema.json#/definitions/status/properties/file_regex")

### file\_regex Type

`object[]` ([Details](definitions-definitions-file_regex-items.md))

## runtime

The runtime section will pass test based on min and max values and compare with actual runtime.

`runtime`

*   is optional

*   Type: `object` ([Details](definitions-definitions-status-properties-runtime.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-runtime.md "definitions.schema.json#/definitions/status/properties/runtime")

### runtime Type

`object` ([Details](definitions-definitions-status-properties-runtime.md))

## assert\_ge

Perform assertion of greater and equal (>=) with reference value

`assert_ge`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_ge-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ge.md "definitions.schema.json#/definitions/status/properties/assert_ge")

### assert\_ge Type

`object[]` ([Details](definitions-definitions-status-properties-assert_ge-items.md))

## assert\_le

Perform assertion of less than and equal (<=) with reference value

`assert_le`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_le-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_le.md "definitions.schema.json#/definitions/status/properties/assert_le")

### assert\_le Type

`object[]` ([Details](definitions-definitions-status-properties-assert_le-items.md))

## assert\_gt

Perform assertion of greater than (>) with reference value

`assert_gt`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_gt-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_gt.md "definitions.schema.json#/definitions/status/properties/assert_gt")

### assert\_gt Type

`object[]` ([Details](definitions-definitions-status-properties-assert_gt-items.md))

## assert\_lt

Perform assertion of less than (<) with reference value

`assert_lt`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_lt-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_lt.md "definitions.schema.json#/definitions/status/properties/assert_lt")

### assert\_lt Type

`object[]` ([Details](definitions-definitions-status-properties-assert_lt-items.md))

## assert\_eq

Perform assertion of equality (=) with reference value

`assert_eq`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_eq-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_eq.md "definitions.schema.json#/definitions/status/properties/assert_eq")

### assert\_eq Type

`object[]` ([Details](definitions-definitions-status-properties-assert_eq-items.md))

## assert\_ne

Perform assertion of not equal with reference value

`assert_ne`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_ne-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne.md "definitions.schema.json#/definitions/status/properties/assert_ne")

### assert\_ne Type

`object[]` ([Details](definitions-definitions-status-properties-assert_ne-items.md))

## assert\_range

Perform assertion based on lower and upper bound

`assert_range`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_range-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range.md "definitions.schema.json#/definitions/status/properties/assert_range")

### assert\_range Type

`object[]` ([Details](definitions-definitions-status-properties-assert_range-items.md))

## contains

Check if metric value is in a list of reference values

`contains`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-contains.md "definitions.schema.json#/definitions/status/properties/contains")

### contains Type

unknown

## not\_contains

Check if metric value not in a list of reference values

`not_contains`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-not_contains.md "definitions.schema.json#/definitions/status/properties/not_contains")

### not\_contains Type

unknown

## is\_symlink

Check for list of files or directory paths that are symbolic links

`is_symlink`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_symlink")

### is\_symlink Type

`string[]`

### is\_symlink Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## exists

Check for list of file or directory path for existences using os.path.exists

`exists`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/exists")

### exists Type

`string[]`

### exists Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## is\_dir

Check for list of filepaths are directories

`is_dir`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_dir")

### is\_dir Type

`string[]`

### is\_dir Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## is\_file

Check for list of filepaths are files

`is_file`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_file")

### is\_file Type

`string[]`

### is\_file Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## file\_count

Perform assertion check by comparing file count in a directory

`file_count`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-file_count-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-file_count.md "definitions.schema.json#/definitions/status/properties/file_count")

### file\_count Type

`object[]` ([Details](definitions-definitions-status-properties-file_count-items.md))

## state

explicitly mark state of test regardless of status calculation

`state`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-state.md "definitions.schema.json#/definitions/status/properties/state")

### state Type

`string`

### state Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"PASS"` |             |
| `"FAIL"` |             |

## mode

Determine how the status check is resolved, for instance it can be logical AND or OR

`mode`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-mode.md "definitions.schema.json#/definitions/status/properties/mode")

### mode Type

`string`

### mode Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | :---------- |
| `"any"` |             |
| `"all"` |             |
