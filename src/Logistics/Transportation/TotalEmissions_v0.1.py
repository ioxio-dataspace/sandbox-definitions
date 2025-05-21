from datetime import date, datetime
from enum import Enum
from typing import Optional, Set

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class IdType(str, Enum):
    WAYBILL_ID = "waybillId"
    DISPATCH_ID = "dispatchId"


class TransportMode(str, Enum):
    AIR = "air"
    RAIL = "rail"
    ROAD = "road"
    SEA = "sea"
    INLAND_WATERWAY = "inland waterway"


class Location(CamelCaseModel):
    city: str = Field(
        ...,
        title="City",
        description="The name of the city.",
        max_length=40,
        examples=["Hamburg"],
    )
    country: str = Field(
        ...,
        title="Country",
        description="The country code in Alpha-2 format.",
        pattern=r"^[A-Z]{2}$",
        examples=["DE"],
    )


class Request(CamelCaseModel):
    id_type: IdType = Field(
        ...,
        title="ID type",
        description="The type of identifier used to query total emissions in the transport chain.",
        examples=[IdType.DISPATCH_ID],
    )
    id: str = Field(
        ...,
        title="ID",
        description="A unique identifier used to track the shipment throughout the entire transport chain, from the origin to the destination.",
        max_length=30,
        examples=["29771_01"],
    )


class Response(CamelCaseModel):
    origin: Location = Field(
        ...,
        title="Origin",
        description="The origin of the transport chain.",
    )
    destination: Location = Field(
        ...,
        title="Destination",
        description="The destination of the transport chain.",
    )
    total_emissions: float = Field(
        ...,
        title="Total emissions (kg of CO2e)",
        description="The total greenhouse gas (GHG) emissions of the transports and logistics hub operations measured in kilograms of CO2e.",
        examples=[5.8],
    )
    calculation_method: str = Field(
        ...,
        title="Calculation method",
        description="A brief description of the method used to calculate the transport emissions.",
        max_length=400,
        examples=[
            "Used primary measured data based on GLEC distance based methodology."
        ],
    )
    distance: Optional[float] = Field(
        None,
        title="Distance (km)",
        description="The distance of the transport chain in kilometers.",
        examples=[484],
    )
    leg_count: Optional[int] = Field(
        None,
        title="Leg count",
        description="The total number of transport legs in the delivery chain, based on changes in the mode of transport.",
        examples=[2],
    )
    transport_modes: list[TransportMode] = Field(
        ...,
        title="Transport modes",
        description="The mode(s) of transport used in the transport chain, reported once per distinct mode as defined by ISO 14083.",
        examples=[[TransportMode.RAIL, TransportMode.ROAD]],
    )
    fossil_share: Optional[float] = Field(
        None,
        title="Fossil share (%)",
        description="The share of emissions from fossil sources, expressed as a percentage of total emissions.",
        gte=0,
        lte=100,
        examples=[25.0],
    )
    biogenic_share: Optional[float] = Field(
        None,
        title="Biogenic share (%)",
        description="The share of emissions from biogenic sources (e.g. biofuels), expressed as a percentage of total emissions.",
        gte=0,
        lte=100,
        examples=[50.0],
    )
    luluc_share: Optional[float] = Field(
        None,
        title="LULUC share (%)",
        description="The share of emissions from land use and land-use change associated with biomass or biofuel production, expressed as a percentage of total emissions.",
        gte=0,
        lte=100,
        examples=[25.0],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Total emissions for a transport chain",
    description="Total emissions for a transport chain compliant with GHG protocol Scope 3 transport emissions.",
    tags=["Logistics"],
    request=Request,
    response=Response,
)
