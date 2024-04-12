import stix2
from stix2.v21 import MarkingDefinition
from stix2.properties import EnumProperty
from stix2.exceptions import ObjectConfigurationError

PAP_MARKING_EXTENSION_ID = 'extension-definition--f8d78575-edfd-406e-8e84-6162a8450f5b'

PAP_NAMES = [
    "PAP:GREEN",
    "PAP:WHITE",
    "PAP:RED",
    "PAP:AMBER",
    "PAP:CLEAR"
]

PAP_COLORS = [
    "green",
    "white",
    "red",
    "amber",
    "clear"
]

PAP_AMBER = {
    'id':'marking-definition--60f8932b-e51e-4458-b265-a2e8be9a80ab',
    'created':"2022-10-02T00:00:00.000Z",
    'name':"PAP:AMBER",
    'extensions':{
        PAP_MARKING_EXTENSION_ID:{
            'pap':'amber'
        }
    }
}


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
        return msg.format(self)

class PAPMarkingDefinition(MarkingDefinition):

    def __init__(self, **kwargs):
        super(PAPMarkingDefinition, self).__init__(**kwargs)
        self._properties.update([
            ('name', EnumProperty(PAP_NAMES, required=True))
        ])
    
    def __eq__(self, other):
        properties_to_compare = ['id', 'name']
        for field in properties_to_compare:
            if self[field] != other[field]:
                return False
        
        if isinstance(other, dict):
            if self['created'] != stix2.utils.parse_into_datetime(other['created']):
                return False
        else:
            if self['created'] != other['created']:
                return False
        
        if self['extensions'][PAP_MARKING_EXTENSION_ID]['pap'] != other['extensions'][PAP_MARKING_EXTENSION_ID]['pap']:
            return False
        return True
    
    def _check_object_constraints(self):
        super(PAPMarkingDefinition, self)._check_object_constraints()

        pap_objects = [PAP_AMBER, PAP_GREEN, PAP_RED, PAP_WHITE, PAP_CLEAR]

        match_found = False
        for pap in pap_objects:
            if pap['name'] == self['name']: 
                match_found = True
                if not self == pap:
                    raise PAPMarkingDefinitionError
        
        if not match_found:
            raise PAPMarkingDefinitionError
