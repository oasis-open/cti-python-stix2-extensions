import pytest
import stix2.exceptions

import incident.vocab as vocab
from incident.common import EntityCountProperty, StateChange


def test_state_change_no_refs():
    with pytest.raises(stix2.exceptions.AtLeastOnePropertyError):
        StateChange(
            state_change_type=vocab.STATE_CHANGE_TYPE_INPUT
        )


def test_state_change_bad_ref_types():
    with pytest.raises(stix2.exceptions.ObjectConfigurationError):
        StateChange(
            state_change_type=vocab.STATE_CHANGE_TYPE_CONTRIBUTED_TO,
            # These refs must be the same object type
            initial_ref="identity--d1b35587-8fe2-4ae5-8458-54be8051d7a2",
            result_ref="threat-actor--66880f06-e55d-4963-a725-893d71fe9d29"
        )


def test_entity_counts_int():
    prop = EntityCountProperty(spec_version="2.1")

    cleaned, _ = prop.clean({"a": 1})
    assert cleaned["a"] == 1


def test_entity_counts_float_integral():
    prop = EntityCountProperty(spec_version="2.1")

    cleaned, _ = prop.clean({"a": 1.0})
    assert cleaned["a"] == 1
    assert isinstance(cleaned["a"], int)


def test_entity_counts_float_fractional():
    prop = EntityCountProperty(spec_version="2.1")

    with pytest.raises(ValueError):
        prop.clean({"a": 1.2})


def test_entity_counts_negative():
    prop = EntityCountProperty(spec_version="2.1")

    with pytest.raises(ValueError):
        prop.clean({"a": -1})


def test_entity_counts_non_number():
    prop = EntityCountProperty(spec_version="2.1")

    with pytest.raises(TypeError):
        prop.clean({"a": 1+2j})
