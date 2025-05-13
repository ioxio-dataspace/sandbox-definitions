from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Material(CamelCaseModel):
    name: str = Field(
        ...,
        title="Material name",
        description="The generic name of the material.",
        min_length=0,
        max_length=40,
        examples=["cotton"],
    )
    share: float = Field(
        ...,
        title="Material share (%)",
        description="The percentage of material present in the garment, expressed as a percentage by weight.",
        gte=0,
        lte=100,
        examples=[50.0],
    )
    recycling_rate: Optional[float] = Field(
        None,
        title="Recycling rate (%)",
        description="The amount of recycled content in the material substance, expressed as a percentage by weight.",
        gte=0,
        lte=100,
        examples=[50.0],
    )


class MaterialInformation(CamelCaseModel):
    certifications: list[str] = Field(
        ...,
        title="Certifications",
        description="List of all qualifications and certifications of the garment in the component category.",
        examples=[["OEKO-TEX"]],
    )
    materials: list[Material] = Field(
        ...,
        title="Materials",
        description="The list of materials.",
    )
    chemicals: Optional[str] = Field(
        None,
        title="Chemicals",
        description="Statement about chemicals used in the garment including safety or compliance.",
        min_length=0,
        max_length=250,
        examples=[
            "Tested for and free from known skin sensitizers under ISO 10993-10."
        ],
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
    outer_material_information: MaterialInformation = Field(
        ...,
        title="Outer material information",
        description="Information about the fabrics and other materials that make up 5% or more of the garment's total weight, as well as the chemicals used in those materials. Outer materials refer to those forming the garment’s outermost layer.",
    )
    lining_material_information: MaterialInformation = Field(
        ...,
        title="Lining material information",
        description="Information about the fabrics and other materials that make up 5% or more of the garment's total weight, as well as the chemicals used in those materials. Lining materials include those placed between the outer fabric and the innermost layer of the garment to provide structure, stability, warmth, or reinforcement, including padding and insulation.",
    )
    notions_and_trim_information: MaterialInformation = Field(
        ...,
        title="Notions and trim information",
        description="Information about the notions and trim materials that make up 5% or more of the garment's total weight. Notions and trim materials are used for functional and decorative elements of the garment, including safety components, refinement features, and sewing threads.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Garment material disclosure sheet",
    description="Public summary of the garment's material composition, recycled content and material level certifications.",
    tags=["Manufacturing"],
    request=Request,
    response=Response,
)
