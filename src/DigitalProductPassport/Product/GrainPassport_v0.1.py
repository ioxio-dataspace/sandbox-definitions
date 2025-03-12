from datetime import date, datetime
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ProductionMethod(str, Enum):
    CONVENTIONAL = "Conventional"
    ORGANIC = "Organic"
    NON_GMO = "Non-GMO"
    REGENERATIVE = "Regenerative"
    IDENTITY_PRESERVED_GRAIN = "Identity-Preserved Grain"
    OTHER = "Other"


class RecipientInformation(CamelCaseModel):
    company: str = Field(
        ...,
        title="Company",
        description="Name of the company receiving the delivery.",
        max_length=150,
        examples=["Brewing Company Oy"],
    )
    business_id: Optional[str] = Field(
        None,
        title="Business ID",
        description="Business ID of the company receiving the delivery.",
        max_length=150,
        examples=["Y-123456789"],
    )
    address: Optional[str] = Field(
        None,
        title="Address",
        description="Street address of the company receiving the delivery.",
        max_length=150,
        examples=["Example street 12"],
    )
    zipcode: Optional[str] = Field(
        None,
        title="ZIP Code",
        description="ZIP Code of the company receiving the delivery.",
        max_length=40,
        examples=["00100"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        description="City of the company receiving the delivery.",
        max_length=150,
        examples=["Helsinki"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        description="Recipient country in ISO 3166-1 alpha-3.",
        pattern=r"^[A-Z]{3}$",
        min_length=3,
        max_length=3,
        examples=["FIN"],
    )
    contract_number: Optional[str] = Field(
        None,
        title="Contract number",
        description="Contract number given by the sending party to the company receiving the delivery.",
        max_length=150,
        examples=["VM12345"],
    )
    reception_date: Optional[date] = Field(
        None,
        title="Reception date",
        description="Date when the delivery has been made.",
        examples=[date.fromisoformat("2025-02-21")],
    )
    signature: Optional[str] = Field(
        None,
        title="Signature",
        description="Name of the party signing the goods as received.",
        max_length=150,
        examples=["Brewing Company Oy"],
    )


class GrowthRegulatorDetails(CamelCaseModel):
    growth_regulator_date: Optional[date] = Field(
        None,
        title="Growth regulator date",
        description="Date of growth regulator application.",
        examples=[date.fromisoformat("2024-04-15")],
    )
    growth_regulator_type: Optional[str] = Field(
        None,
        title="Growth regulator type",
        description="Type of growth regulator applied.",
        max_length=150,
        examples=["Moddus Evo"],
    )


class FarmerInformation(CamelCaseModel):
    farm: str = Field(
        ...,
        title="Farm",
        description="Name of the producing farm.",
        max_length=150,
        examples=["John Doe's Farm"],
    )
    business_id: Optional[str] = Field(
        None,
        title="Business ID",
        description="Business ID of the producing farm.",
        max_length=150,
        examples=["Y-987654321"],
    )
    address: Optional[str] = Field(
        None,
        title="Address",
        description="Street address of the producing farm.",
        max_length=150,
        examples=["Example road 1"],
    )
    zipcode: Optional[str] = Field(
        None,
        title="ZIP Code",
        description="ZIP Code of the producing farm.",
        max_length=40,
        examples=["11111"],
    )
    city: Optional[str] = Field(
        None,
        title="City",
        description="City of the producing farm.",
        max_length=150,
        examples=["Helsinki"],
    )
    country: Optional[str] = Field(
        None,
        title="Country",
        description="Country of the producing farm in ISO 3166-1 alpha-3.",
        pattern=r"^[A-Z]{3}$",
        min_length=3,
        max_length=3,
        examples=["FIN"],
    )
    processing_equipment: list[str] = Field(
        ...,
        title="Processing equipment",
        description="List of equipment used to process the grain, for example names of storage silos etc.",
        examples=["Silo A3"],
    )
    treated_with_glyphosate: Optional[bool] = Field(
        None,
        title="Treated with glyphosate",
        description="Has the produce been treated with glyphosate?",
        examples=[False],
    )
    treated_with_growth_regulator: Optional[bool] = Field(
        None,
        title="Treated with growth regulator",
        description="Has the produce been treated with growth regulator?",
        examples=[True],
    )
    growth_regulator_details: list[GrowthRegulatorDetails] = Field(
        ...,
        title="Growth regulator details",
        description="Details about growth regulators applied to the grains.",
    )
    signature: str = Field(
        ...,
        title="Signature",
        description="Name of the party signing the handover of the shipment.",
        max_length=150,
        examples=["John Doe"],
    )


class TransportInformation(CamelCaseModel):
    company: str = Field(
        ...,
        title="Company",
        description="Name of the transporting company.",
        max_length=150,
        examples=["Kuljetus Oy"],
    )
    truck_registration_number: Optional[str] = Field(
        None,
        title="Truck registration number",
        description="Registration number of the truck used for transportation.",
        max_length=150,
        examples=["ABC-123"],
    )
    driver: Optional[str] = Field(
        None,
        title="Driver",
        description="Name of the driver delivering the shipment.",
        max_length=150,
        examples=["Maija Mehiläinen"],
    )
    shipment_weight: Optional[float] = Field(
        None,
        title="Shipment weight (kg)",
        description="Weight of the shipment in kg.",
        examples=[28500],
    )
    loading_time: Optional[datetime] = Field(
        None,
        title="Loading time",
        description="Date and time of the loading at the farm, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2025-02-21T10:15:00Z")],
    )
    unloading_time: Optional[datetime] = Field(
        None,
        title="Unloading time",
        description="Date and time of the unloading at the recipient, in RFC 3339 format.",
        examples=[datetime.fromisoformat("2025-02-21T12:45:00Z")],
    )
    previous_content_date: Optional[date] = Field(
        None,
        title="Previous content date",
        description="Date of the previous transportation with the truck in question, in RFC 3339 format.",
        examples=[date.fromisoformat("2025-02-20")],
    )
    previous_content: Optional[str] = Field(
        None,
        title="Previous content",
        description="The last content that has been transported with the truck in question.",
        max_length=150,
        examples=["Oats"],
    )
    previous_sanitation: Optional[str] = Field(
        None,
        title="Previous sanitation",
        description="Details of how the truck has been cleaned after the previous delivery.",
        max_length=150,
        examples=["Water and detergent"],
    )


