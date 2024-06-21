from enum import Enum


class ConfigurateMethod(Enum):
    """
    Enum class for configurate method of provider model.
    """
    PREDEFINED_MODEL = "predefined-model"
    CUSTOMIZABLE_MODEL = "customizable-model"
