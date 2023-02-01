# Untitled object in JSON Schema Definitions File.  Schema

```txt
definitions.schema.json#/definitions/status/properties/assert_ne/items
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                         |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [definitions.schema.json\*](../out/definitions.schema.json "open original schema") |

## items Type

`object` ([Details](definitions-definitions-status-properties-assert_ne-items.md))

# items Properties

| Property      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :------------ | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name) | `string` | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne-items-properties-name.md "definitions.schema.json#/definitions/status/properties/assert_ne/items/properties/name") |
| [ref](#ref)   | Merged   | Required | cannot be null | [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne-items-properties-ref.md "definitions.schema.json#/definitions/status/properties/assert_ne/items/properties/ref")   |

## name

Name of metric to use for comparison

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne-items-properties-name.md "definitions.schema.json#/definitions/status/properties/assert_ne/items/properties/name")

### name Type

`string`

## ref

Specify reference value (str, int, float) for comparison

`ref`

*   is required

*   Type: merged type ([Details](definitions-definitions-status-properties-assert_ne-items-properties-ref.md))

*   cannot be null

*   defined in: [JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne-items-properties-ref.md "definitions.schema.json#/definitions/status/properties/assert_ne/items/properties/ref")

### ref Type

merged type ([Details](definitions-definitions-status-properties-assert_ne-items-properties-ref.md))

one (and only one) of

*   [Untitled number in JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne-items-properties-ref-oneof-0.md "check type definition")

*   [Untitled string in JSON Schema Definitions File. ](definitions-definitions-status-properties-assert_ne-items-properties-ref-oneof-1.md "check type definition")
