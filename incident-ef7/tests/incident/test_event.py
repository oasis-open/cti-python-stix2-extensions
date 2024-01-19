import pytest
import stix2
import stix2.exceptions

import incident.vocab as vocab
from incident.common import StateChange
from incident.event import (EVENT_EXTENSION_DEFINITION_ID, Event, EventEntry,
                        EventSequenceEntry)


def test_all_props():
    # Just ensure no exceptions are raised
    Event(
        status=vocab.EVENT_STATUS_OCCURRED,
        changed_objects=[
            StateChange(
                state_change_type=vocab.STATE_CHANGE_TYPE_CAUSED,
                initial_ref="identity--a9d2e39a-276a-4aca-ae7d-7412eb2b61d8"
            )
        ],
        description="An event description",
        end_time="1993-08-26T04:43:57.2354Z",
        end_time_fidelity=vocab.TIMESTAMP_FIDELITY_HOUR,
        event_types=[
            vocab.EVENT_TYPE_SPAM,
            "an_event_type"
        ],
        goal="a goal",
        name="a name",
        sighting_refs=[
            "sighting--41050024-eb93-4f67-a17c-24129da6a8b9"
        ],
        start_time="1989-07-26T06:56:37.67522Z",
        start_time_fidelity=vocab.TIMESTAMP_FIDELITY_SECOND,
        subevents=[
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
        ]
    )


def test_parse_all_props():
    # Just ensure no exceptions are raised
    event_dict = {
        "type": "event",
        "id": "event--450eebdf-2f31-4f95-aa5b-9a31cedb5aca",
        "spec_version": "2.1",
        "created": "1997-11-28T09:45:47.351115Z",
        "modified": "1999-08-29T15:48:26.23255Z",
        "status": vocab.EVENT_STATUS_OCCURRED,
        "changed_objects": [
            {
                "state_change_type": vocab.STATE_CHANGE_TYPE_CAUSED,
                "initial_ref": "identity--a9d2e39a-276a-4aca-ae7d-7412eb2b61d8"
            }
        ],
        "description": "An event description",
        "end_time": "1993-08-26T04:43:57.2354Z",
        "end_time_fidelity": vocab.TIMESTAMP_FIDELITY_HOUR,
        "event_types": [
            vocab.EVENT_TYPE_SPAM,
            "an_event_type"
        ],
        "goal": "a goal",
        "name": "a name",
        "sighting_refs": [
            "sighting--41050024-eb93-4f67-a17c-24129da6a8b9"
        ],
        "start_time": "1989-07-26T06:56:37.67522Z",
        "start_time_fidelity": vocab.TIMESTAMP_FIDELITY_SECOND,
        "subevents": [
            {
                "event_ref": "event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                "sequence_start": False
            }, {
                "event_ref": "event--5a15f261-d124-4289-813b-f0922b8ef201",
                "next_steps": [
                    {
                        "event_ref": "event--0e40486e-c290-4f80-adf1-cc3db48bf7ff",
                        "condition_type": vocab.ACTIVITY_CONDITION_OPTIONAL,
                        "transition_type": vocab.ACTIVITY_TRANSITION_SUCCESS
                    }, {
                        "event_ref": "event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                        "condition_type": vocab.ACTIVITY_CONDITION_REQUIRED,
                        "transition_type": vocab.ACTIVITY_TRANSITION_COMPLETION
                    }
                ],
                "sequence_start": True
            }, {
                "event_ref": "event--0e40486e-c290-4f80-adf1-cc3db48bf7ff",
                "next_steps": [
                    {
                        "event_ref": "event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                        "condition_type": vocab.ACTIVITY_CONDITION_UNKNOWN,
                        "transition_type": vocab.ACTIVITY_TRANSITION_FAILURE
                    }
                ],
                "sequence_start": False
            }
        ]
    }

    event = stix2.parse(event_dict)

    assert isinstance(event, Event)
    assert EVENT_EXTENSION_DEFINITION_ID in event.extensions


def test_subevents_no_sequence_start():
    with pytest.raises(stix2.exceptions.ObjectConfigurationError):
        Event(
            status=vocab.EVENT_STATUS_NOT_OCCURRED,
            subevents=[
                EventEntry(
                    event_ref="event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                    sequence_start=False
                )
            ]
        )


def test_subevents_undefined_next_event():
    with pytest.raises(stix2.exceptions.ObjectConfigurationError):
        Event(
            status=vocab.EVENT_STATUS_NOT_OCCURRED,
            subevents=[
                EventEntry(
                    event_ref="event--02aae82a-b66f-41d5-82f4-72dfe6865980",
                    sequence_start=True,
                    next_steps=[
                        EventSequenceEntry(
                            # the following event is undefined in subevents.
                            event_ref="event--ae7cd248-bb2c-438f-a45b-c174dfa876e5",
                            condition_type=vocab.ACTIVITY_CONDITION_UNKNOWN,
                            transition_type=vocab.ACTIVITY_TRANSITION_COMPLETION
                        )
                    ]
                )
            ]
        )
