This is an implementation of the [PAP Data Marking Extension](https://github.com/oasis-open/cti-stix-common-objects/tree/main/extension-definition-specifications/pap-f8d/STIX-2.1-PAP-marking-defintion.adoc) for STIX 2.1.

See example PAP definitions (JSON) using this extension in the `/examples` subdirectory.

Example Python usage:

```
import stix2
from pap.pap import (PAPMarkingDefinition, PAPMarkingDefinitionError, 
                PAP_MARKING_EXTENSION_ID, PAPExtension)

pap_marking = PAPMarkingDefinition(
    id='marking-definition--60f8932b-e51e-4458-b265-a2e8be9a80ab',
    created="2022-10-02T00:00:00.000Z",
    name="PAP:AMBER",
    extensions={
        PAP_MARKING_EXTENSION_ID:{
            'pap':'amber'
        }
    }
)
```

Tests can be run with Tox by executing the `tox` command.