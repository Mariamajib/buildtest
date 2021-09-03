# Untitled integer in buildtest configuration schema Schema

```txt
settings.schema.json#/definitions/pbs/properties/max_jobs
```

Maximum number of jobs that can be run at a given time for a particular executor

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [settings.schema.json*](../out/settings.schema.json "open original schema") |

## max_jobs Type

`integer`

## max_jobs Constraints

**minimum**: the value of this number must greater than or equal to: `1`