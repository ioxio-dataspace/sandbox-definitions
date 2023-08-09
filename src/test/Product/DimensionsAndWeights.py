from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class DimensionsAndWeightsResponse(CamelCaseModel):
    gross_weight: str = Field(..., title="Gross weight")
    height: float = Field(..., title="Height")
    length: float = Field(..., title="Length")
    net_weight: float = Field(..., title="Net weight")
    product_description: str = Field(..., title="Product description")
    product_name: str = Field(..., title="Product name")
    volume: float = Field(..., title="Volume")
    width: float = Field(..., title="Width")


class DimensionsAndWeightsRequest(CamelCaseModel):
    product_code: str = Field(..., title="Product code")


DEFINITION = DataProductDefinition(
    description="Data Product for Dimensions And Weights",
    request=DimensionsAndWeightsRequest,
    response=DimensionsAndWeightsResponse,
    summary="Dimensions And Weights",
)
