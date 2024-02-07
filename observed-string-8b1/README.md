# Observed String Extension Version 1.0

This is an implementation of the
[Observed String Extension Version 1.0](https://github.com/oasis-open/cti-stix-common-objects/blob/main/extension-definition-specifications/observed-string-8b1/Observed%20String.adoc).
It includes the data marking extension itself, and a set of tests.

## Example usage
Creating a marking definition and applying it to an indicator:

```
obs_string = ObservedString(
    "id": "observed-string--d28133c6-610f-54e7-9cb4-4add1a2929f7",
    "value": "This is the decoded message",
    "purpose": "decoded",
    "extensions": {
        "extension-definition--8b1aa84c-5532-4c69-a8e7-b6170facfd3d": {
            "extension_type": "new-sco"
        }
    }
)

```

## Running the tests
Tests can be run with Tox by executing the `tox` command.

The PYTHONPATH needs to be set in env. This enables the tests to find the data marking module. 

On a Mac:
`export PYTHONPATH=$(pwd)/src`
or on Windows:
`set PYTHONPATH=$(cd)/src`

Run the tests:
`tox -c tox.ini`