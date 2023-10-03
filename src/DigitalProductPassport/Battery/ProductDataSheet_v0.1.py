from enum import Enum
from typing import Set

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CellType(str, Enum):
    LTO = "lithium-titanate"
    LIPO = "lithium-ion polymer"


class IPCode(str, Enum):
    IP5X = "IP5X"
    IP50 = "IP50"
    IP51 = "IP51"
    IP52 = "IP52"
    IP53 = "IP53"
    IP54 = "IP54"
    IP54K = "IP54K"
    IP55 = "IP55"
    IP56 = "IP56"
    IP56K = "IP56K"
    IP57 = "IP57"
    IP58 = "IP58"
    IP59K = "IP59K"
    IP5KX = "IP5KX"
    IP5K0 = "IP5K0"
    IP5K1 = "IP5K1"
    IP5K2 = "IP5K2"
    IP5K3 = "IP5K3"
    IP5K4 = "IP5K4"
    IP5K4K = "IP5K4K"
    IP5K5 = "IP5K5"
    IP5K6 = "IP5K6"
    IP5K6K = "IP5K6K"
    IP5K7 = "IP5K7"
    IP5K8 = "IP5K8"
    IP5K9K = "IP5K9K"
    IP6X = "IP6X"
    IP60 = "IP60"
    IP61 = "IP61"
    IP62 = "IP62"
    IP63 = "IP63"
    IP64 = "IP64"
    IP64K = "IP64K"
    IP65 = "IP65"
    IP66 = "IP66"
    IP66K = "IP66K"
    IP67 = "IP67"
    IP68 = "IP68"
    IP69K = "IP69K"
    IP6KX = "IP6KX"
    IP6K0 = "IP6K0"
    IP6K1 = "IP6K1"
    IP6K2 = "IP6K2"
    IP6K3 = "IP6K3"
    IP6K4 = "IP6K4"
    IP6K4K = "IP6K4K"
    IP6K5 = "IP6K5"
    IP6K6 = "IP6K6"
    IP6K6K = "IP6K6K"
    IP6K7 = "IP6K7"
    IP6K8 = "IP6K8"
    IP6K9K = "IP6K9K"


class ComplianceStandard(str, Enum):
    ECE_R100 = "ECE R100"
    ECE_R10 = "ECE R10"
    UN_38_3 = "UN 38.3"
    ISO_16750 = "ISO 16750"
    IEC_61508_SIL_2 = "IEC 61508 SIL 2"
    ISO_13849_PL_C = "ISO 13849 PL C"
    IEC_62061_SIL_2 = "IEC 62061 SIL 2"


class Voltage(CamelCaseModel):
    min: float = Field(
        ...,
        title="Minimum voltage",
        example=38.0,
    )
    max: float = Field(
        ...,
        title="Maximum voltage",
        example=56.0,
    )
    nominal: float = Field(
        ...,
        title="Nominal voltage",
        example=48.3,
    )


class Dimensions(CamelCaseModel):
    length: int = Field(
        ...,
        title="Length [mm]",
        example=483,
    )
    width: int = Field(
        ...,
        title="Width [mm]",
        example=380,
    )
    height: int = Field(
        ...,
        title="Height [mm]",
        example=160,
    )


class OperatingTemperature(CamelCaseModel):
    min: float = Field(
        ...,
        title="Minimum operating temperature [°C]",
        example=-30.0,
    )
    max: float = Field(
        ...,
        title="Maximum operating temperature [°C]",
        example=55.0,
    )
    recommended_min: float = Field(
        ...,
        title="Minimum recommended operating temperature [°C]",
        example=5.0,
    )
    recommended_max: float = Field(
        ...,
        title="Maximum recommended operating temperature [°C]",
        example=35,
    )


class BatteryDataRequest(CamelCaseModel):
    product: str = Field(
        ...,
        title="Product identifier",
        description="Technical product identifier used by the manufacturer",
        example="battery-100wh-s",
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier of the product",
        example="177389-09633",
    )


class BatteryDataResponse(CamelCaseModel):
    manufacturer: str = Field(
        ...,
        title="Manufacturer",
        description="The manufacturer of the battery",
        example="Valmet Automotive",
    )
    product: str = Field(
        ...,
        title="Product identifier",
        description="Technical product identifier used by the manufacturer",
        example="battery-100wh-s",
    )
    id: str = Field(
        ...,
        title="Identifier",
        description="Unique identifier of the product",
        example="177389-09633",
    )
    name: str = Field(
        ...,
        title="Product Name",
        example="Modular Power Pack, 48 V",
    )
    cell_type: CellType = Field(
        ...,
        title="Cell Type",
        example=CellType.LTO,
    )
    capacity: float = Field(
        ...,
        title="Capacity",
        description="Battery capacity in kWh",
        example=2.2,
    )
    energy: float = Field(
        ...,
        title="Energy (Ah)",
        description="Energy, Ah [1C @ 25°C]",
        example=46.0,
    )
    voltage: Voltage = Field(
        ...,
        title="Voltage",
        description="Information about the voltage of the battery",
    )
    peak_discharging_power: float = Field(
        ...,
        title="Peak Discharging Power [kW]",
        example=20.0,
    )
    peak_charging_power: float = Field(
        ...,
        title="Peak Charging Power [kW]",
        example=20.0,
    )
    continuous_power: float = Field(
        ...,
        title="Continuous Power [kW]",
        example=10.0,
    )
    standby_consumption: float = Field(
        ...,
        title="Standby Power Consumption [W]",
        example=1.0,
    )
    cycle_life: int = Field(
        ...,
        title="Cycle Life",
        description="Minimum number of cycles the battery can be recharged to at least 80% of initial capacity",
        example=20000,
    )
    dimensions: Dimensions = Field(
        ...,
        title="Dimensions",
        description="Physical dimensions of the battery",
    )
    weight: float = Field(
        ...,
        title="Weight [kg]",
        description="Total dry weight [kg]",
        example=41.0,
    )
    operating_temperature: OperatingTemperature = Field(
        ...,
        title="Operating Temperature [°C]",
    )
    ip_rating: IPCode = Field(
        ...,
        title="IP Rating",
        example=IPCode.IP6K9K,
    )
    max_coolant_pressure: float = Field(
        ...,
        title="Max Coolant Pressure [bar]",
        example=3.5,
    )
    standards_compliance: Set[str] = Field(
        title="Standards Compliance",
        example={
            ComplianceStandard.ECE_R100,
            ComplianceStandard.ECE_R10,
            ComplianceStandard.UN_38_3,
            ComplianceStandard.ISO_16750,
            ComplianceStandard.IEC_61508_SIL_2,
            ComplianceStandard.ISO_13849_PL_C,
            ComplianceStandard.IEC_62061_SIL_2,
        },
    )


DEFINITION = DataProductDefinition(
    version="0.1.0",
    title="Battery product data sheet",
    description="Technical details of a battery such as capacity and voltage",
    request=BatteryDataRequest,
    response=BatteryDataResponse,
)
