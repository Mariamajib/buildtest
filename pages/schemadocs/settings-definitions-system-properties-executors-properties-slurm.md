# Untitled object in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/system/properties/executors/properties/slurm
```

The `slurm` section is used for declaring Slurm executors for running jobs using Slurm scheduler

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                   |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json\*](../out/settings.schema.json "open original schema") |

## slurm Type

`object` ([Details](settings-definitions-system-properties-executors-properties-slurm.md))

# slurm Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                            |
| :-------------------- | :------- | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional Properties | `object` | Optional | cannot be null | [buildtest configuration schema](settings-definitions-slurm.md "settings.schema.json#/definitions/system/properties/executors/properties/slurm/additionalProperties") |

## Additional Properties

Additional properties are allowed, as long as they follow this schema:

An instance object of slurm executor

*   is optional

*   Type: `object` ([Details](settings-definitions-slurm.md))

*   cannot be null

*   defined in: [buildtest configuration schema](settings-definitions-slurm.md "settings.schema.json#/definitions/system/properties/executors/properties/slurm/additionalProperties")

### additionalProperties Type

`object` ([Details](settings-definitions-slurm.md))
