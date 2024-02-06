import stix2
import stix2.exceptions
import stix2.properties

import incident.vocab as vocab
from incident.event import EventEntry, EventSequenceEntry
from incident.incident import (INCIDENT_EXTENSION_DEFINITION_ID, IncidentExtension,
                           IncidentScore)
from incident.task import TaskEntry, TaskSequenceEntry


def test_all_props():
    stix2.Incident(
        description='This file hash indicates that a sample of Poison Ivy is present.',
        name='Valid Incident',
        labels=['malicious-activity'],
        extensions={
            INCIDENT_EXTENSION_DEFINITION_ID: IncidentExtension(
                determination=vocab.INCIDENT_DETERMINATION_BLOCKED,
                investigation_status=vocab.INCIDENT_INVESTIGATION_NEW,
                criticality=99,
                detection_methods=[
                    vocab.DETECTION_METHODS_AUTOMATED_TOOL,
                    vocab.DETECTION_METHODS_HUMAN_REVIEW,
                    vocab.DETECTION_METHODS_SYSTEM_OUTAGE
                ],
                impact_refs=[
                    "impact--2c89cb8e-6884-47f2-b55e-f2894a4f00d1",
                    "impact--89754959-2d69-469c-951a-9becca10cc40"
                ],
                impacted_entity_counts={
                    'organization': 10,
                    'sector': 1,
                    'system': 1000
                },
                incident_types=[
                    vocab.EVENT_TYPE_MAJOR,
                    vocab.EVENT_TYPE_DENIAL_OF_SERVICE
                ],
                recoverability=vocab.RECOVERABILITY_REGULAR,
                scores=[
                    IncidentScore(
                        name='score1',
                        value=3214,
                        description='incident test score'
                    ),
                    IncidentScore(
                        name='score2',
                        value=371,
                        description='incident test 2 score'
                    ),
                ],

                events=[
                    EventEntry(
                        event_ref="event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                        sequence_start=False
                    ), EventEntry(
                        event_ref="event--5a15f261-d124-4289-813b-f0922b8ef201",
                        next_steps=[
                            EventSequenceEntry(
                                event_ref="event--0e40486e-c290-4f80-adf1-cc3db48bf7ff",
                                condition_type=vocab.ACTIVITY_CONDITION_OPTIONAL,
                                transition_type=vocab.ACTIVITY_TRANSITION_SUCCESS
                            ), EventSequenceEntry(
                                event_ref="event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                                condition_type=vocab.ACTIVITY_CONDITION_REQUIRED,
                                transition_type=vocab.ACTIVITY_TRANSITION_COMPLETION
                            )
                        ],
                        sequence_start=True
                    ), EventEntry(
                        event_ref="event--0e40486e-c290-4f80-adf1-cc3db48bf7ff",
                        next_steps=[
                            EventSequenceEntry(
                                event_ref="event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                                condition_type=vocab.ACTIVITY_CONDITION_UNKNOWN,
                                transition_type=vocab.ACTIVITY_TRANSITION_FAILURE
                            )
                        ],
                        sequence_start=False
                    )
                ],

                tasks=[
                    TaskEntry(
                        task_ref="task--741432b2-b445-4dc0-9362-2ec0323ad877",
                        sequence_start=False
                    ),
                    TaskEntry(
                        task_ref="task--5c3e2ef7-d287-4913-ab20-3c802dd0a7c6",
                        sequence_start=False,
                        next_steps=[
                            TaskSequenceEntry(
                                task_ref="task--741432b2-b445-4dc0-9362-2ec0323ad877",
                                condition_type=vocab.ACTIVITY_CONDITION_UNKNOWN,
                                transition_type=vocab.ACTIVITY_TRANSITION_COMPLETION
                            )
                        ]
                    ),
                    TaskEntry(
                        task_ref="task--b45ef1d8-4731-48f1-ae86-22e14fd7c00e",
                        sequence_start=True,
                        next_steps=[
                            TaskSequenceEntry(
                                task_ref="task--5c3e2ef7-d287-4913-ab20-3c802dd0a7c6",
                                condition_type=vocab.ACTIVITY_CONDITION_OPTIONAL,
                                transition_type=vocab.ACTIVITY_TRANSITION_SUCCESS
                            ),
                            TaskSequenceEntry(
                                task_ref="task--741432b2-b445-4dc0-9362-2ec0323ad877",
                                condition_type=vocab.ACTIVITY_CONDITION_REQUIRED,
                                transition_type=vocab.ACTIVITY_TRANSITION_FAILURE
                            )
                        ]
                    )
                ]
            )
        }
    )


