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
    version="0.0.2",
    strict_validation=False,
    title="Dimensions and weights of a product",
    description="Get the physical dimensions and weights of a product based on its product code",
    request=DimensionsAndWeightsRequest,
    response=DimensionsAndWeightsResponse,
)
