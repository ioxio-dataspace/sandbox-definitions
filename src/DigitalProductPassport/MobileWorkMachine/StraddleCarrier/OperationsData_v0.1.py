from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class OperationsDataResponse(CamelCaseModel):
    fuel_use: float = Field(
        ...,
        title="Fuel use",
        description="The total fuel consumption logged in liters (l)",
        examples=[286.5],
    )
    electricity_use: float = Field(
        ...,
        title="Electricity use",
        description="The total electricity consumption logged in kilowatt-hours (kWh)",
        examples=[158.9],
    )
    distance: float = Field(
        ...,
        title="Distance",
        description="The total distance driven with the machine in kilometers (km)",
        examples=[350.0],
    )


class OperationsDataRequest(CamelCaseModel):
    product: str = Field(
        ...,
        max_length=150,
        title="Product",
        description="The product code used for identifying the product type",
        examples=["straddle-carrier-1234a"],
    )
    id: str = Field(
        ...,
        max_length=40,
        title="Id",
        description="The unique identifier of the product",
        examples=["faf1e386-6a07-4f89-bdbe-b0a6a6241c69"],
    )


DEFINITION = DataProductDefinition(
    version="0.1.2",
    strict_validation=False,
    title="Straddle carrier operations data",
    description="Operations data of a straddle carrier to retrieve fuel use, "
    "electricity use and distance driven",
    request=OperationsDataRequest,
    response=OperationsDataResponse,
)
