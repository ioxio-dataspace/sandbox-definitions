from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class FatContent(CamelCaseModel):
    fats: float = Field(
        ...,
        title="Fats",
        description="The amount of fat per 100g measured in grams.",
        examples=[6],
    )
    saturated_fats: float = Field(
        ...,
        title="Saturated Fats",
        description="The amount of saturated fat per 100g measured in grams.",
        examples=[0.4],
    )


class EnergyContent(CamelCaseModel):
    energy: int = Field(
        ...,
        title="Energy",
        description="The amount of energy per 100g measured in kilojoules.",
        examples=[750],
    )
    calories: int = Field(
        ...,
        title="Calories",
        description="The number of calories per 100g measured in kilocalories.",
        examples=[180],
    )


class NutritionalValuesRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product code",
        description="The product code used for identifying the product type.",
        examples=["french-fries-500g"],
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier of the product.",
        examples=["550e8400-e29b-41d4-a716-446655440000"],
    )


class NutritionalValuesResponse(CamelCaseModel):
    energy_content: EnergyContent = Field(
        ...,
        title="Energy Content",
        description="The details of the energy content of the food artifact.",
    )
    fat_content: FatContent = Field(
        ...,
        title="Fat Content",
        description="The details of the fat content of the food artifact.",
    )
    carbon_hydrates: float = Field(
        ...,
        title="Carbon Hydrates",
        description="The amount of carbon hydrates per 100g measured in grams.",
        examples=[28],
    )
    sugar: float = Field(
        ...,
        title="Sugar",
        description="The amount of sugar per 100g measured in grams.",
        examples=[0.5],
    )
    protein: float = Field(
        ...,
        title="Protein",
        description="The amount of protein per 100g measured in grams.",
        examples=[3],
    )
    salt: float = Field(
        ...,
        title="Salt",
        description="The amount of salt per 100g measured in grams.",
        examples=[0.01],
    )


DEFINITION = DataProductDefinition(
    version="0.1.2",
    strict_validation=False,
    title="Food Artifact Nutritional Values",
    description="Returns the nutritional values of a food product.",
    request=NutritionalValuesRequest,
    response=NutritionalValuesResponse,
    tags=["Digital Product Passport"],
    requires_authorization=False,
    requires_consent=False,
)
