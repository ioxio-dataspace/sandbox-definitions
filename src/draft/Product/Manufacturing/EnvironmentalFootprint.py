from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnvironmentalFootprintRequest(CamelCaseModel):
    serial_number: str = Field(
        ...,
        title="Serial Number",
        description="The serial number given by the manufacturer",
        example="MPP48V-296cde7f",
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
    title="Environmental footprint information for a product",
    description="Information about environmenal footprint that a product produces",
    request=EnvironmentalFootprintRequest,
    response=EnvironmentalFootprintResponse,
)
