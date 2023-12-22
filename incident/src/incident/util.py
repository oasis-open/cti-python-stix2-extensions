from stix2.exceptions import InvalidValueError, ObjectConfigurationError


def check_open_bounds(cls, prop_name, value, min_exc=None, max_exc=None):
    """
    Check a value against an open bound.  stix2's numeric Property objects only
    support checking against closed bounds.

    :param cls: The python class corresponding to the STIX type whose property
        value is being checked
    :param prop_name: The name of the property being checked
    :param value: The numeric value to check
    :param min_exc: An exclusive numeric lower bound
    :param max_exc: An exclusive numeric upper bound
    :raise InvalidValueError: If value is out of bounds
    """
    if min_exc is not None and value <= min_exc:
        raise InvalidValueError(
            cls, prop_name,
            "value must be greater than {}: {}".format(
                min_exc, value
            )
        )

    if max_exc is not None and value >= max_exc:
        raise InvalidValueError(
            cls, prop_name,
            "value must be less than {}: {}".format(
                max_exc, value
            )
        )


# Functions below copied from stix2-incident library, authored by DOD Cyber
# Crime Center (DC3)
# https://github.com/dod-cyber-crime-center
def validate_event_sequence(sequence):
    if sequence is None:
        return

    has_start = False
    ids = set()
    for item in sequence:
        ids.add(item.event_ref)
        has_start = has_start or item.sequence_start

    if not has_start:
        raise ObjectConfigurationError("At least one Event in a list must have sequence_start set to True")

    for item in sequence:
        for subitem in item.get("next_steps", []):
            if subitem.event_ref not in ids:
                raise ObjectConfigurationError(
                    "All next_step event_ref values must be Event entries in the parent list")


def validate_task_sequence(sequence):
    if sequence is None:
        return

    has_start = False
    ids = set()
    for item in sequence:
        ids.add(item.task_ref)
        has_start = has_start or item.sequence_start

    if not has_start:
        raise ObjectConfigurationError("At least one Task in a list must have sequence_start set to True")

    for item in sequence:
        for subitem in item.get("next_steps", []):
            if subitem.task_ref not in ids:
                raise ObjectConfigurationError("All next_step task_ref values must be Task entries in the parent list")

# End of stix2-incident functions
