from enum import StrEnum
from maleo.types.string import ListOfStrings


class Granularity(StrEnum):
    BASIC = "basic"
    STANDARD = "standard"
    FULL = "full"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class IdentifierType(StrEnum):
    ID = "id"
    UUID = "uuid"
    KEY = "key"
    NAME = "name"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class Key(StrEnum):
    REGULAR = "regular"
    INTERNAL = "internal"
    CLIENT = "client"
    PARTNER = "partner"
    VENDOR = "vendor"
    GOVERNMENT = "government"
    HOSPITAL_SYSTEM = "hospital_system"
    HOSPITAL = "hospital"
    MEDICAL_GROUP = "medical_group"
    DEPARTMENT = "deparment"
    DIVISION = "division"
    CLINIC = "clinic"
    PRIMARY_HEALTH_CARE = "primary_health_care"
    BRANCH = "branch"
    NETWORK = "network"
    UNIT = "unit"
    CORPORATION = "corporation"
    SUBSIDIARY = "subsidiary"
    REGIONAL_OFFICE = "reginal_office"
    APPLICATION = "application"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]
