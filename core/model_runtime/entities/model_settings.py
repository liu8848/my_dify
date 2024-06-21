from pydantic import BaseModel

from core.model_runtime.entities.enums.model_types import ModelType
from core.model_runtime.entities.model_load_balancing_configuration import ModelLoadBalancingConfiguration


class ModelSettings(BaseModel):
    """
    Model class for model settings.
    """
    model: str
    model_type: ModelType
    enabled: bool = True
    load_balancing_configs: list[ModelLoadBalancingConfiguration] = []
