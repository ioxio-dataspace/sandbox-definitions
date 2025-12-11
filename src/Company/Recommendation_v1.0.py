from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class RecommendationRequest(CamelCaseModel):
    keywords: str = Field(
        ...,
        title="Keywords",
        description="Keyword data to base recommendations on.",
        examples=["Looking for data product companies to invest on"],
    )

    model_config: ConfigDict = ConfigDict(title="Recommendation request")


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
        examples=["IOXIO Oy"],
    )

    model_config: ConfigDict = ConfigDict(title="Recommendation")


class RecommendationResponse(CamelCaseModel):
    results: List[Recommendation] = Field(
        ..., title="Recommendation results", description="List of recommendations."
    )

    model_config: ConfigDict = ConfigDict(title="Recommendation response")


DEFINITION = DataProductDefinition(
    version="1.0.4",
    strict_validation=False,
    title="Company recommendations based on keywords",
    description="Recommendation of companies based on provided keywords. Each result has a score.",
    tags=["Company"],
    request=RecommendationRequest,
    response=RecommendationResponse,
)
