import pytest
import stix2
import stix2.exceptions
import stix2.properties

from stix2.properties import (OpenVocabProperty,
                              StringProperty)
from stix2.exceptions import MissingPropertiesError

from observed_string.observed_string import ObservedString, OBSERVED_STRING_EXTENSION_ID

def test_parse_all_props():
    obs_dict = {
        "type": "observed-string",
        "spec_version": "2.1",
        "id": "observed-string--c7609355-8be6-5af7-a072-039a6c853a1f",
        "value": "0fC0Gpnccrxc1YDEVkwJLjCEImtfgo5plWBMwqxulsbwVC6la4",
        "purpose": "unknown",
        "extensions": {
            "extension-definition--8b1aa84c-5532-4c69-a8e7-b6170facfd3d": {
            "extension_type": "new-sco"
            }
        }
    }

    obs = stix2.parse(obs_dict)

    assert isinstance(obs, ObservedString)


def test_observed_string_no_purpose():
    with pytest.raises(MissingPropertiesError):
        ObservedString(
            value="12345",
            extensions={
                "extension-definition--8b1aa84c-5532-4c69-a8e7-b6170facfd3d": {
                "extension_type": "new-sco"
                }
            }
        ) 

def test_observed_string_no_value():
    with pytest.raises(MissingPropertiesError):
        ObservedString(
            purpose="unknown",
            extensions={
                "extension-definition--8b1aa84c-5532-4c69-a8e7-b6170facfd3d": {
                "extension_type": "new-sco"
                }
            }
        ) 
