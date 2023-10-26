from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class FreightType(str, Enum):
    PALLETIZED = "Palletized"
    DRY_BULK = "Dry bulk"
    LIQUID_BULK = "Liquid bulk"
    CONTAINERIZED = "Containerized"
    VEHICLE_TRANSPORT = "Vehicle transport"
    HEAVY_CARGO = "Heavy cargo"
    LIGHT_CARGO = "Light cargo"


class RoadLegFreightCondition(str, Enum):
    AMBIENT = "Ambient"
    TEMPERATURE_CONTROLLED = "Temperature-controlled"


class SeaLegFreightCondition(str, Enum):
    AMBIENT = "Ambient"
    TEMPERATURE_CONTROLLED = "Temperature-controlled"
    MIXED = "Mixed ambient and temperature-controlled"


class JourneyType(str, Enum):
    LONG_HAUL = "Long-haul"
    COLLECTION_AND_DELIVERY = "Collection and delivery"


class ContractType(str, Enum):
    SHARED_TRANSPORT = "Shared transport"
    DEDICATED_CONTRACT = "Dedicated contract"


class ServiceType(str, Enum):
    SCHEDULED = "Scheduled"
    TRAMP = "Tramp"


class VesselType(str, Enum):
    BULK_CARRIER = "Bulk carrier"
    CHEMICAL_TANKER = "Chemical tanker"
    GENERAL_CARGO = "General cargo"
    RO_RO = "Ro-Ro"
    LIQUEFIED_GAS_TANKER = "Liquefied gas tanker"
    OIL_TANKER = "Oil tanker"
    OTHER_LIQUEFIED_TANKER = "Other liquefied tanker"
    CONTAINER = "Container"
    VEHICLE_CARRIER = "Vehicle carrier"


class EmissionsPerTCE(CamelCaseModel):
    description: Optional[str] = Field(
        None,
        max_length=250,
        title="Description",
        description="The description of the transport chain element (TCE) related to the leg",
        example="Loading for road transport",
    )
    emissions: Optional[float] = Field(
        None,
        title="Emissions",
        description="The green house gas (GHG) emissions of the transport "
        "chain element related to the road tranport leg in CO2e tonnes",
        example=1.2,
    )
    source_for_the_emissions: Optional[str] = Field(
        None,
        max_length=250,
        title="Source For The Emissions",
        description="The source that generated the emission in the TCE",
        example="Diesel",
    )


class RoadLeg(CamelCaseModel):
    leg_identifier: Optional[str] = Field(
        None,
        max_length=20,
        description="The leg identifier",
        example="7623456365",
    )
    origin: Optional[str] = Field(
        None,
        max_length=250,
        title="Origin",
        description="The location of the transport origin",
        example="Tampere",
    )
    destination: Optional[str] = Field(
        None,
        max_length=250,
        title="Destination",
        description="The location of the transport destination",
        example="Turku",
    )
    freight_type: Optional[FreightType] = Field(
        None,
        title="Freight Type",
        description="The type of the freight used for the road transport",
        example=FreightType.PALLETIZED,
    )
    condition: Optional[RoadLegFreightCondition] = Field(
        None,
        title="Condition",
        description="The conditions that the cargo is being transported with",
        example=RoadLegFreightCondition.AMBIENT,
    )
    journey_type: Optional[JourneyType] = Field(
        None,
        title="Journey Type",
        description="The type of the road transport",
        example=JourneyType.LONG_HAUL,
    )
    contract_type: Optional[ContractType] = Field(
        None,
        title="Contract Type",
        description="The type of the transport contract",
        example=ContractType.DEDICATED_CONTRACT,
    )
    total_emissions_per_leg: Optional[float] = Field(
        None,
        title="Total Emissions",
        description="The total green house gas (GHG) emissions of the road transport "
        "and other related logistics hub operations measured in CO2e tonnes",
        example=5.8,
    )
    emission_intensity: Optional[float] = Field(
        None,
        title="Emission Intensity",
        description="The GHG emission intensity of the road transport "
        "per transported tonne and kilometer in CO2e grams / tonne / km",
        example=200,
    )
    emissions_per_tce: List[EmissionsPerTCE] = Field(
        None,
        title="Emissions per TCE",
        description="The GHG emissions of the transport chain element related to the road transport leg",
    )


class SeaLeg(CamelCaseModel):
    leg_identifier: Optional[str] = Field(
        None,
        max_length=20,
        description="The leg identifier",
        example="7623456365",
    )
    origin: Optional[str] = Field(
        None,
        max_length=250,
        title="Origin",
        description="The location of the transport origin",
        example="Turku",
    )
    destination: Optional[str] = Field(
        None,
        max_length=250,
        title="Destination",
        description="The location of the transport destination",
        example="Stockholm",
    )
    vessel_type: Optional[VesselType] = Field(
        None,
        title="Vessel Type",
        description="The type of the vessel used for the sea transport",
        example=VesselType.RO_RO,
    )
    freight_condition: Optional[SeaLegFreightCondition] = Field(
        None,
        title="Freight Condition",
        description="The conditions that the cargo is being transported with",
        example=SeaLegFreightCondition.TEMPERATURE_CONTROLLED,
    )
    service_type: Optional[ServiceType] = Field(
        None,
        title="Service Type",
        description="The type of the sea transport service",
        example=ServiceType.SCHEDULED,
    )
    total_emissions: Optional[float] = Field(
        None,
        title="Total Emissions",
        description="The total green house gas (GHG) emissions of the road "
        "transport and other related logistics hub operations measured in CO2e tonnes",
        example=7.4,
    )
    emission_intensity: Optional[float] = Field(
        None,
        title="Emission Intensity",
        description="The GHG emission intensity of the sea transport per "
        "transported tonne and kilometer in CO2e grams / tonne / km",
        example=500,
    )
    emissions_per_tce: List[EmissionsPerTCE] = Field(
        None,
        title="Emissions per TCE",
        description="The GHG emissions of the transport chain element related to the road transport leg",
    )


class LogisticsEmissionsDataRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product identifier",
        description="Technical product identifier used by the manufacturer",
        example="battery-100wh-s",
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier for the product",
        example="177389-09633",
    )


class LogisticsEmissionsDataResponse(CamelCaseModel):
    road_freight_emissions: List[RoadLeg] = Field(
        None,
        title="Road Freight Emissions",
    )
    sea_freight_emissions: List[SeaLeg] = Field(
        None,
        title="Sea Freight Emissions",
    )
    waybill_number: str = Field(
        ...,
        title="Waybill Number",
        description="The unique identifier which is used to "
        "track a shipment through the entire delivery chain",
        example="5308956234",
        max_length=20,
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Logistics Emissions",
    description="Returns the total emission per leg for "
    "an end-to-end shipment compliant with the European "
    "Union's count emissions reporting regulation",
    request=LogisticsEmissionsDataRequest,
    response=LogisticsEmissionsDataResponse,
    requires_authorization=False,
    requires_consent=False,
)