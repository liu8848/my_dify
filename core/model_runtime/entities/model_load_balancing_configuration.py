from pydantic import BaseModel


class ModelLoadBalancingConfiguration(BaseModel):
    """
    Class for model load balancing configuration.
    """
    id: str
    name: str
    credentials: dict

