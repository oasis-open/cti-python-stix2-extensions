import stix2
from collections import OrderedDict
from stix2.v21.base import _STIXBase21
import identity_contact_information.vocab as vocab
from stix2.properties import StringProperty, ListProperty, ReferenceProperty, EmbeddedObjectProperty, EnumProperty

IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID = 'extension-definition--66e2492a-bbd3-4be6-88f5-cc91a017a498'


class ContactNumber(_STIXBase21):

    _properties = OrderedDict([
        ('description', StringProperty()),
        ('contact_number_type', EnumProperty(vocab.CONTACT_NUMBER_OV, required=True)),
        ('contact_number', StringProperty(required=True))
    ])


class EmailContact(_STIXBase21):

    _properties = OrderedDict([
        ('description', StringProperty()),
        ('digital_contact_type', EnumProperty(vocab.DIGITAL_CONTACT_OV, required=True)),
        ("email_address_ref", ReferenceProperty(valid_types='email-addr', spec_version='2.1', required=True))
    ])


class SocialMediaContact(_STIXBase21):

    _properties = OrderedDict([
        ('description', StringProperty()),
        ('digital_contact_type', EnumProperty(vocab.DIGITAL_CONTACT_OV, required=True)),
        ('user_account_ref', ReferenceProperty(valid_types='user-account', spec_version='2.1', required=True))
    ])


@stix2.v21.CustomExtension(
    IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID, [
        ('contact_numbers', ListProperty(EmbeddedObjectProperty(type=ContactNumber))),
        ('email_addresses', ListProperty(EmbeddedObjectProperty(type=EmailContact))),
        ('first_name', StringProperty()),
        ('last_name', StringProperty()),
        ('middle_name', StringProperty()),
        ('prefix', StringProperty()),
        ('social_media_accounts', ListProperty(EmbeddedObjectProperty(type=SocialMediaContact))),
        ('suffix', StringProperty()),
    ],
)
class IdentityContactInformation:
    extension_type = 'property-extension'
