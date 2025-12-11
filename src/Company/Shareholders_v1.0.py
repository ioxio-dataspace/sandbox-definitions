from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class ShareSeries(CamelCaseModel):
    series_name: str = Field(
        ...,
        title="Series Name",
        description="Classification of the share.",
        examples=["A"],
    )
    votes_per_share: int = Field(
        ...,
        title="Votes per share",
        description="Number of votes per share in the share series.",
        examples=[1],
    )
    total_shares: int = Field(
        ...,
        title="Total Shares",
        description="Total number of shares in the share series.",
        examples=[1000],
    )

    model_config: ConfigDict = ConfigDict(title="Share series")


class Ownerships(CamelCaseModel):
    series_name: str = Field(
        ...,
        title="Series Name",
        description="Name of the share series.",
        examples=["A"],
    )
    quantity: int = Field(
        ...,
        title="Number of Shares",
        description="Number of shares held by the owner.",
        examples=[100],
    )

    model_config: ConfigDict = ConfigDict(title="Ownerships")


class Owners(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name of the Shareholder",
        description="Name of the shareholder.",
        examples=["Matti Meikäläinen | Oy Company Ltd"],
    )
    ownerships: List[Ownerships] = Field(
        ..., title="Ownerships", description="List of Ownerships."
    )

    model_config: ConfigDict = ConfigDict(title="Owners")


class ShareholdersInfoRequest(CamelCaseModel):
    company_id: str = Field(
        ...,
        title="Company ID",
        description="The ID of the company.",
        examples=["2464491-9"],
    )

    model_config: ConfigDict = ConfigDict(title="Shareholders info request")


class ShareholdersInfoResponse(CamelCaseModel):
    share_series: List[ShareSeries] = Field(
        ..., title="Share series", description="List of share series."
    )
    owners: List[Owners] = Field(..., title="Owners", description="List of owners")

    model_config: ConfigDict = ConfigDict(title="Shareholders info response")


DEFINITION = DataProductDefinition(
    version="1.0.4",
    strict_validation=False,
    title="List of the shareholders of a company",
    description="Information about the shareholders of a company such as owners and shares quantity.",
    tags=["Company"],
    request=ShareholdersInfoRequest,
    response=ShareholdersInfoResponse,
)
