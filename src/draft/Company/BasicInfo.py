from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class BasicCompanyInfoRequest(CamelCaseModel):
    company_id: str = Field(
        ...,
        title="Company ID",
        description="The ID of the company",
        example="2464491-9",
    )


class BasicCompanyInfoResponse(CamelCaseModel):
    name: str = Field(
        ..., title="Name of the company", example="Digital Living International Oy"
    )
    company_id: str = Field(..., title="ID of the company", example="2464491-9")
    company_form: str = Field(
        ..., title="The company form of the company", example="LLC"
    )
    registration_date: str = Field(
        ..., title="Date of registration for the company", example="2012-02-23"
    )


DEFINITION = DataProductDefinition(
    title="Basic information about a company",
    description="Legal information about a company such as company registration date",
    request=BasicCompanyInfoRequest,
    response=BasicCompanyInfoResponse,
)
