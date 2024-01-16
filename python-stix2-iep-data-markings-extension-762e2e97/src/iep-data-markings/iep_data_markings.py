from stix2.v21 import CustomExtension
from stix2.properties import (
    EnumProperty, FloatProperty, ListProperty,
    StringProperty, TimestampProperty
)
from iep_data_markings.vocab import IEP_PERMITTED_ACTIONS, MAY, MUST, MUST_NOT

IEP_DATA_MARKING_EXTENSION_ID = 'extension-definition--762e2e97-ee51-43e5-a9ea-165fbb862c4a'


@CustomExtension(IEP_DATA_MARKING_EXTENSION_ID, [
    ('encrypt_in_transit', StringProperty(required=True)),
    ('encrypt_in_transit', EnumProperty(allowed=[MUST, MAY], required=True)),
    ('permitted_actions', ListProperty(
        EnumProperty(IEP_PERMITTED_ACTIONS), required=True,
    )),
    ('affected_party_notifications', EnumProperty(allowed=[MAY, MUST_NOT], required=True)),
    ('tlp', StringProperty(required=True)),
    ('provider_attribution', EnumProperty(
        allowed=[MAY, MUST, MUST_NOT], required=True,
    )),
    ('unmodified_resale', EnumProperty(allowed=[MAY, MUST_NOT], required=True)),
    ('iep_id', StringProperty(required=True)),
    ('iep_version', FloatProperty(required=True)),
    ('policy_name', StringProperty(required=True)),
    ('description', StringProperty(required=True)),
    ('start_date', TimestampProperty(required=True)),
    ('end_date', TimestampProperty(required=False)),
])
class IEPDataMarking:
    extension_type = 'property-extension'
