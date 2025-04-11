from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CarbonFootprint(CamelCaseModel):
    raw_material_footprint: Optional[float] = Field(
        None,
        title="Raw material footprint (kg of CO2e)",
        description="The carbon footprint of the raw material acquisition "
        "of the product calculated as kg of CO2e using PEF and PEFCR methods.",
        examples=[1546.3],
    )
    component_production_footprint: Optional[float] = Field(
        None,
        title="Component production footprint (kg of CO2e)",
        description="The carbon footprint of the component production phase of the product "
        "calculated as kg of CO2e using PEF and PEFCR methods.",
        examples=[2345.7],
    )
    main_production_footprint: Optional[float] = Field(
        None,
        title="Main production footprint (kg of CO2e)",
        description="The carbon footprint of the main production or assembly of "
        "the product calculated as kg of CO2e using PEF and PEFCR methods.",
        examples=[3504.4],
    )
    transportation_footprint: Optional[float] = Field(
        None,
        title="Transportation footprint (kg of CO2e)",
        description="The carbon footprint of the component transportation calculated "
        "as kg of CO2e using PEF and PEFCR methods.",
        examples=[421.3],
    )
    reference_material: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference material",
        description="The link to the study supporting the carbon footprint values.",
        examples=["https://example.com/CarbonFootprint"],
    )


class MaterialWaste(CamelCaseModel):
    amount: Optional[float] = Field(
        None,
        title="Amount (kg)",
        description="The amount of material waste in kilograms generated during the production.",
        examples=[500],
    )
    reference_material: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference material",
        description="The link to the study supporting the material waste values.",
        examples=["https://example.com/materialWaste"],
    )


class ProductEnvironmentalFootprintResponse(CamelCaseModel):
    carbon_footprint: CarbonFootprint = Field(
        ...,
        title="Carbon footprint",
        description="The details of the carbon footprint during production.",
    )
    material_waste: Optional[MaterialWaste] = Field(
        None,
        title="Material waste",
        description="The details of the material waste generated during production.",
    )


class ProductEnvironmentalFootprintRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["product-modelX-1234"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="ID",
        description="The unique identifier of the product.",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.1",
    title="Product environmental footprint",
    description="The environmental impact of the product manufacturing",
    request=ProductEnvironmentalFootprintRequest,
    response=ProductEnvironmentalFootprintResponse,
    tags=[
        "Carbon footprint",
        "Product environmental category rules",
        "Environment",
    ],
)
