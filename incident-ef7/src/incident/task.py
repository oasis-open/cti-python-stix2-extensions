from collections import OrderedDict

import stix2
from stix2.exceptions import ObjectConfigurationError
from stix2.properties import (BooleanProperty, EnumProperty, IntegerProperty,
                              ListProperty, OpenVocabProperty,
                              ReferenceProperty, StringProperty,
                              TimestampProperty)
from stix2.v21 import _STIXBase21

import incident.util as util
import incident.vocab as vocab
from incident.common import EntityCountProperty, StateChange

# Event Extension Data
TASK_EXTENSION_DEFINITION_ID = 'extension-definition--2074a052-8be4-4932-849e-f5e7798e0030'


class TaskSequenceEntry(_STIXBase21):
    _properties = OrderedDict([
        # required properties
        ('task_ref', ReferenceProperty(valid_types='task', required=True)),
        ('condition_type', EnumProperty(vocab.ACTIVITY_CONDITION, required=True)),
        ('transition_type', EnumProperty(vocab.ACTIVITY_TRANSITION, required=True))
   ])


class TaskEntry(_STIXBase21):
    _properties = OrderedDict([
        # required properties
        ('task_ref', ReferenceProperty(valid_types='task', required=True)),
        # optional properties
        ('next_steps', ListProperty(TaskSequenceEntry)),
        ('sequence_start', BooleanProperty(default=lambda: True))
    ])


@stix2.v21.CustomObject(
    'task',
    [
        # required properties
        ('outcome', EnumProperty(vocab.TASK_OUTCOME, required=True)),
        # optional properties
        ('changed_objects', ListProperty(StateChange)),
        ('task_types', ListProperty(OpenVocabProperty(vocab.TASK_TYPE))),
        ('description', StringProperty()),
        ('end_time', TimestampProperty()),
        ('end_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY)),
        ('error', StringProperty()),
        ('impacted_entity_types', EntityCountProperty(spec_version='2.1')),
        ('name', StringProperty()),
        ('priority', IntegerProperty(min=0, max=100)),
        ('start_time', TimestampProperty()),
        ('start_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY)),
        ('subtasks', ListProperty(TaskEntry))
    ],
    TASK_EXTENSION_DEFINITION_ID
)
class Task:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        util.validate_task_sequence(self.get("subtasks"))

        start_time = self.get('start_time')
        end_time = self.get('end_time')

        if start_time is not None and end_time is not None:
            if start_time >= end_time:
                raise ObjectConfigurationError(
                    'task start time is equal to or later than end time:'
                    ' {} >= {}'.format(start_time, end_time),
                )
