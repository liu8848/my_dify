from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.enums.configurate_method import ConfigurateMethod
from core.model_runtime.entities.enums.model_types import ModelType
from core.model_runtime.entities.model_credential_schema import ModelCredentialSchema
from core.model_runtime.entities.provider_credential_schema import ProviderCredentialSchema
from core.model_runtime.entities.provider_model import ProviderModel
from core.model_runtime.entities.simple_provider_entity import SimpleProviderEntity


class ProviderHelpEntity(BaseModel):
    """
    Model class for provider help.
    """
    title: I18nObject
    url: I18nObject


class ProviderEntity(BaseModel):
    """
    模型供应商实体模型
    """
    provider: str
    label: I18nObject
    description: Optional[I18nObject] = None
    icon_small: Optional[I18nObject] = None
    icon_large: Optional[I18nObject] = None
    background: Optional[str] = None
    help: Optional[ProviderHelpEntity] = None
    supported_model_types: list[ModelType]
    configurate_methods: list[ConfigurateMethod]
    models: list[ProviderModel] = []
    provider_credential_schema: Optional[ProviderCredentialSchema] = None
    model_credential_schema: Optional[ModelCredentialSchema] = None

    class Config:
        protected_namespace=()

    def to_simple_provider(self)->SimpleProviderEntity:
        """
        转换为简单形式
        :return:
        """
        return SimpleProviderEntity(
            provider=self.provider,
            label=self.label,
            icon_small=self.icon_small,
            icon_large=self.icon_large,
            supported_model_types=self.supported_model_types,
            models=self.models
        )

