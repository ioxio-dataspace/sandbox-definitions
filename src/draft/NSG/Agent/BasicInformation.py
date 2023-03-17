from datetime import date
from enum import Enum
from typing import Optional

from converter import CamelCaseModel, DataProductDefinition
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


class ISO_3166_1_Alpha_2(str, Enum):
    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


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
    admin_unit_level_1: ISO_3166_1_Alpha_2 = Field(
        ...,
        title="Admin unit level 1",
        description="The name of the uppermost level of the address, almost always a "
        "country. ISO 3166 two character (Alpha 2) format",
        example="US",
    )
    admin_unit_level_2: Optional[str] = Field(
        None,
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
    description="In the Nordic Smart Government information exchange context the agent "
    'represents both registered organizations ("companies") and persons who are doing '
    "business without being registered organizations, usually as sole traders (sole "
    "proprietors). This data product definition returns basic information content for "
    "any agent.",
    request=BasicInformationRequest,
    response=BasicInformationResponse,
    summary="Agent Basic Information",
)
