# buildtest configuration schema Schema

```txt
settings.schema.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                 |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------- |
| Can be instantiated | Yes        | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json](../out/settings.schema.json "open original schema") |

## buildtest configuration schema Type

`object` ([buildtest configuration schema](settings.md))

# buildtest configuration schema Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                |
| :---------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------- |
| [system](#system) | `object` | Required | cannot be null | [buildtest configuration schema](settings-properties-system.md "settings.schema.json#/properties/system") |

## system



`system`

*   is required

*   Type: `object` ([Details](settings-properties-system.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-properties-system.md "settings.schema.json#/properties/system")

### system Type

`object` ([Details](settings-properties-system.md))

# buildtest configuration schema Definitions

## Definitions group terse

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/terse"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group format

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/format"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group count

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/count"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group system

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/system"}
```

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

### hostnames

Specify a list of hostnames to check where buildtest can run for the given system record

`hostnames`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-hostnames.md "settings.schema.json#/definitions/system/properties/hostnames")

#### hostnames Type

`string[]`

### description

system description field

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-description.md "settings.schema.json#/definitions/system/properties/description")

#### description Type

`string`

### poolsize

Specify size of Process Pool for parallel processing using `multiprocessing.Pool`

`poolsize`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-poolsize.md "settings.schema.json#/definitions/system/properties/poolsize")

#### poolsize Type

`integer`

#### poolsize Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### testdir

Specify full path to test directory where buildtest will write tests.

`testdir`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-testdir.md "settings.schema.json#/definitions/system/properties/testdir")

#### testdir Type

`string`

### logdir

Specify location where buildtest will write log files

`logdir`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-logdir.md "settings.schema.json#/definitions/system/properties/logdir")

#### logdir Type

`string`

### moduletool

Specify modules tool used for interacting with `module` command.

`moduletool`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-moduletool.md "settings.schema.json#/definitions/system/properties/moduletool")

#### moduletool Type

`string`

#### moduletool Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                   | Explanation |
| :---------------------- | :---------- |
| `"environment-modules"` |             |
| `"lmod"`                |             |
| `"N/A"`                 |             |

### timeout

Specify timeout duration in number of seconds

`timeout`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-timeout.md "settings.schema.json#/definitions/system/properties/timeout")

#### timeout Type

`integer`

#### timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### pager

A boolean to determine whether to enable paging when viewing buildspec cache

`pager`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-pager.md "settings.schema.json#/definitions/system/properties/pager")

#### pager Type

`boolean`

### buildspecs

Specify configuration for `buildtest buildspec` command

`buildspecs`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-buildspecs.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs.md "settings.schema.json#/definitions/system/properties/buildspecs")

#### buildspecs Type

`object` ([Details](settings-definitions-system-properties-buildspecs.md))

### report



`report`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-report.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report.md "settings.schema.json#/definitions/system/properties/report")

#### report Type

`object` ([Details](settings-definitions-system-properties-report.md))

### processor

Specify processor information

`processor`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-processor.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-processor.md "settings.schema.json#/definitions/system/properties/processor")

#### processor Type

`object` ([Details](settings-definitions-system-properties-processor.md))

### compilers

Declare compiler section for defining system compilers that can be referenced in buildspec.

`compilers`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-compilers.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-compilers.md "settings.schema.json#/definitions/system/properties/compilers")

#### compilers Type

`object` ([Details](settings-definitions-system-properties-compilers.md))

### executors

The executor section is used for declaring your executors that are responsible for running jobs. The executor section can be `local`, `lsf`, `slurm`, `cobalt`. The executors are referenced in buildspec using `executor` field.

`executors`

*   is required

*   Type: `object` ([Details](settings-definitions-system-properties-executors.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-executors.md "settings.schema.json#/definitions/system/properties/executors")

#### executors Type

`object` ([Details](settings-definitions-system-properties-executors.md))

### cdash

Specify CDASH configuration used to upload tests via 'buildtest cdash' command

`cdash`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-cdash.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-cdash.md "settings.schema.json#/definitions/system/properties/cdash")

#### cdash Type

`object` ([Details](settings-definitions-system-properties-cdash.md))

### profiles

The profiles section is used for declaring one or more profiles that can be used to run `buildtest build` that are captured as command options

