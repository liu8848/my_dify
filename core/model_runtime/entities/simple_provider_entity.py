from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.enums.ai_model_entity import AIModelEntity
from core.model_runtime.entities.enums.model_types import ModelType


class SimpleProviderEntity(BaseModel):
    """
    模型供应商简单形式
    """
    provider: str
    label: I18nObject
    icon_small: Optional[I18nObject] = None
    icon_large: Optional[I18nObject] = None
    supported_model_types: list[ModelType]
    models: list[AIModelEntity] = []