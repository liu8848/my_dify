from enum import Enum


class ModelFeature(Enum):
    """
    Enum class for llm feature.
    llm特征枚举类
    """
    TOOL_CALL = "tool-call"
    MULTI_TOOL_CALL = "multi-tool-call"
    AGENT_THOUGHT = "agent-thought"
    VISION = "vision"
    STREAM_TOOL_CALL = "stream-tool-call"
