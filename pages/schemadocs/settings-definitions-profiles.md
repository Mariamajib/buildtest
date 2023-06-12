# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/profiles
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## profiles Type

`object` ([Details](settings-definitions-profiles.md))

# profiles Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                          |
| :---------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [buildspecs](#buildspecs)                 | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/buildspecs")                     |
| [exclude-buildspecs](#exclude-buildspecs) | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-buildspecs")             |
| [tags](#tags)                             | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/tags")                           |
| [exclude-tags](#exclude-tags)             | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-tags")                   |
| [executors](#executors)                   | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/executors")                      |
| [filter](#filter)                         | `object`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-filter.md "settings.schema.json#/definitions/profiles/properties/filter")                 |
| [module](#module)                         | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-module.md "settings.schema.json#/definitions/profiles/properties/module")                 |
| [unload-modules](#unload-modules)         | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-unload-modules.md "settings.schema.json#/definitions/profiles/properties/unload-modules") |
| [module-purge](#module-purge)             | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-module-purge.md "settings.schema.json#/definitions/profiles/properties/module-purge")     |
| [rebuild](#rebuild)                       | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-rebuild.md "settings.schema.json#/definitions/profiles/properties/rebuild")               |
| [limit](#limit)                           | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-limit.md "settings.schema.json#/definitions/profiles/properties/limit")                   |
| [account](#account)                       | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-account.md "settings.schema.json#/definitions/profiles/properties/account")               |
| [maxpendtime](#maxpendtime)               | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-maxpendtime.md "settings.schema.json#/definitions/profiles/properties/maxpendtime")       |
| [pollinterval](#pollinterval)             | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-pollinterval.md "settings.schema.json#/definitions/profiles/properties/pollinterval")     |
| [procs](#procs)                           | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/procs")                |
| [nodes](#nodes)                           | `array`   | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/nodes")                |
| [testdir](#testdir)                       | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-testdir.md "settings.schema.json#/definitions/profiles/properties/testdir")               |
| [timeout](#timeout)                       | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-timeout.md "settings.schema.json#/definitions/profiles/properties/timeout")               |
| [executor-type](#executor-type)           | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-executor-type.md "settings.schema.json#/definitions/profiles/properties/executor-type")   |

## buildspecs



`buildspecs`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/buildspecs")

### buildspecs Type

`string[]`

### buildspecs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## exclude-buildspecs



`exclude-buildspecs`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-buildspecs")

### exclude-buildspecs Type

`string[]`

### exclude-buildspecs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## tags



`tags`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/tags")

### tags Type

`string[]`

### tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## exclude-tags



`exclude-tags`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/exclude-tags")

### exclude-tags Type

`string[]`

### exclude-tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## executors



`executors`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/executors")

### executors Type

`string[]`

### executors Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## filter



`filter`

*   is optional

*   Type: `object` ([Details](settings-definitions-profiles-properties-filter.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-filter.md "settings.schema.json#/definitions/profiles/properties/filter")

### filter Type

`object` ([Details](settings-definitions-profiles-properties-filter.md))

## module



`module`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-module.md "settings.schema.json#/definitions/profiles/properties/module")

### module Type

`string`

## unload-modules



`unload-modules`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-unload-modules.md "settings.schema.json#/definitions/profiles/properties/unload-modules")

### unload-modules Type

`string`

## module-purge



`module-purge`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-module-purge.md "settings.schema.json#/definitions/profiles/properties/module-purge")

### module-purge Type

`boolean`

## rebuild



`rebuild`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-rebuild.md "settings.schema.json#/definitions/profiles/properties/rebuild")

### rebuild Type

`integer`

### rebuild Constraints

**maximum**: the value of this number must smaller than or equal to: `50`

**minimum**: the value of this number must greater than or equal to: `1`

## limit



`limit`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-limit.md "settings.schema.json#/definitions/profiles/properties/limit")

### limit Type

`integer`

### limit Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## account



`account`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-account.md "settings.schema.json#/definitions/profiles/properties/account")

### account Type

`string`

## maxpendtime



`maxpendtime`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-maxpendtime.md "settings.schema.json#/definitions/profiles/properties/maxpendtime")

### maxpendtime Type

`integer`

### maxpendtime Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## pollinterval



`pollinterval`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-pollinterval.md "settings.schema.json#/definitions/profiles/properties/pollinterval")

### pollinterval Type

`integer`

### pollinterval Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## procs



`procs`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/procs")

### procs Type

`integer[]`

### procs Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## nodes



`nodes`

*   is optional

*   Type: `integer[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_positive_integers.md "settings.schema.json#/definitions/profiles/properties/nodes")

### nodes Type

`integer[]`

### nodes Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## testdir



`testdir`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-testdir.md "settings.schema.json#/definitions/profiles/properties/testdir")

### testdir Type

`string`

## timeout



`timeout`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-timeout.md "settings.schema.json#/definitions/profiles/properties/timeout")

### timeout Type

`integer`

### timeout Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## executor-type

Specify the `executor-type` field used by `--executor-type` option which determines if test will run by local or batch executor

`executor-type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-executor-type.md "settings.schema.json#/definitions/profiles/properties/executor-type")

### executor-type Type

`string`

### executor-type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"local"` |             |
| `"batch"` |             |
