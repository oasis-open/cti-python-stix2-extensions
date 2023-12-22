import pytest
import stix2
from stix2.exceptions import (DependentPropertiesError, InvalidValueError,
                              ObjectConfigurationError)

import incident.vocab as vocab
from incident.impact import (AvailabilityImpactExt, ConfidentialityImpactExt,
                         Impact, IntegrityImpactExt, MonetaryImpactExt,
                         PhysicalImpactExt)


def test_all_props():
    # Just ensure no exceptions are raised
    Impact(
        impact_category="availability-ext",
        criticality=50,
        description="impact description",
        start_time="1982-04-27T19:46:14.234234Z",
        start_time_fidelity="year",
        end_time="1983-03-02T02:59:43.35Z",
        end_time_fidelity="month",
        impacted_entity_counts={"a": 1},
        impacted_refs=[
            "file--b2305fb4-0253-4589-b84d-e96e06acfabc",
            "threat-actor--1f4117f3-06d0-4498-9b11-fa1c0b7cb083"
        ],
        recoverability="regular",
        superseded_by_ref="impact--762048c4-3b3e-4eb2-b435-f69695ecf52d",
        extensions={
            "availability-ext": AvailabilityImpactExt(
                availability_impact=25
            )
        }
    )


def test_parse_all_props():
    imp_dict = {
        "type": "impact",
        "spec_version": "2.1",
        "id": "impact--298c3679-475b-4098-8d60-e61b38a50e96",
        "created": "1986-01-08T08:52:02.252Z",
        "modified": "1998-08-18T12:05:06.49212Z",
        "impact_category": "availability-ext",
        "criticality": 50,
        "description": "impact description",
        "start_time": "1982-04-27T19:46:14.234234Z",
        "start_time_fidelity": "year",
        "end_time": "1983-03-02T02:59:43.35Z",
        "end_time_fidelity": "month",
        "impacted_entity_counts": {"a": 1},
        "impacted_refs": [
            "file--b2305fb4-0253-4589-b84d-e96e06acfabc",
            "threat-actor--1f4117f3-06d0-4498-9b11-fa1c0b7cb083"
        ],
        "recoverability": "regular",
        "superseded_by_ref": "impact--762048c4-3b3e-4eb2-b435-f69695ecf52d",
        "extensions": {
            "availability-ext": {
                "availability_impact": 25
            }
        }
    }

    imp = stix2.parse(imp_dict)

    # Ensure types were resolvable to classes
    assert isinstance(imp, Impact)
    assert isinstance(
        imp.extensions["availability-ext"], AvailabilityImpactExt
    )


def test_bad_category():
    with pytest.raises(InvalidValueError):
        Impact(
            impact_category="does_not_exist"
        )

    with pytest.raises(InvalidValueError):
        Impact(
            impact_category="does_not_exist",
            extensions={
                "availability-ext": AvailabilityImpactExt(
                    availability_impact=25
                )
            }
        )


@pytest.mark.parametrize(
    "entity_count", [
        {"a": "1"},
        {"a": 1.5},
        {}
    ]
)
def test_entity_count_error(entity_count):
    with pytest.raises(InvalidValueError):
        Impact(
            impact_category="availability-ext",
            impacted_entity_counts=entity_count,
            extensions={
                "availability-ext": AvailabilityImpactExt(
                    availability_impact=25
                )
            }
        )


def test_superseded_by_ref_dependency():
    with pytest.raises(DependentPropertiesError):
        Impact(
            impact_category="availability-ext",
            # When superseded_by_ref is present, the impact MUST have an
            # end_time.
            superseded_by_ref="impact--762048c4-3b3e-4eb2-b435-f69695ecf52d",
            extensions={
                "availability-ext": AvailabilityImpactExt(
                    availability_impact=25
                )
            }
        )


