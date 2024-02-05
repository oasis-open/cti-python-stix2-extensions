import pytest
import incident.util as util
from stix2.exceptions import InvalidValueError


def test_check_open_bounds_high():
    with pytest.raises(InvalidValueError):
        # any old class and prop name will do
        util.check_open_bounds(list, "foo", 2, max_exc=2)

    with pytest.raises(InvalidValueError):
        util.check_open_bounds(list, "foo", 2, max_exc=1)


def test_check_open_bounds_low():
    with pytest.raises(InvalidValueError):
        # any old class and prop name will do
        util.check_open_bounds(list, "foo", 1, min_exc=1)

    with pytest.raises(InvalidValueError):
        util.check_open_bounds(list, "foo", 1, min_exc=2)
