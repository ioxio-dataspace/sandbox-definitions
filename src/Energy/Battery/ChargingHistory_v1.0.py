from datetime import datetime
from typing import Dict, List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ChargingHistoryRequest(CamelCaseModel):
    serial_number: str = Field(
        ...,
        title="Serial Number",
        description="The serial number of the battery",
        example="MPP48V-296cde7f",
    )
    start: Optional[datetime] = Field(
        None,
        title="Start Time",
        description="Include history entries starting from this time (inclusive)",
        example=datetime.fromisoformat("2022-09-09 00:00:00"),
    )
    end: Optional[datetime] = Field(
        None,
        title="End Time",
        description="Include history entries until this time (exclusive)",
        example=datetime.fromisoformat("2022-09-10 00:00:00"),
    )
    limit: int = Field(
        100,
        ge=1,
        le=100,
        title="Limit",
        description="Limit number of history entries to return",
    )
    offset: int = Field(
        0,
        ge=0,
        title="Offset",
        description="Offset of history records to return",
    )


class ChargingHistoryEntry(CamelCaseModel):
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


class ChargingHistoryResponse(CamelCaseModel):
    battery_charging_history: List[ChargingHistoryEntry] = Field(
        ...,
        title="Battery Charging History",
    )
    total_count: int = Field(
        ...,
        title="Total Count",
        description="Total count of history entries",
        example=1,
    )


DEFINITION = DataProductDefinition(
    version="1.0.0",
    title="Charging history of a battery",
    description="Charging history of a battery",
    request=ChargingHistoryRequest,
    response=ChargingHistoryResponse,
)
