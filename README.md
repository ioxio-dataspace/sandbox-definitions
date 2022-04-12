# IOXIO Sandbox Nexus Definitions

This repository contains Data Product definitions for the IOXIO Sandbox nexus.

Specification for describing data product definitions can be found in
[./DataProducts/README.md](./DataProducts/README.md).

_Please note that this repository is under active development, and all the definitions
are subjects to change at any time._

# Repo structure

- [./src](./src) - Definition sources in python format
- [./DataProducts](./DataProducts) - Final Definitions as OpenAPI 3.0 specs
- [.github/workflows](.github/workflows) - Pre-configured CI workflows for validating
  and converting definitions from sources

# Getting started

## Adding new Data Product Definition

There are two ways of contribution:

1. **Submit OpenAPI spec directly**

   For example, to add a definition for `Foo/Bar`:

   - create `DataProducts/<version>/Foo/Bar.json`
   - make sure you follow the data product definition
     [guidelines](./DataProducts/README.md)

2. **Submit definition as python file**

   If you're familiar with python and
   [pydantic](https://github.com/samuelcolvin/pydantic) library, you may find it easier
   to create the definition as a set of pydantic models.

   For example, to add a definition for `Foo/Bar`:

   - create `DataProducts/<version>/Foo/Bar.py`

   You have 2 options to use the converter:

   1. By running `pre-commit install` after cloning the repo. Then definitions will be
      converted automatically before each commit
   2. By creating a PR to the `main` branch. CI workflow will run the automation and
      push updated/generated files if needed.

## Test version of definitions

Everyone can submit to this repo whatever definitions they seem appropriate. It will
allow to create data products using these definitions in IOXIO Sandbox Nexus and
experiment with the system. In order to do this:

1. Fork this repository
2. Create your definitions under `src/test/<your_github_username>/` if you're familiar
   with Python approach, or directly under `DataProducts/test/<your_github_username>` if
   you know what you're doing
3. Submit a PR and wait for CI Workflow to run and validate the changes
4. Once PR is merged, it's possible to use the definitions in IOXIO Sandbox Nexus

## Python sources

Each python file located in the `src` folder is treated as a Data Product definition.

For example, `src/AirQuality/Current.py` defines `AirQuality/Current` data product.

These files are then converted to OpenAPI 3.0 specs, which are final forms of
definitions. To make the converter work correctly, each file must follow the same
structure:

```python
from pydantic import Field

from converter import CamelCaseModel, DataProductDefinition


class Request(CamelCaseModel):
    ...


class Response(CamelCaseModel):
    ...


DEFINITION = DataProductDefinition(
    description="...",
    request=Request,
    response=Response,
    route_description="...",
    summary="...",
)

```

Considering `CamelCaseModel` is a subclass of `pydantic`'s `BaseModel`, it's better to
understand how to use this library. Please read
[pydantic](https://pydantic-docs.helpmanual.io/)'s documentation if you're not familiar
with it yet.

Each data product definition represented as python file must define a `DEFINITION`
variable which is an instance of `DataProductDefinition` class.

DataProductDefinition is a structure consisting of:

- `summary`

  Summary used in top of OpenAPI spec

- `description`

  Data product description, used in top of OpenAPI spec

- `request`

  pydantic model describing body of POST request

- `response`

  pydantic model describing expected response from data source

- `route_summary`

  Summary for the POST route

- `route_description`

  Description for the POST route

- `generic_description`

  You may omit providing `summary`, `description`, `route_summary` and
  `route_description` if you define this field. Others will be generated automatically
  based on it. Use something brief and meaningful, like "Company Recommendations" or
  "Cargo receipt".

### Example

There's an example of Data Product Definition for current weather:

```python
from pydantic import Field

from converter import CamelCaseModel, DataProductDefinition


class CurrentWeatherMetricRequest(CamelCaseModel):
    lat: float = Field(
        ...,
        title="Latitude",
        description="The latitude coordinate of the desired location",
        ge=-90.0,
        le=90.0,
        example=60.192059,
    )
    lon: float = Field(
        ...,
        title="Longitude",
        description="The longitude coordinate of the desired location",
        ge=-180.0,
        le=180.0,
        example=24.945831,
    )


class CurrentWeatherMetricResponse(CamelCaseModel):
    humidity: float = Field(..., title="Current relative air humidity in %", example=72)
    pressure: float = Field(..., title="Current air pressure in hPa", example=1007)
    rain: bool = Field(
        ..., title="Rain status", description="If it's currently raining or not."
    )
    temp: float = Field(
        ..., title="Current temperature in Celsius", example=17.3, ge=-273.15
    )
    wind_speed: float = Field(..., title="Current wind speed in m/s", example=2.1, ge=0)
    wind_direction: float = Field(
        ...,
        title="Current wind direction in meteorological wind direction degrees",
        ge=0,
        le=360,
        example=220.0,
    )


DEFINITION = DataProductDefinition(
    description="Data Product for current weather with metric units",
    request=CurrentWeatherMetricRequest,
    response=CurrentWeatherMetricResponse,
    route_description="Current weather in metric units",
    summary="Current Weather (Metric)",
)
```
