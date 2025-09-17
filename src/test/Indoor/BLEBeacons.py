from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import BaseModel, Field


class Beacon(CamelCaseModel):
    beacon_id: str = Field(
        ...,
        title="Beacon ID",
        description="Beacon ID",
        examples=["0d9b38d3-f8a0-4efe-ad62-f781fea62b86"],
    )
    rssi: float = Field(
        ...,
        title="RSSI",
        description="Received Signal Strength Indication, in dBm",
        examples=[-55],
    )


class BLEBeaconsRequest(BaseModel):
    beacons: List[Beacon]


class BLEBeaconsResponse(CamelCaseModel):
    location_id: str = Field(
        ...,
        title="Location ID",
        description="Location ID",
        examples=["849cc493-efb7-483f-b634-7a44849270f9"],
    )
    location_name: str = Field(
        ..., title="Location name", description="Location name", examples=["Deck #3"]
    )


DEFINITION = DataProductDefinition(
    version="0.0.2",
    strict_validation=False,
    title="Indoor location based on BLE beacons",
    description="Determine the indoor location based on BLE beacons a device can hear and the signal strength in dBm.",
    request=BLEBeaconsRequest,
    response=BLEBeaconsResponse,
)
