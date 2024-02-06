# IEP Marking Definition Version 2.0

This is an implementation of the
[IEP Marking Definition Version 2.0](https://github.com/oasis-open/cti-stix-common-objects/blob/main/extension-definition-specifications/iep-marking-definition-762/STIX-2.1-IEP2.0-marking-definition.adoc).
It includes the data marking extension itself, and a set of tests.

## Example usage
Creating a marking definition and applying it to an indicator:

```
iep_data_marking = MarkingDefinition(
        id='marking-definition--da05d443-ad8d-46fc-abf5-31d3d00290f1',
        name='IEP data marking',
        created="2024-01-10T14:52:41.853121Z",
        extensions={
            IEP_DATA_MARKING_EXTENSION_ID: IEPDataMarking(
                extension_type='property-extension',
                encrypt_in_transit='may',
                permitted_actions='externally-visible-direct-actions',
                affected_party_notifications='may',
                tlp='amber',
                provider_attribution='must-not',
                unmodified_resale='must-not',
                iep_id='0224bfdf-ea3a-49c3-96f6-66d908bb1845',
                iep_version='2.0',
                description='This is a TLP-AMBER Information Exchange Policy',
                start_date='2022-10-01T00:00:00.000Z'
            )
        }
    )

    indicator = Indicator(
        id="indicator--1f1abcee-3b7a-468c-a7d4-635148ce2946",
        pattern_type="stix",
        pattern="[file:hashes.md5 = 'd41d8cd98f00b204e9800998ecf8427e']",
        created="2024-01-10T15:52:58.032211Z",
        modified="2024-01-10T15:52:58.032211Z",
        valid_from="2024-01-10T15:52:58.032211Z",
        object_marking_refs=iep_data_marking
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