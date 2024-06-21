from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.form_show_on_object import FormShowOnObject


class FormOption(BaseModel):
    """
    模型设置
    """
    label: I18nObject
    value: str
    show_on: list[FormShowOnObject] = []

    def __init__(self, **data):
        super().__init__(**data)
        if not self.label:
            self.label = I18nObject(
                en_US=self.value
            )