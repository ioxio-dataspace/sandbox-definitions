from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ShareSeries(CamelCaseModel):
    series_name: str = Field(
        ..., title="Series Name", description="Classification of the share", example="A"
    )
    votes_per_share: int = Field(
        ...,
        title="Votes per share",
        description="Number of votes per share in the share series",
        example=1,
    )
    total_shares: int = Field(
        ...,
        title="Total Shares",
        description="Total number of shares in the share series",
        example=1000,
    )


class Ownerships(CamelCaseModel):
    series_name: str = Field(
        ..., title="Series Name", description="Name of the share series", example="A"
    )
    quantity: int = Field(
        ...,
        title="Number of Shares",
        description="Number of shares held by the owner",
        example=100,
    )


class Owners(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name of the Shareholder",
        description="Name of the shareholder",
        example="Matti Meikäläinen | Oy Company Ltd",
    )
    ownerships: List[Ownerships] = Field(
        ..., title="Ownerships", description="List of Ownerships"
    )


class ShareholdersInfoRequest(CamelCaseModel):
    company_id: str = Field(
        ...,
        title="Company ID",
        description="The ID of the company, only supports Finnish business ID's",
        example="2464491-9",
    )


class ShareholdersInfoResponse(CamelCaseModel):
    share_series: List[ShareSeries] = Field(
        ..., title="Share series", description="List of share series"
    )
    owners: List[Owners] = Field(..., title="Owners", description="List of owners")


DEFINITION = DataProductDefinition(
    version="0.0.1",
    deprecated=True,
    title="List of the shareholders of a company",
    description="Information about the shareholders of a company such as owners and shares quantity.",
    request=ShareholdersInfoRequest,
    response=ShareholdersInfoResponse,
)
