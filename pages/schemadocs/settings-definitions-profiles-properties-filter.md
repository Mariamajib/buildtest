# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/profiles/properties/filter
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## filter Type

`object` ([Details](settings-definitions-profiles-properties-filter.md))

# filter Properties

| Property                    | Type    | Required | Nullable       | Defined by                                                                                                                                                                          |
| :-------------------------- | :------ | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)               | `array` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles-properties-filter-properties-type.md "settings.schema.json#/definitions/profiles/properties/filter/properties/type") |
| [tags](#tags)               | `array` | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/filter/properties/tags")                         |
| [maintainers](#maintainers) | `array` | Optional | cannot be null | [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/filter/properties/maintainers")                  |

## type

Specify the `type` field to determine which schema to use during filtering

`type`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles-properties-filter-properties-type.md "settings.schema.json#/definitions/profiles/properties/filter/properties/type")

### type Type

`string[]`

### type Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## tags

Filter by tags

`tags`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/filter/properties/tags")

### tags Type

`string[]`

### tags Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## maintainers

Filter by maintainers

`maintainers`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [buildtest configuration schema](definitions-definitions-list_of_strings.md "settings.schema.json#/definitions/profiles/properties/filter/properties/maintainers")

### maintainers Type

`string[]`

### maintainers Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.
