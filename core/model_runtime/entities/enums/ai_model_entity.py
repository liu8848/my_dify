from typing import Optional

from core.model_runtime.entities.parameter_rule import ParameterRule
from core.model_runtime.entities.price_config import PriceConfig
from core.model_runtime.entities.provider_model import ProviderModel


class AIModelEntity(ProviderModel):
    """
    Model class for AI model.
    """
    parameter_rules: list[ParameterRule] = []
    pricing: Optional[PriceConfig] = None
