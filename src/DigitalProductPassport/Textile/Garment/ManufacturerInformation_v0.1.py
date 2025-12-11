from datetime import date
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class ManufacturingPhase(str, Enum):
    MAIN_PRODUCTION = "main production"
    SEWING = "sewing"
    FINISHING = "finishing"
    ASSEMBLY = "assembly"
    COMPONENT_SUPPLIER = "component supplier"


class ManufacturingLocation(CamelCaseModel):
    country: str = Field(
        ...,
        title="Country",
        description="The country code of the manufacturing location in ISO 3166-1 alpha-3 format.",
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

    model_config: ConfigDict = ConfigDict(title="Manufacturing location")


class Manufacturer(CamelCaseModel):
    manufacturing_phase: ManufacturingPhase = Field(
        ...,
        title="Manufacturing phase",
        description="The description of the production phase.",
        examples=[ManufacturingPhase.MAIN_PRODUCTION],
    )
    manufacturing_date: date = Field(
        ...,
        title="Manufacturing date",
        description="The date of the garment was manufactured in ISO 8601 format.",
        examples=[date.fromisoformat("2023-01-01")],
    )
    manufacturer_name: str = Field(
        ...,
        title="Manufacturer name",
        description="The name of the manufacturer of the corresponding phase.",
        min_length=0,
        max_length=40,
        examples=["Acme manufacturing Oy"],
    )
    manufacturing_location: ManufacturingLocation = Field(
        ...,
        title="Manufacturing location",
        description="The details of the manufacturing location.",
    )
    facility_id: Optional[str] = Field(
        None,
        title="Facility ID",
        description="The facility ID of the manufacturing site in the GLN format.",
        min_length=0,
        max_length=40,
        examples=["1234567000004"],
    )

    model_config: ConfigDict = ConfigDict(title="Manufacturer")


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

    model_config: ConfigDict = ConfigDict(title="Request")


class Response(CamelCaseModel):
    manufacturers: list[Manufacturer] = Field(
        ...,
        title="Manufacturers",
        description="The manufacturer details.",
    )

    model_config: ConfigDict = ConfigDict(title="Response")


DEFINITION = DataProductDefinition(
    version="0.1.3",
    strict_validation=False,
    title="Garment manufacturer information",
    description="Details of the garment manufacturers and facilities.",
    tags=["Manufacturing"],
    request=Request,
    response=Response,
)
