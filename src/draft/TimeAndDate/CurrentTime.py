from datetime import datetime
from enum import Enum

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class Country(str, Enum):
    AD = "ad"
    AE = "ae"
    AF = "af"
    AG = "ag"
    AI = "ai"
    AL = "al"
    AM = "am"
    AO = "ao"
    AQ = "aq"
    AR = "ar"
    AS = "as"
    AT = "at"
    AU = "au"
    AW = "aw"
    AX = "ax"
    AZ = "az"
    BA = "ba"
    BB = "bb"
    BD = "bd"
    BE = "be"
    BF = "bf"
    BG = "bg"
    BH = "bh"
    BI = "bi"
    BJ = "bj"
    BL = "bl"
    BM = "bm"
    BN = "bn"
    BO = "bo"
    BQ = "bq"
    BR = "br"
    BS = "bs"
    BT = "bt"
    BV = "bv"
    BW = "bw"
    BY = "by"
    BZ = "bz"
    CA = "ca"
    CC = "cc"
    CD = "cd"
    CF = "cf"
    CG = "cg"
    CH = "ch"
    CI = "ci"
    CK = "ck"
    CL = "cl"
    CM = "cm"
    CN = "cn"
    CO = "co"
    CR = "cr"
    CU = "cu"
    CV = "cv"
    CW = "cw"
    CX = "cx"
    CY = "cy"
    CZ = "cz"
    DE = "de"
    DJ = "dj"
    DK = "dk"
    DM = "dm"
    DO = "do"
    DZ = "dz"
    EC = "ec"
    EE = "ee"
    EG = "eg"
    EH = "eh"
    ER = "er"
    ES = "es"
    ET = "et"
    FI = "fi"
    FJ = "fj"
    FK = "fk"
    FM = "fm"
    FO = "fo"
    FR = "fr"
    GA = "ga"
    GB = "gb"
    GD = "gd"
    GE = "ge"
    GF = "gf"
    GG = "gg"
    GH = "gh"
    GI = "gi"
    GL = "gl"
    GM = "gm"
    GN = "gn"
    GP = "gp"
    GQ = "gq"
    GR = "gr"
    GS = "gs"
    GT = "gt"
    GU = "gu"
    GW = "gw"
    GY = "gy"
    HK = "hk"
    HM = "hm"
    HN = "hn"
    HR = "hr"
    HT = "ht"
    HU = "hu"
    ID = "id"
    IE = "ie"
    IL = "il"
    IM = "im"
    IN = "in"
    IO = "io"
    IQ = "iq"
    IR = "ir"
    IS = "is"
    IT = "it"
    JE = "je"
    JM = "jm"
    JO = "jo"
    JP = "jp"
    KE = "ke"
    KG = "kg"
    KH = "kh"
    KI = "ki"
    KM = "km"
    KN = "kn"
    KP = "kp"
    KR = "kr"
    KW = "kw"
    KY = "ky"
    KZ = "kz"
    LA = "la"
    LB = "lb"
    LC = "lc"
    LI = "li"
    LK = "lk"
    LR = "lr"
    LS = "ls"
    LT = "lt"
    LU = "lu"
    LV = "lv"
    LY = "ly"
    MA = "ma"
    MC = "mc"
    MD = "md"
    ME = "me"
    MF = "mf"
    MG = "mg"
    MH = "mh"
    MK = "mk"
    ML = "ml"
    MM = "mm"
    MN = "mn"
    MO = "mo"
    MP = "mp"
    MQ = "mq"
    MR = "mr"
    MS = "ms"
    MT = "mt"
    MU = "mu"
    MV = "mv"
    MW = "mw"
    MX = "mx"
    MY = "my"
    MZ = "mz"
    NA = "na"
    NC = "nc"
    NE = "ne"
    NF = "nf"
    NG = "ng"
    NI = "ni"
    NL = "nl"
    NO = "no"
    NP = "np"
    NR = "nr"
    NU = "nu"
    NZ = "nz"
    OM = "om"
    PA = "pa"
    PE = "pe"
    PF = "pf"
    PG = "pg"
    PH = "ph"
    PK = "pk"
    PL = "pl"
    PM = "pm"
    PN = "pn"
    PR = "pr"
    PS = "ps"
    PT = "pt"
    PW = "pw"
    PY = "py"
    QA = "qa"
    RE = "re"
    RO = "ro"
    RS = "rs"
    RU = "ru"
    RW = "rw"
    SA = "sa"
    SB = "sb"
    SC = "sc"
    SD = "sd"
    SE = "se"
    SG = "sg"
    SH = "sh"
    SI = "si"
    SJ = "sj"
    SK = "sk"
    SL = "sl"
    SM = "sm"
    SN = "sn"
    SO = "so"
    SR = "sr"
    SS = "ss"
    ST = "st"
    SV = "sv"
    SX = "sx"
    SY = "sy"
    SZ = "sz"
    TC = "tc"
    TD = "td"
    TF = "tf"
    TG = "tg"
    TH = "th"
    TJ = "tj"
    TK = "tk"
    TL = "tl"
    TM = "tm"
    TN = "tn"
    TO = "to"
    TR = "tr"
    TT = "tt"
    TV = "tv"
    TW = "tw"
    TZ = "tz"
    UA = "ua"
    UG = "ug"
    UM = "um"
    US = "us"
    UY = "uy"
    UZ = "uz"
    VA = "va"
    VC = "vc"
    VE = "ve"
    VG = "vg"
    VI = "vi"
    VN = "vn"
    VU = "vu"
    WF = "wf"
    WS = "ws"
    YE = "ye"
    YT = "yt"
    ZA = "za"
    ZM = "zm"
    ZW = "zw"


class CurrentTimeRequest(CamelCaseModel):
    country_code: Country = Field(title="ISO 3166-1 alpha-2 country code")


class CurrentTimeResponse(CamelCaseModel):
    current_time: str = Field(
        title="Current time in the desired country in RFC 3339 format"
    )


DEFINITION = DataProductDefinition(
    version="0.0.1",
    deprecated=True,
    title="Current time in a given country",
    description="Get the current time in a given country based on the ISO 3166-1 alpha-2 country code, formatted in RFC 3339 format",
    request=CurrentTimeRequest,
    response=CurrentTimeResponse,
)
