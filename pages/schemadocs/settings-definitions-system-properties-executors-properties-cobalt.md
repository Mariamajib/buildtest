# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/executors/properties/cobalt
```

The `cobalt` section is used for declaring Cobalt executors for running jobs using Cobalt scheduler

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## cobalt Type

`object` ([Details](settings-definitions-system-properties-executors-properties-cobalt.md))

# cobalt Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                              |
| :-------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-cobalt.md "settings.schema.json#/definitions/system/properties/executors/properties/cobalt/additionalProperties") |

## Additional Properties

Additional properties are allowed, as long as they follow this schema:

An instance object of cobalt executor

*   is optional

*   Type: `object` ([Details](settings-definitions-cobalt.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-cobalt.md "settings.schema.json#/definitions/system/properties/executors/properties/cobalt/additionalProperties")

### additionalProperties Type

`object` ([Details](settings-definitions-cobalt.md))
