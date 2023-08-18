from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CurrentAirQualityRequest(CamelCaseModel):
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the desired location",
        example=60.192059,
        ge=-90,
        le=90,
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the desired location",
        example=24.945831,
        ge=-180,
        le=180,
    )


class CurrentAirQualityResponse(CamelCaseModel):
    air_quality_index: int = Field(
        ...,
        title="Air Quality Index",
        description=(
            "Current air quality index.\nRanges:\n0-50 Good;\n51-100 Moderate;\n"
            "101-150 Unhealthy For Sensitive Groups;\n151-200 Unhealthy;\n"
            "201-300 Very Unhealthy;\n301+ Hazardous"
        ),
        ge=0,
        example=30,
    )
    timestamp: str = Field(
        ...,
        title="Timestamp",
        description="Current timestamp in RFC 3339 format",
        example="2020-04-03T13:00:00Z",
    )
    attribution: List[str] = Field(
        ...,
        title="Source Attribution",
        description="List of text to show required credits to data sources",
        example=[
            "Moscow State environmental monitoring "
            "(Государственный экологический мониторинг в Москве)",
            "World Air Quality Index Project",
        ],
    )


DEFINITION = DataProductDefinition(
    title="Current air quality in a given location",
    description="Current Air Quality Index (AQI) in a given location with attribution of the sources",
    request=CurrentAirQualityRequest,
    response=CurrentAirQualityResponse,
    route_description="Current air quality",
)
