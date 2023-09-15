from datetime import date
from enum import Enum
from typing import Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class BasicInformationRequest(CamelCaseModel):
    national_identifier: str = Field(
        ...,
        title="National Identifier",
        description="National identifier for a legal entity",
        example="2464491-9",
    )


class NordicLegalForm(str, Enum):
    NO_AAFY = "NO_AAFY"
    NO_ADOS = "NO_ADOS"
    NO_ANNA = "NO_ANNA"
    NO_ANS = "NO_ANS"
    NO_AS = "NO_AS"
    NO_ASA = "NO_ASA"
    NO_BA = "NO_BA"
    NO_BBL = "NO_BBL"
    NO_BEDR = "NO_BEDR"
    NO_BO = "NO_BO"
    NO_BRL = "NO_BRL"
    NO_DA = "NO_DA"
    NO_ENK = "NO_ENK"
    NO_ESEK = "NO_ESEK"
    NO_EOEFG = "NO_EOEFG"
    NO_FKF = "NO_FKF"
    NO_FLI = "NO_FLI"
    NO_FYLK = "NO_FYLK"
    NO_GFS = "NO_GFS"
    NO_IKJP = "NO_IKJP"
    NO_IKS = "NO_IKS"
    NO_KBO = "NO_KBO"
    NO_KF = "NO_KF"
    NO_KIRK = "NO_KIRK"
    NO_KOMM = "NO_KOMM"
    NO_KS = "NO_KS"
    NO_KTRF = "NO_KTRF"
    NO_NUF = "NO_NUF"
    NO_OPMV = "NO_OPMV"
    NO_ORGL = "NO_ORGL"
    NO_PERS = "NO_PERS"
    NO_PK = "NO_PK"
    NO_PRE = "NO_PRE"
    NO_SA = "NO_SA"
    NO_SAM = "NO_SAM"
    NO_SE = "NO_SE"
    NO_SF = "NO_SF"
    NO_SPA = "NO_SPA"
    NO_STAT = "NO_STAT"
    NO_STI = "NO_STI"
    NO_SAER = "NO_SAER"
    NO_TVAM = "NO_TVAM"
    NO_VPFO = "NO_VPFO"
    SE_I = "SE_I"
    SE_TSF = "SE_TSF"
    SE_MB = "SE_MB"
    SE_SE = "SE_SE"
    SE_SCE = "SE_SCE"
    SE_SF = "SE_SF"
    SE_HB = "SE_HB"
    SE_BAB = "SE_BAB"
    SE_EK = "SE_EK"
    SE_KB = "SE_KB"
    SE_SB = "SE_SB"
    SE_FOF = "SE_FOF"
    SE_OFB = "SE_OFB"
    SE_FAB = "SE_FAB"
    SE_KHF = "SE_KHF"
    SE_EEIG = "SE_EEIG"
    SE_EGTS = "SE_EGTS"
    SE_BRF = "SE_BRF"
    SE_BF = "SE_BF"
    SE_AB = "SE_AB"
    SE_BFL = "SE_BFL"
    SE_E = "SE_E"
    SE_EB = "SE_EB"
    SE_FL = "SE_FL"
    SE_S = "SE_S"
    FI_AYH = "FI_AYH"
    FI_AHVELL = "FI_AHVELL"
    FI_AHVE = "FI_AHVE"
    FI_ASH = "FI_ASH"
    FI_ASY = "FI_ASY"
    FI_AOY = "FI_AOY"
    FI_AY = "FI_AY"
    FI_EYHT = "FI_EYHT"
    FI_ESAA = "FI_ESAA"
    FI_EVL = "FI_EVL"
    FI_ELSYH = "FI_ELSYH"
    FI_ETS = "FI_ETS"
    FI_ETY = "FI_ETY"
    FI_EUOKKT = "FI_EUOKKT"
    FI_SCE = "FI_SCE"
    FI_SCP = "FI_SCP"
    FI_SE = "FI_SE"
    FI_EVLUT = "FI_EVLUT"
    FI_HYYH = "FI_HYYH"
    FI_KVJ = "FI_KVJ"
    FI_OYJ = "FI_OYJ"
    FI_VOJ = "FI_VOJ"
    FI_KK = "FI_KK"
    FI_KOY = "FI_KOY"
    FI_KVAKYH = "FI_KVAKYH"
    FI_KVY = "FI_KVY"
    FI_KY = "FI_KY"
    FI_KONK = "FI_KONK"
    FI_KUNTLL = "FI_KUNTLL"
    FI_KUNT = "FI_KUNT"
    FI_KUNTLLL = "FI_KUNTLLL"
    FI_KUNTYHT = "FI_KUNTYHT"
    FI_KP = "FI_KP"
    FI_LIY = "FI_LIY"
    FI_MHY = "FI_MHY"
    FI_MJUO = "FI_MJUO"
    FI_MUUKOY = "FI_MUUKOY"
    FI_MSAA = "FI_MSAA"
    FI_MTYH = "FI_MTYH"
    FI_MUVE = "FI_MUVE"
    FI_MYH = "FI_MYH"
    FI_MUYP = "FI_MUYP"
    FI_MUU = "FI_MUU"
    FI_MOHLO = "FI_MOHLO"
    FI_ORTO = "FI_ORTO"
    FI_OY = "FI_OY"
    FI_OK = "FI_OK"
    FI_OP = "FI_OP"
    FI_PY = "FI_PY"
    FI_PK = "FI_PK"
    FI_SL = "FI_SL"
    FI_SP = "FI_SP"
    FI_SAA = "FI_SAA"
    FI_TYH = "FI_TYH"
    FI_TEKA = "FI_TEKA"
    FI_TYKA = "FI_TYKA"
    FI_ULKO = "FI_ULKO"
    FI_VAKK = "FI_VAKK"
    FI_VOY = "FI_VOY"
    FI_VY = "FI_VY"
    FI_VALT = "FI_VALT"
    FI_VALTLL = "FI_VALTLL"
    FI_VEYHT = "FI_VEYHT"
    FI_YHTE = "FI_YHTE"
    FI_YHME = "FI_YHME"
    FI_YEH = "FI_YEH"
    FI_YO = "FI_YO"
    FI_UYK = "FI_UYK"


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


