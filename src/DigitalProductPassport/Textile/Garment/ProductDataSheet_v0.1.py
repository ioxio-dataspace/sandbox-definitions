from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Gender(str, Enum):
    WOMEN = "women"
    MEN = "men"
    UNISEX = "unisex"


class SizingSystem(str, Enum):
    EU = "eu"
    US = "us"
    UK = "uk"
    IT = "it"
    FR = "fr"
    JP = "jp"
    CN = "cn"
    INT = "int"


class IdentifierScheme(str, Enum):
    GLN = "GLN"
    NATIONAL_BUSINESS_ID = "national business id"
    DUNS = "DUNS"


class ColorScheme(str, Enum):
    PANTONE = "Pantone"
    RAL = "RAL"
    VENDOR_SPECIFIC = "vendor specific"


class CompanyIdentification(CamelCaseModel):
    identifier_scheme: IdentifierScheme = Field(
        ...,
        title="Identifier scheme",
        description="The identification scheme in use for the company.",
        examples=[IdentifierScheme.GLN],
    )
    identifier: str = Field(
        ...,
        title="Identifier",
        description="The identification number according to the selected scheme.",
        min_length=0,
        max_length=20,
        examples=["1234567890123"],
    )


class BrandInformation(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The brand name of the garment.",
        min_length=0,
        max_length=250,
        examples=["Acme workwear Oy"],
    )
    website: Optional[str] = Field(
        None,
        title="Website",
        description="The link to the brand website.",
        pattern=r"^https://",
        max_length=2083,
        examples=["https://example.com/"],
    )
    company_identification: CompanyIdentification = Field(
        ...,
        title="Company identification",
        description="The identification of the company being responsible of the DPP.",
    )


class SizeInformation(CamelCaseModel):
    sizing_system: Optional[SizingSystem] = Field(
        None,
        title="Sizing system",
        description="The sizing system indicating the garment size.",
        examples=[SizingSystem.EU],
    )
    size: Optional[str] = Field(
        None,
        title="Size",
        description="The size of the garment according to the selected sizing system.",
        min_length=0,
        max_length=10,
        examples=["40"],
    )


class ColorInformation(CamelCaseModel):
    color_name: str = Field(
        ...,
        title="Color name",
        description="The name of the color.",
        max_length=40,
        examples=["Classic Blue"],
    )
    color_scheme: Optional[ColorScheme] = Field(
        None,
        title="Color scheme",
        description="The coloring scheme indicating the garment size.",
        examples=[ColorScheme.PANTONE],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="The color of the garment according to the selected color scheme.",
        max_length=20,
        examples=["19-4052 TCX"],
    )


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        min_length=0,
        max_length=150,
        examples=["model-x-1234"],
    )
    id: str = Field(
        ...,
        title="ID",
        description="The unique identifier of the product model, batch or item level.",
        min_length=0,
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


class Response(CamelCaseModel):
    product_name: str = Field(
        ...,
        title="Product name",
        description="The name of the product.",
        min_length=0,
        max_length=40,
        examples=["waterproof jacket"],
    )
    product_website: Optional[str] = Field(
        None,
        title="Product website",
        description="The link to the product website.",
        pattern=r"^https://",
        max_length=2083,
        examples=["https://example.com/"],
    )
    product_class: str = Field(
        ...,
        title="Product class",
        description="A broad classification that groups similar types of garments based on their function or style.",
        min_length=0,
        max_length=40,
        examples=["Healthcare workwear"],
    )
    taric_code: str = Field(
        ...,
        title="Taric code",
        description="The TARIC code related to the garment.",
        min_length=0,
        max_length=10,
        examples=["6109100010"],
    )
    brand_information: BrandInformation = Field(
        ...,
        title="Brand information",
        description="The details of the brand selling the garment.",
    )
    size_information: SizeInformation = Field(
        ...,
        title="Size information",
        description="The size information of the garment.",
    )
    gender: Optional[Gender] = Field(
        None,
        title="Gender",
        description="The main target gender for the garment.",
        examples=[Gender.WOMEN],
    )
    color_information: ColorInformation = Field(
        ...,
        title="Color information",
        description="The color information of the garment main color.",
    )
    weight: Optional[float] = Field(
        None,
        title="Weight (kg)",
        description="The weight of the garment in kilograms.",
        examples=[1.0],
    )
    certifications: list[str] = Field(
        ...,
        title="Certifications",
        description="List of all qualifications and certifications of the garment.",
        examples=[["OEKO-TEX", "GOTS"]],
    )
    standards_conformity: list[str] = Field(
        ...,
        title="Standards conformity",
        description="List of all standards that the garment conforms.",
        examples=[["EN ISO 13688", "EN ISO 11612:2015"]],
    )
    regulatory_compliance: list[str] = Field(
        ...,
        title="Regulatory compliance",
        description="List of all regulations that the garment complies with.",
        examples=[["REACH", "ESPR"]],
    )
    conformity_declaration: Optional[str] = Field(
        None,
        title="Conformity declaration",
        description="The link to the EU declaration of conformity documentation.",
        pattern=r"^https://",
        max_length=2083,
        examples=["https://example.com/"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.2",
    strict_validation=False,
    title="Garment product data sheet",
    description="General specifications of a garment.",
    tags=["Manufacturing", "ESPR"],
    request=Request,
    response=Response,
)