def test_confidentiality_impact_information_type_dependency():
    with pytest.raises(ObjectConfigurationError):
        ConfidentialityImpactExt(
            loss_type=vocab.CONFIDENTIALITY_LOSS_CONTAINED
        )

    ConfidentialityImpactExt(
        loss_type=vocab.CONFIDENTIALITY_LOSS_NONE
    )


def test_confidentiality_impact_record_count():
    with pytest.raises(InvalidValueError):
        ConfidentialityImpactExt(
            loss_type=vocab.CONFIDENTIALITY_LOSS_CONTAINED,
            information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
            record_count=-1
        )

    ConfidentialityImpactExt(
        loss_type=vocab.CONFIDENTIALITY_LOSS_CONTAINED,
        information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
        record_count=0
    )


def test_confidentiality_impact_record_size():
    with pytest.raises(InvalidValueError):
        ConfidentialityImpactExt(
            loss_type=vocab.CONFIDENTIALITY_LOSS_CONTAINED,
            information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
            record_size=-1
        )

    ConfidentialityImpactExt(
        loss_type=vocab.CONFIDENTIALITY_LOSS_CONTAINED,
        information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
        record_size=0
    )


def test_integrity_impact_information_type_dependency():
    with pytest.raises(ObjectConfigurationError):
        IntegrityImpactExt(
            alteration=vocab.INTEGRITY_ALTERATION_FULL_MODIFICATION
        )

    IntegrityImpactExt(
        alteration=vocab.INTEGRITY_ALTERATION_NONE
    )


def test_integrity_impact_record_count():
    with pytest.raises(InvalidValueError):
        IntegrityImpactExt(
            alteration=vocab.INTEGRITY_ALTERATION_FULL_MODIFICATION,
            information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
            record_count=-1
        )

    IntegrityImpactExt(
        alteration=vocab.INTEGRITY_ALTERATION_FULL_MODIFICATION,
        information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
        record_count=0
    )


def test_integrity_impact_record_size():
    with pytest.raises(InvalidValueError):
        IntegrityImpactExt(
            alteration=vocab.INTEGRITY_ALTERATION_FULL_MODIFICATION,
            information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
            record_size=-1
        )

    IntegrityImpactExt(
        alteration=vocab.INTEGRITY_ALTERATION_FULL_MODIFICATION,
        information_type=vocab.INFORMATION_TYPE_PROPRIETARY,
        record_size=0
    )


def test_monetary_impact_minimal():
    # Just ensure no crashes
    MonetaryImpactExt(
        variety=vocab.MONETARY_IMPACT_RANSOM_DEMAND
    )


def test_monetary_impact_maximal():
    # Just ensure no crashes
    MonetaryImpactExt(
        variety=vocab.MONETARY_IMPACT_RANSOM_DEMAND,
        conversion_rate=1.4,
        conversion_time="2001-03-04T23:12:02.34562Z",
        currency="ABC",
        currency_actual="DEF",
        max_amount=1.2,
        min_amount=3.4
    )


def test_monetary_impact_dependency_min_amount():
    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            min_amount=10000
        )

    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            min_amount=10000,
            max_amount=20000
        )

    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            min_amount=10000,
            currency="USD"
        )


def test_monetary_impact_dependency_max_amount():
    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            max_amount=10000
        )

    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            max_amount=10000,
            currency="USD"
        )


def test_monetary_impact_dependency_conversion_rate():
    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            max_amount=10000,
            conversion_rate=3.2
        )


def test_monetary_impact_dependency_currency_actual():
    with pytest.raises(DependentPropertiesError):
        MonetaryImpactExt(
            variety=vocab.MONETARY_IMPACT_BRAND_DAMAGE,
            max_amount=10000,
            currency_actual="XYZ"
        )


def test_physical_impact_dependency_asset_type():
    with pytest.raises(ObjectConfigurationError):
        PhysicalImpactExt(
            impact_type=vocab.PHYSICAL_IMPACT_DESTRUCTION
        )

    PhysicalImpactExt(
        impact_type=vocab.PHYSICAL_IMPACT_NONE
    )
