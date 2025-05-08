from datetime import date, datetime
from enum import Enum
from typing import Optional, Set

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ManufacturingLocation(CamelCaseModel):
    country: str = Field(
        ...,
        title="Country",
        description="The country code of the manufacturing location in Alpha-3 format.",
        pattern=r"^[A-Z]{3}$",
        examples=["POL"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        description="The city of the manufacturing location.",
        min_length=0,
        max_length=40,
        examples=["Warsaw"],
    )


class Manufacturer(CamelCaseModel):
    manufacturing_phase: str = Field(
        ...,
        title="Manufacturing phase",
        description="The description of the production phase.",
        min_length=0,
        max_length=40,
        examples=["main production"],
    )
    manufacturer_name: str = Field(
        ...,
        title="Manufacturer name",
        description="The name of the manufacturer of the corresponding phase.",
        min_length=0,
        max_length=40,
        examples=["company x"],
    )
    manufacturing_location: ManufacturingLocation = Field(
        ...,
        title="Manufacturing location",
        description="The details of the manufacturing location.",
    )
    facility_id: Optional[str] = Field(
        None,
        title="Facility ID",
        description="The facility id of the manufacturing site in the GLN format.",
        min_length=0,
        max_length=40,
        examples=["1234567000004"],
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
        description="The unique identifier of the product model, batch or item level.",
        min_length=0,
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


class Response(CamelCaseModel):
    manufacturing_date: date = Field(
        ...,
        title="Manufacturing date",
        description="The date of the garment was manufactured.",
        examples=[date.fromisoformat("2023-01-01")],
    )
    manufacturers: list[Manufacturer] = Field(
        ...,
        title="Manufacturers",
        description="The manufacturer details.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Garment manufacturer information",
    description="Details of the garment manufacturers and facilities.",
    tags=["Manufacturing"],
    request=Request,
    response=Response,
)
