from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class OperationsDataResponse(CamelCaseModel):
    cumulative_fuel_use: float = Field(
        ...,
        title="Cumulative Fuel Use",
        description="The cumulative fuel consumption up until requested date in liters "
        "(l)",
        examples=[286.5],
    )
    cumulative_electricity_use: float = Field(
        ...,
        title="Cumulative Electricity Use",
        description="The cumulative electricity consumption up until requested date in "
        "kilowatt-hours (kWh)",
        examples=[158.9],
    )
    total_distance: float = Field(
        ...,
        title="Total Distance",
        description="The cumulative distance driven with the machine in kilometers "
        "(km)",
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
    version="0.1.0",
    title="Straddle Carrier Operations Data",
    description="Operations data of a Straddle Carrier",
    request=OperationsDataRequest,
    response=OperationsDataResponse,
)
