# Untitled object in spack schema version 1.0 Schema

```txt
spack-v1.0.schema.json#/properties/spack
```

Entry point to spack configuration

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [spack-v1.0.schema.json*](../out/spack-v1.0.schema.json "open original schema") |

## spack Type

`object` ([Details](spack-v1-properties-spack.md))

# spack Properties

| Property                        | Type      | Required | Nullable       | Defined by                                                                                                                                            |
| :------------------------------ | :-------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [root](#root)                   | `string`  | Required | cannot be null | [spack schema version 1.0](spack-v1-properties-spack-properties-root.md "spack-v1.0.schema.json#/properties/spack/properties/root")                   |
| [compiler_find](#compiler_find) | `boolean` | Optional | cannot be null | [spack schema version 1.0](spack-v1-properties-spack-properties-compiler_find.md "spack-v1.0.schema.json#/properties/spack/properties/compiler_find") |
| [mirror](#mirror)               | `object`  | Optional | cannot be null | [spack schema version 1.0](definitions-definitions-env.md "spack-v1.0.schema.json#/properties/spack/properties/mirror")                               |
| [env](#env)                     | `object`  | Optional | cannot be null | [spack schema version 1.0](spack-v1-definitions-env.md "spack-v1.0.schema.json#/properties/spack/properties/env")                                     |
| [install](#install)             | `object`  | Optional | cannot be null | [spack schema version 1.0](spack-v1-definitions-install.md "spack-v1.0.schema.json#/properties/spack/properties/install")                             |
| [verify_spack](#verify_spack)   | `boolean` | Optional | cannot be null | [spack schema version 1.0](spack-v1-properties-spack-properties-verify_spack.md "spack-v1.0.schema.json#/properties/spack/properties/verify_spack")   |
| [test](#test)                   | `object`  | Optional | cannot be null | [spack schema version 1.0](spack-v1-definitions-test.md "spack-v1.0.schema.json#/properties/spack/properties/test")                                   |

## root



`root`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [spack schema version 1.0](spack-v1-properties-spack-properties-root.md "spack-v1.0.schema.json#/properties/spack/properties/root")

### root Type

`string`

## compiler_find

Run `spack compiler find` if set to `True`. This is run right after sourcing spack startup script.

`compiler_find`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [spack schema version 1.0](spack-v1-properties-spack-properties-compiler_find.md "spack-v1.0.schema.json#/properties/spack/properties/compiler_find")

### compiler_find Type

`boolean`

## mirror

One or more key value pairs for an environment (key=value)

`mirror`

*   is optional

*   Type: `object` ([Details](definitions-definitions-env.md))

*   cannot be null

*   defined in: [spack schema version 1.0](definitions-definitions-env.md "spack-v1.0.schema.json#/properties/spack/properties/mirror")

### mirror Type

`object` ([Details](definitions-definitions-env.md))

### mirror Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

## env

Used for managing spack environment using `spack env` command.

`env`

*   is optional

*   Type: `object` ([Details](spack-v1-definitions-env.md))

*   cannot be null

*   defined in: [spack schema version 1.0](spack-v1-definitions-env.md "spack-v1.0.schema.json#/properties/spack/properties/env")

### env Type

`object` ([Details](spack-v1-definitions-env.md))

## install

Install spack packages using `spack install` command

`install`

*   is optional

*   Type: `object` ([Details](spack-v1-definitions-install.md))

*   cannot be null

*   defined in: [spack schema version 1.0](spack-v1-definitions-install.md "spack-v1.0.schema.json#/properties/spack/properties/install")

### install Type

`object` ([Details](spack-v1-definitions-install.md))

## verify_spack

This boolean will determine if we need to check for file existence where spack is cloned via `root` property and file **$SPACK_ROOT/share/spack/setup-env.sh** exists. These checks can be disabled by setting this to `False` which can be useful if you dont want buildtest to raise exception during test generation process and test is skipped.

`verify_spack`

*   is optional

*   Type: `boolean`

*   cannot be null

*   defined in: [spack schema version 1.0](spack-v1-properties-spack-properties-verify_spack.md "spack-v1.0.schema.json#/properties/spack/properties/verify_spack")

### verify_spack Type

`boolean`

### verify_spack Default Value

The default value is:

```json
true
```

## test

Entry point to `spack test`

`test`

*   is optional

*   Type: `object` ([Details](spack-v1-definitions-test.md))

*   cannot be null

*   defined in: [spack schema version 1.0](spack-v1-definitions-test.md "spack-v1.0.schema.json#/properties/spack/properties/test")

### test Type

`object` ([Details](spack-v1-definitions-test.md))