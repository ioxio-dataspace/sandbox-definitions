from datetime import date
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Event(CamelCaseModel):
    event_date: Optional[date] = Field(
        None,
        title="Event date",
        description="The date of the event.",
        examples=[date.fromisoformat("2024-02-10")],
    )
    event_description: Optional[str] = Field(
        None,
        title="Event description",
        description="The description of the event related to the garment.",
        min_length=0,
        max_length=250,
        examples=["Stitched a hole in the left arm"],
    )


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        min_length=0,
        max_length=150,
        examples=["model-x-1234"],
    )
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the product, batch or item level.",
        min_length=0,
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


class Response(CamelCaseModel):
    commissioning_date: date = Field(
        ...,
        title="Commissioning date",
        description="The date when the garment was delivered to the customer.",
        examples=[date.fromisoformat("2023-06-01")],
    )
    washing_cycles: int = Field(
        ...,
        title="Washing cycles",
        description="The number of times the garment has been washed according to the instructions.",
        examples=[10],
    )
    repair_events: list[Event] = Field(
        ...,
        title="Repair events",
        description="The list of the repair events done for the garment.",
    )
    harmful_events: list[Event] = Field(
        ...,
        title="Harmful events",
        description="The list of harmful events the garment has been exposed to which have an effect on the repairability and recyclability.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Garment maintenance log",
    description="Details of the garment's care, repair and incidents.",
    tags=["Manufacturing"],
    request=Request,
    response=Response,
)
