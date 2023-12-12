from datetime import datetime
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class Status(str, Enum):
    ORIGINAL = "original"
    REPURPOSED = "repurposed"
    RE_USED = "re-used"
    REMANUFACTURED = "remanufactured"
    WASTE = "waste"


class OriginalPerformance(CamelCaseModel):
    capacity: float = Field(
        ...,
        title="Capacity",
        description="The remaining capacity of the battery in ampere-hours (Ah)",
        examples=[80.0],
    )
    power: float = Field(
        ...,
        title="Power",
        description="The original power capability of the battery in watts",
        examples=[20000.0],
    )
    resistance: float = Field(
        ...,
        title="Internal Resistance",
        description="The internal resistance of the battery pack in ohms (Ω)",
    )
    cycle_life: int = Field(
        ...,
        title="Cycle Life",
        description="The expected cycle life of the battery that exceed 80% of the capacity under teh reference conditions for which it has been designed",
        examples=[5000.0],
    )
    calendar_years: int = Field(
        ...,
        title="Calendar Years",
        description="The expected lifetime of the battery in calendar years under the reference conditions for which it has been designed",
    )


class OperationDetail(CamelCaseModel):
    date: datetime = Field(
        ...,
        title="Date",
        description="The date of the data point measurement",
        examples=["2024-05-24"],
    )
    state_of_charge: float = Field(
        ...,
        title="State Of Charge",
        description="The state of charge measured in ampere-hours (Ah)",
        examples=[99.8],
    )
    temperature: float = Field(
        ...,
        title="Temperature",
        description="The temperature of the operating environment measured in celsius degrees",
        examples=[8.0],
        le=100,
        ge=-100,
    )


class HealthState(CamelCaseModel):
    cumulative_cycle_count: int = Field(
        ...,
        title="Cumulative Cycle Count",
        description="The number of charging and discharging cycles of the battery",
        examples=[3500],
    )
    capacity_fade: float = Field(
        ...,
        title="Capacity Fade",
        description="The capacity fade of the battery compared to the original capacity in percentage (%)",
        examples=[20.0],
    )
    power_fade: float = Field(
        ...,
        title="Power Fade",
        description="The power fade pf the battery compared to the original power in percentage (%)",
    )
    resistance_increase: float = Field(
        ...,
        title="Resistance Increase",
        description="The value of resistance increase since the battery was first commissioned in percentage (%)",
    )
    operation_details: List[OperationDetail] = Field(
        ...,
        title="Operation Detail",
        description="periodic information of he battery operation",
    )


class HarmfulEvents(CamelCaseModel):
    date: Optional[datetime] = Field(
        ...,
        title="Date",
        description="The date when the incident or accident happened",
        examples=["2024-02-10"],
    )
    event_description: str = Field(
        ...,
        title="Event Description",
        max_length=250,
        description="The description of the harmful incident that has happened to the battery",
    )


class HealthDataResponse(CamelCaseModel):
    status: Status = Field(
        ...,
        title="Status",
        description="The status of the battery based on its history use",
        examples=[Status.ORIGINAL],
    )
    manufacturing_date: str = Field(
        ...,
        title="Manufacturing Date",
        description="The date of manufacture using month and year",
        patterns=[r"^\d{4}-\d{2}$"],
        examples=["2023-07"],
    )
    service_initiation_date: Optional[str] = Field(
        None,
        title="Service Initiation Date",
        description="The date on which the battery was first commissioned",
        patterns=[r"^\d{4}-\d{2}$"],
        examples=["2023-12"],
    )
    original_performance: OriginalPerformance = Field(
        ...,
        title="Original Performance",
        description="The details of the original performance of the battery",
    )
    health_state: HealthState = Field(
        ...,
        title="Health State",
        description="The state of the health of the battery",
    )
    harmful_events: List[HarmfulEvents] = Field(
        ...,
        title="Harmful Events",
        description="The harmful events or incidents that have occurred for the battery",
    )


class HealthDataRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type",
        examples=["sodium-ion-75kWh"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["660e8400-e29b-41d4-a716-446655440000"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Battery Health Data",
    description="The health and status data of a battery as required by Battery Passport specification of the European Commission's Battery Act (2023/1542)",
    request=HealthDataRequest,
    response=HealthDataResponse,
)
