from typing import Optional, Any

from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.enums.parameter_type import ParameterType


class ParameterRule(BaseModel):
    """
    Model class for parameter rule.
    """
    name: str
    use_template: Optional[str] = None
    label: I18nObject
    type: ParameterType
    help: Optional[I18nObject] = None
    required: bool = False
    default: Optional[Any] = None
    min: Optional[float] = None
    max: Optional[float] = None
    precision: Optional[int] = None
    options: list[str] = []
