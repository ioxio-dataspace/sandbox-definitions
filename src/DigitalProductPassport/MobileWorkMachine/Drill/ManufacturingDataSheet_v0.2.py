from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class PowerSystemType(str, Enum):
    FULLY_ELECTRIC = "fully electric"
    HYBRID = "hybrid"
    FUEL_POWERED = "fuel powered"


class ManufacturerInformation(CamelCaseModel):
    name: Optional[str] = Field(
        None,
        max_length=250,
        title="Name",
        description="The registered trade name of the manufacturer company.",
        examples=["Drilling Company A"],
    )
    street_name: Optional[str] = Field(
        None,
        title="Street Name",
        max_length=40,
        description="The street address of the manufacturer's headquarters.",
        examples=["Example Street 100"],
    )
    postal_code: Optional[str] = Field(
        None,
        title="Postal Code",
        max_length=10,
        description="The postal code of the manufacturer's headquarters.",
        examples=["112233"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        max_length=40,
        description="The city of the manufacturer's headquarters.",
        examples=["Stockholm"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        pattern=r"^[A-Z]{3}$",
        description="The country code of the manufacturer's headquarters location in "
        "Alpha-3 format.",
        examples=["SWE"],
    )
    website: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Website",
        description="The website of the battery manufacturer.",
        examples=["https://example.com/"],
    )
    email: Optional[EmailStr] = Field(
        None,
        title="Email",
        description="The email address of the battery manufacturer.",
        examples=["info@example.com"],
    )


class ElectricMotors(CamelCaseModel):
    motor_type: Optional[str] = Field(
        None,
        title="Motor Type",
        description="The type of the electric motor in use in the machine.",
        max_length=100,
        examples=["induction motor"],
    )
    count: Optional[int] = Field(
        None,
        title="Count",
        description="The number of corresponding motors in use in the machine.",
        ge=0,
        examples=[2],
    )


class Batteries(CamelCaseModel):
    power: Optional[float] = Field(
        None,
        title="Power (kW)",
        description="The power of the battery in use the machine in kilowatts.",
        ge=0,
        examples=[75.0],
    )
    cell_type: Optional[str] = Field(
        None,
        title="Cell Type",
        description="The type of cells used in the battery pack.",
        max_length=250,
        examples=["sodium-ion"],
    )
    count: Optional[int] = Field(
        None,
        title="Count",
        description="The number of corresponding batteries in use in the machine.",
        ge=0,
        examples=[2],
    )


class PowerSystem(CamelCaseModel):
    type: Optional[PowerSystemType] = Field(
        None,
        title="Type",
        description="The type of the machine power system.",
        examples=[PowerSystemType.HYBRID],
    )
    electric_motors: List[ElectricMotors] = Field(
        ...,
        title="Electric Motors",
        description="The list of the electric motors in the machine.",
    )
    batteries: List[Batteries] = Field(
        None,
        title="Batteries",
        description="The list of batteries in the machine.",
    )


class ManufacturingDataSheetResponse(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        max_length=150,
        title="Product Name",
        description="The official sales name of the product.",
        examples=["Undergound drill A"],
    )
    manufacturer_information: Optional[ManufacturerInformation] = Field(
        None,
        title="Manufacturer Information",
        description="The details of the drill manufacturer.",
    )
    power_system: Optional[PowerSystem] = Field(
        None,
        title="Power System",
        description="The details of the drill power system.",
    )
    boom_coverage: Optional[float] = Field(
        None,
        title="Boom Coverage (m)",
        description="The largest distance to which the drill boom can reach from the "
        "machine in meters.",
        examples=[3.0],
    )
    tramming_distance: Optional[float] = Field(
        None,
        title="Tramming Distance (km)",
        description="The maximum tramming distance of the drill movement in kilometers.",
        examples=[3.0],
    )
    maximum_hole_length: Optional[float] = Field(
        None,
        title="Maximum Hole Length (m)",
        description="The maximum length of the drilled hole in meters.",
        examples=[54.0],
    )
    minimum_hole_diameter: Optional[float] = Field(
        None,
        title="Minimum Hole Diameter (mm)",
        description="The minimum diameter measure of the drilling hole in millimeters.",
        examples=[76.0],
    )
    maximum_hole_diameter: Optional[float] = Field(
        None,
        title="Maximum Hole Diameter (mm)",
        description="The maximum diameter measure of the drilling hole in millimeters.",
        examples=[127.0],
    )
    drilling_power: Optional[float] = Field(
        None,
        title="Drilling Power (kW)",
        description="The maximum drilling power of the machine in kilowatts.",
        examples=[160.0],
    )
    reference_data_sheet: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Reference Data Sheet",
        description="The link to the detailed product specifications.",
        examples=["https://example.com/productDocument"],
    )
    safety_data_sheet: Optional[str] = Field(
        None,
        pattern=r"^https://",
        max_length=2083,
        title="Safety Data Sheet",
        description="The link to the safety control measures of the product.",
        examples=["https://example.com/safetyDocument"],
    )


class ManufacturingDataSheetRequest(CamelCaseModel):
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
    version="0.2.2",
    strict_validation=False,
    title="Drill Manufacturing Data Sheet",
    description="Manufacturing data sheet of a Mobile Drill Machine.",
    tags=["Digital Product Passport"],
    request=ManufacturingDataSheetRequest,
    response=ManufacturingDataSheetResponse,
)
