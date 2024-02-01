import stix2
from collections import OrderedDict
from stix2.v21.base import _STIXBase21
from stix2.properties import StringProperty, OpenVocabProperty, DictionaryProperty
from pap import PAP_MARKING_EXTENSION_ID, PapExtension
from vocab import PAP_NAMES, PAP_COLORS

@stix2.v21.CustomObservable(
    'marking-definition', [
        ('name', OpenVocabProperty(PAP_NAMES, required=True)),
        (PAP_MARKING_EXTENSION_ID, PapExtension(
            'pap'
        ))
    ]
)
class PapMarking:
    extension_type = 'property-extension'

test = PapMarking(name="PAP:GREEN", pap="GREEN")
print(test.serialize(pretty=True))
