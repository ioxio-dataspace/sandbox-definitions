from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field, StringConstraints
from typing_extensions import Annotated


class BasicCountryInfoRequest(CamelCaseModel):
    code: str = Field(
        ...,
        title="Code",
        description="ISO 3166-1 alpha-2 code for the country",
        examples=["FI"],
        min_length=2,
        max_length=2,
    )


class Capital(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the capital of the Country",
        examples=["Helsinki"],
    )
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the Capital",
        ge=-90.0,
        le=90.0,
        examples=[60.170833],
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the Capital",
        ge=-180.0,
        le=180.0,
        examples=[24.9375],
    )


class BasicCountryInfoResponse(CamelCaseModel):
    code: str = Field(
        ...,
        title="Code",
        description="ISO 3166-1 alpha-2 code for the country",
        examples=["FI"],
        min_length=2,
        max_length=2,
    )
    name: str = Field(
        ...,
        title="Name",
        description="The name of the country",
        examples=["Finland"],
    )
    area: float = Field(
        ...,
        title="Area",
        description="The area of the country in km^2",
        examples=[338455],
    )
    languages: List[Annotated[str, StringConstraints(min_length=2, max_length=2)]] = (
        Field(
            ...,
            title="Official languages",
            description="ISO 639-1 language codes for the official languages",
            examples=[["fi", "sv"]],
        )
    )
    capital: Optional[Capital] = Field(
        None,
        title="Capital",
        description="The capital of the country, legislative if multiple",
    )


DEFINITION = DataProductDefinition(
    version="0.0.1",
    title="Information about a country",
    description="Information about a country",
    request=BasicCountryInfoRequest,
    response=BasicCountryInfoResponse,
)