def test_parse_all_props():
    incident_dict = {
        'id': 'incident--e97bfccf-8970-4a3c-9cd1-5b5b97ed5d0c',
        "spec_version": "2.1",
        'created': '2014-02-20T09:16:08.989000Z',
        'modified': '2014-02-20T09:16:08.989000Z',
        'description': 'This file hash indicates that a sample of Poison Ivy is present.',
        'type': 'incident',
        'name': 'Valid Incident',
        'labels': [
            'malicious-activity',
        ],
        'extensions': {
            INCIDENT_EXTENSION_DEFINITION_ID: {
                'determination': 'blocked',
                'extension_type': 'property-extension',
                'investigation_status': 'new',
                'detection_methods': ['automated-tool', 'human-review', 'system-outage'],
                "impact_refs": [
                    "impact--2c89cb8e-6884-47f2-b55e-f2894a4f00d1",
                    "impact--89754959-2d69-469c-951a-9becca10cc40"
                ],
                'impacted_entity_counts': {
                    'organization': 10,
                    'sector': 1,
                    'system': 1000
                },
                'incident_types': ['major', 'denial-of-service'],
                'recoverability': 'regular',
                'scores': [
                    {
                        'name': 'score1',
                        'value': 3214,
                        'description': 'incident test score'
                    },
                    {
                        'name': 'score2',
                        'value': 371,
                        'description': 'incident test 2 score'
                    },
                ],

                "events": [
                    {
                        "event_ref": "event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                        "sequence_start": False,
                    }, {
                        "event_ref": "event--5a15f261-d124-4289-813b-f0922b8ef201",
                        "sequence_start": True,
                        "next_steps": [
                            {
                                "event_ref": "event--0e40486e-c290-4f80-adf1-cc3db48bf7ff",
                                "condition_type": "optional",
                                "transition_type": "success"
                            }, {
                                "event_ref": "event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                                "condition_type": "required",
                                "transition_type": "completion"
                            }
                        ],
                    }, {
                        "event_ref": "event--0e40486e-c290-4f80-adf1-cc3db48bf7ff",
                        "sequence_start": False,
                        "next_steps": [
                            {
                                "event_ref": "event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                                "condition_type": "unknown",
                                "transition_type": "failure"
                            }
                        ],
                    }
                ],

                "tasks": [
                    {
                        "task_ref": "task--741432b2-b445-4dc0-9362-2ec0323ad877",
                        "sequence_start": False
                    }, {
                        "task_ref": "task--5c3e2ef7-d287-4913-ab20-3c802dd0a7c6",
                        "sequence_start": False,
                        "next_steps": [
                            {
                                "task_ref": "task--741432b2-b445-4dc0-9362-2ec0323ad877",
                                "condition_type": "unknown",
                                "transition_type": "completion"
                            }
                        ]
                    }, {
                        "task_ref": "task--b45ef1d8-4731-48f1-ae86-22e14fd7c00e",
                        "sequence_start": True,
                        "next_steps": [
                            {
                                "task_ref": "task--5c3e2ef7-d287-4913-ab20-3c802dd0a7c6",
                                "condition_type": "optional",
                                "transition_type": "success"
                            }, {
                                "task_ref": "task--741432b2-b445-4dc0-9362-2ec0323ad877",
                                "condition_type": "required",
                                "transition_type": "failure"
                            }
                        ]
                    }
                ]
            }
        }
    }

    incident = stix2.parse(incident_dict)

    assert isinstance(incident, stix2.Incident)
    assert isinstance(
        incident.extensions[INCIDENT_EXTENSION_DEFINITION_ID],
        IncidentExtension
    )
