from pydantic import BaseModel

from core.model_runtime.entities.enums.model_types import ModelType


class CustomModelConfiguration(BaseModel):
    """
    Model class for provider custom model configuration.
    """
    model: str
    model_type: ModelType
    credentials: dict