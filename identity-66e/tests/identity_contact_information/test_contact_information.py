import stix2
import pytest
import stix2.exceptions
from stix2 import Identity
from identity_contact_information.identity_contact_information import (IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID, 
                                                                IdentityContactInformation, ContactNumber, EmailContact,
                                                                SocialMediaContact)

def test_parse_all():
    identity = Identity(
        id="identity--32a6ff61-167a-4481-b678-38e20b1989dc",
        created="2023-08-06T01:02:00.000Z",
        modified="2023-11-16T01:03:01.000Z",
        spec_version="2.1",
        name="Firstname Lastname",
        description="a contact person",
        identity_class="individual",
        contact_information="102-030-4050 / f.lastname@address.com",
        extensions={
            IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: IdentityContactInformation(
                extension_type="property-extension",
                first_name="Firstname",
                last_name="Lastname",
                middle_name="Middlename",
                prefix="Ms",
                suffix="Dr",
                contact_numbers=ContactNumber(
                    description="a contact number",
                    contact_number_type="personal-mobile-phone",
                    contact_number="123-456-7890"
                ),
                email_addresses=EmailContact(
                    description="an email address",
                    digital_contact_type="personal",
                    email_address_ref="email-addr--d80eb6d5-7d01-4cd2-b710-20ac765dc9c5"
                ),
                social_media_accounts=SocialMediaContact(
                    description="a social media account",
                    digital_contact_type="personal",
                    user_account_ref="user-account--a60d5641-a860-4a86-8ed8-6bbbeaf300e9"
                )
            )
        }
    )
    assert isinstance(identity, Identity)
    assert isinstance(
        identity_contact_information.extensions[IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID],
        IdentityContactInformation
    )

def test_missing_required_fields():
    with pytest.raises(stix2.exceptions.MissingPropertiesError):
        Identity(
            type="identity",
            name="MissingRequiredFieldsIdentity",
            extensions={
                IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: IdentityContactInformation()
            }
        )

def test_invalid_value():
    with pytest.raises(stix2.exceptions.InvalidValueError):
        Identity(
            type="identity",
            name="InvalidValueIdentity",
            extensions={
                IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: IdentityContactInformation(
                    extension_type="property-extension",
                    contact_numbers=ContactNumber(
                        contact_number_type="invalid contact number type",
                        contact_number="123-456-7890"
                    )
                )
            }
        )

def test_wrong_field_type():
    with pytest.raises(stix2.exceptions.InvalidValueError):
        Identity(
            type="identity",
            name="InvalidFieldTypeIdentity",
            extensions={
                IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: IdentityContactInformation(
                    extension_type="property-extension",
                    contact_numbers=ContactNumber(
                        contact_number_type="personal-mobile-phone",
                        contact_number=123
                    )
                )
            }
        )