from datetime import date, datetime
from enum import Enum
from typing import Optional, Set

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ComponentType(str, Enum):
    TEXTILE = "textile"
    SOFT_NON_TEXTILE = "soft non-textile"
    HARD_NON_TEXTILE = "hard non-textile"


class ClassificationSystem(str, Enum):
    CAS = "cas"
    ECHA = "echa"


class ColourInformation(CamelCaseModel):
    colour_scheme: Optional[str] = Field(
        None,
        title="Colour scheme",
        description="The colouring scheme indicating the garment size.",
        min_length=0,
        max_length=10,
        examples=["ral"],
    )
    colour: Optional[str] = Field(
        None,
        title="Colour",
        description="The colour of the garment according to the selected colour scheme.",
        min_length=0,
        max_length=10,
        examples=["19-4052"],
    )


class Material(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The generic name of the material.",
        min_length=0,
        max_length=40,
        examples=["cotton"],
    )
    share: float = Field(
        ...,
        title="Share (%)",
        description="The percentage of material content in the component, expressed as a percentage by weight.",
        gte=0,
        lte=100,
        examples=[50],
    )
    recycling_rate: Optional[float] = Field(
        None,
        title="Recycling rate (%)",
        description="The amount of recycled content in the material substance, expressed as a percentage by weight.",
        gte=0,
        lte=100,
        examples=[50],
    )


class Chemical(CamelCaseModel):
    classification_system: ClassificationSystem = Field(
        ...,
        title="Classification system",
        description="The classification system used for classifying the chemical substance.",
        examples=["echa"],
    )
    chemical_identifier: str = Field(
        ...,
        title="Chemical identifier",
        description="The identifier of the chemical.",
        min_length=0,
        max_length=20,
        examples=["200-001-8"],
    )


class Component(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the material in the garment.",
        min_length=0,
        max_length=40,
        examples=["zipper xyz / fabric silk xyz"],
    )
    type: ComponentType = Field(
        ...,
        title="Type",
        description="The type of the component divided into textile and non-textile components based on their structure.",
        examples=["textile"],
    )
    colour_information: Optional[ColourInformation] = Field(
        None,
        title="Colour information",
        description="The colour information of the garment.",
    )
    materials: list[Material] = Field(
        ...,
        title="Materials",
        description="The list of materials in the component.",
    )
    chemicals: list[Chemical] = Field(
        ...,
        title="Chemicals",
        description="The list of chemicals in the component.",
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
        description="The unique identifier of the product, batch or item level.",
        min_length=0,
        max_length=40,
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


class Response(CamelCaseModel):
    outer_components: list[Component] = Field(
        ...,
        title="Outer components",
        description="List of all outer components. The outer components include fabrics and other structures that create the outermost layer of a garment.",
    )
    lining_components: list[Component] = Field(
        ...,
        title="Lining components",
        description="List of all lining components. The lining components include fabrics and other structures that create the innermost lining of the garment and materials placed between the outer fabric and the lining of a garment to provide structure, stability, warmth, or reinforcement, including padding and insulation.",
    )
    notions_and_trim_components: list[Component] = Field(
        ...,
        title="Notions and trim components",
        description="List of all notions and trim components. The notions and trim components include fabrics and other structures used for the functional and decorative elements of the garment, including safety elements, refinement features and sewing threads.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Garment Bill of Materials",
    description="Details of the garment's bill of materials.",
    tags=["Manufacturing"],
    request=Request,
    response=Response,
)
