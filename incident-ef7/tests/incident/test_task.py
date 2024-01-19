import pytest
import stix2
from stix2.exceptions import ObjectConfigurationError

import incident.vocab as vocab
from incident.common import StateChange
from incident.task import (TASK_EXTENSION_DEFINITION_ID, Task, TaskEntry,
                       TaskSequenceEntry)


def test_all_props():

    Task(
        outcome=vocab.TASK_OUTCOME_ONGOING,
        changed_objects=[
            StateChange(
                state_change_type=vocab.STATE_CHANGE_TYPE_CAUSED,
                initial_ref="identity--a4553576-15c0-4369-bed7-fcb36a028f56",
                result_ref="identity--c3e6bc72-5aac-4719-8932-22b0a8ac0ffc"
            )
        ],
        task_types=[vocab.TASK_TYPE_ADMINISTRATIVE, vocab.TASK_TYPE_REPORTED],
        description="A task description",
        end_time="2001-06-22T23:24:28.58332Z",
        end_time_fidelity=vocab.TIMESTAMP_FIDELITY_DAY,
        error="A task error",
        impacted_entity_types={
            "a": 1,
            "b": 2.0
        },
        name="task name",
        priority=72,
        start_time="1998-01-30T17:40:37.48329Z",
        start_time_fidelity=vocab.TIMESTAMP_FIDELITY_SECOND,

        subtasks=[
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


def test_parse_all_props():
    task_dict = {
        "type": "task",
        "id": "task--86e51c24-e88a-4b3f-a67f-f2b3ac16fc4b",
        "spec_version": "2.1",
        "created": "1988-05-24T09:33:16.1564Z",
        "modified": "1996-08-13T00:44:30.49472Z",
        "outcome": vocab.TASK_OUTCOME_ONGOING,
        "changed_objects": [
            {
                "state_change_type": vocab.STATE_CHANGE_TYPE_CAUSED,
                "initial_ref": "identity--a4553576-15c0-4369-bed7-fcb36a028f56",
                "result_ref": "identity--c3e6bc72-5aac-4719-8932-22b0a8ac0ffc"
            }
        ],
        "task_types": [
            vocab.TASK_TYPE_ADMINISTRATIVE, vocab.TASK_TYPE_REPORTED
        ],
        "description": "A task description",
        "end_time": "2001-06-22T23:24:28.58332Z",
        "end_time_fidelity": vocab.TIMESTAMP_FIDELITY_DAY,
        "error": "A task error",
        "impacted_entity_types": {
            "a": 1,
            "b": 2.0
        },
        "name": "task name",
        "priority": 72,
        "start_time": "1998-01-30T17:40:37.48329Z",
        "start_time_fidelity": vocab.TIMESTAMP_FIDELITY_SECOND,

        "subtasks": [
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

    task = stix2.parse(task_dict)

    assert isinstance(task, Task)
    assert TASK_EXTENSION_DEFINITION_ID in task.extensions


def test_subtasks_no_sequence_start():
    with pytest.raises(ObjectConfigurationError):
        Task(
            outcome=vocab.TASK_OUTCOME_FAILED,
            subtasks=[
                TaskEntry(
                    task_ref="task--245bbc0a-9983-4dd2-a9e1-f6611d1e1820",
                    sequence_start=False
                )
            ]
        )


def test_subtasks_undefined_next_step():
    with pytest.raises(ObjectConfigurationError):
        Task(
            outcome=vocab.TASK_OUTCOME_FAILED,
            subtasks=[
                TaskEntry(
                    task_ref="task--245bbc0a-9983-4dd2-a9e1-f6611d1e1820",
                    sequence_start=True,
                    next_steps=[
                        TaskSequenceEntry(
                            # the following task is undefined in subtasks.
                            task_ref="task--371f7ce0-1e53-47c8-adfb-1b3763ca0485",
                            condition_type=vocab.ACTIVITY_CONDITION_OPTIONAL,
                            transition_type=vocab.ACTIVITY_TRANSITION_FAILURE
                        )
                    ]
                )
            ]
        )
