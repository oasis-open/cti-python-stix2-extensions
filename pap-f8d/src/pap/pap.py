import stix2
from collections import OrderedDict
from stix2.v21.base import _STIXBase21
from stix2.v21 import MarkingDefinition
from stix2.properties import StringProperty, DictionaryProperty, EnumProperty
from stix2.exceptions import ObjectConfigurationError

PAP_MARKING_EXTENSION_ID = 'extension-definition--f8d78575-edfd-406e-8e84-6162a8450f5b'

PAP_NAMES = [
    "PAP:GREEN",
    "PAP:WHITE",
    "PAP:RED",
    "PAP:AMBER"
]

PAP_COLORS = [
    "green",
    "white",
    "red",
    "amber"
]

PAP_AMBER = {
    'id':'marking-definition--60f8932b-e51e-4458-b265-a2e8be9a80ab',
    'created': '2022-10-02T00:00:00.000Z',
    'name': 'PAP:AMBER',
    'extensions': {
        PAP_MARKING_EXTENSION_ID:{
            'pap':'amber'
        }
    }
}

def check_pap_marking(pap_marking):
    pass

@stix2.v21.CustomExtension(
    PAP_MARKING_EXTENSION_ID, [
        ('pap', EnumProperty(PAP_COLORS, required=True))
    ]
)

class PAPExtension:
    extension_type = 'property-extension'


class PAPMarkingDefinitionError(ObjectConfigurationError):

    def __str__(self):
        msg = "The only instances of PAP marking definitions permitted are those defined in the PAP Extension Specification"


class PAPMarkingDefinition(MarkingDefinition):

    def __init__(self, **kwargs):
        super(PAPMarkingDefinition, self).__init__(**kwargs)
        self._properties.update([
            ('name', EnumProperty(PAP_NAMES, required=True))
        ])
    
    def __eq__(self, other):
        properties_to_compare = ['id', 'created', 'name']
        for field in properties_to_compare:
            if self[field] != other[field]:
                return False
        
        if self['extensions'][PAP_MARKING_EXTENSION_ID]['pap'] != other['extensions'][PAP_MARKING_EXTENSION_ID]['pap']:
            return False
        
        return True
    
    def _check_object_constraints(self):
        super(PAPMarkingDefinition, self)._check_object_constraints()
        check_pap_marking(self)


PAP_AMBER = PAPMarkingDefinition(
    id='marking-definition--60f8932b-e51e-4458-b265-a2e8be9a80ab',
    created="2022-10-02T00:00:00.000Z",
    name="PAP:AMBER",
    extensions={
        PAP_MARKING_EXTENSION_ID:{
            'pap':'amber'
        }
    }
)

PAP_GREEN = PAPMarkingDefinition(
    id='marking-definition--c43594d1-4b11-4c59-93ab-1c9b14d53ce9',
    created="2022-10-09T00:00:00.000Z",
    name="PAP:GREEN",
    extensions={
        PAP_MARKING_EXTENSION_ID:{
            'pap':'green'
        }
    }
)

PAP_RED = PAPMarkingDefinition(
    id='marking-definition--740d36e5-7714-4c30-961a-3ae632ceee0e',
    created="2022-10-06T00:00:00.000Z",
    name="PAP:RED",
    extensions={
        PAP_MARKING_EXTENSION_ID:{
            'pap':'red'
        }
    }
)

PAP_WHITE = PAPMarkingDefinition(
    id='marking-definition--a3bea94c-b469-41dc-9cfe-d6e7daba7730',
    created="2022-10-01T00:00:00.000Z",
    name="PAP:WHITE",
    extensions={
        PAP_MARKING_EXTENSION_ID:{
            'pap':'white'
        }
    }
)

def check_pap_marking(pap_marking):
    pap_objects = [PAP_AMBER, PAP_GREEN, PAP_RED, PAP_WHITE]
    if pap_marking not in pap_objects:
        raise PAPMarkingDefinitionError