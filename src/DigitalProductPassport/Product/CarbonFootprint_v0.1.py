from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


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
    material_footprint: Optional[float] = Field(
        None,
        title="Material footprint (kg of CO2e)",
        description="The carbon footprint of all materials used for manufacturing the product calculated as kilograms of carbon dioxide equivalents using Product Category Rule (PCR) methods.",
        examples=[4.8],
    )
    processing_footprint: Optional[float] = Field(
        None,
        title="Processing footprint (kg of CO2e)",
        description="The carbon footprint generated from the manufacturing process of the product calculated as kilograms of carbon dioxide equivalents using Product Category Rule (PCR) methods.",
        examples=[5.3],
    )
    logistics_footprint: Optional[float] = Field(
        None,
        title="Logistics footprint (kg of CO2e)",
        description="The carbon footprint generated from the upstream logistics of delivering the product materials to manufacturing calculated as kilograms of carbon dioxide equivalents using Product Category Rule (PCR) methods.",
        examples=[0.3],
    )


DEFINITION = DataProductDefinition(
    version="0.1.1",
    strict_validation=False,
    title="Product carbon footprint",
    description="The carbon footprint of manufacturing a product.",
    tags=["Carbon footprint", "PCR", "Product category rules"],
    request=Request,
    response=Response,
)
