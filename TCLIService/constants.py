#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from .ttypes import *

PRIMITIVE_TYPES = set([
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
])
COMPLEX_TYPES = set([
    10,
    11,
    12,
    13,
    14,
])
COLLECTION_TYPES = set([
    10,
    11,
])
TYPE_NAMES = {
    0 : "BOOLEAN",
    1 : "TINYINT",
    2 : "SMALLINT",
    3 : "INT",
    4 : "BIGINT",
    5 : "FLOAT",
    6 : "DOUBLE",
    7 : "STRING",
    8 : "TIMESTAMP",
    9 : "BINARY",
    10 : "ARRAY",
    11 : "MAP",
    12 : "STRUCT",
    13 : "UNIONTYPE",
    15 : "DECIMAL",
    16 : "NULL",
    17 : "DATE",
    18 : "VARCHAR",
    19 : "CHAR",
    20 : "INTERVAL_YEAR_MONTH",
    21 : "INTERVAL_DAY_TIME",
}
CHARACTER_MAXIMUM_LENGTH = "characterMaximumLength"
PRECISION = "precision"
SCALE = "scale"
