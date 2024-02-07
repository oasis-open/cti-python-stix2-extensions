This is an implementation of the [Identity Contact Information Extension](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/identity-66e/Identity Contact Information.adoc) for STIX 2.1. 

See example Identity Contact definitions (JSON) using this extension in the `/examples` subdirectory.

Example Python usage:

`import stix2
from identity_contact_information.identity_contact_information import (IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID, 
                                                                IdentityContactInformation, ContactNumber)

identity_extension = stix2.Identity(
    type="identity",
    name="MissingRequiredPropertyIdentity",
    extensions={
        IDENTITY_CONTACT_INFORMATION_EXTENSION_DEFINITION_ID: IdentityContactInformation(
            first_name="FIrstname",
            last_name="Lastname",
            contact_numbers=[{
                'contact_number_type': 'personal-mobile-phone',
                'contact_number': '123-456-7890'
            }]
        )  
    }
)`

Tests can be run with Tox by executing the `tox` command.