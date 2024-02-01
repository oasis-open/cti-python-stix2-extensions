import stix2
from collections import OrderedDict
from stix2.v21.base import _STIXBase21
from stix2.properties import StringProperty, OpenVocabProperty, DictionaryProperty
from vocab import PAP_COLORS

PAP_MARKING_EXTENSION_ID = 'extension-definition--f8d78575-edfd-406e-8e84-6162a8450f5b'

@stix2.v21.CustomExtension(
    PAP_MARKING_EXTENSION_ID, [
        ('pap', OpenVocabProperty(PAP_COLORS, required=True))
    ]
)

class PapExtension:
    extension_type = 'property-extension'