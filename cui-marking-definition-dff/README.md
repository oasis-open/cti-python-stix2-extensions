# Controlled Unclassified Information (CUI) Data Markings

This is an implementation of the
[CUI data marking extension](https://github.com/oasis-open/cti-stix-common-objects/blob/main/extension-definition-specifications/cui-marking-definition-dff/STIX-2.1-CUI-marking.adoc) for STIX 2.1.

See example marking definitions (JSON) using this extension in the `/examples` subdirectory.

Example Python usage:

```
import stix2
from cui.cui import CUIExtension, CUI_MARKING_EXTENSION_ID


designator = stix2.Identity(name='a CUI designator')
stix2.MarkingDefinition(
    extensions={
        CUI_MARKING_EXTENSION_ID: CUIExtension(
            control='CUI',
            designator_ref=designator.id
        )
    }
)
```

Tests can be run with Tox by executing the `tox` command.
