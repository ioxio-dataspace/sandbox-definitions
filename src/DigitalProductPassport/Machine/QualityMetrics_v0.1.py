from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Measurement(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        max_length=150,
        description="Name of the measurement.",
        examples=["Charge level"],
    )
    ok: bool = Field(
        ...,
        title="OK",
        description="Whether the measurement is considered to be in an OK state or not.",
        examples=[True],
    )
    value: float = Field(
        ...,
        title="Value",
        description="Value of the measurement.",
        examples=[100.0],
    )


class Metric(CamelCaseModel):
    serial: str = Field(
        ...,
        title="Serial number",
        max_length=150,
        description="Serial number of the component.",
        examples=["123456"],
    )
    name: str = Field(
        ...,
        title="Name",
        max_length=150,
        description="Name of the component.",
        examples=["Battery"],
    )
    measurements: List[Measurement] = Field(
        ...,
        title="Measurements",
        description="Quality metric measurements for the component.",
    )


class QualityMetricsResponse(CamelCaseModel):
    metrics: List[Metric] = Field(
        ...,
        title="Metrics",
        description="List of metrics per component.",
    )


class QualityMetricsRequest(CamelCaseModel):
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
    version="0.1.0",
    title="Measured quality metrics of a machine",
    description="Quality monitoring data for machines, including product serial number "
    "and quality performance measures.",
    request=QualityMetricsRequest,
    response=QualityMetricsResponse,
    tags=[],
)
