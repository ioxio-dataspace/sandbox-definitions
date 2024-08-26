from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class InspectionConformity(CamelCaseModel):
    inspection_name: str = Field(
        ...,
        max_length=40,
        title="Inspection name",
        description="The name of the inspection conducted.",
        examples=["Tension test"],
    )
    inspection_description: str = Field(
        ...,
        max_length=400,
        title="Inspection description",
        description="The description of the inspection conducted.",
        examples=["A tension test measures a material's resistance to pulling forces."],
    )
    standards_compliance: List[str] = Field(
        ...,
        title="Standards compliance",
        description="The standard(s) defining the test requirements.",
        examples=[["EN 11223", "ISO 1234-5"]],
    )


class MaterialCertificateResponse(CamelCaseModel):
    product_name: Optional[str] = Field(
        None,
        max_length=150,
        title="Product name",
        description="The official sales name of the product.",
        examples=["Product model A"],
    )
    cast_number: str = Field(
        ...,
        title="Cast number",
        description="The number of the cast.",
        max_length=20,
        examples=["0123456"],
    )
    order_number: str = Field(
        ...,
        title="Order number",
        description="The order number associated with the cast.",
        max_length=20,
        examples=["8976543"],
    )
    cast_analysis: Optional[str] = Field(
        None,
        title="Cast analysis",
        description="The link to the detailed cast analysis.",
        pattern=r"^https://",
        max_length=2083,
        examples=["https://example.com/castAnalysis"],
    )
    inspection_conformity: List[InspectionConformity] = Field(
        ...,
        title="Inspection conformity",
        description="The details of the conformity with the legal and standard requirements.",
    )


class MaterialCertificateRequest(CamelCaseModel):
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
    version="0.2.0",
    title="Piston material certificate",
    description="Material certificate on the elements and tests",
    request=MaterialCertificateRequest,
    response=MaterialCertificateResponse,
    tags=[
        "Mining",
        "Rock drill",
    ],
)
