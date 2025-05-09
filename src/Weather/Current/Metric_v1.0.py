from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CurrentWeatherMetricRequest(CamelCaseModel):
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the desired location.",
        ge=-90.0,
        le=90.0,
        examples=[60.192059],
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the desired location.",
        ge=-180.0,
        le=180.0,
        examples=[24.945831],
    )


class CurrentWeatherMetricResponse(CamelCaseModel):
    humidity: float = Field(
        ...,
        title="Current relative air humidity (%)",
        description="Current relative air humidity in percentages.",
        examples=[72],
    )
    pressure: float = Field(..., title="Current air pressure in hPa", examples=[1007])
    rain: bool = Field(
        ..., title="Rain status", description="If it's currently raining or not."
    )
    temp: float = Field(
        ...,
        title="Current temperature (°C)",
        description="Current temperature in Celsius.",
        examples=[17.3],
        ge=-273.15,
    )
    wind_speed: float = Field(
        ...,
        title="Current wind speed (m/s)",
        description="Current wind speed in meter per second.",
        examples=[2.1],
        ge=0,
    )
    wind_direction: float = Field(
        ...,
        title="Current wind direction",
        description="Current wind direction in meteorological wind direction degrees.",
        ge=0,
        le=360,
        examples=[220.0],
    )


DEFINITION = DataProductDefinition(
    version="1.0.1",
    title="Current weather in a given location",
    description="Common data points about the current weather with metric units in a given location. Simplified for example use, and not following industry standards.",
    request=CurrentWeatherMetricRequest,
    response=CurrentWeatherMetricResponse,
    tags=["Environment"],
)
