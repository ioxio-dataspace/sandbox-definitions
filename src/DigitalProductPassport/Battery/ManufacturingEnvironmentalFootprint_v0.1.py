from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnvironmentalFootprintRequest(CamelCaseModel):
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


class EnvironmentalFootprintResponse(CamelCaseModel):
    carbon_equivalent: float = Field(
        ...,
        title="Carbon Equivalent (CO2e) [kg]",
        description="The amount of emissions from all greenhouse gases converted to CO2 emission equivalents in the product manufacturing phase",
        example=200.0,
    )
    material_waste: float = Field(
        ...,
        title="Material Waste [kg]",
        description="The amount of material waste produced in the product manufacturing phase",
        example=8.0,
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Environmental footprint information for a product",
    description="Information about environmental footprint of a product in the manufacturing phase",
    request=EnvironmentalFootprintRequest,
    response=EnvironmentalFootprintResponse,
)
