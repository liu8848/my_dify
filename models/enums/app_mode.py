from enum import Enum


class AppMode(Enum):
    COMPLETION = 'completion'
    WORKFLOW = 'workflow'
    CHAT = 'chat'
    ADVANCED_CHAT = 'advanced-chat'
    AGENT_CHAT = 'agent-chat'
    CHANNEL = 'channel'

    @classmethod
    def value_of(cls, value: str) -> 'AppMode':
        """
        获取mode的代码value
        :param value: mode名称
        :return: mode
        """
        for mode in cls:
            if mode.value == value:
                return mode
        raise ValueError(f'{value} is not a valid mode')
