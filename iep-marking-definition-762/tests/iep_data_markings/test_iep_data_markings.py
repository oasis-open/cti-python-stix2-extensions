import pytest
import stix2.exceptions
from stix2 import MarkingDefinition, Indicator
from iep_data_markings.iep_data_markings import IEP_DATA_MARKING_EXTENSION_ID, IEPDataMarking

EXPECTED_IEP_DATA_MARKING = """{
    "type": "marking-definition",
    "spec_version": "2.1",
    "id": "marking-definition--da05d443-ad8d-46fc-abf5-31d3d00290f1",
    "created": "2024-01-10T14:52:41.853121Z",
    "name": "IEP data marking",
    "extensions": {
        "extension-definition--762e2e97-ee51-43e5-a9ea-165fbb862c4a": {
            "extension_type": "property-extension",
            "encrypt_in_transit": "may",
            "permitted_actions": "externally-visible-direct-actions",
            "affected_party_notifications": "may",
            "tlp": "amber",
            "provider_attribution": "must-not",
            "unmodified_resale": "must-not",
            "iep_id": "0224bfdf-ea3a-49c3-96f6-66d908bb1845",
            "iep_version": 2.0,
            "description": "This is a TLP-AMBER Information Exchange Policy",
            "start_date": "2022-10-01T00:00:00Z"
        }
    }
}"""

INDICATOR_WITH_DATA_MARKING = """{
    "type": "indicator",
    "spec_version": "2.1",
    "id": "indicator--1f1abcee-3b7a-468c-a7d4-635148ce2946",
    "created": "2024-01-10T15:52:58.032211Z",
    "modified": "2024-01-10T15:52:58.032211Z",
    "pattern": "[file:hashes.md5 = 'd41d8cd98f00b204e9800998ecf8427e']",
    "pattern_type": "stix",
    "pattern_version": "2.1",
    "valid_from": "2024-01-10T15:52:58.032211Z",
    "object_marking_refs": [
        "marking-definition--da05d443-ad8d-46fc-abf5-31d3d00290f1"
    ]
}"""


def test_is_iep_data_marking():
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

    assert isinstance(iep_data_marking, MarkingDefinition)
    assert isinstance(
        iep_data_marking.extensions[IEP_DATA_MARKING_EXTENSION_ID],
        IEPDataMarking
    )
    assert iep_data_marking.serialize(pretty=True) == EXPECTED_IEP_DATA_MARKING
    # assert iep_data_marking.serialize(pretty=True) == EXPECTED_IEP_DATA_MARKING,
    # '{0} != {1}'.format(iep_data_marking.serialize(pretty=True), EXPECTED_IEP_DATA_MARKING)


def test_invalid_values():
    with pytest.raises(stix2.exceptions.InvalidValueError) as excinfo:
        MarkingDefinition(
            name='IEP data marking',
            extensions={
                IEP_DATA_MARKING_EXTENSION_ID: IEPDataMarking(
                    extension_type='property-extension',
                    encrypt_in_transit='yes', # Should be 'may'
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

    assert excinfo.value.prop_name == "encrypt_in_transit"
    assert excinfo.value.reason == "value 'yes' is not valid for this enumeration."
    assert str(excinfo.value) == "Invalid value for IEPDataMarking 'encrypt_in_transit': value 'yes' is not valid for this enumeration."


def test_missing_required_fields():
    with pytest.raises(stix2.exceptions.MissingPropertiesError) as excinfo:
        MarkingDefinition(
            name='IEP data marking',
            extensions={
                IEP_DATA_MARKING_EXTENSION_ID: IEPDataMarking()
            }
        )

    assert str(excinfo.value) == "No values for required properties for IEPDataMarking: (affected_party_notifications, description, encrypt_in_transit, iep_id, iep_version, permitted_actions, provider_attribution, start_date, tlp, unmodified_resale)."


def test_wrong_type_raises_exception():
    with pytest.raises(stix2.exceptions.InvalidValueError) as excinfo:
        MarkingDefinition(
            name='IEP data marking',
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
                    iep_version='2.0.a',
                    description='This is a TLP-AMBER Information Exchange Policy',
                    start_date='2022-10-01T00:00:00.000Z'
                )
            }
        )

    assert str(excinfo.value) == "Invalid value for IEPDataMarking 'iep_version': must be a float."


def test_apply_iep_data_marking():
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

    assert isinstance(indicator, Indicator)
    assert indicator.serialize(pretty=True) == INDICATOR_WITH_DATA_MARKING
