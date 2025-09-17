from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnvironmentalFootprintRequest(CamelCaseModel):
    serial_number: str = Field(
        ...,
        title="Serial Number",
        description="The serial number given by the manufacturer.",
        examples=["MPP48V-296cde7f"],
    )


class EnvironmentalFootprintResponse(CamelCaseModel):
    carbon_equivalent: float = Field(
        ...,
        title="Carbon Equivalent (CO2e) [kg]",
        description="The amount of emissions from all greenhouse gases converted to CO2 emission equivalents in the product manufacturing phase.",
        examples=[200.0],
    )
    material_waste: float = Field(
        ...,
        title="Material Waste [kg]",
        description="The amount of material waste produced in the product manufacturing phase.",
        examples=[8.0],
    )


DEFINITION = DataProductDefinition(
    version="1.0.2",
    strict_validation=False,
    title="Environmental footprint information for a product",
    description="Information about environmental footprint of a product in the manufacturing phase.",
    tags=["Product environmental category rules", "Manufacturing"],
    request=EnvironmentalFootprintRequest,
    response=EnvironmentalFootprintResponse,
)
