import stix2 
from .observed_string_ov import STRING_PURPOSE
from stix2.properties import (OpenVocabProperty,
                              StringProperty)


OBSERVED_STRING_EXTENSION_ID = "extension-definition--8b1aa84c-5532-4c69-a8e7-b6170facfd3d"


@stix2.v21.CustomExtension(
    applies_to = "sco",
    type = OBSERVED_STRING_EXTENSION_ID,
    properties =
    [
            # required fields
            ('purpose', OpenVocabProperty(STRING_PURPOSE, required=True)),
            ('value', StringProperty(required=True))
    ]
)
class ObservedString:
    extension_type = 'new-sco'
