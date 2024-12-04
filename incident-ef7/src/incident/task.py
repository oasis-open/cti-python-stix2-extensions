from collections import OrderedDict

import stix2
from stix2.exceptions import ObjectConfigurationError
from stix2.properties import (EnumProperty, IntegerProperty,
                              ListProperty, OpenVocabProperty,
                              ReferenceProperty, StringProperty,
                              TimestampProperty)

import util
import vocab
from .common import EntityCountProperty, StateChange

# Event Extension Data
TASK_EXTENSION_DEFINITION_ID = 'extension-definition--2074a052-8be4-4932-849e-f5e7798e0030'


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
        ('next_task_ref', ListProperty(ReferenceProperty(valid_types='task'))),
        ('priority', IntegerProperty(min=0, max=100)),
        ('start_time', TimestampProperty()),
        ('start_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY))
    ],
    TASK_EXTENSION_DEFINITION_ID
)
class Task:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        start_time = self.get('start_time')
        end_time = self.get('end_time')

        if start_time is not None and end_time is not None:
            if start_time >= end_time:
                raise ObjectConfigurationError(
                    'task start time is equal to or later than end time:'
                    ' {} >= {}'.format(start_time, end_time),
                )
