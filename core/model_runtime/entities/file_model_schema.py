from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject


class FieldModelSchema(BaseModel):
    label: I18nObject
    placeholder: Optional[I18nObject] = None
