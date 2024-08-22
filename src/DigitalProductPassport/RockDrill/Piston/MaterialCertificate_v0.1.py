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
    standard_compliancy: List[str] = Field(
        ...,
        title="Standard compliancy",
        description="The standard(s) defining the test requirements.",
        examples=[["EN 11223", "ISO 1234-5"]],
    )


class CastAnalysis(CamelCaseModel):
    element: str = Field(
        ...,
        pattern=r"^[A-Z][a-z]?$",
        title="Element",
        description="The symbol of the material element in the cast.",
        examples=["Si"],
    )
    composition: float = Field(
        ...,
        gt=0,
        le=100,
        title="Composition (%)",
        description="The material element composition in the cast.",
        examples=[0.25],
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
        examples=["0123456"],
    )
    cast_analysis: List[CastAnalysis] = Field(
        ...,
        title="Cast analysis",
        description="The material composition of the cast.",
    )
    inspection_conformity: List[InspectionConformity] = Field(
        ...,
        title="Inspection Conformity",
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
    version="0.1.0",
    title="Rock drill material certificate",
    description="Material certificate on the elements and tests",
    request=MaterialCertificateRequest,
    response=MaterialCertificateResponse,
    tags=[
        "Mining",
        "Rock drill",
    ],
)
