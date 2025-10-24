from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class ManufacturingLocation(CamelCaseModel):
    country: Optional[str] = Field(
        None,
        title="Country",
        pattern=r"^[A-Z]{3}$",
        description="The country code of the battery manufacturing location in Alpha-3 "
        "format.",
        examples=["DEU"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the battery manufacturing location.",
        examples=["Hamburg"],
    )


class ManufacturerInformation(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        max_length=250,
        title="Name",
        description="The registered trade name of the manufacturer company.",
        examples=["Battery Manufacturer A"],
    )
    street_name: Optional[str] = Field(
        None,
        title="Street name",
        max_length=40,
        description="The street address of the manufacturer's headquarters.",
        examples=["Example Street 100"],
    )
    postal_code: Optional[str] = Field(
        None,
        title="Postal code",
        max_length=10,
        description="The postal code of the manufacturer's headquarters.",
        examples=["75034"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the manufacturer's headquarters.",
        examples=["Seattle"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        pattern=r"^[A-Z]{3}$",
        description="The country code of the manufacturer's headquarters location in "
        "Alpha-3 format.",
        examples=["USA"],
    )
    website: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Website",
        description="The website of the manufacturer.",
        examples=["https://example.com/"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the manufacturer.",
        examples=["info@example.com"],
    )


class CarbonFootprint(CamelCaseModel):
    pre_production_footprint: Optional[float] = Field(
        None,
        title="Pre production footprint",
        description="The carbon footprint of the raw material acquisition and "
        "pre-processing phase of the battery calculated as kilograms (kg) of CO2e per "
        "one kilowatt-hour (kWh) using preferably PEF and PEFCR methods.",
        examples=[2345.7],
    )
    main_production_footprint: Optional[float] = Field(
        None,
        title="Main production footprint",
        description="The carbon footprint of the battery main production phase "
        "calculated as kilograms (kg) of CO2e per one kilowatt-hour (kWh) using "
        "preferably PEF and PEFCR methods.",
        examples=[3504.4],
    )
    reference_material: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference material",
        description="The web link giving access to a public version of the study "
        "supporting the carbon footprint values.",
        examples=["https://example.com/CarbonFootprint"],
    )


class CarbonFootprintResponse(CamelCaseModel):
    manufacturer_information: Optional[ManufacturerInformation] = Field(
        None,
        title="Manufacturer information",
        description="The details of the battery manufacturer.",
    )
    battery_model: Optional[str] = Field(
        None,
        max_length=40,
        title="Battery model",
        description="The model of the battery.",
        examples=["Z37-310-76"],
    )
    conformity_declaration: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Conformity declaration",
        description="The link to the EU declaration of conformity documentation.",
        examples=["https://example.com/EUdeclaration"],
    )
    manufacturing_location: Optional[ManufacturingLocation] = Field(
        None,
        title="Manufacturing location",
        description="The details of the location of the battery manufacturing plant.",
    )
    carbon_footprint: Optional[CarbonFootprint] = Field(
        None,
        title="Carbon footprint",
        description="The details of the carbon footprint for the battery production "
        "phases.",
    )


class CarbonFootprintRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["sodium-ion-75kWh"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product.",
        examples=["660e8400-e29b-41d4-a716-446655440000"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.5",
    strict_validation=False,
    title="Battery carbon footprint",
    description="Carbon footprint of a battery as required by the European "
    "Commission's Battery Act (2023/1542).",
    tags=["Digital Product Passport", "Battery"],
    request=CarbonFootprintRequest,
    response=CarbonFootprintResponse,
)
