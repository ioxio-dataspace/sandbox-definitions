from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class RecommendationRequest(CamelCaseModel):
    keywords: str = Field(
        ...,
        title="Keywords",
        description="Keyword data to base recommendations on",
        example="Looking for data product companies to invest on",
    )


class Recommendation(CamelCaseModel):
    score: int = Field(
        ..., description="Recommendation score of the company", example=231
    )
    company_id: str = Field(
        ..., title="Company ID", description="Company ID", example="2464491-9"
    )
    company_name: str = Field(
        ...,
        title="Company name",
        description="Company name",
        example="Digital Living Oy",
    )


class RecommendationResponse(CamelCaseModel):
    results: List[Recommendation] = Field(
        ..., title="Recommendation results", description="List of recommendations"
    )


DEFINITION = DataProductDefinition(
    request=RecommendationRequest,
    response=RecommendationResponse,
    route_description="Data Product for company recommendations score",
    description="Data Product for company recommendations score",
    summary="Company Recommendations Scores",
)
