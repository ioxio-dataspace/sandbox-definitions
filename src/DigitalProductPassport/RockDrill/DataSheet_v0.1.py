from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class ManufacturerInformation(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        max_length=250,
        title="Name",
        description="The registered trade name of the manufacturer company.",
        examples=["Company A"],
    )
    street_name: Optional[str] = Field(
        None,
        max_length=40,
        title="Street name",
        description="The street address of the manufacturer's headquarters.",
        examples=["Example Street 100"],
    )
    postal_code: Optional[str] = Field(
        None,
        max_length=10,
        title="Postal code",
        description="The postal code of the manufacturer's headquarters.",
        examples=["112233"],
    )
    city: Optional[str] = Field(
        None,
        max_length=40,
        title="City",
        description="The city of the manufacturer's headquarters.",
        examples=["Stockholm"],
    )
    country: Optional[str] = Field(
        None,
        pattern=r"^[A-Z]{3}$",
        title="Country",
        description="The country code of the manufacturer's headquarters location "
        "in Alpha-3 format.",
        examples=["SWE"],
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


class ManufacturingLocation(CamelCaseModel):
    country: Optional[str] = Field(
        None,
        pattern=r"^[A-Z]{3}$",
        title="Country",
        description="The country code of the manufacturing location in Alpha-3 format.",
        examples=["DEU"],
    )
    city: Optional[str] = Field(
        None,
        max_length=40,
        title="City",
        description="The city of the manufacturing location.",
        examples=["Hamburg"],
    )


class DataSheetResponse(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        max_length=150,
        title="Product name",
        description="The official sales name of the product.",
        examples=["Product model A"],
    )
    manufacturer_information: Optional[ManufacturerInformation] = Field(
        None,
        title="Manufacturer information",
        description="The details of the manufacturer.",
    )
    manufacturing_location: Optional[ManufacturingLocation] = Field(
        None,
        title="Manufacturing location",
        description="Location where this drill was manufactured.",
    )
    minimum_hole_diameter: Optional[float] = Field(
        None,
        title="Minimum hole diameter (mm)",
        description="The minimum diameter of the drilling hole in millimeters.",
        examples=[76],
    )
    maximum_hole_diameter: Optional[float] = Field(
        None,
        title="Maximum hole diameter (mm)",
        description="The maximum diameter of the drilling hole in millimeters.",
        examples=[127],
    )
    weight: Optional[float] = Field(
        None,
        title="Weight (kg)",
        description="The net weight of the product in kilograms.",
        examples=[200],
    )
    percussion_rate: Optional[float] = Field(
        None,
        title="Percussion rate (Hz)",
        description="The frequency at which drill percussive action occurs in hertz.",
        examples=[50],
    )
    drilling_power: Optional[float] = Field(
        None,
        title="Drilling power (kW)",
        description="The maximum drilling power in kilowatts.",
        examples=[160],
    )
    reference_data_sheet: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference data sheet",
        description="The link to the detailed product specifications.",
        examples=["https://example.com/productDocument"],
    )
    user_manual: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="User manual",
        description="The link to the detailed user manual.",
        examples=["https://example.com/userManual"],
    )
    safety_manual: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Safety manual",
        description="The link to the detailed safety manual.",
        examples=["https://example.com/safetyManual"],
    )


class DataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["equipment-modelX-1234"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="ID",
        description="The unique identifier of the product.",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.4",
    strict_validation=False,
    title="Rock drill data sheet",
    description="General as-built data of a rock drill.",
    request=DataSheetRequest,
    response=DataSheetResponse,
    tags=[
        "Mining",
        "Rock drill",
        "Digital Product Passport",
    ],
)
