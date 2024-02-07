import pytest
import stix2
from pap.pap import (PAPMarkingDefinition, PAPMarkingDefinitionError, 
                PAP_MARKING_EXTENSION_ID, PAPExtension)
import os

def test_bad_pap_amber():
    with pytest.raises(PAPMarkingDefinitionError):
        PAPMarkingDefinition(
            id='marking-definition--70f8932b-e51e-4458-b265-a2e8be9a80ab', #this is not correct 
            created="2022-10-02T00:00:00.000Z",
            name="PAP:AMBER",
            extensions={
                PAP_MARKING_EXTENSION_ID:{
                    'pap':'amber'
                }
            }
        )

def test_bad_pap_green():
    with pytest.raises(PAPMarkingDefinitionError):
        PAPMarkingDefinition(
            id='marking-definition--c43594d1-4b11-4c59-93ab-1c9b14d53ce9',
            created="2023-10-09T00:00:00.000Z", #incorrect
            name="PAP:GREEN",
            extensions={
                PAP_MARKING_EXTENSION_ID:{
                    'pap':'green'
                }
            }
        )

def test_bad_pap_red():
    with pytest.raises(stix2.exceptions.InvalidValueError):
        PAPMarkingDefinition(
            id='marking-definition--740d36e5-7714-4c30-961a-3ae632ceee0e',
            created="2022-10-06T00:00:00.000Z",
            name="PAP:PINK",
            extensions={
                PAP_MARKING_EXTENSION_ID:{
                    'pap':'red'
                }
            }
        )

def test_bad_pap_white():
    with pytest.raises(stix2.exceptions.InvalidValueError):
        PAPMarkingDefinition(
            id='marking-definition--a3bea94c-b469-41dc-9cfe-d6e7daba7730',
            created="2022-10-01T00:00:00.000Z",
            name="PAP:WHITE",
            extensions={
                PAP_MARKING_EXTENSION_ID:{
                    'pap':'grey'
                }
            }
        )

def test_successful_pap():
    PAPMarkingDefinition(
        id='marking-definition--60f8932b-e51e-4458-b265-a2e8be9a80ab',
        created="2022-10-02T00:00:00.000Z",
        name="PAP:AMBER",
        extensions={
            PAP_MARKING_EXTENSION_ID:{
                'pap':'amber'
            }
        }
    )

def test_parse_props():
    input_file = 'pap-amber.json'
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), input_file)
    with open(filepath) as content:
        marking = stix2.parse(content)

    assert isinstance(marking, stix2.MarkingDefinition)
    assert isinstance(
        marking.extensions[PAP_MARKING_EXTENSION_ID],
        PAPExtension
    )

