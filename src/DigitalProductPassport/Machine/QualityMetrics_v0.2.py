from typing import List

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Measurement(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        max_length=150,
        description="Name of the measurement.",
        examples=["Diameter"],
    )
    ok: bool = Field(
        ...,
        title="OK",
        description="Whether the measurement is considered to be in a good state or not.",
        examples=[True],
    )
    target_deviation: str = Field(
        ...,
        title="Target vs actual deviation",
        description="Actual deviation from target value.",
        max_length=150,
        examples=["0.004 mm"],
    )
    cp: float = Field(
        ...,
        title="Process capability",
        description="Process capability (Cp) of the manufacturing process.",
        examples=[1.33],
    )
    cpk: float = Field(
        ...,
        title="Process capability index",
        description="Process capability index (Cpk) which measures how centered the process is.",
        examples=[1.2],
    )
    pp: float = Field(
        ...,
        title="Process performance",
        description="Process performance (Pp) of the manufacturing process.",
        examples=[1.5],
    )
    ppk: float = Field(
        ...,
        title="Process performance index",
        description="Process performance index (Ppk) which measures how centered the performance is.",
        examples=[1.45],
    )


class Metric(CamelCaseModel):
    identification: str = Field(
        ...,
        title="Identification number",
        max_length=150,
        description="Identification number of the component.",
        examples=["ID9876"],
    )
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
        examples=["Cylinder"],
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
    version="0.2.2",
    strict_validation=False,
    title="Measured quality metrics of a machine",
    description="Quality monitoring data for machines, including product serial number "
    "and quality performance measures.",
    request=QualityMetricsRequest,
    response=QualityMetricsResponse,
    tags=["Digital Product Passport"],
)