`profiles`

*   is optional

*   Type: `object` ([Details](settings-definitions-system-properties-profiles.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-profiles.md "settings.schema.json#/definitions/system/properties/profiles")

#### profiles Type

`object` ([Details](settings-definitions-system-properties-profiles.md))

## Definitions group cc

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/cc"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group cxx

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/cxx"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group fc

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/fc"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group max\_jobs

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/max_jobs"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group compiler\_section

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/compiler_section"}
```

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                    |
| :---------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [cc](#cc)         | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-compiler_section-properties-cc.md "settings.schema.json#/definitions/compiler_section/properties/cc")   |
| [cxx](#cxx)       | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-compiler_section-properties-cxx.md "settings.schema.json#/definitions/compiler_section/properties/cxx") |
| [fc](#fc)         | `string` | Required | cannot be null | [buildtest configuration schema](settings-definitions-compiler_section-properties-fc.md "settings.schema.json#/definitions/compiler_section/properties/fc")   |
| [module](#module) | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/compiler_section/properties/module")                       |

### cc

Specify path to C compiler wrapper. You may specify a compiler wrapper such as `gcc` assuming its in $PATH or you can use `modules` property to resolve path to compiler wrapper.

`cc`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-compiler_section-properties-cc.md "settings.schema.json#/definitions/compiler_section/properties/cc")

#### cc Type

`string`

### cxx

Specify path to C++ compiler wrapper. You may specify a compiler wrapper such as `g++` assuming its in $PATH or you can use `modules` property to resolve path to compiler wrapper.

`cxx`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-compiler_section-properties-cxx.md "settings.schema.json#/definitions/compiler_section/properties/cxx")

#### cxx Type

`string`

### fc

Specify path to Fortran compiler wrapper. You may specify a compiler wrapper such as `gfortran` assuming its in $PATH or you can use `modules` property to resolve path to compiler wrapper.

`fc`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-compiler_section-properties-fc.md "settings.schema.json#/definitions/compiler_section/properties/fc")

#### fc Type

`string`

### module



`module`

*   is optional

*   Type: `object` ([Details](settings-definitions-module.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/compiler_section/properties/module")

#### module Type

`object` ([Details](settings-definitions-module.md))

## Definitions group unique\_string\_array

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/unique_string_array"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group disable

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/disable"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group module

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/module"}
```

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                                        |
| :------------------ | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| [purge](#purge)     | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module-properties-purge.md "settings.schema.json#/definitions/module/properties/purge")     |
| [load](#load)       | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/module/properties/load")           |
| [swap](#swap)       | `array`   | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module-properties-swap.md "settings.schema.json#/definitions/module/properties/swap")       |
| [restore](#restore) | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module-properties-restore.md "settings.schema.json#/definitions/module/properties/restore") |

### purge

Run `module purge` if purge is set

`purge`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module-properties-purge.md "settings.schema.json#/definitions/module/properties/purge")

#### purge Type

`boolean`

### load

Load one or more modules via `module load`

`load`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/module/properties/load")

#### load Type

`string[]`

#### load Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### swap

Swap modules using `module swap`. The swap property expects 2 unique modules.

`swap`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module-properties-swap.md "settings.schema.json#/definitions/module/properties/swap")

#### swap Type

`string[]`

#### swap Constraints

**maximum number of items**: the maximum number of items for this array is: `2`

**minimum number of items**: the minimum number of items for this array is: `2`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### restore

Load a collection name via `module restore`

`restore`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module-properties-restore.md "settings.schema.json#/definitions/module/properties/restore")

#### restore Type

`string`

## Definitions group script

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/script"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group maxpendtime

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/maxpendtime"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group account

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/account"}
```

| Property | Type | Required | Nullable | Defined by |
| :------- | :--- | :------- | :------- | :--------- |

## Definitions group local

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/local"}
```

| Property                         | Type          | Required | Nullable       | Defined by                                                                                                                                                  |
| :------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description-1)    | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-description.md "settings.schema.json#/definitions/local/properties/description")     |
| [shell](#shell)                  | `string`      | Required | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-shell.md "settings.schema.json#/definitions/local/properties/shell")                 |
| [before\_script](#before_script) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-before_script.md "settings.schema.json#/definitions/local/properties/before_script") |
| [max\_jobs](#max_jobs)           | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-max_jobs.md "settings.schema.json#/definitions/local/properties/max_jobs")           |
| [disable](#disable)              | `boolean`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-local-properties-disable.md "settings.schema.json#/definitions/local/properties/disable")             |
| [module](#module-1)              | `object`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/local/properties/module")                                |

### description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-local-properties-description.md "settings.schema.json#/definitions/local/properties/description")

#### description Type

`string`

### shell

Specify the shell launcher you want to use when running tests locally

`shell`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-local-properties-shell.md "settings.schema.json#/definitions/local/properties/shell")

#### shell Type

`string`

### before\_script



`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-local-properties-before_script.md "settings.schema.json#/definitions/local/properties/before_script")

#### before\_script Type

unknown

### max\_jobs

Maximum number of jobs that can be run at a given time for a particular executor

`max_jobs`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-local-properties-max_jobs.md "settings.schema.json#/definitions/local/properties/max_jobs")

#### max\_jobs Type

`integer`

#### max\_jobs Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### disable

Disable executor

`disable`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-local-properties-disable.md "settings.schema.json#/definitions/local/properties/disable")

#### disable Type

`boolean`

### module



`module`

*   is optional

*   Type: `object` ([Details](settings-definitions-module.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/local/properties/module")

#### module Type

`object` ([Details](settings-definitions-module.md))

## Definitions group slurm

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/slurm"}
```

| Property                           | Type          | Required | Nullable       | Defined by                                                                                                                                                  |
| :--------------------------------- | :------------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description-2)      | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-description.md "settings.schema.json#/definitions/slurm/properties/description")     |
| [launcher](#launcher)              | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-launcher.md "settings.schema.json#/definitions/slurm/properties/launcher")           |
| [options](#options)                | `array`       | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-options.md "settings.schema.json#/definitions/slurm/properties/options")             |
| [cluster](#cluster)                | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-cluster.md "settings.schema.json#/definitions/slurm/properties/cluster")             |
| [partition](#partition)            | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-partition.md "settings.schema.json#/definitions/slurm/properties/partition")         |
| [qos](#qos)                        | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-qos.md "settings.schema.json#/definitions/slurm/properties/qos")                     |
| [before\_script](#before_script-1) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-before_script.md "settings.schema.json#/definitions/slurm/properties/before_script") |
| [maxpendtime](#maxpendtime)        | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-maxpendtime.md "settings.schema.json#/definitions/slurm/properties/maxpendtime")     |
| [account](#account)                | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-account.md "settings.schema.json#/definitions/slurm/properties/account")             |
| [max\_jobs](#max_jobs-1)           | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-max_jobs.md "settings.schema.json#/definitions/slurm/properties/max_jobs")           |
| [disable](#disable-1)              | `boolean`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm-properties-disable.md "settings.schema.json#/definitions/slurm/properties/disable")             |
| [module](#module-2)                | `object`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/slurm/properties/module")                                |

### description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-description.md "settings.schema.json#/definitions/slurm/properties/description")

#### description Type

`string`

### launcher

Specify the slurm batch scheduler to use. This overrides the default `launcher` field. This must be `sbatch`.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-launcher.md "settings.schema.json#/definitions/slurm/properties/launcher")

#### launcher Type

`string`

#### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value      | Explanation |
| :--------- | :---------- |
| `"sbatch"` |             |

### options

Specify any other options for `sbatch` used by this executor for running all jobs.

`options`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-options.md "settings.schema.json#/definitions/slurm/properties/options")

#### options Type

`string[]`

### cluster

Specify the slurm cluster you want to use `-M <cluster>`

`cluster`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-cluster.md "settings.schema.json#/definitions/slurm/properties/cluster")

#### cluster Type

`string`

### partition

Specify the slurm partition you want to use `-p <partition>`

`partition`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-partition.md "settings.schema.json#/definitions/slurm/properties/partition")

#### partition Type

`string`

### qos

Specify the slurm qos you want to use `-q <qos>`

`qos`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-qos.md "settings.schema.json#/definitions/slurm/properties/qos")

#### qos Type

`string`

### before\_script

The `before_script` section can be used to specify commands before start of test. The script will be sourced in active shell.

`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-before_script.md "settings.schema.json#/definitions/slurm/properties/before_script")

#### before\_script Type

unknown

### maxpendtime

Cancel job if it is still pending in queue beyond maxpendtime

`maxpendtime`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-maxpendtime.md "settings.schema.json#/definitions/slurm/properties/maxpendtime")

#### maxpendtime Type

`integer`

#### maxpendtime Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### maxpendtime Default Value

The default value is:

```json
86400
```

### account

Specify Job Account for charging resources

`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-account.md "settings.schema.json#/definitions/slurm/properties/account")

#### account Type

`string`

### max\_jobs

Maximum number of jobs that can be run at a given time for a particular executor

`max_jobs`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-max_jobs.md "settings.schema.json#/definitions/slurm/properties/max_jobs")

#### max\_jobs Type

`integer`

#### max\_jobs Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### disable

Disable executor

`disable`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm-properties-disable.md "settings.schema.json#/definitions/slurm/properties/disable")

#### disable Type

`boolean`

### module



`module`

*   is optional

*   Type: `object` ([Details](settings-definitions-module.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/slurm/properties/module")

#### module Type

`object` ([Details](settings-definitions-module.md))

## Definitions group lsf

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/lsf"}
```

| Property                           | Type          | Required | Nullable       | Defined by                                                                                                                                              |
| :--------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description-3)      | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-description.md "settings.schema.json#/definitions/lsf/properties/description")     |
| [launcher](#launcher-1)            | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-launcher.md "settings.schema.json#/definitions/lsf/properties/launcher")           |
| [options](#options-1)              | `array`       | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-options.md "settings.schema.json#/definitions/lsf/properties/options")             |
| [queue](#queue)                    | `string`      | Required | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-queue.md "settings.schema.json#/definitions/lsf/properties/queue")                 |
| [before\_script](#before_script-2) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-before_script.md "settings.schema.json#/definitions/lsf/properties/before_script") |
| [maxpendtime](#maxpendtime-1)      | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-maxpendtime.md "settings.schema.json#/definitions/lsf/properties/maxpendtime")     |
| [account](#account-1)              | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-account.md "settings.schema.json#/definitions/lsf/properties/account")             |
| [max\_jobs](#max_jobs-2)           | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-max_jobs.md "settings.schema.json#/definitions/lsf/properties/max_jobs")           |
| [disable](#disable-2)              | `boolean`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-lsf-properties-disable.md "settings.schema.json#/definitions/lsf/properties/disable")             |
| [module](#module-3)                | `object`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/lsf/properties/module")                              |

### description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-description.md "settings.schema.json#/definitions/lsf/properties/description")

#### description Type

`string`

### launcher

Specify the lsf batch scheduler to use. This overrides the default `launcher` field. It must be `bsub`.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-launcher.md "settings.schema.json#/definitions/lsf/properties/launcher")

#### launcher Type

`string`

#### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"bsub"` |             |

### options

Specify any options for `bsub` for this executor when running all jobs associated to this executor

`options`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-options.md "settings.schema.json#/definitions/lsf/properties/options")

#### options Type

`string[]`

### queue

Specify the lsf queue you want to use `-q <queue>`

`queue`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-queue.md "settings.schema.json#/definitions/lsf/properties/queue")

#### queue Type

`string`

### before\_script

The `before_script` section can be used to specify commands before start of test. The script will be sourced in active shell.

`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-before_script.md "settings.schema.json#/definitions/lsf/properties/before_script")

#### before\_script Type

unknown

### maxpendtime

Cancel job if it is still pending in queue beyond maxpendtime

`maxpendtime`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-maxpendtime.md "settings.schema.json#/definitions/lsf/properties/maxpendtime")

#### maxpendtime Type

`integer`

#### maxpendtime Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### maxpendtime Default Value

The default value is:

```json
86400
```

### account

Specify Job Account for charging resources

`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-account.md "settings.schema.json#/definitions/lsf/properties/account")

#### account Type

`string`

### max\_jobs

Maximum number of jobs that can be run at a given time for a particular executor

`max_jobs`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-max_jobs.md "settings.schema.json#/definitions/lsf/properties/max_jobs")

#### max\_jobs Type

`integer`

#### max\_jobs Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### disable

Disable executor

`disable`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-lsf-properties-disable.md "settings.schema.json#/definitions/lsf/properties/disable")

#### disable Type

`boolean`

### module



`module`

*   is optional

*   Type: `object` ([Details](settings-definitions-module.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/lsf/properties/module")

#### module Type

`object` ([Details](settings-definitions-module.md))

## Definitions group cobalt

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/cobalt"}
```

| Property                           | Type          | Required | Nullable       | Defined by                                                                                                                                                    |
| :--------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description-4)      | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-description.md "settings.schema.json#/definitions/cobalt/properties/description")     |
| [launcher](#launcher-2)            | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-launcher.md "settings.schema.json#/definitions/cobalt/properties/launcher")           |
| [options](#options-2)              | `array`       | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-options.md "settings.schema.json#/definitions/cobalt/properties/options")             |
| [queue](#queue-1)                  | `string`      | Required | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-queue.md "settings.schema.json#/definitions/cobalt/properties/queue")                 |
| [before\_script](#before_script-3) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-before_script.md "settings.schema.json#/definitions/cobalt/properties/before_script") |
| [maxpendtime](#maxpendtime-2)      | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-maxpendtime.md "settings.schema.json#/definitions/cobalt/properties/maxpendtime")     |
| [account](#account-2)              | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-account.md "settings.schema.json#/definitions/cobalt/properties/account")             |
| [max\_jobs](#max_jobs-3)           | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-max_jobs.md "settings.schema.json#/definitions/cobalt/properties/max_jobs")           |
| [disable](#disable-3)              | `boolean`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt-properties-disable.md "settings.schema.json#/definitions/cobalt/properties/disable")             |
| [module](#module-4)                | `object`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/cobalt/properties/module")                                 |

### description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-description.md "settings.schema.json#/definitions/cobalt/properties/description")

#### description Type

`string`

### launcher

Specify the cobalt batch scheduler to use. This overrides the default `launcher` field. It must be `qsub`.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-launcher.md "settings.schema.json#/definitions/cobalt/properties/launcher")

#### launcher Type

`string`

#### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"qsub"` |             |

### options

Specify any options for `qsub` for this executor when running all jobs associated to this executor

`options`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-options.md "settings.schema.json#/definitions/cobalt/properties/options")

#### options Type

`string[]`

### queue

Specify the lsf queue you want to use `-q <queue>`

`queue`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-queue.md "settings.schema.json#/definitions/cobalt/properties/queue")

#### queue Type

`string`

### before\_script

The `before_script` section can be used to specify commands before start of test. The script will be sourced in active shell.

`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-before_script.md "settings.schema.json#/definitions/cobalt/properties/before_script")

#### before\_script Type

unknown

### maxpendtime

Cancel job if it is still pending in queue beyond maxpendtime

`maxpendtime`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-maxpendtime.md "settings.schema.json#/definitions/cobalt/properties/maxpendtime")

#### maxpendtime Type

`integer`

#### maxpendtime Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### maxpendtime Default Value

The default value is:

```json
86400
```

### account

Specify Job Account for charging resources

`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-account.md "settings.schema.json#/definitions/cobalt/properties/account")

#### account Type

`string`

### max\_jobs

Maximum number of jobs that can be run at a given time for a particular executor

`max_jobs`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-max_jobs.md "settings.schema.json#/definitions/cobalt/properties/max_jobs")

