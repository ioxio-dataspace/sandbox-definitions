from datetime import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class LatestChargingEntryRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product identifier",
        description="Technical product identifier used by the manufacturer",
        example="battery-100wh-s",
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier of the product",
        example="177389-09633",
    )


class LatestChargingEntryResponse(CamelCaseModel):
    time: datetime = Field(
        ...,
        title="Time",
        description="Time of the charging history event",
        example=datetime.fromisoformat("2022-09-10 00:00:00"),
    )
    operating_hours: float = Field(
        ...,
        title="Operating Hours [h]",
        description="The cumulative operating hours of the battery",
        example=428.7,
    )
    cycle_count: int = Field(
        ...,
        title="Cycle Count",
        description="The cycle count of the battery",
        example=15,
    )
    max_capacity: float = Field(
        ...,
        title="Maximum Capacity [Ah]",
        description="The maximum capacity of the battery",
        example=46.0,
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Last Charge Entry",
    description="Information about latest charge cycle of a battery",
    request=LatestChargingEntryRequest,
    response=LatestChargingEntryResponse,
)
