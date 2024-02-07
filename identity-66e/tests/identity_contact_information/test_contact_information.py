import stix2
import pytest
import stix2.exceptions
from stix2 import Identity
from identity_contact_information.identity_contact_information import (IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID, 
                                                                IdentityContactInformation)

def test_parse_all_props():
    identity_dict = {
        'id': 'identity--32a6ff61-167a-4481-b678-38e20b1989dc',
        'created': '2023-08-06T01:02:00.000Z',
        'modified': '2023-11-16T01:03:01.000Z',
        'spec_version': '2.1',
        'type': 'identity',
        'name': 'Firstname Lastname',
        'description': 'a contact person',
        'identity_class': 'individual',
        'contact_information': '102-030-4050 / f.lastname@address.com',
        'extensions': {
            IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: {
                'extension_type':'property-extension',
                'first_name':'Firstname',
                'last_name':'Lastname',
                'middle_name':'Middlename',
                'prefix':'Ms',
                'suffix':'Dr',
                'contact_numbers': [{
                    'description':'a contact number',
                    'contact_number_type':'personal-mobile-phone',
                    'contact_number':'123-456-7890'
                }],
                'email_addresses': [{
                    "email_address_ref": "email-addr--d80eb6d5-7d01-4cd2-b710-20ac765dc9c5",
                    "digital_contact_type": "personal",
                    "classified": 'false'
                }]
            }
        }
    }
    
    identity = stix2.parse(identity_dict)
    assert isinstance(identity, stix2.Identity)

def test_missing_required_fields():
    with pytest.raises(stix2.exceptions.MissingPropertiesError):
        Identity(
            type="identity",
            name="MissingRequiredFieldsIdentity",
            extensions={
              IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: IdentityContactInformation()  
            }
        )