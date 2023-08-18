from datetime import date
from enum import Enum
from typing import List, Optional

from definition_tooling.converter import CamelCaseModel, DataProductDefinition
from pydantic import EmailStr, Field


class IndustrySector(str, Enum):
    NACE_01 = "01"
    NACE_01_1 = "01.1"
    NACE_01_11 = "01.11"
    NACE_01_12 = "01.12"
    NACE_01_13 = "01.13"
    NACE_01_14 = "01.14"
    NACE_01_15 = "01.15"
    NACE_01_16 = "01.16"
    NACE_01_19 = "01.19"
    NACE_01_2 = "01.2"
    NACE_01_21 = "01.21"
    NACE_01_22 = "01.22"
    NACE_01_23 = "01.23"
    NACE_01_24 = "01.24"
    NACE_01_25 = "01.25"
    NACE_01_26 = "01.26"
    NACE_01_27 = "01.27"
    NACE_01_28 = "01.28"
    NACE_01_29 = "01.29"
    NACE_01_3 = "01.3"
    NACE_01_30 = "01.30"
    NACE_01_4 = "01.4"
    NACE_01_41 = "01.41"
    NACE_01_42 = "01.42"
    NACE_01_43 = "01.43"
    NACE_01_44 = "01.44"
    NACE_01_45 = "01.45"
    NACE_01_46 = "01.46"
    NACE_01_47 = "01.47"
    NACE_01_49 = "01.49"
    NACE_01_5 = "01.5"
    NACE_01_50 = "01.50"
    NACE_01_6 = "01.6"
    NACE_01_61 = "01.61"
    NACE_01_62 = "01.62"
    NACE_01_63 = "01.63"
    NACE_01_64 = "01.64"
    NACE_01_7 = "01.7"
    NACE_01_70 = "01.70"
    NACE_02 = "02"
    NACE_02_1 = "02.1"
    NACE_02_10 = "02.10"
    NACE_02_2 = "02.2"
    NACE_02_20 = "02.20"
    NACE_02_3 = "02.3"
    NACE_02_30 = "02.30"
    NACE_02_4 = "02.4"
    NACE_02_40 = "02.40"
    NACE_03 = "03"
    NACE_03_1 = "03.1"
    NACE_03_11 = "03.11"
    NACE_03_12 = "03.12"
    NACE_03_2 = "03.2"
    NACE_03_21 = "03.21"
    NACE_03_22 = "03.22"
    NACE_05 = "05"
    NACE_05_1 = "05.1"
    NACE_05_10 = "05.10"
    NACE_05_2 = "05.2"
    NACE_05_20 = "05.20"
    NACE_06 = "06"
    NACE_06_1 = "06.1"
    NACE_06_10 = "06.10"
    NACE_06_2 = "06.2"
    NACE_06_20 = "06.20"
    NACE_07 = "07"
    NACE_07_1 = "07.1"
    NACE_07_10 = "07.10"
    NACE_07_2 = "07.2"
    NACE_07_21 = "07.21"
    NACE_07_29 = "07.29"
    NACE_08 = "08"
    NACE_08_1 = "08.1"
    NACE_08_11 = "08.11"
    NACE_08_12 = "08.12"
    NACE_08_9 = "08.9"
    NACE_08_91 = "08.91"
    NACE_08_92 = "08.92"
    NACE_08_93 = "08.93"
    NACE_08_99 = "08.99"
    NACE_09 = "09"
    NACE_09_1 = "09.1"
    NACE_09_10 = "09.10"
    NACE_09_9 = "09.9"
    NACE_09_90 = "09.90"
    NACE_10 = "10"
    NACE_10_1 = "10.1"
    NACE_10_11 = "10.11"
    NACE_10_12 = "10.12"
    NACE_10_13 = "10.13"
    NACE_10_2 = "10.2"
    NACE_10_20 = "10.20"
    NACE_10_3 = "10.3"
    NACE_10_31 = "10.31"
    NACE_10_32 = "10.32"
    NACE_10_39 = "10.39"
    NACE_10_4 = "10.4"
    NACE_10_41 = "10.41"
    NACE_10_42 = "10.42"
    NACE_10_5 = "10.5"
    NACE_10_51 = "10.51"
    NACE_10_52 = "10.52"
    NACE_10_6 = "10.6"
    NACE_10_61 = "10.61"
    NACE_10_62 = "10.62"
    NACE_10_7 = "10.7"
    NACE_10_71 = "10.71"
    NACE_10_72 = "10.72"
    NACE_10_73 = "10.73"
    NACE_10_8 = "10.8"
    NACE_10_81 = "10.81"
    NACE_10_82 = "10.82"
    NACE_10_83 = "10.83"
    NACE_10_84 = "10.84"
    NACE_10_85 = "10.85"
    NACE_10_86 = "10.86"
    NACE_10_89 = "10.89"
    NACE_10_9 = "10.9"
    NACE_10_91 = "10.91"
    NACE_10_92 = "10.92"
    NACE_11 = "11"
    NACE_11_0 = "11.0"
    NACE_11_01 = "11.01"
    NACE_11_02 = "11.02"
    NACE_11_03 = "11.03"
    NACE_11_04 = "11.04"
    NACE_11_05 = "11.05"
    NACE_11_06 = "11.06"
    NACE_11_07 = "11.07"
    NACE_12 = "12"
    NACE_12_0 = "12.0"
    NACE_12_00 = "12.00"
    NACE_13 = "13"
    NACE_13_1 = "13.1"
    NACE_13_10 = "13.10"
    NACE_13_2 = "13.2"
    NACE_13_20 = "13.20"
    NACE_13_3 = "13.3"
    NACE_13_30 = "13.30"
    NACE_13_9 = "13.9"
    NACE_13_91 = "13.91"
    NACE_13_92 = "13.92"
    NACE_13_93 = "13.93"
    NACE_13_94 = "13.94"
    NACE_13_95 = "13.95"
    NACE_13_96 = "13.96"
    NACE_13_99 = "13.99"
    NACE_14 = "14"
    NACE_14_1 = "14.1"
    NACE_14_11 = "14.11"
    NACE_14_12 = "14.12"
    NACE_14_13 = "14.13"
    NACE_14_14 = "14.14"
    NACE_14_19 = "14.19"
    NACE_14_2 = "14.2"
    NACE_14_20 = "14.20"
    NACE_14_3 = "14.3"
    NACE_14_31 = "14.31"
    NACE_14_39 = "14.39"
    NACE_15 = "15"
    NACE_15_1 = "15.1"
    NACE_15_11 = "15.11"
    NACE_15_12 = "15.12"
    NACE_15_2 = "15.2"
    NACE_15_20 = "15.20"
    NACE_16 = "16"
    NACE_16_1 = "16.1"
    NACE_16_10 = "16.10"
    NACE_16_2 = "16.2"
    NACE_16_21 = "16.21"
    NACE_16_22 = "16.22"
    NACE_16_23 = "16.23"
    NACE_16_24 = "16.24"
    NACE_16_29 = "16.29"
    NACE_17 = "17"
    NACE_17_1 = "17.1"
    NACE_17_11 = "17.11"
    NACE_17_12 = "17.12"
    NACE_17_2 = "17.2"
    NACE_17_21 = "17.21"
    NACE_17_22 = "17.22"
    NACE_17_23 = "17.23"
    NACE_17_24 = "17.24"
    NACE_17_29 = "17.29"
    NACE_18 = "18"
    NACE_18_1 = "18.1"
    NACE_18_11 = "18.11"
    NACE_18_12 = "18.12"
    NACE_18_13 = "18.13"
    NACE_18_14 = "18.14"
    NACE_18_2 = "18.2"
    NACE_18_20 = "18.20"
    NACE_19 = "19"
    NACE_19_1 = "19.1"
    NACE_19_10 = "19.10"
    NACE_19_2 = "19.2"
    NACE_19_20 = "19.20"
    NACE_20 = "20"
    NACE_20_1 = "20.1"
    NACE_20_11 = "20.11"
    NACE_20_12 = "20.12"
    NACE_20_13 = "20.13"
    NACE_20_14 = "20.14"
    NACE_20_15 = "20.15"
    NACE_20_16 = "20.16"
    NACE_20_17 = "20.17"
    NACE_20_2 = "20.2"
    NACE_20_20 = "20.20"
    NACE_20_3 = "20.3"
    NACE_20_30 = "20.30"
    NACE_20_4 = "20.4"
    NACE_20_41 = "20.41"
    NACE_20_42 = "20.42"
    NACE_20_5 = "20.5"
    NACE_20_51 = "20.51"
    NACE_20_52 = "20.52"
    NACE_20_53 = "20.53"
    NACE_20_59 = "20.59"
    NACE_20_6 = "20.6"
    NACE_20_60 = "20.60"
    NACE_21 = "21"
    NACE_21_1 = "21.1"
    NACE_21_10 = "21.10"
    NACE_21_2 = "21.2"
    NACE_21_20 = "21.20"
    NACE_22 = "22"
    NACE_22_1 = "22.1"
    NACE_22_11 = "22.11"
    NACE_22_19 = "22.19"
    NACE_22_2 = "22.2"
    NACE_22_21 = "22.21"
    NACE_22_22 = "22.22"
    NACE_22_23 = "22.23"
    NACE_22_29 = "22.29"
    NACE_23 = "23"
    NACE_23_1 = "23.1"
    NACE_23_11 = "23.11"
    NACE_23_12 = "23.12"
    NACE_23_13 = "23.13"
    NACE_23_14 = "23.14"
    NACE_23_19 = "23.19"
    NACE_23_2 = "23.2"
    NACE_23_20 = "23.20"
    NACE_23_3 = "23.3"
    NACE_23_31 = "23.31"
    NACE_23_32 = "23.32"
    NACE_23_4 = "23.4"
    NACE_23_41 = "23.41"
    NACE_23_42 = "23.42"
    NACE_23_43 = "23.43"
    NACE_23_44 = "23.44"
    NACE_23_49 = "23.49"
    NACE_23_5 = "23.5"
    NACE_23_51 = "23.51"
    NACE_23_52 = "23.52"
    NACE_23_6 = "23.6"
    NACE_23_61 = "23.61"
    NACE_23_62 = "23.62"
    NACE_23_63 = "23.63"
    NACE_23_64 = "23.64"
    NACE_23_65 = "23.65"
    NACE_23_69 = "23.69"
    NACE_23_7 = "23.7"
    NACE_23_70 = "23.70"
    NACE_23_9 = "23.9"
    NACE_23_91 = "23.91"
    NACE_23_99 = "23.99"
    NACE_24 = "24"
    NACE_24_1 = "24.1"
    NACE_24_10 = "24.10"
    NACE_24_2 = "24.2"
    NACE_24_20 = "24.20"
    NACE_24_3 = "24.3"
    NACE_24_31 = "24.31"
    NACE_24_32 = "24.32"
    NACE_24_33 = "24.33"
    NACE_24_34 = "24.34"
    NACE_24_4 = "24.4"
    NACE_24_41 = "24.41"
    NACE_24_42 = "24.42"
    NACE_24_43 = "24.43"
    NACE_24_44 = "24.44"
    NACE_24_45 = "24.45"
    NACE_24_46 = "24.46"
    NACE_24_5 = "24.5"
    NACE_24_51 = "24.51"
    NACE_24_52 = "24.52"
    NACE_24_53 = "24.53"
    NACE_24_54 = "24.54"
    NACE_25 = "25"
    NACE_25_1 = "25.1"
    NACE_25_11 = "25.11"
    NACE_25_12 = "25.12"
    NACE_25_2 = "25.2"
    NACE_25_21 = "25.21"
    NACE_25_29 = "25.29"
    NACE_25_3 = "25.3"
    NACE_25_30 = "25.30"
    NACE_25_4 = "25.4"
    NACE_25_40 = "25.40"
    NACE_25_5 = "25.5"
    NACE_25_50 = "25.50"
    NACE_25_6 = "25.6"
    NACE_25_61 = "25.61"
    NACE_25_62 = "25.62"
    NACE_25_7 = "25.7"
    NACE_25_71 = "25.71"
    NACE_25_72 = "25.72"
    NACE_25_73 = "25.73"
    NACE_25_9 = "25.9"
    NACE_25_91 = "25.91"
    NACE_25_92 = "25.92"
    NACE_25_93 = "25.93"
    NACE_25_94 = "25.94"
    NACE_25_99 = "25.99"
    NACE_26 = "26"
    NACE_26_1 = "26.1"
    NACE_26_11 = "26.11"
    NACE_26_12 = "26.12"
    NACE_26_2 = "26.2"
    NACE_26_20 = "26.20"
    NACE_26_3 = "26.3"
    NACE_26_30 = "26.30"
    NACE_26_4 = "26.4"
    NACE_26_40 = "26.40"
    NACE_26_5 = "26.5"
    NACE_26_51 = "26.51"
    NACE_26_52 = "26.52"
    NACE_26_6 = "26.6"
    NACE_26_60 = "26.60"
    NACE_26_7 = "26.7"
    NACE_26_70 = "26.70"
    NACE_26_8 = "26.8"
    NACE_26_80 = "26.80"
    NACE_27 = "27"
    NACE_27_1 = "27.1"
    NACE_27_11 = "27.11"
    NACE_27_12 = "27.12"
    NACE_27_2 = "27.2"
    NACE_27_20 = "27.20"
    NACE_27_3 = "27.3"
    NACE_27_31 = "27.31"
    NACE_27_32 = "27.32"
    NACE_27_33 = "27.33"
    NACE_27_4 = "27.4"
    NACE_27_40 = "27.40"
    NACE_27_5 = "27.5"
    NACE_27_51 = "27.51"
    NACE_27_52 = "27.52"
    NACE_27_9 = "27.9"
    NACE_27_90 = "27.90"
    NACE_28 = "28"
    NACE_28_1 = "28.1"
    NACE_28_11 = "28.11"
    NACE_28_12 = "28.12"
    NACE_28_13 = "28.13"
    NACE_28_14 = "28.14"
    NACE_28_15 = "28.15"
    NACE_28_2 = "28.2"
    NACE_28_21 = "28.21"
    NACE_28_22 = "28.22"
    NACE_28_23 = "28.23"
    NACE_28_24 = "28.24"
    NACE_28_25 = "28.25"
    NACE_28_29 = "28.29"
    NACE_28_3 = "28.3"
    NACE_28_30 = "28.30"
    NACE_28_4 = "28.4"
    NACE_28_41 = "28.41"
    NACE_28_49 = "28.49"
    NACE_28_9 = "28.9"
    NACE_28_91 = "28.91"
    NACE_28_92 = "28.92"
    NACE_28_93 = "28.93"
    NACE_28_94 = "28.94"
    NACE_28_95 = "28.95"
    NACE_28_96 = "28.96"
    NACE_28_99 = "28.99"
    NACE_29 = "29"
    NACE_29_1 = "29.1"
    NACE_29_10 = "29.10"
    NACE_29_2 = "29.2"
    NACE_29_20 = "29.20"
    NACE_29_3 = "29.3"
    NACE_29_31 = "29.31"
    NACE_29_32 = "29.32"
    NACE_30 = "30"
    NACE_30_1 = "30.1"
    NACE_30_11 = "30.11"
    NACE_30_12 = "30.12"
    NACE_30_2 = "30.2"
    NACE_30_20 = "30.20"
    NACE_30_3 = "30.3"
    NACE_30_30 = "30.30"
    NACE_30_4 = "30.4"
    NACE_30_40 = "30.40"
    NACE_30_9 = "30.9"
    NACE_30_91 = "30.91"
    NACE_30_92 = "30.92"
    NACE_30_99 = "30.99"
    NACE_31 = "31"
    NACE_31_0 = "31.0"
    NACE_31_01 = "31.01"
    NACE_31_02 = "31.02"
    NACE_31_03 = "31.03"
    NACE_31_09 = "31.09"
    NACE_32 = "32"
    NACE_32_1 = "32.1"
    NACE_32_11 = "32.11"
    NACE_32_12 = "32.12"
    NACE_32_13 = "32.13"
    NACE_32_2 = "32.2"
    NACE_32_20 = "32.20"
    NACE_32_3 = "32.3"
    NACE_32_30 = "32.30"
    NACE_32_4 = "32.4"
    NACE_32_40 = "32.40"
    NACE_32_5 = "32.5"
    NACE_32_50 = "32.50"
    NACE_32_9 = "32.9"
    NACE_32_91 = "32.91"
    NACE_32_99 = "32.99"
    NACE_33 = "33"
    NACE_33_1 = "33.1"
    NACE_33_11 = "33.11"
    NACE_33_12 = "33.12"
    NACE_33_13 = "33.13"
    NACE_33_14 = "33.14"
    NACE_33_15 = "33.15"
    NACE_33_16 = "33.16"
    NACE_33_17 = "33.17"
    NACE_33_19 = "33.19"
    NACE_33_2 = "33.2"
    NACE_33_20 = "33.20"
    NACE_35 = "35"
    NACE_35_1 = "35.1"
    NACE_35_11 = "35.11"
    NACE_35_12 = "35.12"
    NACE_35_13 = "35.13"
    NACE_35_14 = "35.14"
    NACE_35_2 = "35.2"
    NACE_35_21 = "35.21"
    NACE_35_22 = "35.22"
    NACE_35_23 = "35.23"
    NACE_35_3 = "35.3"
    NACE_35_30 = "35.30"
    NACE_36 = "36"
    NACE_36_0 = "36.0"
    NACE_36_00 = "36.00"
    NACE_37 = "37"
    NACE_37_0 = "37.0"
    NACE_37_00 = "37.00"
    NACE_38 = "38"
    NACE_38_1 = "38.1"
    NACE_38_11 = "38.11"
    NACE_38_12 = "38.12"
    NACE_38_2 = "38.2"
    NACE_38_21 = "38.21"
    NACE_38_22 = "38.22"
    NACE_38_3 = "38.3"
    NACE_38_31 = "38.31"
    NACE_38_32 = "38.32"
    NACE_39 = "39"
    NACE_39_0 = "39.0"
    NACE_39_00 = "39.00"
    NACE_41 = "41"
    NACE_41_1 = "41.1"
    NACE_41_10 = "41.10"
    NACE_41_2 = "41.2"
    NACE_41_20 = "41.20"
    NACE_42 = "42"
    NACE_42_1 = "42.1"
    NACE_42_11 = "42.11"
    NACE_42_12 = "42.12"
    NACE_42_13 = "42.13"
    NACE_42_2 = "42.2"
    NACE_42_21 = "42.21"
    NACE_42_22 = "42.22"
    NACE_42_9 = "42.9"
    NACE_42_91 = "42.91"
    NACE_42_99 = "42.99"
    NACE_43 = "43"
    NACE_43_1 = "43.1"
    NACE_43_11 = "43.11"
    NACE_43_12 = "43.12"
    NACE_43_13 = "43.13"
    NACE_43_2 = "43.2"
    NACE_43_21 = "43.21"
    NACE_43_22 = "43.22"
    NACE_43_29 = "43.29"
    NACE_43_3 = "43.3"
    NACE_43_31 = "43.31"
    NACE_43_32 = "43.32"
    NACE_43_33 = "43.33"
    NACE_43_34 = "43.34"
    NACE_43_39 = "43.39"
    NACE_43_9 = "43.9"
    NACE_43_91 = "43.91"
    NACE_43_99 = "43.99"
    NACE_45 = "45"
    NACE_45_1 = "45.1"
    NACE_45_11 = "45.11"
    NACE_45_19 = "45.19"
    NACE_45_2 = "45.2"
    NACE_45_20 = "45.20"
    NACE_45_3 = "45.3"
    NACE_45_31 = "45.31"
    NACE_45_32 = "45.32"
    NACE_45_4 = "45.4"
    NACE_45_40 = "45.40"
    NACE_46 = "46"
    NACE_46_1 = "46.1"
    NACE_46_11 = "46.11"
    NACE_46_12 = "46.12"
    NACE_46_13 = "46.13"
    NACE_46_14 = "46.14"
    NACE_46_15 = "46.15"
    NACE_46_16 = "46.16"
    NACE_46_17 = "46.17"
    NACE_46_18 = "46.18"
    NACE_46_19 = "46.19"
    NACE_46_2 = "46.2"
    NACE_46_21 = "46.21"
    NACE_46_22 = "46.22"
    NACE_46_23 = "46.23"
    NACE_46_24 = "46.24"
    NACE_46_3 = "46.3"
    NACE_46_31 = "46.31"
    NACE_46_32 = "46.32"
    NACE_46_33 = "46.33"
    NACE_46_34 = "46.34"
    NACE_46_35 = "46.35"
    NACE_46_36 = "46.36"
    NACE_46_37 = "46.37"
    NACE_46_38 = "46.38"
    NACE_46_39 = "46.39"
    NACE_46_4 = "46.4"
    NACE_46_41 = "46.41"
    NACE_46_42 = "46.42"
    NACE_46_43 = "46.43"
    NACE_46_44 = "46.44"
    NACE_46_45 = "46.45"
    NACE_46_46 = "46.46"
    NACE_46_47 = "46.47"
    NACE_46_48 = "46.48"
    NACE_46_49 = "46.49"
    NACE_46_5 = "46.5"
    NACE_46_51 = "46.51"
    NACE_46_52 = "46.52"
    NACE_46_6 = "46.6"
    NACE_46_61 = "46.61"
    NACE_46_62 = "46.62"
    NACE_46_63 = "46.63"
    NACE_46_64 = "46.64"
    NACE_46_65 = "46.65"
    NACE_46_66 = "46.66"
    NACE_46_69 = "46.69"
    NACE_46_7 = "46.7"
    NACE_46_71 = "46.71"
    NACE_46_72 = "46.72"
    NACE_46_73 = "46.73"
    NACE_46_74 = "46.74"
    NACE_46_75 = "46.75"
    NACE_46_76 = "46.76"
    NACE_46_77 = "46.77"
    NACE_46_9 = "46.9"
    NACE_46_90 = "46.90"
    NACE_47 = "47"
    NACE_47_1 = "47.1"
    NACE_47_11 = "47.11"
    NACE_47_19 = "47.19"
    NACE_47_2 = "47.2"
    NACE_47_21 = "47.21"
    NACE_47_22 = "47.22"
    NACE_47_23 = "47.23"
    NACE_47_24 = "47.24"
    NACE_47_25 = "47.25"
    NACE_47_26 = "47.26"
    NACE_47_29 = "47.29"
    NACE_47_3 = "47.3"
    NACE_47_30 = "47.30"
    NACE_47_4 = "47.4"
    NACE_47_41 = "47.41"
    NACE_47_42 = "47.42"
    NACE_47_43 = "47.43"
    NACE_47_5 = "47.5"
    NACE_47_51 = "47.51"
    NACE_47_52 = "47.52"
    NACE_47_53 = "47.53"
    NACE_47_54 = "47.54"
    NACE_47_59 = "47.59"
    NACE_47_6 = "47.6"
    NACE_47_61 = "47.61"
    NACE_47_62 = "47.62"
    NACE_47_63 = "47.63"
    NACE_47_64 = "47.64"
    NACE_47_65 = "47.65"
    NACE_47_7 = "47.7"
    NACE_47_71 = "47.71"
    NACE_47_72 = "47.72"
    NACE_47_73 = "47.73"
    NACE_47_74 = "47.74"
    NACE_47_75 = "47.75"
    NACE_47_76 = "47.76"
    NACE_47_77 = "47.77"
    NACE_47_78 = "47.78"
    NACE_47_79 = "47.79"
    NACE_47_8 = "47.8"
    NACE_47_81 = "47.81"
    NACE_47_82 = "47.82"
    NACE_47_89 = "47.89"
    NACE_47_9 = "47.9"
    NACE_47_91 = "47.91"
    NACE_47_99 = "47.99"
    NACE_49 = "49"
    NACE_49_1 = "49.1"
    NACE_49_10 = "49.10"
    NACE_49_2 = "49.2"
    NACE_49_20 = "49.20"
    NACE_49_3 = "49.3"
    NACE_49_31 = "49.31"
    NACE_49_32 = "49.32"
    NACE_49_39 = "49.39"
    NACE_49_4 = "49.4"
    NACE_49_41 = "49.41"
    NACE_49_42 = "49.42"
    NACE_49_5 = "49.5"
    NACE_49_50 = "49.50"
    NACE_50 = "50"
    NACE_50_1 = "50.1"
    NACE_50_10 = "50.10"
    NACE_50_2 = "50.2"
    NACE_50_20 = "50.20"
    NACE_50_3 = "50.3"
    NACE_50_30 = "50.30"
    NACE_50_4 = "50.4"
    NACE_50_40 = "50.40"
    NACE_51 = "51"
    NACE_51_1 = "51.1"
    NACE_51_10 = "51.10"
    NACE_51_2 = "51.2"
    NACE_51_21 = "51.21"
    NACE_51_22 = "51.22"
    NACE_52 = "52"
    NACE_52_1 = "52.1"
    NACE_52_10 = "52.10"
    NACE_52_2 = "52.2"
    NACE_52_21 = "52.21"
    NACE_52_22 = "52.22"
    NACE_52_23 = "52.23"
    NACE_52_24 = "52.24"
    NACE_52_29 = "52.29"
    NACE_53 = "53"
    NACE_53_1 = "53.1"
    NACE_53_10 = "53.10"
    NACE_53_2 = "53.2"
    NACE_53_20 = "53.20"
    NACE_55 = "55"
    NACE_55_1 = "55.1"
    NACE_55_10 = "55.10"
    NACE_55_2 = "55.2"
    NACE_55_20 = "55.20"
    NACE_55_3 = "55.3"
    NACE_55_30 = "55.30"
    NACE_55_9 = "55.9"
    NACE_55_90 = "55.90"
    NACE_56 = "56"
    NACE_56_1 = "56.1"
    NACE_56_10 = "56.10"
    NACE_56_2 = "56.2"
    NACE_56_21 = "56.21"
    NACE_56_29 = "56.29"
    NACE_56_3 = "56.3"
    NACE_56_30 = "56.30"
    NACE_58 = "58"
    NACE_58_1 = "58.1"
    NACE_58_11 = "58.11"
    NACE_58_12 = "58.12"
    NACE_58_13 = "58.13"
    NACE_58_14 = "58.14"
    NACE_58_19 = "58.19"
    NACE_58_2 = "58.2"
    NACE_58_21 = "58.21"
    NACE_58_29 = "58.29"
    NACE_59 = "59"
    NACE_59_1 = "59.1"
    NACE_59_11 = "59.11"
    NACE_59_12 = "59.12"
    NACE_59_13 = "59.13"
    NACE_59_14 = "59.14"
    NACE_59_2 = "59.2"
    NACE_59_20 = "59.20"
    NACE_60 = "60"
    NACE_60_1 = "60.1"
    NACE_60_10 = "60.10"
    NACE_60_2 = "60.2"
    NACE_60_20 = "60.20"
    NACE_61 = "61"
    NACE_61_1 = "61.1"
    NACE_61_10 = "61.10"
    NACE_61_2 = "61.2"
    NACE_61_20 = "61.20"
    NACE_61_3 = "61.3"
    NACE_61_30 = "61.30"
    NACE_61_9 = "61.9"
    NACE_61_90 = "61.90"
    NACE_62 = "62"
    NACE_62_0 = "62.0"
    NACE_62_01 = "62.01"
    NACE_62_02 = "62.02"
    NACE_62_03 = "62.03"
    NACE_62_09 = "62.09"
    NACE_63 = "63"
    NACE_63_1 = "63.1"
    NACE_63_11 = "63.11"
    NACE_63_12 = "63.12"
    NACE_63_9 = "63.9"
    NACE_63_91 = "63.91"
    NACE_63_99 = "63.99"
    NACE_64 = "64"
    NACE_64_1 = "64.1"
    NACE_64_11 = "64.11"
    NACE_64_19 = "64.19"
    NACE_64_2 = "64.2"
    NACE_64_20 = "64.20"
    NACE_64_3 = "64.3"
    NACE_64_30 = "64.30"
    NACE_64_9 = "64.9"
    NACE_64_91 = "64.91"
    NACE_64_92 = "64.92"
    NACE_64_99 = "64.99"
    NACE_65 = "65"
    NACE_65_1 = "65.1"
    NACE_65_11 = "65.11"
    NACE_65_12 = "65.12"
    NACE_65_2 = "65.2"
    NACE_65_20 = "65.20"
    NACE_65_3 = "65.3"
    NACE_65_30 = "65.30"
    NACE_66 = "66"
    NACE_66_1 = "66.1"
    NACE_66_11 = "66.11"
    NACE_66_12 = "66.12"
    NACE_66_19 = "66.19"
    NACE_66_2 = "66.2"
    NACE_66_21 = "66.21"
    NACE_66_22 = "66.22"
    NACE_66_29 = "66.29"
    NACE_66_3 = "66.3"
    NACE_66_30 = "66.30"
    NACE_68 = "68"
    NACE_68_1 = "68.1"
    NACE_68_10 = "68.10"
    NACE_68_2 = "68.2"
    NACE_68_20 = "68.20"
    NACE_68_3 = "68.3"
    NACE_68_31 = "68.31"
    NACE_68_32 = "68.32"
    NACE_69 = "69"
    NACE_69_1 = "69.1"
    NACE_69_10 = "69.10"
    NACE_69_2 = "69.2"
    NACE_69_20 = "69.20"
    NACE_70 = "70"
    NACE_70_1 = "70.1"
    NACE_70_10 = "70.10"
    NACE_70_2 = "70.2"
    NACE_70_21 = "70.21"
    NACE_70_22 = "70.22"
    NACE_71 = "71"
    NACE_71_1 = "71.1"
    NACE_71_11 = "71.11"
    NACE_71_12 = "71.12"
    NACE_71_2 = "71.2"
    NACE_71_20 = "71.20"
    NACE_72 = "72"
    NACE_72_1 = "72.1"
    NACE_72_11 = "72.11"
    NACE_72_19 = "72.19"
    NACE_72_2 = "72.2"
    NACE_72_20 = "72.20"
    NACE_73 = "73"
    NACE_73_1 = "73.1"
    NACE_73_11 = "73.11"
    NACE_73_12 = "73.12"
    NACE_73_2 = "73.2"
    NACE_73_20 = "73.20"
    NACE_74 = "74"
    NACE_74_1 = "74.1"
    NACE_74_10 = "74.10"
    NACE_74_2 = "74.2"
    NACE_74_20 = "74.20"
    NACE_74_3 = "74.3"
    NACE_74_30 = "74.30"
    NACE_74_9 = "74.9"
    NACE_74_90 = "74.90"
    NACE_75 = "75"
    NACE_75_0 = "75.0"
    NACE_75_00 = "75.00"
    NACE_77 = "77"
    NACE_77_1 = "77.1"
    NACE_77_11 = "77.11"
    NACE_77_12 = "77.12"
    NACE_77_2 = "77.2"
    NACE_77_21 = "77.21"
    NACE_77_22 = "77.22"
    NACE_77_29 = "77.29"
    NACE_77_3 = "77.3"
    NACE_77_31 = "77.31"
    NACE_77_32 = "77.32"
    NACE_77_33 = "77.33"
    NACE_77_34 = "77.34"
    NACE_77_35 = "77.35"
    NACE_77_39 = "77.39"
    NACE_77_4 = "77.4"
    NACE_77_40 = "77.40"
    NACE_78 = "78"
    NACE_78_1 = "78.1"
    NACE_78_10 = "78.10"
    NACE_78_2 = "78.2"
    NACE_78_20 = "78.20"
    NACE_78_3 = "78.3"
    NACE_78_30 = "78.30"
    NACE_79 = "79"
    NACE_79_1 = "79.1"
    NACE_79_11 = "79.11"
    NACE_79_12 = "79.12"
    NACE_79_9 = "79.9"
    NACE_79_90 = "79.90"
    NACE_80 = "80"
    NACE_80_1 = "80.1"
    NACE_80_10 = "80.10"
    NACE_80_2 = "80.2"
    NACE_80_20 = "80.20"
    NACE_80_3 = "80.3"
    NACE_80_30 = "80.30"
    NACE_81 = "81"
    NACE_81_1 = "81.1"
    NACE_81_10 = "81.10"
    NACE_81_2 = "81.2"
    NACE_81_21 = "81.21"
    NACE_81_22 = "81.22"
    NACE_81_29 = "81.29"
    NACE_81_3 = "81.3"
    NACE_81_30 = "81.30"
    NACE_82 = "82"
    NACE_82_1 = "82.1"
    NACE_82_11 = "82.11"
    NACE_82_19 = "82.19"
    NACE_82_2 = "82.2"
    NACE_82_20 = "82.20"
    NACE_82_3 = "82.3"
    NACE_82_30 = "82.30"
    NACE_82_9 = "82.9"
    NACE_82_91 = "82.91"
    NACE_82_92 = "82.92"
    NACE_82_99 = "82.99"
    NACE_84 = "84"
    NACE_84_1 = "84.1"
    NACE_84_11 = "84.11"
    NACE_84_12 = "84.12"
    NACE_84_13 = "84.13"
    NACE_84_2 = "84.2"
    NACE_84_21 = "84.21"
    NACE_84_22 = "84.22"
    NACE_84_23 = "84.23"
    NACE_84_24 = "84.24"
    NACE_84_25 = "84.25"
    NACE_84_3 = "84.3"
    NACE_84_30 = "84.30"
    NACE_85 = "85"
    NACE_85_1 = "85.1"
    NACE_85_10 = "85.10"
    NACE_85_2 = "85.2"
    NACE_85_20 = "85.20"
    NACE_85_3 = "85.3"
    NACE_85_31 = "85.31"
    NACE_85_32 = "85.32"
    NACE_85_4 = "85.4"
    NACE_85_41 = "85.41"
    NACE_85_42 = "85.42"
    NACE_85_5 = "85.5"
    NACE_85_51 = "85.51"
    NACE_85_52 = "85.52"
    NACE_85_53 = "85.53"
    NACE_85_59 = "85.59"
    NACE_85_6 = "85.6"
    NACE_85_60 = "85.60"
    NACE_86 = "86"
    NACE_86_1 = "86.1"
    NACE_86_10 = "86.10"
    NACE_86_2 = "86.2"
    NACE_86_21 = "86.21"
    NACE_86_22 = "86.22"
    NACE_86_23 = "86.23"
    NACE_86_9 = "86.9"
    NACE_86_90 = "86.90"
    NACE_87 = "87"
    NACE_87_1 = "87.1"
    NACE_87_10 = "87.10"
    NACE_87_2 = "87.2"
    NACE_87_20 = "87.20"
    NACE_87_3 = "87.3"
    NACE_87_30 = "87.30"
    NACE_87_9 = "87.9"
    NACE_87_90 = "87.90"
    NACE_88 = "88"
    NACE_88_1 = "88.1"
    NACE_88_10 = "88.10"
    NACE_88_9 = "88.9"
    NACE_88_91 = "88.91"
    NACE_88_99 = "88.99"
    NACE_90 = "90"
    NACE_90_0 = "90.0"
    NACE_90_01 = "90.01"
    NACE_90_02 = "90.02"
    NACE_90_03 = "90.03"
    NACE_90_04 = "90.04"
    NACE_91 = "91"
    NACE_91_0 = "91.0"
    NACE_91_01 = "91.01"
    NACE_91_02 = "91.02"
    NACE_91_03 = "91.03"
    NACE_91_04 = "91.04"
    NACE_92 = "92"
    NACE_92_0 = "92.0"
    NACE_92_00 = "92.00"
    NACE_93 = "93"
    NACE_93_1 = "93.1"
    NACE_93_11 = "93.11"
    NACE_93_12 = "93.12"
    NACE_93_13 = "93.13"
    NACE_93_19 = "93.19"
    NACE_93_2 = "93.2"
    NACE_93_21 = "93.21"
    NACE_93_29 = "93.29"
    NACE_94 = "94"
    NACE_94_1 = "94.1"
    NACE_94_11 = "94.11"
    NACE_94_12 = "94.12"
    NACE_94_2 = "94.2"
    NACE_94_20 = "94.20"
    NACE_94_9 = "94.9"
    NACE_94_91 = "94.91"
    NACE_94_92 = "94.92"
    NACE_94_99 = "94.99"
    NACE_95 = "95"
    NACE_95_1 = "95.1"
    NACE_95_11 = "95.11"
    NACE_95_12 = "95.12"
    NACE_95_2 = "95.2"
    NACE_95_21 = "95.21"
    NACE_95_22 = "95.22"
    NACE_95_23 = "95.23"
    NACE_95_24 = "95.24"
    NACE_95_25 = "95.25"
    NACE_95_29 = "95.29"
    NACE_96 = "96"
    NACE_96_0 = "96.0"
    NACE_96_01 = "96.01"
    NACE_96_02 = "96.02"
    NACE_96_03 = "96.03"
    NACE_96_04 = "96.04"
    NACE_96_09 = "96.09"
    NACE_97 = "97"
    NACE_97_0 = "97.0"
    NACE_97_00 = "97.00"
    NACE_98 = "98"
    NACE_98_1 = "98.1"
    NACE_98_10 = "98.10"
    NACE_98_2 = "98.2"
    NACE_98_20 = "98.20"
    NACE_99 = "99"
    NACE_99_0 = "99.0"
    NACE_99_00 = "99.00"


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