class LegalStatus(str, Enum):
    NORMAL = "NORMAL"
    LIQUIDATION = "LIQUIDATION"
    RESTRUCTURING = "RESTRUCTURING"
    BANKRUPTCY = "BANKRUPTCY"


class RegisteredAddress(CamelCaseModel):
    full_address: Optional[str] = Field(
        None,
        title="Full address",
        description="The complete address written as a string. Use of this property is "
        "recommended as it will not suffer any misunderstandings that might arise "
        "through the breaking up of an address into its component parts.",
        example="Tietotie 4 A 7, 00100 Helsinki, Finland",
        min_length=1,
        max_length=250,
    )
    thoroughfare: Optional[str] = Field(
        None,
        title="Thoroughfare",
        description="The name of a passage or way through from one location to "
        "another. A thoroughfare is usually a street, but it might be a waterway or "
        "some other feature.",
        example="Avenue des Champs-Élysées",
        min_length=1,
        max_length=40,
    )
    locator_designator: Optional[str] = Field(
        None,
        title="Locator designator",
        description="A number or sequence of characters that uniquely identifies the "
        "locator within the relevant scope. In simpler terms, this is the building "
        "number, apartment number, etc.",
        example="Flat 3, 17 or 3 A 4",
        min_length=1,
        max_length=10,
    )
    locator_name: Optional[str] = Field(
        None,
        title="Locator name",
        description="Proper noun(s) applied to the real world entity identified by the "
        "locator. The locator name could be the name of the property or complex, of "
        "the building or part of the building, or it could be the name of a room "
        "inside a building. The key difference between a locator and a locator name is "
        "that the latter is a proper name and is unlikely to include digits.",
        example="Shumann, Berlaymont (meeting room name)",
        min_length=1,
        max_length=40,
    )
    address_area: Optional[str] = Field(
        None,
        title="Address area",
        description="The name of a geographic area that groups Addresses. This would "
        "typically be part of a city, a neighbourhood or village. Address area is not "
        "an administrative unit.",
        example="Montmartre (in Paris)",
        min_length=1,
        max_length=40,
    )
    post_code: Optional[str] = Field(
        None,
        title="Post code",
        description="The code created and maintained for postal purposes to identify a "
        "subdivision of addresses and postal delivery points.",
        example="75000",
        min_length=1,
        max_length=10,
    )
    post_name: Optional[str] = Field(
        None,
        title="Post name",
        description="A name created and maintained for postal purposes to identify a "
        "subdivision of addresses and postal delivery points. Usually a city.",
        example="Paris",
        min_length=1,
        max_length=40,
    )
    po_box: Optional[str] = Field(
        None,
        title="PO box",
        description="A location designator for a postal delivery point at a post "
        "office, usually a number.",
        example="9383",
        min_length=1,
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
        example="Uusimaa",
        min_length=1,
        max_length=40,
    )
    address_id: Optional[str] = Field(
        None,
        title="Address id",
        description="A globally unique identifier for each instance of an Address. The "
        "concept of adding a globally unique identifier for each instance of an "
        "address is a crucial part of the INSPIRE data spec. A number of EU countries "
        "have already implemented an ID (a UUID) in their Address Register, among them "
        "Denmark.",
        example="123e4567-e89b-12d3-a456-42661417400",
        min_length=1,
        max_length=40,
    )


class BasicInformationResponse(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The name of the legal entity",
        example="Oy Example Ab",
    )
    legal_form: NordicLegalForm = Field(
        ...,
        title="Legal form",
        description="The [Nordic Legal Form code](https://koodistot.suomi.fi/"
        "codescheme;registryCode=verotus;schemeCode=LegalForm2) for the company.",
        example=NordicLegalForm.FI_OY,
    )
    legal_status: LegalStatus = Field(
        ...,
        title="Legal status",
        description="Status of the legal entity",
        example=LegalStatus.NORMAL,
    )
    registration_date: date = Field(
        ...,
        title="Registration date",
        description="Official registration date of the legal entity in the national "
        "trade registry",
    )
    registered_address: RegisteredAddress


DEFINITION = DataProductDefinition(
    version="0.0.1",
    deprecated=True,
    title="NSG Agent information",
    description="In the Nordic Smart Government information exchange context the agent "
    'represents both registered organizations ("companies") and persons who are doing '
    "business without being registered organizations, usually as sole traders (sole "
    "proprietors). This data product definition returns basic information content for "
    "any agent.",
    request=BasicInformationRequest,
    response=BasicInformationResponse,
)
