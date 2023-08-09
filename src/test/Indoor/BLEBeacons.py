from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import BaseModel, Field


class Beacon(CamelCaseModel):
    beacon_id: str = Field(
        ...,
        title="Beacon ID",
        description="Beacon ID",
        example="0d9b38d3-f8a0-4efe-ad62-f781fea62b86",
    )
    rssi: float = Field(
        ...,
        title="RSSI",
        description="Received Signal Strength Indication, in dBm",
        example=-55,
    )


class BLEBeaconsRequest(BaseModel):
    beacons: List[Beacon]


class BLEBeaconsResponse(CamelCaseModel):
    location_id: str = Field(
        ...,
        title="Location ID",
        description="Location ID",
        example="849cc493-efb7-483f-b634-7a44849270f9",
    )
    location_name: str = Field(
        ..., title="Location name", description="Location name", example="Deck #3"
    )


DEFINITION = DataProductDefinition(
    description="Data Product for indoor location based on BLE beacons",
    request=BLEBeaconsRequest,
    response=BLEBeaconsResponse,
    route_description="Indoor location based on BLE beacons",
    summary="BLE Beacons",
)