#### max\_jobs Type

`integer`

#### max\_jobs Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### disable

Disable executor

`disable`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt-properties-disable.md "settings.schema.json#/definitions/cobalt/properties/disable")

#### disable Type

`boolean`

### module



`module`

*   is optional

*   Type: `object` ([Details](settings-definitions-module.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/cobalt/properties/module")

#### module Type

`object` ([Details](settings-definitions-module.md))

## Definitions group pbs

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/pbs"}
```

| Property                           | Type          | Required | Nullable       | Defined by                                                                                                                                              |
| :--------------------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description-5)      | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-description.md "settings.schema.json#/definitions/pbs/properties/description")     |
| [launcher](#launcher-3)            | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-launcher.md "settings.schema.json#/definitions/pbs/properties/launcher")           |
| [options](#options-3)              | `array`       | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-options.md "settings.schema.json#/definitions/pbs/properties/options")             |
| [queue](#queue-2)                  | `string`      | Required | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-queue.md "settings.schema.json#/definitions/pbs/properties/queue")                 |
| [before\_script](#before_script-4) | Not specified | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-before_script.md "settings.schema.json#/definitions/pbs/properties/before_script") |
| [maxpendtime](#maxpendtime-3)      | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-maxpendtime.md "settings.schema.json#/definitions/pbs/properties/maxpendtime")     |
| [account](#account-3)              | `string`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-account.md "settings.schema.json#/definitions/pbs/properties/account")             |
| [max\_jobs](#max_jobs-4)           | `integer`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-max_jobs.md "settings.schema.json#/definitions/pbs/properties/max_jobs")           |
| [disable](#disable-4)              | `boolean`     | Optional | cannot be null | [buildtest configuration schema](settings-definitions-pbs-properties-disable.md "settings.schema.json#/definitions/pbs/properties/disable")             |
| [module](#module-5)                | `object`      | Optional | cannot be null | [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/pbs/properties/module")                              |

### description

description field for documenting your executor

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-description.md "settings.schema.json#/definitions/pbs/properties/description")

#### description Type

`string`

### launcher

Specify the pbs batch scheduler to use. This overrides the default `launcher` field. It must be `qsub`.

`launcher`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-launcher.md "settings.schema.json#/definitions/pbs/properties/launcher")

#### launcher Type

`string`

#### launcher Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value    | Explanation |
| :------- | :---------- |
| `"qsub"` |             |

### options

Specify any options for `qsub` for this executor when running all jobs associated to this executor

`options`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-options.md "settings.schema.json#/definitions/pbs/properties/options")

#### options Type

`string[]`

### queue

Specify the lsf queue you want to use `-q <queue>`

`queue`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-queue.md "settings.schema.json#/definitions/pbs/properties/queue")

#### queue Type

`string`

### before\_script

The `before_script` section can be used to specify commands before start of test. The script will be sourced in active shell.

`before_script`

*   is optional

*   Type: unknown

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-before_script.md "settings.schema.json#/definitions/pbs/properties/before_script")

#### before\_script Type

unknown

### maxpendtime

Cancel job if it is still pending in queue beyond maxpendtime

`maxpendtime`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-maxpendtime.md "settings.schema.json#/definitions/pbs/properties/maxpendtime")

#### maxpendtime Type

`integer`

#### maxpendtime Constraints

**minimum**: the value of this number must greater than or equal to: `1`

#### maxpendtime Default Value

The default value is:

```json
86400
```

### account

Specify Job Account for charging resources

`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-account.md "settings.schema.json#/definitions/pbs/properties/account")

#### account Type

`string`

### max\_jobs

Maximum number of jobs that can be run at a given time for a particular executor

`max_jobs`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-max_jobs.md "settings.schema.json#/definitions/pbs/properties/max_jobs")

