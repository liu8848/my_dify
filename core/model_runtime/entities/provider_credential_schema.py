from pydantic import BaseModel

from core.model_runtime.entities.enums.credential_form_schema import CredentialFormSchema


class ProviderCredentialSchema(BaseModel):
    """
    Model class for provider credential schema.
    """
    credential_form_schemas: list[CredentialFormSchema]