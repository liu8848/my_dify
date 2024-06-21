class ProviderManager:
    """
    ProviderManager：用于管理模型供应商（包括预定义以及自定义的模型供应商）
    """

    def __init__(self) -> None:
        self.decoding_rsa_key = None
        self.decoding_cipher_rsa = None

    def get_configurations(self,tenant_id:str)->ProviderConfigurations:
