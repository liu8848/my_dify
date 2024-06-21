from typing import Optional

from pydantic import BaseModel

from core.model_runtime.entities.common_entities import I18nObject
from core.model_runtime.entities.enums.from_type import FormType
from core.model_runtime.entities.form_option import FormOption
from core.model_runtime.entities.form_show_on_object import FormShowOnObject


class CredentialFormSchema(BaseModel):
    """
    Model class for credential form schema.
    """
    variable: str
    label: I18nObject
    type: FormType
    required: bool = True
    default: Optional[str] = None
    options: Optional[list[FormOption]] = None
    placeholder: Optional[I18nObject] = None
    max_length: int = 0
    show_on: list[FormShowOnObject] = []
