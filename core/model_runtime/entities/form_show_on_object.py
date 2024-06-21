from pydantic import BaseModel


class FormShowOnObject(BaseModel):
    """
    Model class for form show on.
    """
    variable: str
    value: str