from collections import OrderedDict

import stix2
from stix2.exceptions import InvalidValueError, ObjectConfigurationError
from stix2.properties import (EnumProperty, FloatProperty, IntegerProperty,
                              ListProperty, OpenVocabProperty,
                              ReferenceProperty, StringProperty,
                              TimestampProperty)

import incident.vocab as vocab
from .common import EntityCountProperty
from .util import check_open_bounds


@stix2.CustomExtension(
    applies_to="sdo",
    type="availability-ext",
    properties=OrderedDict([
        # required properties
        ('availability_impact', IntegerProperty(min=0, max=100, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
    ])
)
class AvailabilityImpactExt:
    pass


@stix2.CustomExtension(
    applies_to="sdo",
    type="confidentiality-ext",
    properties=OrderedDict([
        # required properties
        ('loss_type', EnumProperty(vocab.CONFIDENTIALITY_LOSS, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
        # optional properties
        ('information_type', OpenVocabProperty(vocab.INFORMATION_TYPE)),
        ('record_count', IntegerProperty(min=0)),
        ('record_size', IntegerProperty(min=0)),
    ])
)
class ConfidentialityImpactExt:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        loss_type = self.get('loss_type')

        if loss_type != 'none' and "information_type" not in self:
            msg = 'Information type required if loss_type is not "none"'
            raise ObjectConfigurationError(msg)


@stix2.CustomExtension(
    applies_to="sdo",
    type="external-ext",
    properties=OrderedDict([
        # required properties
        ('impact_type', OpenVocabProperty(vocab.EXTERNAL_IMPACT, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
    ])
)
class ExternalImpactExt:
    pass


@stix2.CustomExtension(
    applies_to="sdo",
    type="integrity-ext",
    properties=OrderedDict([
        # required properties
        ('alteration', EnumProperty(vocab.INTEGRITY_ALTERATION, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
        # optional properties
        ('information_type', OpenVocabProperty(vocab.INFORMATION_TYPE)),
        ('record_count', IntegerProperty(min=0)),
        ('record_size', IntegerProperty(min=0)),
    ])
)
class IntegrityImpactExt:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        alteration = self.get('alteration')
        if alteration != 'none' and "information_type" not in self:
            msg = 'Information type required if alteration is not "none"'
            raise ObjectConfigurationError(msg)


@stix2.CustomExtension(
    applies_to="sdo",
    type="economic-ext",
    properties=OrderedDict([
        # required properties
        ('variety', OpenVocabProperty(vocab.ECONOMIC_IMPACT, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
        # optional properties
        ('conversion_rate', FloatProperty()),
        ('conversion_time', TimestampProperty()),
        ('currency', StringProperty()),
        ('currency_actual', StringProperty()),
        ('max_amount', FloatProperty()),
        ('min_amount', FloatProperty())
    ])
)
class EconomicImpactExt:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        # Based on these requirements from the schema:
        #
        # "dependentRequired": {
        #     "$comment": "'not currency_actual implies not conversion_rate' not specified here, but is in the spec",
        #     "min_amount": ["currency", "max_amount"],
        #     "currency_actual": ["currency", "conversion_rate"],
        #     "conversion_rate": ["conversion_time"]
        # }

        self._check_properties_dependency(
            [
                "currency", "max_amount"
            ],
            ["min_amount"]
        )
        self._check_properties_dependency(
            [
                "currency", "conversion_rate"
            ],
            ["currency_actual"]
        )
        self._check_properties_dependency(
            [
                "conversion_time"
            ],
            ["conversion_rate"]
        )

        conversion_rate = self.get("conversion_rate")
        if conversion_rate is not None:
            check_open_bounds(
                self.__class__, "conversion_rate", conversion_rate,
                min_exc=0
            )

        max_amount = self.get("max_amount")
        if max_amount is not None:
            check_open_bounds(
                self.__class__, "max_amount", max_amount,
                min_exc=0
            )

        min_amount = self.get("min_amount")
        if min_amount is not None:
            check_open_bounds(
                self.__class__, "min_amount", min_amount,
                min_exc=0
            )

        if min_amount is not None and max_amount is not None:
            if min_amount > max_amount:
                raise ObjectConfigurationError(
                    "monetary impact min_amount is greater than max_amount:"
                    " {} > {}".format(min_amount, max_amount)
                )


@stix2.CustomExtension(
    applies_to="sdo",
    type="physical-ext",
    properties=OrderedDict([
        # required properties
        ('impact_type', EnumProperty(vocab.PHYSICAL_IMPACT, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
        # optional properties
        ('asset_type', OpenVocabProperty(vocab.ASSET_TYPE))
    ])
)
class PhysicalImpactExt:
    def _check_object_constraints(self):
        super()._check_object_constraints()
        impact_type = self.get('impact_type')
        if impact_type != 'none' and "asset_type" not in self:
            msg = 'asset_type required if impact_type is not "none"'
            raise ObjectConfigurationError(msg)


@stix2.CustomExtension(
    applies_to="sdo",
    type="traceability-ext",
    properties=OrderedDict([
        # required properties
        ('traceability_impact', EnumProperty(vocab.TRACEABILITY_IMPACT, required=True)),
        ('extension_type', StringProperty(fixed=None)),  # needed to indicate it's a sub object extension
    ])
)
class TraceabilityImpactExt:
    pass


# Impact Extension Data
IMPACT_EXTENSION_DEFINITION_ID = 'extension-definition--7cc33dd6-f6a1-489b-98ea-522d351d71b9'


@stix2.CustomObject(
    'impact',
    [
        # required properties
        ('impact_category', StringProperty()),
        # optional properties
        ('criticality', IntegerProperty(min=0, max=100)),
        ('description', StringProperty()),
        ('end_time', TimestampProperty()),
        ('end_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY)),
        ('impacted_entity_counts', EntityCountProperty(spec_version="2.1")),
        ('impacted_refs', ListProperty(ReferenceProperty(valid_types=["SCO", "SDO"]))),
        ('recoverability', EnumProperty(vocab.RECOVERABILITY)),
        ('start_time', TimestampProperty()),
        ('start_time_fidelity', EnumProperty(vocab.TIMESTAMP_FIDELITY)),
        ('sub_impact_refs', ListProperty(ReferenceProperty(valid_types='impact'))),
        ('superseded_by_ref', ReferenceProperty(valid_types='impact'))
    ],
    IMPACT_EXTENSION_DEFINITION_ID
)
class Impact:
    def _check_object_constraints(self):
        super()._check_object_constraints()

        self._check_properties_dependency(["end_time"], ["superseded_by_ref"])

        start_time = self.get('start_time')
        end_time = self.get('end_time')

        if start_time is not None and end_time is not None:
            if start_time > end_time:
                raise ObjectConfigurationError(
                    'impact start time is equal to or later than end time:'
                    ' {} > {}'.format(start_time, end_time)
                )

        impact_category = self["impact_category"]
        if impact_category and impact_category + "-ext" not in self.get("extensions"):
            raise InvalidValueError(
                self.__class__, "impact_category",
                "must match the name of one of this object's impact"
                " extensions: " + impact_category
            )
