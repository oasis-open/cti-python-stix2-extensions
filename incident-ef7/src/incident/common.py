from collections import OrderedDict

import stix2.exceptions
import stix2.utils
from stix2.properties import (DictionaryProperty, OpenVocabProperty,
                              ReferenceProperty)
from stix2.v21.base import _STIXBase21

from incident.vocab import STATE_CHANGE_TYPE


class StateChange(_STIXBase21):

    _properties = OrderedDict([
        ('state_change_type', OpenVocabProperty(STATE_CHANGE_TYPE, required=True)),
        ('initial_ref', ReferenceProperty(valid_types="SDO")),
        ('result_ref', ReferenceProperty(valid_types="SDO"))
    ])

    def _check_object_constraints(self):
        super()._check_object_constraints()
        super()._check_at_least_one_property(("initial_ref", "result_ref"))

        initial_ref = self.get("initial_ref")
        result_ref = self.get("result_ref")

        if initial_ref is not None and result_ref is not None:
            initial_ref_type = stix2.utils.get_type_from_id(initial_ref)
            result_ref_type = stix2.utils.get_type_from_id(result_ref)

            if initial_ref_type != result_ref_type:
                raise stix2.exceptions.ObjectConfigurationError(
                    "state-change initial_ref and result_ref must reference"
                    " the same type of object: {}, {}".format(
                        initial_ref_type, result_ref_type
                    )
                )


class EntityCountProperty(DictionaryProperty):
    """
    Enforce some requirements for the entity-count type, and do some simple
    cleaning on values.
    """
    def clean(self, counts, allow_custom=False):
        """
        Enforce the same requirements on keys as the STIX "dictionary" type,
        and also check requirements specific to entity-count.  This also
        enables flexibility w.r.t. count type, as an int or (integral) float.

        :param counts: An entity-count mapping
        :param allow_custom: Whether customization should be allowed
        :return: a (<cleaned-value>, <has-custom>) 2-tuple (which is a
            dict, bool).
        """
        cleaned_dict, has_custom = super().clean(counts, allow_custom)

        for key, count in cleaned_dict.items():
            if not isinstance(count, (float, int)):
                raise TypeError(
                    "entity-count values must be integers: " + str(count)
                )

            if count < 0:
                raise ValueError(
                    "entity-count values must be greater than or equal to"
                    " zero: " + str(count)
                )

            int_count = int(count)
            if int_count != count:
                raise ValueError(
                    "entity-count values must be integers: " + str(count)
                )

            cleaned_dict[key] = int_count

        return cleaned_dict, has_custom
