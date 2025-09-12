from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class SerialNumber(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        max_length=150,
        description="Name of the component.",
        examples=["Rock Drill"],
    )
    serial: str = Field(
        ...,
        title="Serial number",
        max_length=150,
        description="Serial number of the component.",
        examples=["S05001"],
    )


class MachineSerialNumberResponse(CamelCaseModel):
    serial_numbers: list[SerialNumber] = Field(
        ...,
        title="Component serial numbers",
        description="Serial numbers of components of the machine.",
    )


class MachineSerialNumberRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type.",
        examples=["equipment-modelX-1234"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="ID",
        description="The unique identifier of the product.",
        examples=["71b51878-8a00-11ee-b9d1-0242ac120002"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.2",
    strict_validation=False,
    title="Machine component serial numbers",
    description="List serial numbers of components in a machine.",
    tags=["Digital Product Passport"],
    request=MachineSerialNumberRequest,
    response=MachineSerialNumberResponse,
)
