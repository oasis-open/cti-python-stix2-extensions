import stix2
import pytest
import stix2.exceptions
#from identity-contact-information-extension-66e2492a.src import ContactNumber, EmailContact, SocialMediaContact, IdentityContactInformation

def test_all_fields():
    contact_info_dict = {
        "id": "identity--32a6ff61-167a-4481-b678-38e20b1989dc",
        "created": "2023-08-06T01:02:00.000Z",
        "modified": "2023-11-16T01:03:01.000Z",
        "spec_version": "2.1",
        "name": "Michael Michaelson",
        "description": "a contact person",
        "identity_class": "individual",
        "contact_information": "102-030-4050 / m.michaelson@address.com",
        "extensions" :{
            PROPERTY_EXTENSION_DEFINITION_ID: {
                "first_name": "Firstname",
                "last_name": "Lastname",
                "middle_name": "Middlename",
                "prefix": "Ms",
                "suffix": "Dr",
                "contact_number": {
                    "description": "a contact number",
                    "contact_number_type": "personal-mobile-phone",
                    "contact_number": "123-456-7890"
                },
                "email_contact": {
                    "description": "an email address",
                    "digital_contact_type": "personal",
                    "email_address_ref": "email-addr--d80eb6d5-7d01-4cd2-b710-20ac765dc9c5"
                },
                "social_media_accounts": {
                    "description": "a social media account",
                    "digital_contact_type": "personal",
                    "user_account_ref": "user-account--a60d5641-a860-4a86-8ed8-6bbbeaf300e9"
                }
            }
        }

    }

    identity_info = stix2.parse(contact_info_dict)

    assert isinstance(identity_info, stix2.IdentityContactInformation)


