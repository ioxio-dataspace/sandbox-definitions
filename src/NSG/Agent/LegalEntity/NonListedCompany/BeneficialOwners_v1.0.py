from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ShareOwnership(CamelCaseModel):
    share_series_class: str = Field(
        ...,
        title="Share series class",
        description="The class of the share series that the shareholder owns.",
        example="B",
        max_length=5,
    )
    quantity: int = Field(
        ...,
        title="Quantity",
        description="The number of shares that the shareholder owns a share series",
        example=20,
    )


class ShareSeries(CamelCaseModel):
    share_series_class: str = Field(
        ...,
        title="Share series class",
        description="The type of the share series of a company",
        example="A",
        max_length=5,
    )
    number_of_shares: int = Field(
        ...,
        title="Number of shares",
        description="The total number of the shares in the share series class",
        example=1000,
    )
    votes_per_share: int = Field(
        ...,
        title="Votes per share",
        description="The number of votes per share in the share series",
        example=1,
    )


class Shareholder(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of a shareholder of the company",
        example="Lars Lindberg | Company Ltd",
        max_length=250,
    )
    share_ownership: List[ShareOwnership] = Field(
        ...,
        title="Share ownership",
        description="The list of ownerships that the shareholder has in the company",
    )


class BeneficialOwnersRequest(CamelCaseModel):
    national_identifier: str = Field(
        ...,
        title="National identifier",
        description="The national identifier of the non-listed company issued by the "
        "trade register in any Nordic country.",
        example="FIN: 2464491-9 / SWE: 5560125791 / NOR:  923609016",
        max_length=40,
    )


class BeneficialOwnersResponse(CamelCaseModel):
    share_series: List[ShareSeries] = Field(
        ...,
        title="Share series",
        description="The details of the share series classes of the company",
    )
    shareholders: List[Shareholder] = Field(
        ...,
        title="Shareholder",
        description="The list of beneficial owners of the company",
    )


DEFINITION = DataProductDefinition(
    version="1.0.0",
    title="Beneficial owners of a non-listed company",
    description="The list of beneficial owners of a non-listed company. The "
    "shareholders exceeding 25 % ownership.",
    request=BeneficialOwnersRequest,
    response=BeneficialOwnersResponse,
    requires_authorization=True,
    requires_consent=True,
)
