from enum import Enum


class ProviderQuotaType(Enum):
    PAID = 'paid'
    """hosted paid quota"""

    FREE = 'free'
    """third-party free quota"""

    TRIAL = 'trial'
    """hosted trial quota"""

    @staticmethod
    def value_of(value):
        for member in ProviderQuotaType:
            if member.value == value:
                return member
        raise ValueError(f"No matching enum found for value '{value}'")