class ISO_4217_CurrencyCode(str, Enum):
    EUR = "EUR"
    SEK = "SEK"
    NOK = "NOK"
    DKK = "DKK"
    ISK = "ISK"


class BoardMemberRole(str, Enum):
    CHAIRPERSON = "chairperson"
    MEMBER = "member"
    DEPUTY_MEMBER = "deputy member"


class ManagingDirectorRole(str, Enum):
    DIRECTOR = "director"
    DEPUTY_DIRECTOR = "deputy director"


class Registrant(CamelCaseModel):
    given_name: str = Field(
        ...,
        title="Given name",
        description="The first name that the person is being called by",
        max_length=250,
        example="John",
    )
    last_name: str = Field(
        ...,
        title="Last name",
        description="The person's current family name",
        max_length=250,
        example="Doe",
    )
    email: EmailStr = Field(
        ...,
        title="Email",
        description="The person's contact email address",
        example="john.doe@test.fi",
    )
    phone_number: str = Field(
        ...,
        title="Phone number",
        description="The person's phone number in the international format",
        example="+358501234567",
        max_length=250,
    )


class CompanyDetails(CamelCaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="The desired name to be registered for the company",
        max_length=250,
        example="Digital company X",
    )
    alternative_name: Optional[str] = Field(
        None,
        title="Alternative name",
        description="The second alternative for the desired name to be registered for "
        "the company if the primary name is not available",
        max_length=250,
        example="Digital company Y",
    )
    founding_date: date = Field(
        ...,
        title="Founding date",
        description="The date of memorandum of association",
        example=date(2022, 1, 1),
    )
    industry_sector: IndustrySector = Field(
        ...,
        title="Industry sector",
        description="The industry fields where the company will run its business. The "
        "codes are based on the Statistical classification of economic activities in "
        "the European Community, abbreviated as NACE.",
        example=IndustrySector.NACE_62_01,
    )
    share_capital: float = Field(
        ...,
        title="Share capital",
        description="The total value of the issued shares of the company",
        example=1000.0,
    )
    capital_currency: ISO_4217_CurrencyCode = Field(
        ...,
        title="Capital currency",
        description="The currency used for the share capital in ISO 4217 format",
        example=ISO_4217_CurrencyCode.EUR,
    )
    settlement_deposit: Optional[float] = Field(
        None,
        title="Settlement deposit",
        description="The amount of the deposit paid during the establishment of a "
        "company",
        example=1000.0,
    )
    deposit_currency: Optional[ISO_4217_CurrencyCode] = Field(
        None,
        title="Deposit currency",
        description="The currency used for the paying the settlement deposit in ISO "
        "4217 format",
        example=ISO_4217_CurrencyCode.EUR,
    )
    settlement_date: Optional[date] = Field(
        None,
        title="Settlement date",
        description="The date on which the share deposit has been settled and "
        "available as full",
        example=date(2022, 2, 1),
    )
    country_of_residence: Optional[ISO_3166_1_Alpha_3] = Field(
        None,
        title="Country of residence",
        description="The company's current country of the residence in the three "
        "character (Alpha-3) format if it already exists abroad",
        example=ISO_3166_1_Alpha_3.USA,
    )


