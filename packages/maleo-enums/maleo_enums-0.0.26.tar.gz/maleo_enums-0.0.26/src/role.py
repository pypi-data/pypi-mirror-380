from enum import StrEnum
from maleo.types.string import ListOfStrings


class Organization(StrEnum):
    OWNER = "owner"
    ADMINISTRATOR = "administrator"
    USER = "user"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]


class System(StrEnum):
    ADMINISTRATOR = "administrator"
    ANALYST = "analyst"
    ENGINEER = "engineer"
    SUPPORT = "support"
    MANAGER = "manager"
    OFFICER = "officer"
    OPERATIONS = "operations"
    SECURITY = "security"
    TESTER = "tester"
    USER = "user"

    @classmethod
    def choices(cls) -> ListOfStrings:
        return [e.value for e in cls]
