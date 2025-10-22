from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class RawMaterialEmissions(CamelCaseModel):
    emissions: Optional[float] = Field(
        None,
        title="Emissions (kg of CO2e)",
        description="Raw material emissions for the bag, kilograms of CO2e.",
        examples=[4.8],
    )


class ProcessingEmissions(CamelCaseModel):
    emissions: Optional[float] = Field(
        None,
        title="Emissions (kg of CO2e)",
        description="Processing emissions for the bag, kilograms of CO2e.",
        examples=[3.9],
    )


class TransportEmissions(CamelCaseModel):
    transport_length: Optional[float] = Field(
        None,
        title="Transport length (km)",
        description="Length of the upstream transport, from manufacturer to customer in kilometers.",
        examples=[350],
    )
    fuel_type: Optional[str] = Field(
        None,
        title="Fuel type",
        description="Type of fuel used for the transport.",
        max_length=40,
        examples=["Diesel"],
    )
    emissions: Optional[float] = Field(
        None,
        title="Emissions (kg of CO2e)",
        description="Transport emissions for the bag, kilograms of CO2e.",
        examples=[0.3],
    )


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        max_length=150,
        examples=["FIBC-123"],
    )
    id: str = Field(
        ...,
        title="ID",
        description="The unique bag identifier.",
        max_length=40,
        examples=["123456789"],
    )


class Response(CamelCaseModel):
    carbon_footprint: Optional[float] = Field(
        None,
        title="Carbon footprint (kg of CO2e)",
        description="Manufacturing carbon footprint of the bag, kilograms of CO2e.",
        examples=[4],
    )
    raw_material_emissions: RawMaterialEmissions = Field(
        ...,
        title="Raw material emissions",
        description="Details of emissions from the raw material of the bag.",
    )
    processing_emissions: ProcessingEmissions = Field(
        ...,
        title="Processing emissions",
        description="Details of emissions from the processing and manufacturing of the bag.",
    )
    transport_emissions: TransportEmissions = Field(
        ...,
        title="Transport emissions",
        description="Details of the emissions from the transportation of the bag.",
    )
    circularity_rate: Optional[float] = Field(
        None,
        title="Circularity rate (%)",
        description="The percentage of the FIBC bag made from recycled materials.",
        gte=0,
        lte=100,
        examples=[30],
    )
    is_recyclable: Optional[bool] = Field(
        None,
        title="Is recyclable",
        description="Whether the bag can be recycled or not, depending of its previous usage.",
        examples=[True],
    )
    recycling_instructions: Optional[str] = Field(
        None,
        title="Recycling instructions",
        description="Instructions for recycling the bag after use.",
        max_length=255,
        examples=["Do not burn, recycle at polypropylene (PP) recycling facilities."],
    )
    reuse_policy: Optional[str] = Field(
        None,
        title="Reuse policy",
        description="Instructions for reusability and repairing of the bag.",
        max_length=255,
        examples=[
            "Do not reuse if fabric is severely damaged or has been used for hazardous chemicals."
        ],
    )


DEFINITION = DataProductDefinition(
    version="0.1.2",
    strict_validation=False,
    title="FIBC sustainability data sheet",
    description="Basic sustainability data sheet for FIBC bulk bags.",
    tags=["Environment", "Digital Product Passport"],
    request=Request,
    response=Response,
)