class ShareSeries(CamelCaseModel):
    share_series_class: str = Field(
        ...,
        title="Share series class",
        description="The type of the share series of a company",
        example="A",
        max_length=5,
    )
    number_of_shares: int = Field(
        ...,
        title="Number of shares",
        description="The total number of the shares in the share series class",
        example=100,
    )
    share_value: float = Field(
        ...,
        title="Share value",
        description="The nominal value of a share of this class",
        example=10,
    )
    share_value_currency: ISO_4217_CurrencyCode = Field(
        None,
        title="Share value currency",
        description="The currency used for the share value in ISO 4217 format",
        example=ISO_4217_CurrencyCode.EUR,
    )


class CompanyAddress(CamelCaseModel):
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
        description="The name of a geographic area that groups addresses. This would "
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


class ManagingDirector(CamelCaseModel):
    role: ManagingDirectorRole = Field(
        ...,
        title="Role",
        description="The role of the director",
        example=ManagingDirectorRole.DIRECTOR,
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
        title="Middle name",
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
        description="The birth day of the person",
        example=date(1976, 4, 16),
    )
    nationality: ISO_3166_1_Alpha_3 = Field(
        ...,
        title="Nationality",
        description="The nationality of the person",
        example=ISO_3166_1_Alpha_3.USA,
    )


