from pydantic import BaseModel

from core.model_runtime.entities.enums.provider_quota_type import ProviderQuotaType
from core.model_runtime.entities.enums.quota_unit import QuotaUnit
from core.model_runtime.entities.restrict_model import RestrictModel


class QuotaConfiguration(BaseModel):
    """
    Model class for provider quota configuration.
    """
    quota_type: ProviderQuotaType
    quota_unit: QuotaUnit
    quota_limit: int
    quota_used: int
    is_valid: bool
    restrict_models: list[RestrictModel] = []

