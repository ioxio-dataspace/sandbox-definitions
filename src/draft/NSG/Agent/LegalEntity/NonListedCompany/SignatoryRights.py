from datetime import date
from enum import Enum
from typing import List, Optional

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class ISO_3166_1_Alpha_3(str, Enum):
    AFG = "AFG"
    ALB = "ALB"
    DZA = "DZA"
    ASM = "ASM"
    AND = "AND"
    AGO = "AGO"
    AIA = "AIA"
    ATA = "ATA"
    ATG = "ATG"
    ARG = "ARG"
    ARM = "ARM"
    ABW = "ABW"
    AUS = "AUS"
    AUT = "AUT"
    AZE = "AZE"
    BHS = "BHS"
    BHR = "BHR"
    BGD = "BGD"
    BRB = "BRB"
    BLR = "BLR"
    BEL = "BEL"
    BLZ = "BLZ"
    BEN = "BEN"
    BMU = "BMU"
    BTN = "BTN"
    BOL = "BOL"
    BIH = "BIH"
    BWA = "BWA"
    BVT = "BVT"
    BRA = "BRA"
    IOT = "IOT"
    BRN = "BRN"
    BGR = "BGR"
    BFA = "BFA"
    BDI = "BDI"
    KHM = "KHM"
    CMR = "CMR"
    CAN = "CAN"
    CPV = "CPV"
    CYM = "CYM"
    CAF = "CAF"
    TCD = "TCD"
    CHL = "CHL"
    CHN = "CHN"
    CXR = "CXR"
    CCK = "CCK"
    COL = "COL"
    COM = "COM"
    COG = "COG"
    COD = "COD"
    COK = "COK"
    CRI = "CRI"
    CIV = "CIV"
    HRV = "HRV"
    CUB = "CUB"
    CYP = "CYP"
    CZE = "CZE"
    DNK = "DNK"
    DJI = "DJI"
    DMA = "DMA"
    DOM = "DOM"
    ECU = "ECU"
    EGY = "EGY"
    SLV = "SLV"
    GNQ = "GNQ"
    ERI = "ERI"
    EST = "EST"
    ETH = "ETH"
    FLK = "FLK"
    FRO = "FRO"
    FJI = "FJI"
    FIN = "FIN"
    FRA = "FRA"
    GUF = "GUF"
    PYF = "PYF"
    ATF = "ATF"
    GAB = "GAB"
    GMB = "GMB"
    GEO = "GEO"
    DEU = "DEU"
    GHA = "GHA"
    GIB = "GIB"
    GRC = "GRC"
    GRL = "GRL"
    GRD = "GRD"
    GLP = "GLP"
    GUM = "GUM"
    GTM = "GTM"
    GGY = "GGY"
    GIN = "GIN"
    GNB = "GNB"
    GUY = "GUY"
    HTI = "HTI"
    HMD = "HMD"
    VAT = "VAT"
    HND = "HND"
    HKG = "HKG"
    HUN = "HUN"
    ISL = "ISL"
    IND = "IND"
    IDN = "IDN"
    IRN = "IRN"
    IRQ = "IRQ"
    IRL = "IRL"
    IMN = "IMN"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JPN = "JPN"
    JEY = "JEY"
    JOR = "JOR"
    KAZ = "KAZ"
    KEN = "KEN"
    KIR = "KIR"
    PRK = "PRK"
    KOR = "KOR"
    KWT = "KWT"
    KGZ = "KGZ"
    LAO = "LAO"
    LVA = "LVA"
    LBN = "LBN"
    LSO = "LSO"
    LBR = "LBR"
    LBY = "LBY"
    LIE = "LIE"
    LTU = "LTU"
    LUX = "LUX"
    MAC = "MAC"
    MKD = "MKD"
    MDG = "MDG"
    MWI = "MWI"
    MYS = "MYS"
    MDV = "MDV"
    MLI = "MLI"
    MLT = "MLT"
    MHL = "MHL"
    MTQ = "MTQ"
    MRT = "MRT"
    MUS = "MUS"
    MYT = "MYT"
    MEX = "MEX"
    FSM = "FSM"
    MDA = "MDA"
    MCO = "MCO"
    MNG = "MNG"
    MNE = "MNE"
    MSR = "MSR"
    MAR = "MAR"
    MOZ = "MOZ"
    MMR = "MMR"
    NAM = "NAM"
    NRU = "NRU"
    NPL = "NPL"
    NLD = "NLD"
    ANT = "ANT"
    NCL = "NCL"
    NZL = "NZL"
    NIC = "NIC"
    NER = "NER"
    NGA = "NGA"
    NIU = "NIU"
    NFK = "NFK"
    MNP = "MNP"
    NOR = "NOR"
    OMN = "OMN"
    PAK = "PAK"
    PLW = "PLW"
    PSE = "PSE"
    PAN = "PAN"
    PNG = "PNG"
    PRY = "PRY"
    PER = "PER"
    PHL = "PHL"
    PCN = "PCN"
    POL = "POL"
    PRT = "PRT"
    PRI = "PRI"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    SHN = "SHN"
    KNA = "KNA"
    LCA = "LCA"
    SPM = "SPM"
    VCT = "VCT"
    WSM = "WSM"
    SMR = "SMR"
    STP = "STP"
    SAU = "SAU"
    SEN = "SEN"
    SRB = "SRB"
    SYC = "SYC"
    SLE = "SLE"
    SGP = "SGP"
    SVK = "SVK"
    SVN = "SVN"
    SLB = "SLB"
    SOM = "SOM"
    ZAF = "ZAF"
    SGS = "SGS"
    SSD = "SSD"
    ESP = "ESP"
    LKA = "LKA"
    SDN = "SDN"
    SUR = "SUR"
    SJM = "SJM"
    SWZ = "SWZ"
    SWE = "SWE"
    CHE = "CHE"
    SYR = "SYR"
    TWN = "TWN"
    TJK = "TJK"
    TZA = "TZA"
    THA = "THA"
    TLS = "TLS"
    TGO = "TGO"
    TKL = "TKL"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TKM = "TKM"
    TCA = "TCA"
    TUV = "TUV"
    UGA = "UGA"
    UKR = "UKR"
    ARE = "ARE"
    GBR = "GBR"
    USA = "USA"
    UMI = "UMI"
    URY = "URY"
    UZB = "UZB"
    VUT = "VUT"
    VEN = "VEN"
    VNM = "VNM"
    VGB = "VGB"
    VIR = "VIR"
    WLF = "WLF"
    ESH = "ESH"
    YEM = "YEM"
    ZMB = "ZMB"
    ZWE = "ZWE"


