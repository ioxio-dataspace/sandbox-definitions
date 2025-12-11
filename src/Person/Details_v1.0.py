from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class PersonDetailsRequest(CamelCaseModel):
    model_config: ConfigDict = ConfigDict(title="Person details request")


class PersonDetailsResponse(CamelCaseModel):
    name: str = Field(
        ...,
        title="Full name",
        description="Person's name and surname.",
        examples=["Joshua Gray"],
    )
    address: str = Field(
        ...,
        title="Address",
        description="Person's home address.",
        examples=["6 Raymond river\nRileybury\nCR3 6XA"],
    )

    model_config: ConfigDict = ConfigDict(title="Person details response")


DEFINITION = DataProductDefinition(
    version="1.0.4",
    strict_validation=False,
    deprecated=True,
    title="Person details",
    description="Details about a person such as home address.",
    request=PersonDetailsRequest,
    response=PersonDetailsResponse,
    tags=["Person"],
    requires_authorization=True,
)
