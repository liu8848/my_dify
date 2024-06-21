from enum import Enum


class ProviderType(Enum):
    CUSTOM = 'custom'
    SYSTEM = 'system'

    @staticmethod
    def value_of(value):
        for member in ProviderType:
            if member.value == value:
                return member
        raise ValueError(f"No matching enum found for value '{value}'")