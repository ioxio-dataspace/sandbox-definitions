from typing import Optional

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class PopulationResponse(CamelCaseModel):
    label: str = Field(..., title="Data reference label")
    source: str = Field(..., title="Data source name")
    value: int = Field(..., title="The population value")
    updated: str = Field(..., title="Data updated at timestamp text")


class PopulationRequest(CamelCaseModel):
    # country: Optional[str] = Field(None, title="Country")
    city: Optional[str] = Field(
        "",
        title="City or region",
        description="City or a region name, leaving the field empty selects country's total",
    )
    year: Optional[int] = Field(2021, title="Year")


DEFINITION = DataProductDefinition(
    description="Data Product for population figure",
    request=PopulationRequest,
    response=PopulationResponse,
    summary="Figure for population",
)
