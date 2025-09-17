from datetime import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class InvoiceResponse(CamelCaseModel):
    amount_to_be_paid: float = Field(..., title="Amount to be paid")
    bank_contact_bic: str = Field(..., title="Bank contact BIC")
    bank_contact_iban: str = Field(..., title="Bank contact IBAN")
    bank_contact_name: str = Field(..., title="Bank contact name")
    buyer_contact_person_name: str = Field(..., title="Buyer contact person name")
    buyer_name: str = Field(..., title="Buyer name")
    buyer_vat_number: str = Field(..., title="Buyer VAT number")
    contract_reference: str = Field(..., title="Contract reference")
    country_of_origin: str = Field(..., title="Country of origin")
    currency_code: str = Field(..., title="Currency code")
    description_of_goods: str = Field(..., title="Description of goods")
    handling_units: int = Field(..., title="Handling units")
    incoterm: str = Field(..., title="Incoterm")
    incoterm_place: str = Field(..., title="Incoterm place")
    invoice_note: str = Field(..., title="Invoice note")
    invoice_reference: str = Field(..., title="Invoice reference")
    issue_date: datetime = Field(..., title="Issue date")
    lc_number: str = Field(..., title="LC number")
    letter_of_credit_value: int = Field(..., title="Letter of credit value")
    mode_of_delivery: str = Field(..., title="Mode of delivery")
    order_reference: str = Field(..., title="Order reference")
    project_reference: str = Field(..., title="Project reference")
    seller_contact_person_name: str = Field(..., title="Seller contact person name")
    seller_name: str = Field(..., title="Seller name")
    seller_vat_number: str = Field(..., title="Seller VAT number")
    tax_rate: int = Field(..., title="Tax rate")
    total_gross_weight: float = Field(..., title="Total gross weight")
    total_net_weight: float = Field(..., title="Total net weight")
    total_volume: float = Field(..., title="Total volume")
    value_of_shipment: float = Field(..., title="Value of shipment")


class InvoiceRequest(CamelCaseModel):
    shipment_id: str = Field(..., title="Shipment ID")


DEFINITION = DataProductDefinition(
    version="0.0.2",
    strict_validation=False,
    title="Invoice",
    description="Invoice",
    request=InvoiceRequest,
    response=InvoiceResponse,
)
