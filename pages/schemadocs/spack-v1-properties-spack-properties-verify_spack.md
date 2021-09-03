# Untitled boolean in spack schema version 1.0 Schema

```txt
spack-v1.0.schema.json#/properties/spack/properties/verify_spack
```

This boolean will determine if we need to check for file existence where spack is cloned via `root` property and file **$SPACK_ROOT/share/spack/setup-env.sh** exists. These checks can be disabled by setting this to `False` which can be useful if you dont want buildtest to raise exception during test generation process and test is skipped.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [spack-v1.0.schema.json*](../out/spack-v1.0.schema.json "open original schema") |

## verify_spack Type

`boolean`

## verify_spack Default Value

The default value is:

```json
true
```