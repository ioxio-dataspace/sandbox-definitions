from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class ManufacturerInformation(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        max_length=250,
        title="Name",
        description="The registered trade name of the manufacturer company",
        examples=["Drilling Company A"],
    )
    street_name: Optional[str] = Field(
        None,
        title="Street Name",
        max_length=40,
        description="The street address of the manufacturer's headquarters",
        examples=["Example Street 100"],
    )
    postal_code: Optional[str] = Field(
        None,
        title="Postal Code",
        max_length=10,
        description="The postal code of the manufacturer's headquarters",
        examples=["112233"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the manufacturer's headquarters",
        examples=["Stockholm"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        pattern=r"^[A-Z]{3}$",
        description="The country code of the manufacturer's headquarters location in Alpha-3 format",
        examples=["SWE"],
    )
    website: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Website",
        description="The website of the battery manufacturer",
        examples=["https://example.com/"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the battery manufacturer",
        examples=["info@example.com"],
    )


class ManufacturingDataSheetResponse(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        max_length=150,
        title="Product Name",
        description="The official sales name of the product",
        examples=["Undergound drill A"],
    )
    manufacturer_information: Optional[ManufacturerInformation] = Field(
        None,
        title="Manufacturer Information",
        description="The details of the drill manufacturer",
    )
    boom_coverage: Optional[float] = Field(
        None,
        title="Boom Coverage",
        description="The largest distance to which the drill boom can reach from the machine in meters (m)",
        examples=[3.0],
    )
    tramming_distance: Optional[float] = Field(
        None,
        title="Tramming Distance",
        description="The maximum tramming distance of the drill movement in kilometers (km)",
        examples=[3.0],
    )
    maximum_hole_length: Optional[float] = Field(
        None,
        title="Maximum Hole Length",
        description="The maximum length of the drilled hole in meters (m)",
        examples=[54.0],
    )
    minimum_hole_diameter: Optional[float] = Field(
        None,
        title="Minimum Hole Diameter",
        description="The minimum diameter measure of the drilling hole in millimeters (mm)",
        examples=[76.0],
    )
    maximum_hole_diameter: Optional[float] = Field(
        None,
        title="Maximum Hole Diameter",
        description="The maximum diameter measure of the drilling hole in millimeters (mm)",
        examples=[127.0],
    )
    drilling_power: Optional[float] = Field(
        None,
        title="Drilling Power",
        description="The maximum drilling power of the machine in kilowatts (kW)",
        examples=[160.0],
    )
    reference_data_sheet: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference Data Sheet",
        description="The link to the detailed product specifications",
        examples=["https://example.com/productDocument"],
    )
    safety_data_sheet: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Safety Data Sheet",
        description="The link to the safety control measures of the product",
        examples=["https://example.com/safetyDocument"],
    )


class ManufacturingDataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type",
        examples=["bev-drill-1234a"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Drill Manufacturing Data Sheet",
    description="Manufacturing data sheet of a Mobile Drill Machine",
    request=ManufacturingDataSheetRequest,
    response=ManufacturingDataSheetResponse,
)
