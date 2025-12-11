from datetime import date
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class FIBCType(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class FillingMethod(str, Enum):
    TOP = "Top"
    BOTTOM = "Bottom"


class ManufacturingInformation(CamelCaseModel):
    manufacturer: Optional[str] = Field(
        None,
        title="Manufacturer",
        description="Manufacturing company.",
        max_length=150,
        examples=["Manufacturer Ltd"],
    )
    batch_number: Optional[str] = Field(
        None,
        title="Batch number",
        description="The batch number that the product is a part of.",
        max_length=150,
        examples=["123456"],
    )
    manufacturing_date: Optional[date] = Field(
        None,
        title="Manufacturing date",
        description="Date of the production of the product.",
        examples=[date.fromisoformat("2025-01-02")],
    )
    expiration_date: Optional[date] = Field(
        None,
        title="Expiration date",
        description="Date when the product will be expired according to manufacturer.",
        examples=[date.fromisoformat("2035-01-02")],
    )
    production_city: Optional[str] = Field(
        None,
        title="Production city",
        description="City where the product was produced.",
        max_length=150,
        examples=["Ahmedabad"],
    )
    production_country: Optional[str] = Field(
        None,
        title="Production country",
        description="Country where the product was produced, in ISO 3166-1 alpha-3 format.",
        pattern=r"^[A-Z]{3}$",
        min_length=3,
        max_length=3,
        examples=["IND"],
    )
    safety_factor: Optional[str] = Field(
        None,
        title="Safety factor",
        description="The safety factor indicating the load-bearing capacity in relation to its maximum rated load.",
        max_length=150,
        examples=["SF5:1"],
    )
    compliance_certifications: list[str] = Field(
        ...,
        title="Compliance certifications",
        description="List of relevant certifications that the manufacturing is compliant with.",
        examples=[["ISO 21898", "HACCP"]],
    )

    model_config: ConfigDict = ConfigDict(title="Manufacturing information")


class Dimensions(CamelCaseModel):
    # TODO: These should likely be floats
    external_width: Optional[int] = Field(
        None,
        title="External width (cm)",
        description="External width of the bag, in centimeters.",
        examples=[90],
    )
    external_length: Optional[int] = Field(
        None,
        title="External length (cm)",
        description="External length of the bag, in centimeters.",
        examples=[90],
    )
    external_height: Optional[int] = Field(
        None,
        title="External height (cm)",
        description="External height of the bag, in centimeters.",
        examples=[136],
    )
    internal_width: Optional[int] = Field(
        None,
        title="Internal width (cm)",
        description="Internal width of the bag, in centimeters.",
        examples=[87],
    )
    internal_length: Optional[int] = Field(
        None,
        title="Internal length (cm)",
        description="Internal length of the bag, in centimeters.",
        examples=[87],
    )
    internal_height: Optional[int] = Field(
        None,
        title="Internal height (cm)",
        description="Internal height of the bag, in centimeters.",
        examples=[130],
    )
    volume: Optional[float] = Field(
        None,
        title="Volume (m^3)",
        description="Volume of the bag, in cubic meters.",
        examples=[0.98397],
    )

    model_config: ConfigDict = ConfigDict(title="Dimensions")


class Loops(CamelCaseModel):
    type: Optional[str] = Field(
        None,
        title="Type",
        description="Design of the loops.",
        max_length=150,
        examples=["Corner loop design"],
    )
    height: Optional[float] = Field(
        None,
        title="Height (cm)",
        description="Height of the loops, in centimeters.",
        examples=[30.0],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="Color of the loops.",
        max_length=40,
        examples=["Red"],
    )

    model_config: ConfigDict = ConfigDict(title="Loops")


class Body(CamelCaseModel):
    stitching: Optional[str] = Field(
        None,
        title="Stitching",
        description="Type of sticthing of the body.",
        max_length=150,
        examples=["Double chain"],
    )
    stitching_color: Optional[str] = Field(
        None,
        title="Stitching color",
        description="Color of the stitching of the body.",
        max_length=40,
        examples=["Blue"],
    )
    coating_applied: Optional[bool] = Field(
        None,
        title="Coating applied",
        description="Whether a coating has been applied to the body.",
        examples=[False],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="Color of the body.",
        max_length=40,
        examples=["White"],
    )

    model_config: ConfigDict = ConfigDict(title="Body")


class TopSpout(CamelCaseModel):
    diameter: Optional[float] = Field(
        None,
        title="Diameter (cm)",
        description="Diameter of the top spout, in centimeters.",
        examples=[40.0],
    )
    length: Optional[float] = Field(
        None,
        title="Length (cm)",
        description="Length of the top spout, in centimeters.",
        examples=[50.0],
    )
    coating_applied: Optional[bool] = Field(
        None,
        title="Coating applied",
        description="Whether a coating has been applied to the top spout.",
        examples=[False],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="Color of the top spout.",
        max_length=40,
        examples=["White"],
    )

    model_config: ConfigDict = ConfigDict(title="Top spout")


class Bottom(CamelCaseModel):
    diameter: Optional[float] = Field(
        None,
        title="Diameter (cm)",
        description="Diameter of the bottom part, in centimeters.",
        examples=[60.0],
    )
    length: Optional[float] = Field(
        None,
        title="Length (cm)",
        description="Length of the bottom part, in centimeters.",
        examples=[60.0],
    )
    coating_applied: Optional[bool] = Field(
        None,
        title="Coating applied",
        description="Whether a coating has been applied to the bottom part.",
        examples=[True],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="Color of the bottom part.",
        max_length=40,
        examples=["White"],
    )

    model_config: ConfigDict = ConfigDict(title="Bottom")


class Liner(CamelCaseModel):
    type: Optional[str] = Field(
        None,
        title="Type",
        description="Type of the liner.",
        max_length=150,
        examples=["Shaped and wings"],
    )
    thickness: Optional[float] = Field(
        None,
        title="Thickness (µm)",
        description="Thickness of the liner, microns.",
        examples=[100.0],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="Color of the liner.",
        max_length=40,
        examples=["Transparent"],
    )

    model_config: ConfigDict = ConfigDict(title="Liner")


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        max_length=150,
        examples=["FIBC-123"],
    )
    id: str = Field(
        ...,
        title="ID",
        description="The unique bag identifier.",
        max_length=40,
        examples=["123456789"],
    )

    model_config: ConfigDict = ConfigDict(title="Request")