class Role(str, Enum):
    DIRECTOR = "director"
    DEPUTY_DIRECTOR = "deputy director"
    CHAIRPERSON = "chairperson"
    BOARD_MEMBER = "board member"
    DEPUTY_BOARD_MEMBER = "deputy board member"
    OTHER = "other"


class SignatoryRights(CamelCaseModel):
    role: Role = Field(
        ...,
        title="Role",
        example=Role.CHAIRPERSON,
        description="The role of the person that has a signing right in the company",
    )
    personal_id: Optional[str] = Field(
        None,
        title="Personal ID",
        description="The ID of a person if exists, e.g. social security number or "
        "similar",
        example="1129955131",
        max_length=40,
    )
    given_name: str = Field(
        ...,
        title="Given name",
        description="The first name that the person is being called by",
        example="Mary",
        max_length=250,
    )
    middle_names: str = Field(
        ...,
        title="Middle names",
        description="All the middle names of the person",
        example="Juliet Olive",
        max_length=250,
    )
    last_name: str = Field(
        ...,
        title="Last name",
        description="The person's current family name",
        example="Deo",
        max_length=250,
    )
    date_of_birth: date = Field(
        ...,
        title="Date of birth",
        description="The birth day of a person",
        example=date(1976, 4, 16),
    )
    nationality: ISO_3166_1_Alpha_3 = Field(
        ...,
        title="Nationality",
        description="The nationality of a person",
        example=ISO_3166_1_Alpha_3.USA,
    )

    full_address: Optional[str] = Field(
        None,
        title="Full address",
        description="The complete address written as a string. Use of this property is "
        "recommended as it will not suffer any misunderstandings that might arise "
        "through the breaking up of an address into its component parts.",
        example="Tietotie 4 A 7, 00100 Helsinki, Finland",
        max_length=250,
    )

    thoroughfare: Optional[str] = Field(
        None,
        title="Thoroughfare",
        description="The name of a passage or way through from one location to "
        "another. A thoroughfare is usually a street, but it might be a waterway or "
        "some other feature.",
        example="Avenue des Champs-Élysées",
        max_length=40,
    )
    locator_designator: Optional[str] = Field(
        None,
        title="Locator designator",
        description="A number or sequence of characters that uniquely identifies the "
        "locator within the relevant scope. In simpler terms, this is the building "
        "number, apartment number, etc.",
        example="Flat 3, 17 or 3 A 4",
        max_length=10,
    )
    locator_name: Optional[str] = Field(
        None,
        title="Locator name",
        description="Proper noun(s) applied to the real world entity identified by the "
        "locator. The locator name could be the name of the property or complex, of "
        "the building or part of the building, or it could be the name of a room "
        "inside a building. The key difference between a locator designator and a "
        "locator name is that the latter is a proper name and is unlikely to include "
        "digits.",
        example="Shumann, Berlaymont building",
        max_length=40,
    )
    address_area: Optional[str] = Field(
        None,
        title="Address area",
        description="The name of a geographic area that groups Addresses. This would "
        "typically be part of a city, a neighbourhood or village. Address area is not "
        "an administrative unit.",
        example="Montmartre (in Paris)",
        max_length=40,
    )
    post_code: Optional[str] = Field(
        None,
        title="Post code",
        description="The code created and maintained for postal purposes to identify a "
        "subdivision of addresses and postal delivery points.",
        example="75000",
        max_length=10,
    )
    post_name: Optional[str] = Field(
        None,
        title="Post name",
        description="A name created and maintained for postal purposes to identify a "
        "subdivision of addresses and postal delivery points. Usually a city.",
        example="Paris",
        max_length=40,
    )
    po_box: Optional[str] = Field(
        None,
        title="PO box",
        description="A location designator for a postal delivery point at a post "
        "office, usually a number.",
        example="9383",
        max_length=10,
    )
    admin_unit_level_1: Optional[ISO_3166_1_Alpha_3] = Field(
        None,
        alias="adminUnitLevel1",
        title="Admin unit level 1",
        description="The name of the uppermost level of the address, almost always a "
        "country. ISO 3166 three character (Alpha 3) format.",
        example=ISO_3166_1_Alpha_3.USA,
    )
    admin_unit_level_2: Optional[str] = Field(
        None,
        alias="adminUnitLevel2",
        title="Admin unit level 2",
        description="The name of a secondary level/region of the address, usually a "
        "county, state or other such area that typically encompasses several "
        "localities. Values could be a region or province, more granular than level 1.",
        example="Lapland",
        max_length=40,
    )


class SignatoryRightsRequest(CamelCaseModel):
    national_identifier: str = Field(
        ...,
        title="National identifier",
        description="The national identifier of the non-listed company issued by the "
        "trade register",
        example="FIN: 2464491-9 / SWE: 5560125791 / NOR: 923609016",
        max_length=40,
    )


class SignatoryRightsResponse(CamelCaseModel):
    signing_rights: List[SignatoryRights] = Field(
        ...,
        title="Signing rights",
        description="The list of representatives that have signing rights for the "
        "company",
    )


DEFINITION = DataProductDefinition(
    description="The list of representation rights of a legal entity",
    request=SignatoryRightsRequest,
    response=SignatoryRightsResponse,
    summary="Non-listed Company Signatory Rights",
    requires_authorization=True,
    requires_consent=True,
)
