from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnvironmentalFootprintRequest(CamelCaseModel):
    product_id: str = Field(
        ...,
        title="Product ID",
        description="The product ID given by the manufacturer",
        example="MPP48V-296cde7f",
    )


class EnvironmentalFootprintResponse(CamelCaseModel):
    carbon_equivalent: float = Field(
        ...,
        title="Carbon Equivalent (CO2e) [kg]",
        description="Includes all GHG emissions converted to CO2 emission equivalents",
        example=500.0,
    )
    material_waste: float = Field(
        ...,
        title="Material Waste [kg]",
        description="The amount of material waste produced during the product manufacturing",
        example=20.0,
    )


DEFINITION = DataProductDefinition(
    request=EnvironmentalFootprintRequest,
    response=EnvironmentalFootprintResponse,
    summary="Environmental Footprint information for a product",
)