class Response(CamelCaseModel):
    model: Optional[str] = Field(
        None,
        title="Model",
        description="Model of the FIBC bag.",
        max_length=150,
        examples=["U-Panel"],
    )
    type: Optional[FIBCType] = Field(
        None,
        title="Type",
        description="Type of the FIBC bag.",
        examples=[FIBCType.B],
    )
    # TODO: Should be float
    safe_working_load: Optional[int] = Field(
        None,
        title="Safe working load (kg)",
        description="Safe working load (SWL), maximum capacity of the bag, in kilograms.",
        examples=[1000],
    )
    filling_method: Optional[FillingMethod] = Field(
        None,
        title="Filling method",
        description="Instruction for filling and discharging the bag.",
        examples=[FillingMethod.TOP],
    )
    uv_protected: Optional[bool] = Field(
        None,
        title="UV protected",
        description="Is the product UV resistant?",
        examples=[True],
    )
    # TODO: Should be float
    uv_guarantee_years: Optional[int] = Field(
        None,
        title="UV guarantee years",
        description="Guaranteed length in years for the UV protection to work.",
        examples=[3],
    )
    material_composition: Optional[str] = Field(
        None,
        title="Material composition",
        description="Main materials used in the product.",
        max_length=150,
        examples=["Woven Polypropylene (PP)"],
    )
    manufacturing_information: ManufacturingInformation = Field(
        ...,
        title="Manufacturing information",
        description="The manufacturing details of the bag.",
    )
    dimensions: Dimensions = Field(
        ...,
        title="Dimensions",
        description="The dimensions of the bag.",
    )
    loops: Optional[Loops] = Field(
        None,
        title="Loops",
        description="Description of the loops of the bag.",
    )
    body: Optional[Body] = Field(
        None,
        title="Body",
        description="Description of the body of the bag.",
    )
    top_spout: Optional[TopSpout] = Field(
        None,
        title="Top spout",
        description="Description of the top spout of the bag.",
    )
    bottom: Optional[Bottom] = Field(
        None,
        title="Bottom",
        description="Description of the bottom of the bag.",
    )
    liner: Optional[Liner] = Field(
        None,
        title="Liner",
        description="Description of the liner of the bag.",
    )
    document_pocket: Optional[str] = Field(
        None,
        title="Document pocket",
        description="Description of the document pocket, its size, location and orientation.",
        max_length=255,
        examples=["A4, top seam, landscape"],
    )
    handling_instructions: Optional[str] = Field(
        None,
        title="Handling instructions",
        description="Instructions how to handle and store the bag.",
        max_length=255,
        examples=["Store in a dry, ventilated area, avoid sharp objects"],
    )
    inspection_date: Optional[date] = Field(
        None,
        title="Inspection date",
        description="Date of previous inspection.",
        examples=[date.fromisoformat("2025-01-02")],
    )
    type_markings: list[str] = Field(
        ...,
        title="Type markings",
        description="Type markings of the bag.",
        examples=[["UN"]],
    )
    food_safe: Optional[bool] = Field(
        None,
        title="Food safe",
        description="Is the bag food safe?",
        examples=[True],
    )

    model_config: ConfigDict = ConfigDict(title="Response")


DEFINITION = DataProductDefinition(
    version="0.1.3",
    strict_validation=False,
    title="FIBC Product data sheet",
    description="Product data sheet for FIBC bulk bags.",
    tags=["Digital Product Passport"],
    request=Request,
    response=Response,
)
