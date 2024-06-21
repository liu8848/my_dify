from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.custom_model_configuration import CustomModelConfiguration
from core.model_runtime.entities.custom_provider_configuration import CustomProviderConfiguration


class CustomConfiguration(BaseModel):
    """
    Model class for provider custom configuration.
    """
    provider: Optional[CustomProviderConfiguration] = None
    models: list[CustomModelConfiguration] = []
