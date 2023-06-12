# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/profiles
```

The profiles section is used for declaring one or more profiles that can be used to run `buildtest build` that are captured as command options

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## profiles Type

`object` ([Details](settings-definitions-system-properties-profiles.md))

# profiles Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                             |
| :-------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-profiles.md "settings.schema.json#/definitions/system/properties/profiles/additionalProperties") |

## Additional Properties

Additional properties are allowed, as long as they follow this schema:



*   is optional

*   Type: `object` ([Details](settings-definitions-profiles.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-profiles.md "settings.schema.json#/definitions/system/properties/profiles/additionalProperties")

### additionalProperties Type

`object` ([Details](settings-definitions-profiles.md))
