from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CarbonFootprint(CamelCaseModel):
    pre_production_footprint: Optional[float] = Field(
        None,
        title="Pre Production Footprint",
        description="The carbon footprint of the pre-manufacture phase of the machine "
        "calculated as kg of CO2e per one kWh using preferably PEF and PEFCR methods.",
        examples=[2345.7],
    )
    main_production_footprint: Optional[float] = Field(
        None,
        title="Main Production Footprint",
        description="The carbon footprint of the machine main production phase "
        "calculated as kg of CO2e per one kWh using preferably PEF and PEFCR methods.",
        examples=[3504.4],
    )
    reference_material: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference Material",
        description="The link giving access to a public version of the study "
        "supporting the carbon footprint values.",
        examples=["https://example.com/CarbonFootprint"],
    )


class MaterialWaste(CamelCaseModel):
    amount: Optional[float] = Field(
        None,
        title="Amount",
        description="The amount of material waste in kilograms (kg) generated during "
        "the machine production.",
        examples=[500.0],
    )
    reference_material: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference Material",
        description="The link giving access to a public version of the study "
        "supporting the material waste values.",
        examples=["https://example.com/CarbonFootprint"],
    )


class DataSheetResponse(CamelCaseModel):
    carbon_footprint: CarbonFootprint = Field(
        ...,
        title="Carbon Footprint",
        description="The details of the carbon footprint for the machine production "
        "phases.",
    )
    material_waste: Optional[MaterialWaste] = Field(
        None,
        title="Material Waste",
        description="The details of the material waste generated during the production.",
    )


class DataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["bev-drill-1234a"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product.",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Mobile Work Machine Environmental Footprint",
    description="Carbon Footprint of a Mobile Work Machine.",
    request=DataSheetRequest,
    response=DataSheetResponse,
    tags=["Digital Product Passport"],
)
