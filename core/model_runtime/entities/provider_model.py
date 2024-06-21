from typing import Optional, Any

from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.enums.fetch_from import FetchFrom
from core.model_runtime.entities.enums.model_feature import ModelFeature
from core.model_runtime.entities.enums.model_propertity_key import ModelPropertyKey
from core.model_runtime.entities.enums.model_types import ModelType


class ProviderModel(BaseModel):
    model: str
    label: I18nObject
    model_type: ModelType
    features: Optional[list[ModelFeature]] = None
    fetch_from: FetchFrom
    model_properties: dict[ModelPropertyKey, Any]
    deprecated: bool = False

    class Config:
        protected_namespaces = ()
