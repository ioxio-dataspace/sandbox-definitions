from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class PersonDetailsRequest(CamelCaseModel):
    pass


class PersonDetailsResponse(CamelCaseModel):
    name: str = Field(
        ...,
        title="Full name",
        description="Person's name and surname",
        example="Joshua Gray",
    )
    address: str = Field(
        ...,
        title="Address",
        description="Person's home address",
        example="6 Raymond river\nRileybury\nCR3 6XA",
    )


DEFINITION = DataProductDefinition(
    title="Person details",
    description="Details about a person such as home address",
    request=PersonDetailsRequest,
    response=PersonDetailsResponse,
    requires_authorization=True,
)
