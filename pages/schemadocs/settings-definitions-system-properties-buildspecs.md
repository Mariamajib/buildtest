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

| Property                      | Type      | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :---------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [rebuild](#rebuild)           | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-rebuild.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/rebuild")           |
| [count](#count)               | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-count.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/count")               |
| [formatfields](#formatfields) | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-formatfields.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/formatfields") |
| [terse](#terse)               | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-terse.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/terse")               |
| [pager](#pager)               | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-pager.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/pager")               |

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

Determine number of records to display when running `buildtest buildspec find`

`count`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-count.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/count")

### count Type

`integer`

### count Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## formatfields

Determine the format fields to display when running `buildtest buildspec find`

`formatfields`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-formatfields.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/formatfields")

### formatfields Type

`string`

## terse

A boolean to determine whether to enable terse mode when viewing buildspec cache

`terse`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-terse.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/terse")

### terse Type

`boolean`

## pager

A boolean to determine whether to enable paging when viewing buildspec cache

`pager`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-buildspecs-properties-pager.md "settings.schema.json#/definitions/system/properties/buildspecs/properties/pager")

### pager Type

`boolean`
