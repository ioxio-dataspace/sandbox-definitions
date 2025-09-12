import datetime
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Status(str, Enum):
    ORIGINAL = "original"
    REPURPOSED = "repurposed"
    REUSED = "reused"
    REMANUFACTURED = "remanufactured"
    WASTE = "waste"


class OriginalPerformance(CamelCaseModel):
    capacity: Optional[float] = Field(
        None,
        title="Capacity (Ah)",
        description="The remaining capacity of the battery in ampere-hours.",
        examples=[80.0],
    )
    power: Optional[float] = Field(
        None,
        title="Power (W)",
        description="The original power capability of the battery in watts.",
        examples=[20000.0],
    )
    resistance: Optional[float] = Field(
        None,
        title="Internal resistance (Ω)",
        description="The internal resistance of the battery pack in ohms.",
        examples=[0.005],
    )
    cycle_life: Optional[int] = Field(
        None,
        title="Cycle life",
        ge=0,
        description="The expected cycle life of the battery that exceed 80% of the "
        "capacity under the reference conditions for which it has been designed.",
        examples=[5000],
    )
    years: Optional[int] = Field(
        None,
        title="Years",
        description="The expected lifetime of the battery in years under the reference "
        "conditions for which it has been designed.",
        examples=[10],
    )


class OperationDetail(CamelCaseModel):
    measurement_date: Optional[datetime.date] = Field(
        None,
        title="Measurement date",
        description="The date of the data point measurement.",
        examples=[datetime.date(2024, 5, 24)],
    )
    state_of_charge: Optional[float] = Field(
        None,
        title="Charge (Ah)",
        description="The state of charge measured in ampere-hours.",
        ge=0.0,
        examples=[99.8],
    )
    charge_percentage: Optional[float] = Field(
        None,
        title="Charge (%)",
        description="The state of charge measured in percentages.",
        ge=0.0,
        le=100.0,
        examples=[81.8],
    )
    temperature: Optional[float] = Field(
        None,
        title="Temperature (C°)",
        description="The temperature of the battery measured in Celsius degrees.",
        examples=[40.0],
    )


class HealthState(CamelCaseModel):
    cumulative_cycle_count: Optional[int] = Field(
        None,
        title="Cumulative cycle count",
        description="The number of charging and discharging cycles of the battery.",
        examples=[3500],
    )
    capacity_fade: Optional[float] = Field(
        None,
        title="Capacity fade (%)",
        description="The capacity fade of the battery compared to the original "
        "capacity in percentage.",
        examples=[20.0],
    )
    power_fade: Optional[float] = Field(
        None,
        title="Power fade (%)",
        description="The power fade of the battery compared to the original power in "
        "percentage.",
        examples=[15.0],
    )
    resistance_increase: Optional[float] = Field(
        None,
        title="Resistance increase (%)",
        description="The value of resistance increase since the battery was first "
        "commissioned in percentage.",
        examples=[10.0],
    )
    actual_current: Optional[float] = Field(
        None,
        title="Actual current (A)",
        description="The actual current of the battery in amperes.",
        examples=[10.0],
    )
    actual_power: Optional[float] = Field(
        None,
        title="Actual power (W)",
        description="The actual power of the battery in watts.",
        examples=[1.0],
    )
    actual_voltage: Optional[float] = Field(
        None,
        title="Actual voltage (V)",
        description="The actual voltage of the battery in volts.",
        examples=[10.0],
    )
    operation_details: List[OperationDetail] = Field(
        ...,
        title="Operation details",
        description="The periodic information of the battery operation.",
    )


class HarmfulEvent(CamelCaseModel):
    event_date: Optional[datetime.date] = Field(
        ...,
        title="Event date",
        description="The date when the incident or accident happened.",
        examples=[datetime.date(2024, 2, 10)],
    )
    event_description: Optional[str] = Field(
        None,
        title="Event description",
        max_length=250,
        description="The description of the harmful incident that has happened to the "
        "battery.",
        examples=["30 minutes spent in extreme temperature -50 Celsius"],
    )


class HealthDataResponse(CamelCaseModel):
    status: Optional[Status] = Field(
        None,
        title="Status",
        description="The status of the battery based on its history of use.",
        examples=[Status.ORIGINAL],
    )
    manufacturing_date: Optional[str] = Field(
        None,
        title="Manufacturing date",
        description="The date of manufacture using month and year.",
        pattern=r"^\d{4}-(0[1-9]|1[0-2])$",
        examples=["2023-07"],
    )
    service_initiation_date: Optional[str] = Field(
        None,
        title="Service initiation date",
        description="The date on which the battery was first commissioned.",
        pattern=r"^\d{4}-(0[1-9]|1[0-2])$",
        examples=["2023-12"],
    )
    original_performance: Optional[OriginalPerformance] = Field(
        None,
        title="Original performance",
        description="The details of the original performance of the battery.",
    )
    health_state: Optional[HealthState] = Field(
        None,
        title="Health state",
        description="The state of the health of the battery.",
    )
    harmful_events: List[HarmfulEvent] = Field(
        ...,
        title="Harmful events",
        description="The harmful events or incidents that have occurred for the "
        "battery.",
    )


class HealthDataRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["sodium-ion-75kWh"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product.",
        examples=["660e8400-e29b-41d4-a716-446655440000"],
    )


DEFINITION = DataProductDefinition(
    version="0.2.2",
    strict_validation=False,
    title="Battery health data",
    description="The health and status data of a battery as required by Battery "
    "Passport specification of the European Commission's Battery Act (2023/1542).",
    tags=["Digital Product Passport", "Battery"],
    request=HealthDataRequest,
    response=HealthDataResponse,
)