#### max\_jobs Type

`integer`

#### max\_jobs Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### disable

Disable executor

`disable`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-pbs-properties-disable.md "settings.schema.json#/definitions/pbs/properties/disable")

#### disable Type

`boolean`

### module



`module`

*   is optional

*   Type: `object` ([Details](settings-definitions-module.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-module.md "settings.schema.json#/definitions/pbs/properties/module")

#### module Type

`object` ([Details](settings-definitions-module.md))

## Definitions group profiles

Reference this group by using

```json
{"$ref":"settings.schema.json#/definitions/profiles"}
```

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                          |
| :---------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [buildspecs](#buildspecs-1)               | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/buildspecs")                     |
| [exclude-buildspecs](#exclude-buildspecs) | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-buildspecs")             |
| [tags](#tags)                             | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/tags")                           |
| [exclude-tags](#exclude-tags)             | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-tags")                   |
| [executors](#executors-1)                 | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/executors")                      |
| [filter](#filter)                         | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-filter.md "settings.schema.json#/definitions/profiles/properties/filter")                 |
| [module](#module-6)                       | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-module.md "settings.schema.json#/definitions/profiles/properties/module")                 |
| [unload-modules](#unload-modules)         | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-unload-modules.md "settings.schema.json#/definitions/profiles/properties/unload-modules") |
| [module-purge](#module-purge)             | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-module-purge.md "settings.schema.json#/definitions/profiles/properties/module-purge")     |
| [rebuild](#rebuild)                       | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-rebuild.md "settings.schema.json#/definitions/profiles/properties/rebuild")               |
| [limit](#limit)                           | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-limit.md "settings.schema.json#/definitions/profiles/properties/limit")                   |
| [account](#account-4)                     | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-account.md "settings.schema.json#/definitions/profiles/properties/account")               |
| [maxpendtime](#maxpendtime-4)             | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-maxpendtime.md "settings.schema.json#/definitions/profiles/properties/maxpendtime")       |
| [pollinterval](#pollinterval)             | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-pollinterval.md "settings.schema.json#/definitions/profiles/properties/pollinterval")     |
| [procs](#procs)                           | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/procs")                |
| [nodes](#nodes)                           | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/nodes")                |
| [testdir](#testdir-1)                     | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-testdir.md "settings.schema.json#/definitions/profiles/properties/testdir")               |
| [timeout](#timeout-1)                     | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-timeout.md "settings.schema.json#/definitions/profiles/properties/timeout")               |
| [executor-type](#executor-type)           | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-executor-type.md "settings.schema.json#/definitions/profiles/properties/executor-type")   |

### buildspecs



`buildspecs`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/buildspecs")

#### buildspecs Type

`string[]`

#### buildspecs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### exclude-buildspecs



`exclude-buildspecs`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-buildspecs")

#### exclude-buildspecs Type

`string[]`

#### exclude-buildspecs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### tags



`tags`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/tags")

#### tags Type

`string[]`

#### tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### exclude-tags



`exclude-tags`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-tags")

#### exclude-tags Type

`string[]`

#### exclude-tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### executors



`executors`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/executors")

#### executors Type

`string[]`

#### executors Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### filter



`filter`

*   is optional

*   Type: `object` ([Details](settings-definitions-profiles-properties-filter.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-filter.md "settings.schema.json#/definitions/profiles/properties/filter")

#### filter Type

`object` ([Details](settings-definitions-profiles-properties-filter.md))

### module



`module`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-module.md "settings.schema.json#/definitions/profiles/properties/module")

#### module Type

`string`

### unload-modules



`unload-modules`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-unload-modules.md "settings.schema.json#/definitions/profiles/properties/unload-modules")

#### unload-modules Type

`string`

### module-purge



`module-purge`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-module-purge.md "settings.schema.json#/definitions/profiles/properties/module-purge")

#### module-purge Type

`boolean`

### rebuild



`rebuild`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-rebuild.md "settings.schema.json#/definitions/profiles/properties/rebuild")

#### rebuild Type

`integer`

#### rebuild Constraints

**maximum**: the value of this number must smaller than or equal to: `50`

**minimum**: the value of this number must greater than or equal to: `1`

### limit



`limit`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-limit.md "settings.schema.json#/definitions/profiles/properties/limit")

#### limit Type

`integer`

#### limit Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### account



`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-account.md "settings.schema.json#/definitions/profiles/properties/account")

#### account Type

`string`

### maxpendtime



`maxpendtime`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-maxpendtime.md "settings.schema.json#/definitions/profiles/properties/maxpendtime")

#### maxpendtime Type

`integer`

#### maxpendtime Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### pollinterval



`pollinterval`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-pollinterval.md "settings.schema.json#/definitions/profiles/properties/pollinterval")

#### pollinterval Type

`integer`

#### pollinterval Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### procs



`procs`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/procs")

#### procs Type

`integer[]`

#### procs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### nodes



`nodes`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/nodes")

#### nodes Type

`integer[]`

#### nodes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### testdir



`testdir`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-testdir.md "settings.schema.json#/definitions/profiles/properties/testdir")

#### testdir Type

`string`

### timeout



`timeout`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-timeout.md "settings.schema.json#/definitions/profiles/properties/timeout")

#### timeout Type

`integer`

#### timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### executor-type

Specify the `executor-type` field used by `--executor-type` option which determines if test will run by local or batch executor

`executor-type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-executor-type.md "settings.schema.json#/definitions/profiles/properties/executor-type")

#### executor-type Type

`string`

#### executor-type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"local"` |             |
| `"batch"` |             |
