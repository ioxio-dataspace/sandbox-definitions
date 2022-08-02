from datetime import datetime

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ExportInstructionsResponse(CamelCaseModel):
    advising_bank_bic: str = Field(..., title="Advising bank BIC")
    advising_bank_name: str = Field(..., title="Advising bank name")
    advising_bank_reference: str = Field(..., title="Advising bank reference")
    applicant_address: str = Field(..., title="Applicant address")
    applicant_name: str = Field(..., title="Applicant name")
    beneficiary_address: str = Field(..., title="Beneficiary address")
    beneficiary_name: str = Field(..., title="Beneficiary name")
    confirmation_instructions: str = Field(..., title="Confirmation instructions")
    contract_reference: str = Field(..., title="Contract reference")
    credit_availability: str = Field(..., title="Credit availability")
    currency_code: str = Field(..., title="Currency code")
    date_of_expiry: datetime = Field(..., title="Date of expiry")
    description_of_goods: str = Field(..., title="Description of goods")
    incoterm: str = Field(..., title="Incoterm")
    incoterm_place: str = Field(..., title="Incoterm place")
    issue_date: datetime = Field(..., title="Issue date")
    issuing_bank_bic: str = Field(..., title="Issuing bank BIC")
    issuing_bank_name: str = Field(..., title="Issuing bank name")
    latest_date_of_shipment: datetime = Field(..., title="Latest date of shipment")
    letter_of_credit_value: int = Field(..., title="Letter of credit value")


class ExportInstructionsRequest(CamelCaseModel):
    letter_of_credit_number: str = Field(
        ...,
        alias="letterOfCreditNumber",
        title="Letter of credit number",
        example="123",
    )


DEFINITION = DataProductDefinition(
    description="Data Product for Export Instructions",
    request=ExportInstructionsRequest,
    response=ExportInstructionsResponse,
    summary="Export Instructions",
)
