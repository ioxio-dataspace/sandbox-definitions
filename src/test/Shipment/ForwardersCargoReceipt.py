from datetime import datetime

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ForwardersCargoReceiptResponse(CamelCaseModel):
    carrier_name: str = Field(..., title="Carrier name")
    exporter_name: str = Field(..., title="Exporter name")
    final_destination: str = Field(..., title="Final destination")
    final_destination_address: str = Field(..., title="Final destination address")
    forwarder_contact_person_name: str = Field(
        ..., title="Forwarder contact person name"
    )
    forwarder_contact_person_phone: str = Field(
        ..., title="Forwarder contact person phone"
    )
    forwarder_name: str = Field(..., title="Forwarder name")
    handling_units: int = Field(..., title="Handling units")
    importer_name: str = Field(..., title="Importer name")
    issue_date: datetime = Field(..., title="Issue date")
    lc_number: str = Field(..., title="LC number")
    mode_of_delivery: str = Field(..., title="Mode of delivery")
    place_of_discharge: str = Field(..., title="Place of discharge")
    place_of_loading: str = Field(..., title="Place of loading")
    place_of_receipt: str = Field(..., title="Place of receipt")
    statement: str = Field(..., title="Statement")
    total_gross_weight: float = Field(..., title="Total gross weight")
    total_net_weight: float = Field(..., title="Total net weight")
    total_volume: float = Field(..., title="Total volume")


class ForwardersCargoReceiptRequest(CamelCaseModel):
    shipment_id: str = Field(..., title="Shipment ID")


DEFINITION = DataProductDefinition(
    version="0.0.3",
    strict_validation=False,
    title="Cargo receipt for a forwarder",
    description="Information necessary for the receipt of cargo for a forwarder",
    request=ForwardersCargoReceiptRequest,
    response=ForwardersCargoReceiptResponse,
)
