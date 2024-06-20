from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from core.extension.extensible import Extensible, ExtensionModule


class ModerationAction(Enum):
    DIRECT_OUTPUT = 'direct_output'
    OVERRIDED = 'overrided'


class ModerationInputResult(BaseModel):
    flagged: bool = False
    action: ModerationAction
    preset_response: str = ""
    inputs: dict = {}
    query: str = ""


class ModerationOutResult(BaseModel):
    flagged: bool = False
    action: ModerationAction
    preset_response: str = ""
    text: str = ""


class Moderation(Extensible, ABC):
    module: ExtensionModule = ExtensionModule.MODERATION
