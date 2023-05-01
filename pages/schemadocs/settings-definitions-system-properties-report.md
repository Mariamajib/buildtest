# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/report
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## report Type

`object` ([Details](settings-definitions-system-properties-report.md))

# report Properties

| Property          | Type      | Required | Nullable       | Defined by                                                                                                                                                                          |
| :---------------- | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [terse](#terse)   | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-report-properties-terse.md "settings.schema.json#/definitions/system/properties/report/properties/terse")   |
| [format](#format) | `string`  | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-report-properties-format.md "settings.schema.json#/definitions/system/properties/report/properties/format") |
| [count](#count)   | `integer` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-report-properties-count.md "settings.schema.json#/definitions/system/properties/report/properties/count")   |
| [latest](#latest) | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-report-properties-latest.md "settings.schema.json#/definitions/system/properties/report/properties/latest") |
| [oldest](#oldest) | `boolean` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-system-properties-report-properties-oldest.md "settings.schema.json#/definitions/system/properties/report/properties/oldest") |

## terse

A boolean to determine whether to enable terse mode

`terse`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report-properties-terse.md "settings.schema.json#/definitions/system/properties/report/properties/terse")

### terse Type

`boolean`

## format

Determine the format fields to display when viewing table results

`format`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report-properties-format.md "settings.schema.json#/definitions/system/properties/report/properties/format")

### format Type

`string`

## count

Determine number of records to display in a table

`count`

*   is optional

*   Type: `integer`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report-properties-count.md "settings.schema.json#/definitions/system/properties/report/properties/count")

### count Type

`integer`

### count Constraints

**minimum**: the value of this number must greater than or equal to: `1`

## latest

A boolean to determine whether to show latest test run

`latest`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report-properties-latest.md "settings.schema.json#/definitions/system/properties/report/properties/latest")

### latest Type

`boolean`

## oldest

A boolean to determine whether to show oldest test run

`oldest`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-system-properties-report-properties-oldest.md "settings.schema.json#/definitions/system/properties/report/properties/oldest")

### oldest Type

`boolean`
