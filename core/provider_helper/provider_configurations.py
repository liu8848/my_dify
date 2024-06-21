from pydantic import BaseModel

from core.model_runtime.entities.custom_configuration import CustomConfiguration
from core.model_runtime.entities.enums.configurate_method import ConfigurateMethod
from core.model_runtime.entities.enums.provider_type import ProviderType
from core.model_runtime.entities.model_settings import ModelSettings
from core.model_runtime.entities.provider_entities import ProviderEntity
from core.model_runtime.entities.system_configuration import SystemConfiguration


class ProviderConfiguration(BaseModel):
    """
    供应商配置
    """

    tenant_id: str
    provider: ProviderEntity
    preferred_provider_type: ProviderType
    using_provider_type: ProviderType
    system_configuration:SystemConfiguration
    custom_configuration:CustomConfiguration
    model_settings:list[ModelSettings]


    def __init__(self, **data):
        super().__init__(**data)

        if self.provider.provider not in original_provider_configurate_methods:
            original_provider_configurate_methods[self.provider.provider] = []
            for configurate_method in self.provider.configurate_methods:
                original_provider_configurate_methods[self.provider.provider].append(configurate_method)

        if original_provider_configurate_methods[self.provider.provider] == [ConfigurateMethod.CUSTOMIZABLE_MODEL]:
            if (any([len(quota_configuration.restrict_models) > 0
                     for quota_configuration in self.system_configuration.quota_configurations])
                    and ConfigurateMethod.PREDEFINED_MODEL not in self.provider.configurate_methods):
                self.provider.configurate_methods.append(ConfigurateMethod.PREDEFINED_MODEL)

class ProviderConfigurations(BaseModel):
    """
    模型供应商配置类
    """
    tenant_id: str
    configurations: dict[str, ProviderConfiguration] = {}
