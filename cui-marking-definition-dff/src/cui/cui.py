import stix2
from stix2.properties import (EnumProperty, ListProperty, ReferenceProperty,
                              StringProperty)

CUI_MARKING_EXTENSION_ID = "extension-definition--dff17fb3-edcb-4f99-ad1b-4b751c95738a"
CONTROL_ENUM = [
    "CONTROLLED",
    "CUI",
]


@stix2.v21.CustomExtension(
    CUI_MARKING_EXTENSION_ID, [
        ('control', EnumProperty(CONTROL_ENUM, required=True)),
        ('designator_ref', ReferenceProperty(valid_types='identity', spec_version='2.1', required=True)),
        ('categories', ListProperty(StringProperty())),
        ('disseminations', ListProperty(StringProperty())),
        ('required_statements', ListProperty(StringProperty())),
        ('supplemental_administrative', ListProperty(StringProperty())),
    ],
)
class CUIExtension:
    extension_type = 'property-extension'
