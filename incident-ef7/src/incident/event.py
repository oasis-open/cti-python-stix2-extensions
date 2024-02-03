from collections import OrderedDict

import stix2
from stix2.exceptions import ObjectConfigurationError
from stix2.properties import (BooleanProperty, EnumProperty, ListProperty,
                              OpenVocabProperty, ReferenceProperty,
                              StringProperty, TimestampProperty)
from stix2.v21.base import _STIXBase21

import incident.vocab as vocab
from incident.common import StateChange
from incident.util import validate_event_sequence

# Event Extension Data
EVENT_EXTENSION_DEFINITION_ID = 'extension-definition--4ca6de00-5b0d-45ef-a1dc-ea7279ea910e'


class EventSequenceEntry(_STIXBase21):
    _properties = OrderedDict([
        # required properties
        ('event_ref', ReferenceProperty(valid_types='event', required=True)),
        ('condition_type', EnumProperty(vocab.ACTIVITY_CONDITION, required=True)),
        ('transition_type', EnumProperty(vocab.ACTIVITY_TRANSITION, required=True))
    ])


class EventEntry(_STIXBase21):
    _properties = OrderedDict([
        # required properties
        ('event_ref', ReferenceProperty(valid_types='event', required=True)),
        # optional properties
        ('next_steps', ListProperty(EventSequenceEntry)),
        ('sequence_start', BooleanProperty(default=lambda: True))
    ])


@stix2.v21.CustomObject(
    'event',
    [
        # required properties
        ('status', EnumProperty(vocab.EVENT_STATUS, required=True)),
        # optional properties
        ('changed_objects', ListProperty(StateChange)),
        ('description', StringProperty()),
        ('end_time', TimestampProperty()),
        ('end_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY)),
        ('event_types', ListProperty(OpenVocabProperty(vocab.EVENT_TYPE))),
        ('goal', StringProperty()),
        ('name', StringProperty()),
        ('sighting_refs', ListProperty(ReferenceProperty(valid_types='sighting'))),
        ('start_time', TimestampProperty()),
        ('start_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY)),
        ('subevents', ListProperty(EventEntry)),
    ],
    EVENT_EXTENSION_DEFINITION_ID
)
class Event:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        validate_event_sequence(self.get("subevents"))

        start_time = self.get('start_time')
        end_time = self.get('end_time')

        if start_time is not None and end_time is not None:
            if start_time >= end_time:
                raise ObjectConfigurationError(
                    'event start time is equal to or later than end time:'
                    ' {} >= {}'.format(start_time, end_time)
                )