class BoardMember(CamelCaseModel):
    role: BoardMemberRole = Field(
        ...,
        title="Role",
        description="The role of the person in the board",
        example=BoardMemberRole.MEMBER,
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
        description="The birth day of the person",
        example=date(1976, 4, 16),
    )
    nationality: ISO_3166_1_Alpha_3 = Field(
        ...,
        title="Nationality",
        description="The nationality of the person",
        example=ISO_3166_1_Alpha_3.USA,
    )


class AuditorDetails(CamelCaseModel):
    company_name: Optional[str] = Field(
        None,
        title="Company name",
        description="The name of the auditor company if it exists",
        example="Auditor company X",
        max_length=250,
    )
    national_identifier: Optional[str] = Field(
        None,
        title="National identifier",
        description="The national identifier of the auditor company issued by the "
        "trade register",
        example="2464491-9",
        max_length=40,
    )
    given_name: Optional[str] = Field(
        None,
        title="Given name",
        description="The first name that the person is being called by",
        example="Jane",
        max_length=250,
    )
    last_name: Optional[str] = Field(
        None,
        title="Last name",
        description="The person's current family name",
        example="Doe",
        max_length=250,
    )


class EstablishmentRequest(CamelCaseModel):
    registrant: Registrant = Field(
        ...,
        title="Registrant",
        description="The personal details of the person registering the company",
    )
    company_details: CompanyDetails = Field(
        ...,
        title="Company details",
        description="The details of the company being established",
    )
    share_series: List[ShareSeries] = Field(
        ...,
        title="Share series",
        description="The details of the share series of the company",
    )
    company_address: CompanyAddress = Field(
        ...,
        title="Company address",
        description="The official address of the company",
    )
    managing_directors: List[ManagingDirector] = Field(
        ...,
        title="Managing directors",
    )
    board_members: List[BoardMember] = Field(
        ...,
        title="Board members",
    )
    auditor_details: AuditorDetails = Field(
        ...,
        title="Auditor details",
        description="The details of the company and person auditing the company",
    )


DEFINITION = DataProductDefinition(
    title="Establish a non-listed company",
    description="Create the initial set of data to establish a non-listed company",
    request=EstablishmentRequest,
    response=EstablishmentRequest,
    requires_authorization=True,
    requires_consent=False,
)
