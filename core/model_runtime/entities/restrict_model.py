from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.enums.model_types import ModelType


class RestrictModel(BaseModel):
    model: str
    base_model_name: Optional[str] = None
    model_type: ModelType
