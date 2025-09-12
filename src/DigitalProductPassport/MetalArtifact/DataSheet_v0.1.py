from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class EnStandardCertification(CamelCaseModel):
    en_standard_code: Optional[str] = Field(
        None,
        title="EN Standard Code",
        max_length=20,
        description="The identification code of the EN standard that the product is "
        "compliant with.",
        examples=["EN 10002-1"],
    )


class Measures(CamelCaseModel):
    width: Optional[int] = Field(
        None,
        title="Width",
        description="The width of the product measured in centimeters.",
        examples=[1500],
    )
    length: Optional[int] = Field(
        None,
        title="Length",
        description="The length of the product measured in centimeters.",
        examples=[4000],
    )
    height: Optional[int] = Field(
        None,
        title="Height",
        description="The height of the product measured in centimeters.",
        examples=[0],
    )


class MetalArtifactDataSheetRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product code",
        description="The product code used for identifying the product type.",
        examples=["steel-roll-1234x"],
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier of the product.",
        examples=["550e8400-e29b-41d4-a716-446655440000"],
    )


class MetalArtifactDataSheetResponse(CamelCaseModel):
    product_name: str = Field(
        ...,
        title="Product Name",
        max_length=250,
        description="The commercial name of the metal product.",
        examples=[
            "HOT-DIP ZINC-COATED STEEL STRIP, HIGH STRENGTH STEEL FOR COLD FORMING"
        ],
    )
    product_type: str = Field(
        ...,
        title="Product Type",
        max_length=250,
        description="The type of the metal product.",
        examples=["Steel roll"],
    )
    measures: Optional[Measures] = Field(
        None,
        title="Measures",
        description="The dimensional measures of the metal product.",
    )
    net_weight: float = Field(
        ...,
        title="Net Weight",
        description="Net weight of the metal artifact in kilograms.",
        examples=[11720.0],
    )
    en_standard_certifications: List[EnStandardCertification] = Field(
        ...,
        title="EN Standard Certifications",
        description="The list of EN standards.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.2",
    strict_validation=False,
    title="Data Sheet For Metal Artifacts",
    description="Returns the basic product information of a metal product.",
    request=MetalArtifactDataSheetRequest,
    response=MetalArtifactDataSheetResponse,
    tags=["Digital Product Passport"],
    requires_authorization=False,
    requires_consent=False,
)
