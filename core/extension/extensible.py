import enum
import importlib
import json
import os
from typing import Any, Optional

from pydantic import BaseModel


class ExtensionModule(enum.Enum):
    MODERATION = 'moderation'
    EXTERNAL_DATA_TOOL = 'external_data_tool'


class ModuleExtension(enum.Enum):
    extension_class: Any
    name: str
    label: Optional[dict] = None
    from_schema: Optional[list] = None
    builtin: bool = True
    position: Optional[int] = None


class Extensible:
    module: ExtensionModule
    name: str
    tenant_id: str
    config: Optional[dict] = None

    def __init__(self, tenant_id: str, config: Optional[dict] = None) -> None:
        self.tenant_id = tenant_id
        self.config = config

    @classmethod
    def scan_extensions(cls):
        extensions: list[ModuleExtension]
        position_map = {}

        # 获取当前类的路径
        current_path = os.path.abspath(cls.__module__.replace(".", os.path.sep) + '.py')
