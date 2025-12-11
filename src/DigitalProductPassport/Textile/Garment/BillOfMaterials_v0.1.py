from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class ComponentType(str, Enum):
    TEXTILE = "textile"
    SOFT_NON_TEXTILE = "soft non-textile"
    HARD_NON_TEXTILE = "hard non-textile"


class ClassificationSystem(str, Enum):
    CAS = "CAS"
    ECHA = "ECHA"


class ColorScheme(str, Enum):
    PANTONE = "Pantone"
    RAL = "RAL"
    VENDOR_SPECIFIC = "vendor specific"


class ColorInformation(CamelCaseModel):
    color_scheme: Optional[ColorScheme] = Field(
        None,
        title="Color scheme",
        description="The scheme indicating the garment color.",
        examples=[ColorScheme.PANTONE],
    )
    color: Optional[str] = Field(
        None,
        title="Color",
        description="The main color of the garment according to the followed coloring scheme.",
        min_length=0,
        max_length=20,
        examples=["19-4052 TCX"],
    )

    model_config: ConfigDict = ConfigDict(title="Color information")


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

    model_config: ConfigDict = ConfigDict(title="Material")


class Chemical(CamelCaseModel):
    classification_system: ClassificationSystem = Field(
        ...,
        title="Classification system",
        description="The classification system used for classifying the chemical substance.",
        examples=[ClassificationSystem.ECHA],
    )
    chemical_identifier: str = Field(
        ...,
        title="Chemical identifier",
        description="The identifier of the chemical.",
        min_length=0,
        max_length=20,
        examples=["200-001-8"],
    )

    model_config: ConfigDict = ConfigDict(title="Chemical")


class Component(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the component in the garment.",
        min_length=0,
        max_length=40,
        examples=["zipper", "fabric silk"],
    )
    type: ComponentType = Field(
        ...,
        title="Type",
        description="The type of the component divided into textile and non-textile components based on their structure.",
        examples=[ComponentType.TEXTILE],
    )
    color_information: Optional[ColorInformation] = Field(
        None,
        title="Color information",
        description="The color information of the component.",
    )
    materials: list[Material] = Field(
        ...,
        title="Materials",
        description="List of materials used in the component.",
    )
    chemicals: list[Chemical] = Field(
        ...,
        title="Chemicals",
        description="List of chemicals used in the component.",
    )

    model_config: ConfigDict = ConfigDict(title="Component")


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

    model_config: ConfigDict = ConfigDict(title="Request")


class Response(CamelCaseModel):
    outer_components: list[Component] = Field(
        ...,
        title="Outer components",
        description="List of all outer components. The outer components include fabrics and other structures that create the outermost layer of the garment.",
    )
    lining_components: list[Component] = Field(
        ...,
        title="Lining components",
        description="List of all lining components. The lining components include fabrics and other structures that create the innermost lining of the garment and materials placed between the outer fabric and the lining of the garment to provide structure, stability, warmth, or reinforcement, including padding and insulation.",
    )
    notions_and_trim_components: list[Component] = Field(
        ...,
        title="Notions and trim components",
        description="List of all notions and trim components. The notions and trim components include fabrics and other structures used for the functional and decorative elements of the garment, including safety elements, refinement features and sewing threads.",
    )

    model_config: ConfigDict = ConfigDict(title="Response")


DEFINITION = DataProductDefinition(
    version="0.1.4",
    strict_validation=False,
    title="Garment Bill of Materials",
    description="Details of the garment's bill of materials.",
    tags=["Manufacturing"],
    request=Request,
    response=Response,
)