class Request(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product",
        description="The product code used for identifying the product model.",
        max_length=150,
        examples=["FIBC-123"],
    )
    id: str = Field(
        ...,
        title="ID",
        description="The unique bag identifier.",
        max_length=40,
        examples=["123456789"],
    )


class Response(CamelCaseModel):
    grain_passport_number: str = Field(
        ...,
        title="Grain passport number",
        description="Grain passport number.",
        max_length=150,
        examples=["VM-2025-001"],
    )
    creation_date: date = Field(
        ...,
        title="Creation date",
        description="Grain passport creation date.",
        examples=[date.fromisoformat("2025-02-20")],
    )
    grain_type: str = Field(
        ...,
        title="Grain type",
        description="The general classification of the grain in the bag.",
        max_length=150,
        examples=["Malting Barley"],
    )
    grain_variety: str = Field(
        ...,
        title="Grain variety",
        description="The specific cultivated strain or breed within a grain type.",
        max_length=150,
        examples=["Planet"],
    )
    harvest_year: int = Field(
        ...,
        title="Harvest year",
        description="Year of harvesting.",
        gte=1900,
        lte=2500,
        examples=[2024],
    )
    production_method: ProductionMethod = Field(
        ...,
        title="Production method",
        description="The used farming / production method.",
        examples=[ProductionMethod.CONVENTIONAL],
    )
    recipient_information: list[RecipientInformation] = Field(
        ...,
        title="Recipient information",
        description="Information about all the recipients of the bag.",
    )
    farmer_information: list[FarmerInformation] = Field(
        ...,
        title="Farmer information",
        description="Information about the farmers.",
    )
    transport_information: list[TransportInformation] = Field(
        ...,
        title="Transport information",
        description="Information about the transporting parties.",
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Grain Passport",
    description="Digital Product Passport for one shipment of grains.",
    tags=["Digital Product Passport"],
    request=Request,
    response=Response,
)
