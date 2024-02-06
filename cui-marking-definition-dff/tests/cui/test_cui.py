import os

import pytest
import stix2

from cui.cui import CUIExtension, CUI_MARKING_EXTENSION_ID


def test_all_props():
    designator = stix2.Identity(name='a CUI designator')
    stix2.MarkingDefinition(
        extensions={
            CUI_MARKING_EXTENSION_ID: CUIExtension(
                control='CUI',
                categories=["SP-SSEL", "SBIZ"],
                disseminations=["NOFORN", "NOCON"],
                designator_ref=designator.id,
                required_statements=["MARKING REQUIRED BY AUTHORITY"],
                supplemental_administrative=["Draft"],
            )
        }
    )


@pytest.mark.parametrize(
    "input_file", [
        "banner.json",
        "basic.json",
        "categories.json",
        "supplemental.json",
    ]
)
def test_parse_props(input_file):
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           '../../examples', input_file)
    with open(filepath) as content:
        marking = stix2.parse(content)

    assert isinstance(marking, stix2.MarkingDefinition)
    assert isinstance(
        marking.extensions[CUI_MARKING_EXTENSION_ID],
        CUIExtension
    )


def test_missing_props():
    with pytest.raises(stix2.exceptions.MissingPropertiesError):
        stix2.MarkingDefinition(
            extensions={
                CUI_MARKING_EXTENSION_ID: CUIExtension(
                    categories=["SBIZ"],
                )
            }
        )
