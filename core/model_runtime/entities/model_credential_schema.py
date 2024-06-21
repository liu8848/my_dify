from pydantic import BaseModel

from core.model_runtime.entities.enums.credential_form_schema import CredentialFormSchema
from core.model_runtime.entities.file_model_schema import FieldModelSchema


class ModelCredentialSchema(BaseModel):
    """
    Model class for model credential schema.
    """
    model: FieldModelSchema
    credential_form_schemas: list[CredentialFormSchema]
