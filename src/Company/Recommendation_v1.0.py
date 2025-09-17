from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class RecommendationRequest(CamelCaseModel):
    keywords: str = Field(
        ...,
        title="Keywords",
        description="Keyword data to base recommendations on.",
        examples=["Looking for data product companies to invest on"],
    )


class Recommendation(CamelCaseModel):
    score: int = Field(
        ..., description="Recommendation score of the company.", examples=[231]
    )
    company_id: str = Field(
        ...,
        title="Company ID",
        description="ID of the company.",
        examples=["2464491-9"],
    )
    company_name: str = Field(
        ...,
        title="Company name",
        description="Name of the Company being recommended.",
        examples=["Digital Living Oy"],
    )


class RecommendationResponse(CamelCaseModel):
    results: List[Recommendation] = Field(
        ..., title="Recommendation results", description="List of recommendations."
    )


DEFINITION = DataProductDefinition(
    version="1.0.2",
    strict_validation=False,
    title="Company recommendations based on keywords",
    description="Recommendation of companies based on provided keywords. Each result has a score.",
    tags=["Company"],
    request=RecommendationRequest,
    response=RecommendationResponse,
)
