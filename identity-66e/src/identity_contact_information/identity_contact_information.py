import stix2
from collections import OrderedDict
from stix2.v21.base import _STIXBase21
from stix2.properties import (EmbeddedObjectProperty, StringProperty, ListProperty, ReferenceProperty,
                              BooleanProperty, OpenVocabProperty
                              )

IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID = 'extension-definition--66e2492a-bbd3-4be6-88f5-cc91a017a498'

CONTACT_NUMBER_OV = [
    "personal-landline-phone",
    "personal-mobile-phone",
    "personal-fax",
    "work-phone",
    "work-fax"
]

DIGITAL_CONTACT_OV = [
    "organizational",
    "personal",
    "work"
]


class ContactNumber(_STIXBase21):

    _properties = OrderedDict([
        ('description', StringProperty()),
        ('contact_number_type', OpenVocabProperty(CONTACT_NUMBER_OV)),
        ('contact_number', StringProperty(required=True)),
        ('classified', BooleanProperty())
    ])


class EmailContact(_STIXBase21):

    _properties = OrderedDict([
        ('description', StringProperty()),
        ('digital_contact_type', OpenVocabProperty(DIGITAL_CONTACT_OV)),
        ("email_address_ref", ReferenceProperty(valid_types='email-addr', spec_version='2.1', required=True)),
        ('classified', BooleanProperty())
    ])


class SocialMediaContact(_STIXBase21):

    _properties = OrderedDict([
        ('description', StringProperty()),
        ('digital_contact_type', OpenVocabProperty(DIGITAL_CONTACT_OV)),
        ('user_account_ref', ReferenceProperty(valid_types='user-account', spec_version='2.1', required=True)),
        ('classified', BooleanProperty())
    ])


@stix2.v21.CustomExtension(
    applies_to="sdo",
    type=IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID,
    properties=
    [
        ('contact_numbers', ListProperty(EmbeddedObjectProperty(ContactNumber))),
        ('email_addresses', ListProperty(EmbeddedObjectProperty(EmailContact))),
        ("websites", ListProperty(StringProperty)),
        ('first_name', StringProperty()),
        ('last_name', StringProperty()),
        ('middle_name', StringProperty()),
        ('prefix', StringProperty()),
        ('social_media_accounts', ListProperty(EmbeddedObjectProperty(SocialMediaContact))),
        ('suffix', StringProperty()),
    ],
)
class IdentityContactInformation():
    extension_type = 'property-extension'

    def _check_object_constraints(self):
        super()._check_object_constraints()
        self._check_at_least_one_property(["contact_numbers", "email_addresses", "social_media_accounts"])