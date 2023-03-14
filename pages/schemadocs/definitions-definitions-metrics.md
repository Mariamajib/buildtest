# Untitled object in spack schema version Schema

```txt
spack.schema.json#/properties/metrics
```

This field is used for defining one or more metrics that is recorded for each test. A metric must have a unique name which is recorded in the test metadata.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                             |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [spack.schema.json\*](../out/spack.schema.json "open original schema") |

## metrics Type

`object` ([Details](definitions-definitions-metrics.md))

# metrics Properties

| Property              | Type   | Required | Nullable       | Defined by                                                                                                                  |
| :-------------------- | :----- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | Merged | Optional | cannot be null | [compiler schema](definitions-definitions-metrics_field.md "compiler.schema.json#/properties/metrics/additionalProperties") |

## Additional Properties

Additional properties are allowed, as long as they follow this schema:



*   is optional

*   Type: `object` ([Details](definitions-definitions-metrics_field.md))

*   cannot be null

*   defined in: [compiler schema](definitions-definitions-metrics_field.md "compiler.schema.json#/properties/metrics/additionalProperties")

### additionalProperties Type

`object` ([Details](definitions-definitions-metrics_field.md))

one (and only one) of

*   [Untitled undefined type in JSON Schema Definitions File. ](definitions-definitions-metrics_field-oneof-0.md "check type definition")

*   [Untitled undefined type in JSON Schema Definitions File. ](definitions-definitions-metrics_field-oneof-1.md "check type definition")
