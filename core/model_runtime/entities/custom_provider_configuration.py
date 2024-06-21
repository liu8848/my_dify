from pydantic import BaseModel


class CustomProviderConfiguration(BaseModel):
    """
    Model class for provider custom configuration.
    """
    credentials: dict
