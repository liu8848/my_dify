from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.enums.provider_quota_type import ProviderQuotaType
from core.model_runtime.entities.quota_configuration import QuotaConfiguration


class SystemConfiguration(BaseModel):
    """
    Model class for provider system configuration.
    """
    enabled: bool
    current_quota_type: Optional[ProviderQuotaType] = None
    quota_configurations: list[QuotaConfiguration] = []
    credentials: Optional[dict] = None
