# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## system Type

`object` ([Details](settings-definitions-system.md))

# system Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                |
| :-------------------------- | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [hostnames](#hostnames)     | `array`   | Required | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-hostnames.md "settings.schema.json#/definitions/system/properties/hostnames")     |
| [description](#description) | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-description.md "settings.schema.json#/definitions/system/properties/description") |
| [poolsize](#poolsize)       | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-poolsize.md "settings.schema.json#/definitions/system/properties/poolsize")       |
| [testdir](#testdir)         | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-testdir.md "settings.schema.json#/definitions/system/properties/testdir")         |
| [logdir](#logdir)           | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-logdir.md "settings.schema.json#/definitions/system/properties/logdir")           |
| [moduletool](#moduletool)   | `string`  | Required | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-moduletool.md "settings.schema.json#/definitions/system/properties/moduletool")   |
| [timeout](#timeout)         | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-timeout.md "settings.schema.json#/definitions/system/properties/timeout")         |
| [pager](#pager)             | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-pager.md "settings.schema.json#/definitions/system/properties/pager")             |
| [buildspecs](#buildspecs)   | `object`  | Required | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs.md "settings.schema.json#/definitions/system/properties/buildspecs")   |
| [report](#report)           | `object`  | Required | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-report.md "settings.schema.json#/definitions/system/properties/report")           |
| [processor](#processor)     | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-processor.md "settings.schema.json#/definitions/system/properties/processor")     |
| [compilers](#compilers)     | `object`  | Required | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-compilers.md "settings.schema.json#/definitions/system/properties/compilers")     |
| [executors](#executors)     | `object`  | Required | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-executors.md "settings.schema.json#/definitions/system/properties/executors")     |
| [cdash](#cdash)             | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-cdash.md "settings.schema.json#/definitions/system/properties/cdash")             |
| [profiles](#profiles)       | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-profiles.md "settings.schema.json#/definitions/system/properties/profiles")       |

## hostnames

Specify a list of hostnames to check where buildtest can run for the given system record

`hostnames`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-hostnames.md "settings.schema.json#/definitions/system/properties/hostnames")

### hostnames Type

`string[]`

## description

system description field

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-description.md "settings.schema.json#/definitions/system/properties/description")

### description Type

`string`

## poolsize

Specify size of Process Pool for parallel processing using `multiprocessing.Pool`

`poolsize`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-poolsize.md "settings.schema.json#/definitions/system/properties/poolsize")

### poolsize Type

`integer`

### poolsize Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## testdir

Specify full path to test directory where buildtest will write tests.

`testdir`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-testdir.md "settings.schema.json#/definitions/system/properties/testdir")

### testdir Type

`string`

## logdir

Specify location where buildtest will write log files

`logdir`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-logdir.md "settings.schema.json#/definitions/system/properties/logdir")

### logdir Type

`string`

## moduletool

Specify modules tool used for interacting with `module` command.

`moduletool`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-moduletool.md "settings.schema.json#/definitions/system/properties/moduletool")

### moduletool Type

`string`

### moduletool Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"environment-modules"` |             |
| `"lmod"`                |             |
| `"N/A"`                 |             |

## timeout

Specify timeout duration in number of seconds

`timeout`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-timeout.md "settings.schema.json#/definitions/system/properties/timeout")

### timeout Type

`integer`

### timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## pager

A boolean to determine whether to enable paging when viewing buildspec cache

`pager`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-pager.md "settings.schema.json#/definitions/system/properties/pager")

### pager Type

`boolean`

## buildspecs

Specify configuration for `buildtest buildspec` command

`buildspecs`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-buildspecs.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs.md "settings.schema.json#/definitions/system/properties/buildspecs")

### buildspecs Type

`object` ([Details](settings-definitions-system-properties-buildspecs.md))

## report



`report`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-report.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report.md "settings.schema.json#/definitions/system/properties/report")

### report Type

`object` ([Details](settings-definitions-system-properties-report.md))

## processor

Specify processor information

`processor`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-processor.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-processor.md "settings.schema.json#/definitions/system/properties/processor")

### processor Type

`object` ([Details](settings-definitions-system-properties-processor.md))

## compilers

Declare compiler section for defining system compilers that can be referenced in buildspec.

`compilers`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-compilers.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers.md "settings.schema.json#/definitions/system/properties/compilers")

### compilers Type

`object` ([Details](settings-definitions-system-properties-compilers.md))

## executors

The executor section is used for declaring your executors that are responsible for running jobs. The executor section can be `local`, `lsf`, `slurm`, `cobalt`. The executors are referenced in buildspec using `executor` field.

`executors`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-executors.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-executors.md "settings.schema.json#/definitions/system/properties/executors")

### executors Type

`object` ([Details](settings-definitions-system-properties-executors.md))

## cdash

Specify CDASH configuration used to upload tests via 'buildtest cdash' command

`cdash`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-cdash.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-cdash.md "settings.schema.json#/definitions/system/properties/cdash")

### cdash Type

`object` ([Details](settings-definitions-system-properties-cdash.md))

## profiles

The profiles section is used for declaring one or more profiles that can be used to run `buildtest build` that are captured as command options

`profiles`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-profiles.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-profiles.md "settings.schema.json#/definitions/system/properties/profiles")

### profiles Type

`object` ([Details](settings-definitions-system-properties-profiles.md))
