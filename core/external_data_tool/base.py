from abc import ABC, abstractmethod
from typing import Optional

from core.extension.extensible import Extensible, ExtensionModule

"""
定义的数据操作工具抽象类
"""


class ExternalDataTool(Extensible, ABC):
    module: ExtensionModule = ExtensionModule.EXTERNAL_DATA_TOOL
    '''应用id'''
    app_id: str
    '''应用工具的工具变量名'''
    variable: str

    def __init__(self, tenant_id: str, app_id: str, variable: str, config: Optional[dict] = None) -> None:
        super().__init__(tenant_id, config)
        self.app_id = app_id
        self.variable = variable

    @classmethod
    @abstractmethod
    def validate_config(cls, tenant_id: str, config: dict) -> None:
        """
        验证输入的config配置信息
        :param tenant_id: 工作空间id
        :param config: 来源于配置信息
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def query(self, input: str, query: Optional[str] = None) -> str:
        """
        数据查询工具
        :param input: 用户输入
        :param query: 聊天软件的查询
        :return: 查询工具的结果
        """
        raise NotImplementedError
