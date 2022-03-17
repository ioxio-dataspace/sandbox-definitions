from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class InsuranceCertificateResponse(CamelCaseModel):
    currency_code: str = Field(..., title="Currency code")
    description_of_goods: str = Field(..., title="Description of goods")
    final_destination: str = Field(..., title="Final destination")
    handling_units: int = Field(..., title="Handling units")
    institute_clauses: str = Field(..., title="Institute clauses")
    insurance_value: int = Field(..., title="Insurance value")
    insurance_value_percentage: float = Field(..., title="Insurance value percentage")
    insurer_address: str = Field(..., title="Insurer address")
    insurer_name: str = Field(..., title="Insurer name")
    mode_of_delivery: str = Field(..., title="Mode of delivery")
    place_of_receipt: str = Field(..., title="Place of receipt")
    total_gross_weight: float = Field(..., title="Total gross weight")


class InsuranceCertificateRequest(CamelCaseModel):
    shipment_id: str = Field(..., title="Shipment ID")


DEFINITION = DataProductDefinition(
    generic_description="Insurance Certificate",
    request=InsuranceCertificateRequest,
    response=InsuranceCertificateResponse,
)
