# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/buildspecs
```

Specify configuration for `buildtest buildspec` command

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## buildspecs Type

`object` ([Details](settings-definitions-system-properties-buildspecs.md))

# buildspecs Properties

| Property            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                    |
| :------------------ | :-------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [rebuild](#rebuild) | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-rebuild.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/rebuild") |
| [count](#count)     | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-count.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/count")     |
| [format](#format)   | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-format.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/format")   |
| [terse](#terse)     | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-terse.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/terse")     |
| [root](#root)       | `array`   | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-root.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/root")       |

## rebuild

A boolean to determine whether to rebuild buildspec cache

`rebuild`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-rebuild.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/rebuild")

### rebuild Type

`boolean`

## count

Determine number of records to display in a table

`count`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-count.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/count")

### count Type

`integer`

### count Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## format

Determine the format fields to display when viewing table results

`format`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-format.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/format")

### format Type

`string`

## terse

A boolean to determine whether to enable terse mode

`terse`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-terse.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/terse")

### terse Type

`boolean`

## root

Specify a list of directory paths to search buildspecs. This field can be used with `buildtest buildspec find` to rebuild buildspec cache or build tests using `buildtest build` command

`root`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-root.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/root")

### root Type

`string[]`
