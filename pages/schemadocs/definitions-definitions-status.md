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

| Property                              | Type     | Required | Nullable       | Defined by                                                                                                                                                              |
| :------------------------------------ | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [slurm\_job\_state](#slurm_job_state) | `string` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-slurm_job_state.md "definitions.schema.json#/definitions/status/properties/slurm_job_state") |
| [pbs\_job\_state](#pbs_job_state)     | `string` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-pbs_job_state.md "definitions.schema.json#/definitions/status/properties/pbs_job_state")     |
| [lsf\_job\_state](#lsf_job_state)     | `string` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-lsf_job_state.md "definitions.schema.json#/definitions/status/properties/lsf_job_state")     |
| [returncode](#returncode)             | Merged   | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-int_or_list.md "definitions.schema.json#/definitions/status/properties/returncode")                            |
| [regex](#regex)                       | `object` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-regex.md "definitions.schema.json#/definitions/status/properties/regex")                                       |
| [runtime](#runtime)                   | `object` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-runtime.md "definitions.schema.json#/definitions/status/properties/runtime")                 |
| [assert\_ge](#assert_ge)              | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ge.md "definitions.schema.json#/definitions/status/properties/assert_ge")             |
| [assert\_le](#assert_le)              | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_le.md "definitions.schema.json#/definitions/status/properties/assert_le")             |
| [assert\_gt](#assert_gt)              | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_gt.md "definitions.schema.json#/definitions/status/properties/assert_gt")             |
| [assert\_eq](#assert_eq)              | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_eq.md "definitions.schema.json#/definitions/status/properties/assert_eq")             |
| [assert\_range](#assert_range)        | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range.md "definitions.schema.json#/definitions/status/properties/assert_range")       |
| [exists](#exists)                     | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/exists")                            |
| [is\_dir](#is_dir)                    | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_dir")                            |
| [is\_file](#is_file)                  | `array`  | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-list_of_strings.md "definitions.schema.json#/definitions/status/properties/is_file")                           |
| [state](#state)                       | `string` | Optional | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-state.md "definitions.schema.json#/definitions/status/properties/state")                                       |

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

## assert\_eq

Perform assertion of equality (=) with reference value

`assert_eq`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_eq-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_eq.md "definitions.schema.json#/definitions/status/properties/assert_eq")

### assert\_eq Type

`object[]` ([Details](definitions-definitions-status-properties-assert_eq-items.md))

## assert\_range

Perform assertion based on lower and upper bound

`assert_range`

*   is optional

*   Type: `object[]` ([Details](definitions-definitions-status-properties-assert_range-items.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_range.md "definitions.schema.json#/definitions/status/properties/assert_range")

### assert\_range Type

`object[]` ([Details](definitions-definitions-status-properties-assert_range-items.md))

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
