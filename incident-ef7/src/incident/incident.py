from collections import OrderedDict

import stix2
from stix2.properties import (EnumProperty, FloatProperty, IntegerProperty,
                              ListProperty, OpenVocabProperty,
                              ReferenceProperty, StringProperty)
from stix2.v21.base import _STIXBase21

import incident.vocab as vocab
from .common import EntityCountProperty


INCIDENT_EXTENSION_DEFINITION_ID = 'extension-definition--ef765651-680c-498d-9894-99799f2fa126'


class IncidentScore(_STIXBase21):
    _properties = OrderedDict([
        # required properties
        ('name', StringProperty(required=True)),
        ('value', FloatProperty(required=True)),
        # optional properties
        ('description', StringProperty())
    ])


@stix2.v21.CustomExtension(
    applies_to="sdo",
    type=INCIDENT_EXTENSION_DEFINITION_ID,
    properties=[
        # required properties
        ('determination', EnumProperty(vocab.INCIDENT_DETERMINATION, required=True)),
        ('investigation_status', OpenVocabProperty(vocab.INCIDENT_INVESTIGATION, required=True)),
        # optional properties
        ('criticality', IntegerProperty(min=0, max=100)),
        ('detection_methods', ListProperty(OpenVocabProperty(vocab.DETECTION_METHODS))),
        ('event_refs', ListProperty(ReferenceProperty(valid_types='event'))),
        ('impact_refs', ListProperty(ReferenceProperty(valid_types='impact'))),
        ('incident_types', ListProperty(OpenVocabProperty(vocab.EVENT_TYPE))),
        ('recoverability', EnumProperty(vocab.RECOVERABILITY)),
        ('scores', ListProperty(IncidentScore)),
        ('task_refs', ListProperty(ReferenceProperty(valid_types='task'))),
    ],
)
class IncidentExtension:
    extension_type = 'property-extension'
