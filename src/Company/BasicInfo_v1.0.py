from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import ConfigDict, Field


class BasicCompanyInfoRequest(CamelCaseModel):
    company_id: str = Field(
        ...,
        title="Company ID",
        description="The ID of the company.",
        examples=["2464491-9"],
    )

    model_config: ConfigDict = ConfigDict(title="Basic company info request")


class BasicCompanyInfoResponse(CamelCaseModel):
    name: str = Field(
        ..., title="Name of the company", examples=["Digital Living International Oy"]
    )
    company_id: str = Field(..., title="ID of the company", examples=["2464491-9"])
    company_form: str = Field(
        ..., title="The company form of the company", examples=["LLC"]
    )
    registration_date: str = Field(
        ..., title="Date of registration for the company", examples=["2012-02-23"]
    )

    model_config: ConfigDict = ConfigDict(title="Basic company info response")


DEFINITION = DataProductDefinition(
    version="1.0.4",
    strict_validation=False,
    title="Basic information about a company",
    description="Legal information about a company such as company registration date.",
    tags=["Company"],
    request=BasicCompanyInfoRequest,
    response=BasicCompanyInfoResponse,
)
